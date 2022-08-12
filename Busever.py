import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "Busever",
    "description": "Bu scripti seviceksin. ",
    "version": "0.1",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

sec_kod = sc = True

def yukle_kod(p):
    global kod, sec_kod

    if sec_kod:
        ext.send_to_client('{in:Users}{i:1}{i:6476444}{s:"-Buse."}{s:"Nuvole bianche"}{s:"hr-4117-31-31.hd-627-10.ch-4392-76-1320.lg-710-76.sh-730-76.ha-4354-71-75.ca-4939"}{i:1}{i:3}{i:5}{s:"0.0"}{i:2}{i:1}{s:"f"}{i:64447}{i:3}{s:"um"}{s:""}{i:6269}{b:false}')


ext.intercept(Direction.TO_SERVER, yukle_kod, 'GetGuestRoom')
