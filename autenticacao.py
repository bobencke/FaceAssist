from usuario import Usuario

class Autenticacao:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def inserirCartao(self):
        idCartao = input('Insira o ID de seu cartão: ')

        for usuario in self.usuarios:
            if idCartao == usuario.getId():
                print(f'Entrando na conta de ID {usuario.getId()}...')
                return usuario

        print('\nNão foi identificada a conta.')
        return None

    def inserirSenha(self, usuario):
        if usuario is None:
            print('Nenhum usuário foi identificado.')
            return False

        tentativas = 4
        while tentativas > 0:
            senha = input('Digite sua senha: ')
            if senha == usuario.getSenha():
                return True
            else:
                tentativas -= 1
                if tentativas > 0:
                    print(f'Senha incorreta. Você possui mais {tentativas} restantes.')

        print('Número máximo de tentativas excedido. Conta bloqueada.')
        exit()