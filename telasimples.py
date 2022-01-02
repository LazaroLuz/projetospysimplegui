import PySimpleGUI as sg
import datetime


curr_dt_time = datetime.datetime.now()
horas = curr_dt_time.strftime("%H:%M:%S")
layout = [[sg.T(horas, text_color='blue', border_width=2, font='Arial 25', k='_H_')]
          ]

janela = sg.Window('teste do github', layout)

while True:
    event, value = janela.read(timeout=10)
    curr_dt_time = datetime.datetime.now()
    h_c = curr_dt_time.strftime("%H:%M:%S")
    if event == sg.WIN_CLOSED:
        break
    janela['_H_'].update(h_c)
janela.close()
