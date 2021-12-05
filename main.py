import ctypes
import string
import os
import time
#LICNECE = """
#Copyright © 2021 Drillenissen#4268

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook  # Try to import discord_webhook
except ImportError:  # If it chould not be installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  # Setup try statement to catch the error
    import requests  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  # Exit the program
try:  # Setup try statement to catch the error
    import numpy  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  # Exit the program

# check if user is connected to internet
url = "https://github.com"
try:
    response = requests.get(url)  # Get the responce from the url
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  # Exit program


class NitroGen:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by Drillenissen#4268")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)  # Update title of command prompt

        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """)  # Print the title card
        time.sleep(2)  # Wait a few seconds
        # Print who developed the code
        self.slowType("Made by: Drillenissen#4268 && Benz#3554", .02)
        time.sleep(1)  # Wait a little more
        # Print the first question
        self.slowType(
            "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)

        try:
            num = int(input(''))  # Ask the user for the amount of codes
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()  # Exit program

        if USE_WEBHOOK:
            # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
            url = input('')  # Get the awnser
            # If the url is empty make it be None insted
            webhook = url if url != "" else None
            
        if webhook is not None:
            DiscordWebhook(  # Let the user know it has started logging the ids
                    url=notify,
                    content=f"```Started checking urls\nI will send any valid codes here```"
                ).execute()

        # print() # Print a newline for looks

        valid = []  # Keep track of valid codes
        invalid = 0  # Keep track of how many invalid codes was detected
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        # generate codes faster than using random.choice
        c = numpy.random.choice(chars, size=[num, 19])
        for s in c:  # Loop over the amount of codes to check
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  # Generate the url

                result = self.quickChecker(url, webhook)  # Check the codes

                if result:  # If the code was valid
                    # Add that code to the list of found codes
                    valid.append(url)
                else:  # If the code was not valid
                    invalid += 1  # Increase the invalid counter by one
            except KeyboardInterrupt:
                # If the user interrupted the program
                print("\nInterrupted by user")
                break  # Break the loop

            except Exception as e:  # If the request fails
                print(f" Error | {url} ")  # Tell the user an error occurred

            if os.name == "nt":  # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268")  # Change the title
                print("")
            else:  # If it is a unix system
                # Change the title
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")  # Give a report of the results of the check

        # Tell the user the program finished
        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]  # Wait for 4 enter presses

    # Function used to print text a little more fancier
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            time.sleep(speed)  # Sleep a little before the next one
        if newLine:  # Check if the newLine argument is set to True
            print()  # Print a final newline to make it act more like a normal print statement

    def quickChecker(self, nitro:str, notify=None):  # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  # Get the response from discord

        if response.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                file.write(nitro)

            if notify is not None:  # If a webhook has been added
                DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=notify,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True  # Tell the main function the code was found

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            # Tell the user it tested a code and it was invalid
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  # Tell the main function there was not a code found


if __name__ == '__main__':
    Gen = NitroGen()  # Create the nitro generator object
    Gen.main()  # Run the main code
