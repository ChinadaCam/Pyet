import os, requests,colorama,threading,time
from colorama import Fore, init
from proxy_checker import ProxyChecker

proxis = []
os.chdir(".\\Scripts\\Proxy-checker")

print(os.listdir())


def main():
    os.system(" Proxy Checker by Death Unity Team")
    file = open("proxies.txt", "r") 
    for proxy in file:
          
       value = ProxyChecker().check_proxy(proxy)
       print(value)
       if 'False' in str(value):
           print(Fore.RED + f"{proxy}" + Fore.WHITE)
           with open("bad.txt", "a") as write:
               write.write(f"{proxy}\n")
       else:
           print(Fore.GREEN + f"{proxy}" + Fore.WHITE)
           with open("good.txt", "a") as write:
               write.write(f"{proxy}\n")

    print(Fore.CYAN + f"Done" + Fore.WHITE)

            


    


def checkFile():
    print("Checking if proxies file exists")
    file = open("proxies.txt", "r") 
    file.close() 
    os.system(Fore.GREEN + "File exists " + Fore.WHITE)
    print(Fore.GREEN + "File exists " + Fore.WHITE)
    time.sleep(1)
    main()




checkFile()
main()