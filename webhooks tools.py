from discord_webhook import DiscordWebhook
from time import sleep
import os
import time
import random
import colorama
from pystyle import Colorate, Colors, Write, Anime, Center, Box
from colorama import init, Fore, Style
import json
import requests
from urllib import request
from urllib.error import HTTPError


title = '''
 _       __     __    __                __           __              __    
| |     / /__  / /_  / /_  ____  ____  / /_______   / /_____  ____  / /____
| | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/ ___/  / __/ __ \/ __ \/ / ___/
| |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,< (__  )  / /_/ /_/ / /_/ / (__  ) 
|__/|__/\___/_.___/_/ /_/\____/\____/_/|_/____/   \__/\____/\____/_/____/  
                                                                           
'''[1:]

os.system('cls & mode 100,30')
os.system('Title Webhooks tools')

Anime.Fade(Center.Center(title), Colors.red_to_black, Colorate.Vertical, interval=0.0025, enter=True)

os.system('Title Webhooks Tools - Webooks')
webhook1 = input(F"{Fore.WHITE} >"+ F"{Fore.RED} Webhook"F"{Fore.WHITE}:")


def choice_menu():
    os.system('Title Webhooks Tools - Menu')
    choicetext = """
    [1]Delete Webhooks
    [2]Spam Webhooks
    [3]Send Webhooks (not for spam)
    [4]Credit
    [5]Exit             
    """

    print(Colors.red + Center.XCenter(Box.Lines(title)))
    print(Colors.red + Center.XCenter(Box.DoubleCube(choicetext)))

    choice = str(input(F"{Fore.WHITE} >"+ F"{Fore.RED} Choice"F"{Fore.WHITE}:"))

    if choice == '1':
        os.system('Title Webhooks Tools - Delete')
        requests.delete(webhook1)
        check = requests.get(webhook1)
        if check.status_code == 404:
            print(F"{Fore.WHITE} [LOGS]"+ F"{Fore.RED} webhooks succesfully deleted")
            time.sleep(2)
            os.system('exit')
        elif check.status_code == 200:
            os.system('cls')
            print("\n [LOGS] FAILED TO DELETE WEBHOOK")
            time.sleep(1.5)
            os.system('cls')
            return choice_menu()

    if choice == '2':
        os.system('cls, & title Webhooks Tools - Spammer')
        name_embed = input(F"{Fore.WHITE} >"+ F"{Fore.RED} name of embed"F"{Fore.WHITE}:")
        os.system('cls')
        msg = input(F"{Fore.WHITE} >"+ F"{Fore.RED} The message"F"{Fore.WHITE}:")
        os.system('cls')
        title_embed = input(F"{Fore.WHITE} >"+ F"{Fore.RED} Title of embed"F"{Fore.WHITE}:")
        os.system('cls')
        how_many = int(input(F"{Fore.WHITE} >"+ F"{Fore.RED} How many"F"{Fore.WHITE}:"))
        for i in range(how_many):
            url = webhook1

            data = {
                "username" : name_embed
            }

            data["embeds"] = [
                {
                    "description" : msg,
                    "title" : title_embed,
                }
            ]

            result = requests.post(url, json = data)

            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print(F"{Fore.WHITE} [LOGS]"+ F"{Fore.RED} Msg send")
        os.system('cls')
        time.sleep(0.5)
        print(F"{Fore.WHITE} [LOGS]"+ F"{Fore.RED} done")
        time.sleep(1)
        os.system('cls')
        return choice_menu()
                


    if choice == '3':
        os.system('cls, & title Webhooks Tools - Send')
        msg = input(F"{Fore.WHITE} >"+ F"{Fore.RED} The message"F"{Fore.WHITE}:")
        os.system('cls')
        how_many = int(input(F"{Fore.WHITE} >"+ F"{Fore.RED} How many"F"{Fore.WHITE}:"))
        os.system('cls')
        webhooks_name = input(F"{Fore.WHITE} >"+ F"{Fore.RED} name of webhooks"F"{Fore.WHITE}:")
        for i in range(how_many):
            webhook = DiscordWebhook(url=webhook1, content=msg, username=webhooks_name) 
            response = webhook.execute()
            print(F"{Fore.WHITE} [LOGS]"+ F"{Fore.RED} Msg send")
        os.system('cls')
        time.sleep(0.5)
        print(F"{Fore.WHITE} [LOGS]"+ F"{Fore.RED} done")
        time.sleep(1)
        os.system('cls')
        return choice_menu()


    if choice == '4':
        os.system('cls, & title title Webhooks Tools - Credit')
        print(F"""{Fore.RED}
        
        Discord : GlaxiO#8132
        Github : https://github.com/Glaxifiak

        (presse enter)
        
        """)
        os.system("pause >nul")
        choice_credit = str(input(F"{Fore.WHITE}[1] >"+ F"{Fore.RED} Exit"F"{Fore.WHITE}:"))
        if choice_credit == '1':
            os.system('cls')
            choice_menu()

    if choice == '5':
        os.system('exit')


        

def webhookstest():
    test = requests.get(webhook1)
    if test.status_code == 404:
        os.system('cls')
        print("\n [!] THE WEBHOOK IS INVALID")
        os.system('exit') 
    elif test.status_code == 200:
        os.system('cls')
        choice_menu()

webhookstest()


