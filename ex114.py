import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('deu erro no pudim')
else:
    print('Tudo ok no pudim')
    print(site.read())