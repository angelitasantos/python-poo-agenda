bgColor = (
    '\033[m',               # 0 - sem cor
    '\033[0;30;41m',        # 1 - vermelho
    '\033[0;30;42m',        # 2 - verde
    '\033[0;30;43m',        # 3 - amarelo
    '\033[0;30;44m',        # 4 - azul
    '\033[0;30;45m',        # 5 - roxo
    '\033[7;30m',           # 6 - branco
)

fontColor = (
    '\033[m',               # 0 - sem cor
    '\033[31m',             # 1 - vermelho
    '\033[32m',             # 2 - verde
    '\033[33m',             # 3 - amarelo
    '\033[34m',             # 4 - azul
    '\033[35m',             # 5 - roxo
    '\033[30m',             # 6 - branco
)


class Validacoes:

    def __init__(self, validacao):
        self.validacao = validacao


    def validar_inteiro(self, mensagem=''):
        while True:
            try:
                numero = int(input(mensagem))
            except (ValueError, TypeError):
                print(f'{bgColor[1]}ERRO: Por favor, digite um número inteiro!{bgColor[0]}')
                continue
            except (KeyboardInterrupt):
                print(f'{bgColor[1]}Usuário não digitou um número válido.{bgColor[0]}')
                return 0
            else:
                return numero


    def validar_numero_real(self, mensagem=''):
        while True:
            try:
                numero = float(input(mensagem))
            except (ValueError, TypeError):
                print(f'{bgColor[1]}ERRO: Por favor, digite um número real!{bgColor[0]}')
                continue
            except (KeyboardInterrupt):
                print(f'{bgColor[1]}Usuário não digitou um número válido.{bgColor[0]}')
                return 0
            else:
                return numero