#!/usr/bin/python3
# Original project page: https://github.com/grez911/vk-downloader

import sys
import os
import re
import pyperclip
from urllib.request import urlopen, urlretrieve
from colorama import init, Fore, Back, Style

init(convert=True)


def main():
    clipboard = pyperclip.paste()
    if "vk.com" and "video" and "_" not in clipboard:
        print()
        print("[" + Fore.RED + "-" + Style.RESET_ALL + "]" + " ERROR!!!\n"
              "Put video URL into your clipboard.\n"
              "URL Sample: https://vk.com/video1315763_456239439")
        input("[#]" + " Press Enter to exit...")
        sys.exit(2)
    # converting part
    if "http://" in clipboard:
        clipboard = clipboard.replace("http", "https")
    if "z=" in clipboard:
        newclipboard = clipboard.split("z=", 1)[-1]
        newclipboard = newclipboard.split("%2F", 1)[0]
        newclipboard = "https://vk.com/" + newclipboard

    print("")
    print("[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + " Video URL: " + clipboard)

    page = urlopen(newclipboard)
    content = page.read()
    page.close()
    link = content.decode('utf-8', "ignore")
    string = re.compile('<source src=\\\\"([^"]*)\\\\"')
    urls = string.findall(link)

    for i in ['1080.mp4', '720.mp4', '360.mp4', '240.mp4']:
        for url in urls:
            if i in url:
                source = url.replace('\\/', '/')
                reg = re.compile(r'/([^/]*\.mp4)')
                name = reg.findall(source)[0]
                path = "videos/"
                # checks if folder exists
                if not os.path.exists(path):
                    os.makedirs(path)
                fullpath = os.path.join(path, name)
                if os.path.exists(fullpath):
                    print("[" + Fore.RED + "-" + Style.RESET_ALL + "] " + name + " already exists")
                    input("[#]" + " Press Enter to exit...")
                    sys.exit(0)
                input("[#]" + " Press Enter to start downloading...")
                print("[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + " Downloading...")
                urlretrieve(source, fullpath)
                print("[" + Fore.GREEN + "+" + Style.RESET_ALL + "]" + " Saved as " + name)
                input("[#]" + " Press Enter to exit...")
                sys.exit(0)

    print("[" + Fore.RED + "-" + Style.RESET_ALL + "] " + "Can't find video.")
    input("[#]" + " Press Enter to exit...")
    sys.exit(2)


if __name__ == '__main__':
    main()
