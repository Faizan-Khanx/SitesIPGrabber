import sys
import requests
import re
import socket
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

print("""
[#] Create By ::

    _____   ____  ____  _____   ____  ____       ______   ___    ___   _      _____
|     | /    Tl    j|     T /    T|    \     |      T /   \  /   \ | T    / ___/
|   __jY  o  | |  T l__/  |Y  o  ||  _  Y    |      |Y     YY     Y| |   (   \_ 
|  l_  |     | |  | |   __j|     ||  |  |    l_j  l_j|  O  ||  O  || l___ \__  T
|   _] |  _  | |  | |  /  ||  _  ||  |  |      |  |  |     ||     ||     T/  \ |
|  T   |  |  | j  l |     ||  |  ||  |  |      |  |  l     !l     !|     |\    |
l__j   l__j__j|____jl_____jl__j__jl__j__j      l__j   \___/  \___/ l_____j \___j
                                                                                
                          FAIZAN-TOOLS  https://instagram.com/ethicalfaizan
""")

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    sys.exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


def domain(site):
    site = re.sub(r'^https?://|www\.|\/.*$', '', site)
    return site


def getIP(url):
    try:
        dom = domain(url)
        try:
            ip = socket.gethostbyname(dom)
            print(' -| ' + url + ' --> {}[{}]'.format(fg, ip))
            with open('FaizanIPs.txt', 'a') as f:
                f.write(ip + '\n')
        except socket.error:
            print(' -| ' + url + ' --> {}[DomainNotWork]'.format(fr))
    except Exception as e:
        print(' -| ' + url + ' --> {}[DomainNotWork] - {}'.format(fr, str(e)))


mp = Pool(150)
mp.map(getIP, target)
mp.close()
mp.join()
