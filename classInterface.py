import datetime
data_hora_atuais = datetime.datetime.now()
data_hora_pt_BR = data_hora_atuais.strftime(' %d/%m/%Y %H:%M:%S')

from classValidacoes import *


tamanho = 100


class Interface:

    def __init__(self, cores):
        self.cores = cores


    def incrementar_linha(self, tamanho=42, caracter='-'):
        return caracter * tamanho


    def imprimir_cabecalho_sistema(self, texto='', versao='v1.0 '):
        tam = int(tamanho / 2)
        caracter = '='
        print(f'{bgColor[2]}{Interface.incrementar_linha(self, tamanho, caracter)}{bgColor[0]}')
        texto = texto.center(tamanho)
        print(f'{bgColor[2]}{texto}{bgColor[0]}')
        print(f'{bgColor[2]}{data_hora_pt_BR.ljust(tam)}{versao.rjust(tam)}{bgColor[0]}')
        print(f'{bgColor[2]}{Interface.incrementar_linha(self, tamanho, caracter)}{bgColor[0]}')


    def imprimir_cabecalho_interno(self, texto='', cor=(bgColor[0])):
        print(Interface.incrementar_linha(self, tamanho))
        print(texto.center(tamanho), cor)
        print(Interface.incrementar_linha(self, tamanho))


    def apresentar_menu_principal(self, lista):
        Interface.imprimir_cabecalho_interno(self, 'MENU PRINCIPAL')
        contador = 1
        for item in lista:
            print(f'{fontColor[3]}{contador:>10}{bgColor[0]} - {fontColor[4]}{item}{bgColor[0]}')
            contador += 1
        print(Interface.incrementar_linha(self, tamanho, '~'))
        opcao = Validacoes.validar_inteiro(self, f'{fontColor[3]}Sua Opção: {bgColor[0]}')
        return opcao