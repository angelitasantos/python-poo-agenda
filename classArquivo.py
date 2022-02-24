from classValidacoes import *
from classInterface import *

nome_arquivo = 'contatos.txt'


class Arquivo:

    def __init__(self, arquivo):
        self.arquivo = arquivo


    def analisar_arquivo_existe(self, nome):
        try:
            arquivo = open(nome, 'rt')
            arquivo.close()
        except FileNotFoundError:
            return False
        else:
            return True
    

    def criar_arquivo(self, nome):
        try:
            arquivo = open(nome, 'wt+')
            arquivo.close()
        except:
            print(f'\n{bgColor[1]}ERRO! Ocorreu um erro ao criar o arquivo.{bgColor[0]}\n')
        else:
            print(f'\n{bgColor[2]}Arquivo {nome} criado com sucesso.{bgColor[0]}\n')

        
    def ler_arquivo(self, nome):
        try:
            arquivo = open(nome, 'rt')
        except:
            print(f'\n{bgColor[1]}ERRO! Confira se o arquivo existe.{bgColor[0]}\n')
        else:
            Interface.imprimir_cabecalho_interno(self, 'CONTATOS CADASTRADOS')
            print(f'{bgColor[4]}{"NOME":<20}{"EMAIL":<33}{"TELEFONE":<17} {"CIDADE":<25}{"UF":<4}{bgColor[0]}')
            print(Interface.incrementar_linha(self, tamanho, '~'))
            for linha in arquivo:
                informacao = linha.split(';')
                informacao[4] = informacao[4].replace('\n', '')
                print(f'{informacao[0]:<20}{informacao[1]:<33}{informacao[2]:>17} {informacao[3]:<25}{informacao[4]:<3}')
            print()
        finally:
            arquivo.close()

    
    def cadastrar_contato(self, arquivo, nome='desconhecido', email='', telefone='', cidade='', estado=''):
        try:
            arquivo = open(arquivo, 'at')
        except:
            print(f'\n{bgColor[1]}ERRO! Ocorreu um erro ao abrir o arquivo.{bgColor[0]}\n')
        else:
            try:
                arquivo.write(f'{nome};{email};{telefone};{cidade};{estado}\n')
            except:
                print(f'\n{bgColor[1]}ERRO! Ocorreu um erro ao incluir os dados.{bgColor[0]}\n')
            else:
                print(f'\n{bgColor[2]}Cadastro efetuado com sucesso.{bgColor[0]}')
                print(f'{bgColor[2]}{nome} adicionado(a) aos contatos.{bgColor[0]}\n')
                arquivo.close()