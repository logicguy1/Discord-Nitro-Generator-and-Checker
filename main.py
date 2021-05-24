# https://github.com/logicguy1/Discord-Nitro-Generator-and-Checker/
# I cleaned up a lot, including adding color, multithreading (thanks https://git.io/JsDmT), and auto module install

import os
import random
import string
import time
import ctypes
import threading
from sys import executable


try:  # Try to import modules
    import requests
    from discord_webhook import DiscordWebhook
    from colorama import Fore, Style
except ImportError:  # Ask user to install if there was an error
    install = input(
        'It looks like you don\'t have all dependencies installed, would you like to install them? [Y/N] ')

    installCommand = f'''{executable} -m pip install requests discord_webhook colorama'''

    if 'y' in install.lower():
        os.system(installCommand)

        from discord_webhook import DiscordWebhook  # Import modules again
        import requests
        from colorama import Fore, Style
    else:
        print(f'Okay, you can install the modules with {installCommand}')
        exit()


class NitroGen:
    def __init__(self):
        self.valid = set()  # Sets don't allow repetition, gives better performance
        self.numCodes = None
        self.maxThreads = None
        self.webhookUrl = None
        self.startTime = None
        self.totalCodes = 0
        self.threadingLock = threading.Lock()

    def intro(self):
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        self.setWindowTitle(
            'Nitro Generator and Checker - Made by Drillenissen#4268')

        print(f'''{Style.DIM}\n
         █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
        ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
        ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
        ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
        ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
        ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
        {Style.RESET_ALL}''')

        self.slowType(
            f'{Fore.LIGHTBLUE_EX} Made by: Drillenissen#4268, Benz#4947, & Music_Dude#6374\n', .02)

        time.sleep(1)

    def config(self):
        self.slowType(
            f'{Style.RESET_ALL} Input how many codes to generate and check (0 for infinity): {Fore.RED}', .02, newLine=False)
        while True:
            try:
                self.numCodes = int(input(''))
                break
            except:
                print(
                    f'{Style.RESET_ALL} Invalid number. Enter how many codes to generate and check: {Fore.RED}', end='')
                continue
        if self.numCodes == 0:
            # Generate infinite codes if the user inputs 0
            self.numCodes = float('Inf')

        self.slowType(
            f'{Style.RESET_ALL}\n Do you wish to use a discord webhook? [Y/N] {Fore.RED}', .02, newLine=False)
        useWebhook = input('')
        if 'y' in useWebhook.lower():
            self.slowType(
                f'{Style.RESET_ALL}\n Okay, enter the url here: {Fore.RED}', .02, newLine=False)
            self.webhookUrl = input('')
            try:
                r = requests.get(self.webhookUrl)
                if r.status_code != 200:
                    raise ValueError
            except:
                print(
                    f'{Style.RESET_ALL} Invalid webhook url provided, ignoring!\n')

        self.slowType(
            f'{Style.RESET_ALL}\n What is the maximum number of threads you\'d like to run: {Fore.RED}', .02, newLine=False)

        while True:
            try:
                self.maxThreads = int(input(''))
                if self.maxThreads > self.numCodes:
                    print(
                        f'{Style.RESET_ALL} Max number of threads must be less than the max number of codes to generate.\n Enter another number: {Fore.RED}', end='')
                    continue
                break
            except:
                print(
                    f'{Style.RESET_ALL} Invalid number. Enter the maximum number of threads you\'d like to run: {Fore.RED}', end='')
                continue

        print(
            f'\n\n{Fore.LIGHTBLACK_EX} ------------------------------------------------\n{Style.RESET_ALL}')

    def main(self):
        self.startTime = time.time()
        with self.threadingLock:  # Threading lock prevents threads from generating too many/too few codes
            while self.totalCodes < self.numCodes:
                try:
                    # Generate code URL
                    code = ''.join(random.choices(
                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k=16
                    ))
                    url = f'https://discord.gift/{code}'

                    isValid = self.checkCode(url, self.webhookUrl)

                    if isValid:
                        self.valid.add(url)
                        self.setWindowTitle(
                            f'Nitro Generator and Checker - Valid | {len(self.valid)} - Made by Drillenissen#4268')

                # Catch any errors during execution
                except Exception as e:
                    print(
                        f'{Fore.RED}  Error {Fore.LIGHTWHITE_EX}|{Style.RESET_ALL} {url} ')

                self.totalCodes += 1

    def results(self):
        results = f' Generated {self.totalCodes} codes in {time.time() - self.startTime:0.2F} seconds\n Valid: {len(self.valid)}\n'

        if len(self.valid) > 0:
            # Show valid codes only if there are any
            results += f' Valid Codes: {", ".join(self.valid )}\n'

        print(
            f'\n{Fore.LIGHTBLACK_EX} ------------------------------------------------\n\n{Fore.CYAN}{results}{Style.RESET_ALL}')

    def checkCode(self, code, notify=None):
        url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true'
        response = requests.get(url)

        if response.status_code == 200:  # If the response was valid
            print(f'{Fore.GREEN}  Valid {Fore.LIGHTWHITE_EX}|{Style.RESET_ALL} {code}', flush=True,
                  end='' if os.name == 'nt' else '\n')
            with open('nitro_codes.txt', 'w') as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                file.write(code)

            if notify != None:
                return

            DiscordWebhook(  # Notify webhook that a code was detected
                url=notify,
                username='Nitro Codes',
                content=f'Valid nitro code detected! @everyone\n{code}'
            ).execute()

            return True  # Tell the main function a code was found

        # If the response was invalid
        else:
            print(f'{Fore.LIGHTYELLOW_EX} Invalid {Fore.LIGHTWHITE_EX}|{Style.RESET_ALL} {code}', flush=True,
                  end='' if os.name == 'nt' else '\n')
            return False  # Tell the main function there was not a code found

    # Print text a little fancier
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            # Flush forces Python to print the char
            print(i, end='', flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def setWindowTitle(self, newTitle: str):
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(newTitle)
        else:
            print(f'\33]0;{newTitle}\a',
                  end='', flush=True)


if __name__ == '__main__':
    threadList = []

    Gen = NitroGen()
    Gen.intro()  # Show title screen & info
    Gen.config()  # Get configuration values

    for i in range(Gen.maxThreads):
        t = threading.Thread(target=Gen.main)
        t.start()
        threadList.append(t)

    for t in threading.enumerate():
        if t is not threading.currentThread():  # Don't join main thread
            t.join()  # Join stops main thread from continuing until all threads are finished

    Gen.results()

    input('\n Finished! Press Enter to exit the program.')
