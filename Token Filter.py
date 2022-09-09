import time
from os import system
from art import *
from colorama import Fore, Back, Style


system('mode con: cols=68 lines=10')

print(Fore.RED + text2art('''\n                 @ZVHK''', font="small"))

with open('combo.txt','r') as qq:
        token = qq.read().splitlines()
        lenc = len(token)
       
TokensV = 0

for i in token:

    TokensV+=1
    
    tokens = i.split(":")[2]

    uu = lenc - TokensV

    system(f"title Token Remain : {uu}")

    print(f"[!] - Tokens Extracted : {TokensV}" ,end="\r")

    f = open("Tokens Extracted.txt", "a")
    f.write (f"{tokens}\n")
    f.close()


print("\n[!] - Done !")

a = input('[!] - Press Enter to Exit > ')
if a:
    exit(0)


