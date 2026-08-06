# Install an external module and use it to perfrom an operation of your interest

import subprocess
def say(text):
    subprocess.run(["espeak", text])
say("Hello, I am an external module that can speak!")


# other way to do it by using pyttsx3 module