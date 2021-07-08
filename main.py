LICENSE = """
Copyright © 2021 Drillenissen#4268

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import os

print(LICENSE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes

try: # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook # Try to import discord_webhook
except ImportError: # If it chould not be installed
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() # Exit the program
try: # Setup try statement to catch the error
    import requests # Try to import requests
except ImportError: # If it has not been installed
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # Exit the program


class NitroGen: # Initialise the class
    def __init__(self): # The initaliseaiton function
        self.fileName = "Nitro Codes.txt" # Set the file name the codes are stored in

    def main(self): # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        if os.name == "nt": # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Drillenissen#4268") # Change the
        else: # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a', end='', flush=True) # Update title of command prompt

        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """) # Print the title card
        time.sleep(2) # Wait a few seconds
        self.slowType("Made by: Drillenissen#4268 && Benz#8295", .02) # Print who developed the code
        time.sleep(1) # Wait a little more
        self.slowType("\nInput How Many Codes to Generate and Check: ", .02, newLine = False) # Print the first question

        num = int(input('')) # Ask the user for the amount of codes

        # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
        self.slowType("\nDo you wish to use a discord webhook? \nIf so type it here or press enter to ignore: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None # If the url is empty make it be None insted

        # print() # Print a newline for looks

        valid = [] # Keep track of valid codes
        invalid = 0 # Keep track of how many invalid codes was detected

        for i in range(num): # Loop over the amount of codes to check
            try: # Catch any errors that may happen
                code = "".join(random.choices( # Generate the id for the gift
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # Generate the url

                result = self.quickChecker(url, webhook) # Check the codes

                if result: # If the code was valid
                    valid.append(url) # Add that code to the list of found codes
                else: # If the code was not valid
                    invalid += 1 # Increase the invalid counter by one
            except Exception as e: # If the request fails
                print(f" Error | {url} ") # Tell the user an error occurred

            if os.name == "nt": # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268") # Change the title
                print("")
            else: # If it is a unix system
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268\a', end='', flush=True) # Change the title

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") # Give a report of the results of the check

        input("\nThe end! Press Enter 5 times to close the program.") # Tell the user the program finished
        [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


    def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

    def generator(self, amount): # Function used to generate and store nitro codes in a seperate file
        with open(self.fileName, "w", encoding="utf-8") as file: # Load up the file in write mode
            print("Wait, Generating for you") # Let the user know the code is generating the codes

            start = time.time() # Note the initaliseation time

            for i in range(amount): # Loop the amount of codes to generate
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Generate the code id

                file.write(f"https://discord.gift/{code}\n") # Write the code

            # Tell the user its done generating and how long tome it took
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Function used to check nitro codes from a file
        valid = [] # A list of the valid codes
        invalid = 0 # The amount of invalid codes detected
        with open(self.fileName, "r", encoding="utf-8") as file: # Open the file containing the nitro codes
            for line in file.readlines(): # Loop over each line in the file
                nitro = line.strip("\n") # Remove the newline at the end of the nitro code

                # Create the requests url for later use
                url = f"https://discordapp.com/api/v8/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # Get the responce from the url

                if response.status_code == 200: # If the responce went through
                    print(f" Valid | {nitro} ") # Notify the user the code was valid
                    valid.append(nitro) # Append the nitro code the the list of valid codes

                    if notify is not None: # If a webhook has been added
                        DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else: # If there has not been a discord webhook setup just stop the code
                        break # Stop the loop since a valid code was found

                else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                    print(f" Invalid | {nitro} ") # Tell the user it tested a code and it was invalid
                    invalid += 1 # Increase the invalid counter by one

        return {"valid" : valid, "invalid" : invalid} # Return a report of the results

    def quickChecker(self, nitro, notify = None): # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v8/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Get the response from discord

        if response.status_code == 200: # If the responce went through
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Notify the user the code was valid
            with open("Nitro Codes.txt", "w") as file: # Open file to write
                file.write(nitro) # Write the nitro code to the file it will automatically add a newline

            if notify is not None: # If a webhook has been added
                DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                    url = notify,
                    content = f"Valid Nitro Code detected! @everyone \n{nitro}"
                ).execute()

            return True # Tell the main function the code was found

        else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Tell the user it tested a code and it was invalid
            return False # Tell the main function there was not a code found

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() # Run the main code
