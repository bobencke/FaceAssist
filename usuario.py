# Importando a biblioteca datetime
from datetime import datetime
# Importando a classe Pessoa
from pessoa import Pessoa 

# Criando a classe Usuario que herda da classe Pessoa
class Usuario(Pessoa):
    def __init__(self, id, senha, saldo):
        super().__init__(id, senha)
        self.saldo = saldo
        self.historico = []

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def adicionarTransacao(self, descricao):
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.historico.append(f'{data_hora} - {descricao}')

    def getHistorico(self):
        return self.historico