from lib import main
import os
from termcolor import colored


# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')


print(colored('''
   _____            _         _             _     
  / ____|          | |       | |           | |    
 | |      ___    __| |  ___  | |__   _   _ | |__  
 | |     / _ \  / _` | / _ \ | '_ \ | | | || '_ \ 
 | |____| (_) || (_| ||  __/ | | | || |_| || |_) |
  \_____|\___/  \__,_| \___| |_| |_| \__,_||_.__/ 
                                                  
                                                  ''', "blue"))

print('''
====================================
 Valorant Aimbot (v0.1)
====================================
Suported color: purple
====================================
[INFO] press "ctrl+C" or 'q' to quit...''')

main.start()