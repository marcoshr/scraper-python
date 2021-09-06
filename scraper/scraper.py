#!/usr/bin/python3

from pyquery import PyQuery
import requests
from file_handler import *
from secrets import username, password

print("# START PROGRAM #")

resp = requests.get("https://oficinavirtual.aqualia.es/aqualiacontact/")
doc = PyQuery(resp.text)

title = doc('title').text()
print(title)

user_field = doc("input[id='ctl00_ContentPlaceHolderOficinaVirtual_tbCodigoUsuario']")
user_field.html(username)
#print(user_field.text())
print("Usuario insertado")

password_field = doc("input[id='ctl00_ContentPlaceHolderOficinaVirtual_tbPassword']")
password_field.html(password)
#print(password_field.text())
print("Contraseña insertada")

"""
PARA LOGEARSE
https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module/17633072#17633072
https://2.python-requests.org//en/latest/user/quickstart/#more-complicated-post-requests
"""

payload = {'inUserName': username, 'inUserPass': password}
url = 'https://oficinavirtual.aqualia.es/aqualiacontact/'
requests.post(url, data=payload)

prueba = doc("span[id='ctl00_ContentPlaceHolderOficinaVirtual_Hilo_HiloDescripcion']")
print(prueba)

#createFile()


print("# END PROGRAM #")