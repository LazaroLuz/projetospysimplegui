import PySimpleGUI as sg


layout = [[sg.T('Bom Dia')],
          [sg.T('Teste do Dia')]
          ]

janela = sg.Window('teste do github', layout)

while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
janela.close()
