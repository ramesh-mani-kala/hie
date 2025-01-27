import readline

# List of possible commands for autosuggestion
commands = ['start', 'stop', 'pause', 'resume', 'exit']

# Function to implement autosuggestions
def completer(text, state):
    # Return the list of possible commands that start with the text typed by the user
    options = [cmd for cmd in commands if cmd.startswith(text)]
    try:
        return options[state]
    
    except IndexError:
        return None

# Set the completer function for readline
readline.set_completer(completer)
readline.parse_and_bind('tab: complete')

# A simple loop to take user input
while True:
    user_input = input("Enter command: ")
    if user_input == 'exit':
        print("Exiting program...")
        break
    print(f"Command entered: {user_input}")
