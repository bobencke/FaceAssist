from autenticacao import Autenticacao
from faceassist import *
from gerenciadorUsuarios import GerenciadorUsuarios
from operacoes import Operacoes

def main():
    gerenciaUsuarios = GerenciadorUsuarios()
    usuarios = gerenciaUsuarios.getUsuarios()

    autenticacao = Autenticacao(usuarios)
    usuarioLogado = autenticacao.inserirCartao()
    
    if usuarioLogado is not None:
        operacoes = Operacoes(usuarioLogado, usuarios)

        while True:
            #Inicializa interface tekinter
            root = tk.Tk()
            app = FaceAssist(root)

            print("x--------------------------------x")
            print("|   1 - Saldo                    |")
            print("|   2 - Extrato                  |")
            print("|   3 - Saque                    |")
            print("|   4 - Depósito                 |")
            print("|   5 - Pagamento de Boleto      |")
            print("|   6 - Transferência            |")
            print("|   0 - Sair                     |")
            print("x--------------------------------x")
            #Switch case para o menu
            op = int(input('Opção: '))

            if op == 1:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.saldo()
            elif op == 2:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.extrato()
            elif op == 3:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.saque()
            elif op == 4:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.deposito()
            elif op == 5:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.pagamentoDeBoleto()
            elif op == 6:
                if autenticacao.inserirSenha(usuarioLogado):
                    operacoes.transferencia()
            elif op == 0:
                main()
            else:
                print('Opção inválida')

            root.mainloop()

main()