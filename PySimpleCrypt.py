import os
import sys
import cryptocode as ct
import PySimpleGUI as sg

class Tela:

    def Restart_Script():

        python = sys.executable # Função para reiniciar script
        os.execl(python, python, * sys.argv)

    def Descriptografar(): #Função para Descriptografar os arquivos

        sg.theme('DarkGrey5')

        layout = [
        [sg.Text(' '*90)],
        [sg.Text(" "*6+"Simple Crypt", font=('Arial, 25'))],
        [sg.Text(" "*23+"_"*43, font=('Arial, 7'))],
        [sg.Text(' '*90)],
        [sg.Text(' '*90)],
        [sg.Text("           Local do Arquivo: "), sg.FilesBrowse(key='arquivo-decript')],
        [sg.Text(' '*90)],
        [sg.Text("           Senha:  "), sg.Input(key='senha-decript', size=(25,1))],
        [sg.Text('')],
        [sg.Text(' '*23),sg.Button("  Descriptografar Arquivo  ")],
        [sg.Text(' '*90)],
        [sg.Text(' '*90)],
        [sg.Button("Voltar")],
        [sg.Text(' '*90)]
        ]

        janela1, janela2 = sg.Window("Descriptografar Arquivo", layout=layout, finalize=True), None

        while True:

            window,event,values = sg.read_all_windows()

            if window == janela1 and event == sg.WIN_CLOSED:
                sys.exit()

            if window == janela1 and event == '  Descriptografar Arquivo  ':

                if not values['senha-decript']:
                    sg.popup('Digite a senha', keep_on_top=True, title='Aviso')
                    Tela.Restart_Script()

                if not values['arquivo-decript']:
                    sg.popup('Nenhum arquivo foi selecionado', keep_on_top=True, title='Aviso')
                    Tela.Restart_Script()

                with open(values['arquivo-decript'], 'r') as ler_arquivo2:
                    arquivo_lido2 = ler_arquivo2.read()
                    decriptar = ct.decrypt(arquivo_lido2, values['senha-decript'])

                    if decriptar == False:
                        sg.popup('Senha Incorreta', keep_on_top=True, title='erro')
                        Tela.Restart_Script()

                with open(values['arquivo-decript'], 'wb') as escrever_arquivo2:
                    escrever_arquivo2.write(decriptar.encode('utf-8'))
                    escrever_arquivo2.close()
                    sg.popup('arquivo decriptado com sucesso')
                    Tela.Restart_Script()

            if window == janela1 and event == 'Voltar':
                Tela.Restart_Script()

    def Criptografar(): #Função para Criptografar os arquivos

        sg.theme('DarkGrey5')

        layout = [
        [sg.Text(' '*90)],
        [sg.Text(" "*6+"Simple Crypt", font=('Arial, 25'))],
        [sg.Text(" "*23+"_"*43, font=('Arial, 7'))],
        [sg.Text(' '*90)],
        [sg.Text(' '*90)],
        [sg.Text("           Local do Arquivo: "), sg.FilesBrowse(key='arquivo-cript')],
        [sg.Text(' '*90)],
        [sg.Text("           Senha:  "), sg.Input(key='senha-cript', size=(25,1))],
        [sg.Text('')],
        [sg.Text(' '*26),sg.Button("  Criptografar Arquivo  ")],
        [sg.Text(' '*90)],
        [sg.Text(' '*90)],
        [sg.Button("Voltar")],
        [sg.Text(' '*90)]
        ]

        janela1, janela2 = sg.Window("Criptografar Arquivo", layout=layout, finalize=True), None

        while True:

            window,event,values = sg.read_all_windows()

            if window == janela1 and event == sg.WIN_CLOSED:
                sys.exit()

            if window == janela1 and event == '  Criptografar Arquivo  ':

                if not values['senha-cript']:
                    sg.popup('Defina uma senha', keep_on_top=True, title='Aviso')
                    Tela.Restart_Script()

                if not values['arquivo-cript']:
                    sg.popup('Nenhum arquivo foi selecionado', keep_on_top=True, title='Aviso')
                    Tela.Restart_Script()

                with open(values['arquivo-cript'], 'r') as ler_arquivo:
                    arquivo_lido = ler_arquivo.read()
                    encriptar = ct.encrypt(arquivo_lido, values['senha-cript'])

                with open(values['arquivo-cript'], 'wb') as escrever_arquivo:
                    escrever_arquivo.write(encriptar.encode('utf-8'))
                    escrever_arquivo.close()
                    sg.popup('arquivo encriptado com sucesso')
                    Tela.Restart_Script()

            if window == janela1 and event == 'Voltar':
                Tela.Restart_Script()

    def Home():

        sg.theme('DarkGrey5')

        layout = [
        [sg.Text(' '*90)],
        [sg.Text(" "*6+"Simple Crypt", font=('Arial, 25'))],
        [sg.Text(" "*23+"_"*43, font=('Arial, 7'))],
        [sg.Text(' '*90)],
        [sg.Text(' '*90)],
        [sg.Text("       "), sg.Button("Criptografar", size=(13,2)), sg.Text("    "), sg.Button("Descriptografar", size=(13,2))],
        [sg.Text(' '*90)]
        ]

        janela1, janela2 = sg.Window("Simple Cript", layout=layout, finalize=True), None

        while True:

            window,event,values = sg.read_all_windows()

            if window == janela1 and event == sg.WIN_CLOSED:
                sys.exit()

            if window == janela1 and event == 'Criptografar':
                janela1.hide()
                janela2 = Tela.Criptografar()


            if window == janela1 and event == 'Descriptografar':
                janela1.hide()
                janela2 = Tela.Descriptografar()
Tela.Home()
