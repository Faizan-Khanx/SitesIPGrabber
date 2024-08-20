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
[#] Created By ::

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
except FileNotFoundError:
    sys.exit(f'\n  [!] File not found: {sys.argv[1]}')


def domain(site):
    return re.sub(r'^https?://|www\.|\/.*$', '', site)


def get_IP(url):
    dom = domain(url)
    try:
        ip = socket.gethostbyname(dom)
        print(f' -| {url} --> {fg}[{ip}]')
        with open('FaizanIPs.txt', 'a') as f:
            f.write(ip + '\n')
    except socket.gaierror:
        print(f' -| {url} --> {fr}[DomainNotWork]')
    except Exception as e:
        print(f' -| {url} --> {fr}[Error] - {str(e)}')

with Pool(150) as pool:
    pool.map(get_ip, target)
