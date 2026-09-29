from usuario import Usuario

# Define a classe GerenciadorUsuarios para gerenciar uma lista de usuários
class GerenciadorUsuarios:
    # Função construtora que inicializa a classe
    def __init__(self, arquivo='usuarios.txt'):
        self.arquivo = arquivo  # Define o nome do arquivo que armazena os dados dos usuários
        self.usuarios = self.ler_usuarios_do_arquivo()  # Chamada da função para ler os usuários do arquivo

    # Método para ler os usuários do arquivo
    def ler_usuarios_do_arquivo(self):
        usuarios = []  # Inicializa uma lista vazia para armazenar os usuários
        try:
            with open(self.arquivo, 'r') as file:  # Abre o arquivo em modo de leitura
                for linha in file:  # Itera sobre cada linha do arquivo
                    id, senha, saldo = linha.strip().split(',')  # Remove espaços em branco e divide a linha por vírgulas
                    usuarios.append(Usuario(id, senha, float(saldo)))  # Cria um objeto Usuario e adiciona à lista de usuários
        except FileNotFoundError:  # Caso o arquivo não seja encontrado
            print(f"O arquivo {self.arquivo} não foi encontrado. Inicializando com uma lista vazia.")  # Imprime uma mensagem de erro
        return usuarios  # Retorna a lista de usuários carregados

    # Método para salvar os usuários no arquivo
    def salvar_usuarios_no_arquivo(self):
        # Abre o arquivo em modo de escrita
        with open(self.arquivo, 'w') as file:  
             # Itera sobre cada usuário na lista de usuários
            for usuario in self.usuarios: 
                # Escreve cada usuário no arquivo no formato id,senha,saldo
                file.write(f"{usuario.id},{usuario.senha},{usuario.saldo}\n")  

    # Método getter para retornar a lista de usuários
    def getUsuarios(self):
        return self.usuarios

    # Método setter para atualizar a lista de usuários
    def setUsuarios(self, usuarios):
        self.usuarios = usuarios
        self.salvar_usuarios_no_arquivo()