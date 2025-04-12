# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        # Try to convert age to integer and increment
        age = int(parts[1]) + 1
    except (ValueError, IndexError):
        # Handle cases where age isn't an integer or missing
        age = 0
    print(f'{name} {age}')
    
    # Get next line
    parts = input().split()
    name = parts[0]
