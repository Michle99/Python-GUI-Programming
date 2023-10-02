import json

def is_valid(stale, latest, otjson):
    # Convert the JSON string to a list of operations
    operations = json.loads(otjson)

    # Initialize cursor at the beginning of the stale document
    cursor = 0

    for operation in operations:
        op_type = operation["op"]

        if op_type == "insert":
            chars = operation["chars"]
            # Check if the cursor is within bounds
            if cursor >= 0 and cursor <= len(stale):
                stale = stale[:cursor] + chars + stale[cursor:]
                cursor += len(chars)
            else:
                return False  # Invalid cursor position

        elif op_type == "delete":
            count = operation["count"]
            # Check if the cursor is within bounds
            if cursor >= 0 and cursor + count <= len(stale):
                stale = stale[:cursor] + stale[cursor + count:]
            else:
                return False  # Invalid cursor position

        elif op_type == "skip":
            count = operation["count"]
            # Check if the cursor is within bounds
            if cursor + count >= 0 and cursor + count <= len(stale):
                cursor += count
            else:
                return False  # Invalid cursor position

    # After applying all operations, check if the stale document matches the latest document
    return stale == latest

# Example usage:
stale = 'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.'
latest = 'Repl.it uses operational transformations.'
otjson = '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
result = is_valid(stale, latest, otjson)
print(result)  # Output: True