import os

lista_arquivos = []

def abrir_arquivo_exe(nome_arquivo):
    if nome_arquivo in lista_arquivos:
        os.startfile(nome_arquivo)
    else:
        print(f"O arquivo {nome_arquivo} não está na lista.")

def adicionar_nome_arquivo(nome_arquivo):
    if nome_arquivo not in lista_arquivos:
        lista_arquivos.append(nome_arquivo)
        print(f" arquivo '{nome_arquivo}' adicionado com sucesso.")
    else:
        print(f" '{nome_arquivo}' já está na lista.")

def listar_nomes_arquivos():
    return lista_arquivos

def buscar_nome_arquivo(nome_arquivo):
    if nome_arquivo in lista_arquivos:
        return True
    return False

def remover_nome_arquivo(nome_arquivo):
    if nome_arquivo in lista_arquivos:
        lista_arquivos.remove(nome_arquivo)
        print(f" arquivo '{nome_arquivo}' removido com sucesso.")
    else:
        print(f" '{nome_arquivo}' não está na lista.")