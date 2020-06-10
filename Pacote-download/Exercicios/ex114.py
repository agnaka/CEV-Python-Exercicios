import urllib.request
print()
try:
    site = urllib.request.urlopen('http://www.oficinadodesenho.com.br/')
# except Exception as error:   -> também funciona
except urllib.error.URLError:
    print(f'\033[31mO site Pudim não esta acessível no momento.\033[m')
else:
    print(f'\033[32mConsegui acessar o site Pudim com sucesso!\033[m')