from classArquivo import *
from classInterface import *
from classValidacoes import *
from time import sleep


self = 'self'
arquivo = nome_arquivo
print()
Interface.imprimir_cabecalho_sistema(self, 'AGENDA DE CONTATOS')
lista_menu_principal = [
                        'Criar Arquivo', 
                        'Adicionar Contatos', 
                        'Listar Contatos', 
                        'Sair da Agenda'
                        ]


while True:
    resposta = Interface.apresentar_menu_principal(self, lista_menu_principal)

    if resposta == 1:
        Interface.imprimir_cabecalho_interno(self, 'CRIAR UM NOVO ARQUIVO')
        if not Arquivo.analisar_arquivo_existe(self, arquivo):
            print(f'{fontColor[1]}Criando arquivo ...')
            sleep(2)
            Arquivo.criar_arquivo(self, arquivo)
        else:
            sleep(1)
            print(f'{fontColor[2]}\nArquivo já existe.{fontColor[0]}\n')


    elif resposta == 2:
        Interface.imprimir_cabecalho_interno(self, 'NOVO CADASTRO')

        nome = str(input('Nome: ')).strip().upper()
        email = str(input('E-mail: ')).strip().lower()
        telefone = str(input('Telefone: ')).strip()
        cidade = str(input('Cidade: ')).strip().upper()
        estado = str(input('Estado: ')).strip().upper()
        
        sleep(1)
        Arquivo.cadastrar_contato(self, arquivo, nome, email, telefone, cidade, estado)


    elif resposta == 3:
        sleep(1)
        if not Arquivo.analisar_arquivo_existe(self, arquivo):
            print(f'{fontColor[1]}\nO arquivo {arquivo} não existe.{fontColor[0]}\n')
        else:
            sleep(1)
            Arquivo.ler_arquivo(self, arquivo)
        

    elif resposta == 4:
        print(f'{fontColor[1]}\nSaindo do Sistema ...\n')
        sleep(2)
        Interface.imprimir_cabecalho_interno(self, f'Até breve!', fontColor[1])
        break


    else:
        print(f'{bgColor[1]}ERRO: Por favor, digite uma opção válida!{bgColor[0]}')