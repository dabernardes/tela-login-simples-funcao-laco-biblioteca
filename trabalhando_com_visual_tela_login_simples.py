from PySimpleGUI import PySimpleGUI as sg
import time
user = False
pas = False
erro=0
vl=' '
# funcao


def verifica_pass(window):
    verifica = False
    if window['password'].Get() == 'senha123':
        verifica = True
        return verifica
    else:
        window['password'].update('')
        window['password'].set_focus()
        return verifica


def verifica_user(window):
    verifica = False
    if window['usuario'].Get() == 'Douglas':
        verifica = True
        return verifica
    else:
        window['usuario'].update('')
        window['password'].update('')
        window['usuario'].set_focus()
        return verifica


# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome  :'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha :'), sg.Input(key='password',
                                  password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar',key='-button-')]
]
# janela
janela = sg.Window('Tela de Login', layout)
# eventos
while True:
    evento, valores = janela.read()
    user = verifica_user
    if evento == sg.WIN_CLOSED:
        break
    if evento == '-button-':
        user = verifica_user(janela)

        if user == True:
            pas = verifica_pass(janela)
            if pas == True:
                print('Você logou no sistema!')
            else:
                erro=erro+1
                if erro <= 3 :
                    print('Senha incorreta, tente novamente')
                else:
                    janela['-button-'].update('Boqueado')
                    janela['password'].update(disabled=True)
                    janela['-button-'].update(disabled=True)
                    print('Digitacao Bloqueada por 10 segundos')
                    time.sleep(10)
                    janela['usuario'].update('')
                    janela['usuario'].set_focus()
                    janela['-button-'].update('Entrar', disabled=False)
                    janela['password'].update(disabled=False)
                    erro=0
                    print('tente novamente')
        else:
            print('Usuario digitado não existe no sistema, tente com outro usuario')
