import requests, os, threading, sys, time, random,datetime,ctypes
from colorama import Fore, init

                                                                                                               
                                                                                                               
blue, red, white, green = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.GREEN


messages = [ "https://github.com/ChinadaCam/Death-Unity-Script", "Death", "PY PY PY "]


logo = f"""
  {blue} ____       ____       ______      ______               __  __      __  __      ______      ______    __    __ {white}
  {blue}/\  _`\    /\  _`\    /\  _  \    /\__  _\             /\ \/\ \    /\ \/\ \    /\__  _\    /\__  _\  /\ \  /\ \{white}
  {blue}\ \ \/\ \  \ \ \L\_\  \ \ \L\ \   \/_/\ \/             \ \ \ \ \   \ \ `\\ \   \/_/\ \/    \/_/\ \/  \ `\`\\/'/{white}
  {blue} \ \ \ \ \  \ \  _\L   \ \  __ \     \ \ \              \ \ \ \ \   \ \ , ` \     \ \ \       \ \ \   `\ `\ /' {white}
  {blue}  \ \ \_\ \  \ \ \L\ \  \ \ \/\ \     \ \ \              \ \ \_\ \   \ \ \`\ \     \_\ \__     \ \ \    `\ \ \ {white}
  {blue}   \ \____/   \ \____/   \ \_\ \_\     \ \_\              \ \_____\   \ \_\ \_\    /\_____\     \ \_\     \ \_\{white}
  {blue}    \/___/     \/___/     \/_/\/_/      \/_/               \/_____/    \/_/\/_/    \/_____/      \/_/      \/_/{white}
                                                                                 """



def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Death Unity Script- By Death Unity Team")
    print("\n" + logo + "\n")
    print("  Coded by Death Unity Team - \"{}\"".format(random.choice(messages)))
    print()
    print("  Where do you wanna go")
    print("\n  [1] Thing r\n  [2] Thing 2\n  [3] Open github page \n  [4] Credits\n  [5] Quit")
    try:
        question = int(input("  "))
    except Exception:
        print("Invalid input..")
        time.sleep(2)
        main()
    if question == 1:
         #some
         pass
    elif question == 2:
        #some
        pass
    elif question == 3:
        webbrowser.open_new("https://github.com/ChinadaCam/Death-Unity-Script")
        main()
    elif question == 4:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Checker - By ExtremeDev")
        print("\n" + logo + "\n")
        print("  Coded by Death Unity team - \"{}\"".format(random.choice(messages)))
        print()
        print("  Developers: ChinadaCam \n  Owner: ChinadaCam ")
        print()
        input("  Press ENTER to get on menu..")
        main()
    elif question == 5:
        print("  Closing..")
        time.sleep(2)
        sys.exit()
    else:
        print("  Invalid input..")
        time.sleep(2)
        main()


main()