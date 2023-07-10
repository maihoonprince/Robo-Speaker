
# This program is for mac and Linux:------->

import os

if __name__ == '__main__':
    print("Welcom to Robo Speaker,Created by Prince.")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)

#program that utilizes the os module in Python to make your computer speak using the say command. Here's a breakdown of how it works:

# The import os statement imports the os module, which provides a way to interact with the operating system.

# The if __name__ == '__main__': condition checks whether the script is being run directly (as opposed to being imported as a module).
# This allows the code within the if block to execute when the script is run.

# The print("Welcome to Robo Speaker, Created by Prince.") statement displays a welcome message when the program starts.

# The while True: statement creates an infinite loop that will continue until the loop is explicitly broken.

# The x = input("Enter what you want to speak: ") line prompts the user to input what they want the computer to speak and assigns the input to the variable x.

#The if x == "q": condition checks if the user has entered "q" to quit the program. If the condition is true, it executes the following block of code.

# The os.system("say 'bye bye friend'") line uses the os.system() function to execute the say command with the specified text, which in this case is "bye bye friend.
# " This command makes the computer speak the provided text.
#
# The break statement terminates the loop and exits the program.
#
# If the user input is not "q", the program assumes it's the text the user wants the computer to speak.
# It creates a command string by formatting the input using an f-string (f"say {x}").
#
# The os.system(command) line executes the say command with the user-provided text, making the computer speak the text.
#
# To use this code, you need to have the say command available on your operating system.
# This code assumes you are using a macOS or Linux system where the say command is available.
# On Windows, you would need to use a different command or install a text-to-speech engine that supports command-line usage.





#On Windows, you can use the pyttsx3 library to achieve text-to-speech functionality.
# It provides a platform-independent way to interact with text-to-speech engines.
#
# First, you'll need to install the pyttsx3 library. ' \
# You can install it using pip by running the following command in your command prompt or terminal:

# pip install pyttsx3


# this program for Windows:--->
import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo Speaker, Created by Prince.")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()