# Bring in the subprocess module so I can use it later
import subprocess

# The 'open()' function, used with mode 'w', opens the specified file for writing and
# will overwrite anything that already exists in the .txt file (use 'a' to append text).
# If the specified file does not exist, it will create it.
# After the file is opened, f.write will add whatever text is put in the parenthesis to the .txt
# file. Text must be in quotes (") or apostrophes (')
with open('Not_a_Bot.txt', 'w') as f:
    f.write('The robots are taking over.')

#Use the subprocess module's call function to call (execute) notepad in Windows and open TheEndIsNear.txt
subprocess.call(["notepad.exe", "Not_a_Bot.txt"])
