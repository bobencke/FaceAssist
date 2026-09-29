from usuario import Usuario

# Define a classe Operacoes para realizar operações de saque, depósito, pagamento de boleto e transferencia
class Operacoes:
    # Função construtora que inicializa a classe
    def __init__(self, usuario, usuarios):
        # Define o usuário logado
        self.usuario = usuario
        # Define a lista de usuários
        self.usuarios = usuarios

    # Método para realizar o saque
    def saldo(self):
        # Imprime o saldo do usuário
        print(f'Você possui um saldo total de: R$ {self.usuario.getSaldo()}.')

    # Método para realizar o depósito
    def extrato(self):
        # Obtém o histórico de transações do usuário
        historico = self.usuario.getHistorico()
        # Se histórico retornar vazio
        if not historico: 
            # Imprime mensagem de erro
            print("Nenhuma transação realizada.") 
        # Caso contrário imprime o histórico
        else: 
            print("Extrato de transações:")
            # Itera sobre cada transação no histórico
            for transacao in historico:
                # Imprime a transação
                print(transacao) 

    # Método para realizar o pagamento de boleto
    def saque(self):
        # Solicita ao usuário o valor do saque
        valor = float(input("Digite o valor do saque: "))
        # Se o valor for maior que o saldo
        if valor > self.usuario.getSaldo(): 
            # Imprime mensagem de erro
            print("Saldo insuficiente.") 
        else: # Caso contrário
            # Atualiza o saldo do usuário
            self.usuario.setSaldo(self.usuario.getSaldo() - valor) 
            # Adiciona a transação ao histórico
            self.usuario.adicionarTransacao(f'Saque de R$ {valor}') 
            print("Saque realizado com sucesso.")

    # Método para realizar a transferência
    def deposito(self):
         # Solicita ao usuário o valor do depósito
        valor = float(input("Digite o valor do depósito: "))
        # Atualiza o saldo do usuário
        self.usuario.setSaldo(self.usuario.getSaldo() + valor) 
        # Adiciona a transação ao histórico
        self.usuario.adicionarTransacao(f'Depósito de R$ {valor}') 
        print("Depósito realizado com sucesso.")

    # Método para realizar o pagamento de boleto
    def pagamentoDeBoleto(self):
        # Solicita ao usuário o valor do pagamento
        valor = float(input("Digite o valor do pagamento: ")) 
        # Se o valor for maior que o saldo
        if valor > self.usuario.getSaldo(): 
            # Imprime mensagem de erro
            print("Saldo insuficiente.") 
        else: # Caso contrário
            # Solicita ao usuário o código do boleto
            codigo_boleto = input("Digite o código do boleto: ") 
            # Atualiza o saldo do usuário
            self.usuario.setSaldo(self.usuario.getSaldo() - valor) 
            # Adiciona a transação ao histórico
            self.usuario.adicionarTransacao(f'Pagamento de boleto {codigo_boleto} no valor de R$ {valor}') 
            print("Pagamento realizado com sucesso.")

    # Método para realizar a transferência
    def transferencia(self):
        # Solicita ao usuário o valor da transferência
        valor = float(input("Digite o valor da transferência: "))
        # Se o valor for maior que o saldo
        if valor > self.usuario.getSaldo(): 
            # Imprime mensagem de erro
            print("Saldo insuficiente.") 
        else: # Caso contrário
            # Solicita ao usuário o ID da conta de destino
            id_destino = input("Digite o ID da conta de destino: ") 
            # Se o ID for o mesmo do usuário
            if self.usuario.getId() == id_destino: 
                # Imprime mensagem de erro
                print("Não é possível realizar transferência para a conta de origem.") 
            # Caso contrário
            else: 
                # Define uma variável para armazenar o usuário de destino
                usuario_destino = None 
                # Itera sobre cada usuário na lista de usuários
                for usuario in self.usuarios: 
                    # Se o ID for igual ao ID da conta de destino
                    if usuario.getId() == id_destino: 
                        # Define o usuário de destino
                        usuario_destino = usuario 
                        break
                # Se usuário de destino for None
                if usuario_destino is None: 
                    # Imprime mensagem de erro
                    print("Conta de destino não encontrada.")
                else: # Caso contrário
                    # Atualiza o saldo do usuário
                    self.usuario.setSaldo(self.usuario.getSaldo() - valor)
                    # Atualiza o saldo do usuário de destino
                    usuario_destino.setSaldo(usuario_destino.getSaldo() + valor)
                    # Adiciona a transação ao histórico
                    self.usuario.adicionarTransacao(f'Transferência de R$ {valor} para a conta de ID {id_destino}') 
                    # Adiciona a transação ao histórico
                    usuario_destino.adicionarTransacao(f'Recebimento de transferência de R$ {valor} da conta de ID {self.usuario.getId()}') 
                    print("\nTransferência realizada com sucesso.")