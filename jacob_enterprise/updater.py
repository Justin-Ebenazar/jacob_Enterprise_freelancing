import subprocess
import time

# Define the git pull command
cmd_command = 'git pull'

try:
    # Run the command
    result = subprocess.run(cmd_command, shell=True, check=True, text=True, capture_output=True)

    # Print the command output
    print('Command Output:')
    print(result.stdout)
    time.sleep(10)

    # Print the command error output (if any)
    if result.stderr:
        print('Command Error Output:')
        print(result.stderr)
        time.sleep(10)

except subprocess.CalledProcessError as e:
    print(f'An error occurred: {e}')
    time.sleep(10)
