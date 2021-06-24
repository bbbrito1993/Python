def escrever_arquivo(texto):
    arquivo = open('Arquivo_com_def.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Textando a brincadeira.\n')
    aluno = 'Benedito, 10 , 10, 10, 10'
    atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('Arquivo_com_def.txt')