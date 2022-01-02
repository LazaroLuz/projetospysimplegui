import requests
import base64
import PySimpleGUI as sg
from convert import convert_to_bytes


url = 'https://apiquadrinho.herokuapp.com/'

response = requests.get(url)

# res = json.loads(response.content)
res = response.json()
revistas = res['Quadrinho']
print(revistas[0]['title'])
# for l in revistas:
#     print(l['detail'])
#     print(l['img'])
#     print(l['link'])
capa = requests.get(revistas[0]['img']).content
layout = [
    [sg.T(revistas[0]['title'], justification='center')],
    [sg.Image(data=convert_to_bytes(capa, (400, 400)), k='_imgs_')],
]
janela = sg.Window('Capa Quadrinho Erotico', layout=layout, resizable=True)


while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
janela.close()
