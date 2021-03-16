#/usr/bin/python
import requests
import json
import os

# kode warna

m='\033[31;1m'
h='\033[32;1m'
k='\033[33;1m'
p='\033[37;1m'
b='\033[34;1m'
n='\033[00;1m'
p_='\033[47;1m'

logo = """{}
╭━━╮ ╭╮╭━━╮
┃━━╋┳┫╰╋╮╮┣━╮    {}Subdomain Scanner
{}┣━━┃┃┃╋┣┻╯┃╋┃
╰━━┻━┻━┻━━┻━╯       {}{}{} AsukaDev {}{}

""".format(n, h, n, p, m, p_, n, p)

class Scan:
    def __init__(self, url, save):
        self.url = url
        self.save = save
    def scan(self):
        domain = url
        File = save
        # api by Ahmad Badali
        # github : https://github.com/jamet1337i/
        api = 'http://jamet1337.ml/api/subdo.php?url='
        req = requests.get(api+domain)
        jeson = json.loads(req.text)
        print('{}[{}={}] {}Scan subdomain....'.format(p, h, p, p)) 
        print('{}[{}={}] {}Subdomain: {}'.format(p, h, p, p, h))
        List = jeson['hasil']
        print(List)
        simpan = open(File, 'w')
        simpan.write(List)
        print('{}subdomain save to file : {}'.format(p, h)+File)


if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    url = input('{}[{}+{}] {}Enter domain: {}'.format(p, k, p, p, k))
    save = input('{}[{}+{}] {}Enter file to save subdomain: {}'.format(p, k, p, p, k))
    Scan(url, save).scan()
