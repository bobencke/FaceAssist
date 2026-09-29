# Classe mãe responsável por definir os atributos de uma pessoa
class Pessoa:
  def __init__(self, id, senha):
      self.id = id
      self.senha = senha

  def getId(self):
      return self.id

  def setId(self, id):
      self.id = id

  def getSenha(self):
      return self.senha

  def setSenha(self, senha):
      self.senha = senha