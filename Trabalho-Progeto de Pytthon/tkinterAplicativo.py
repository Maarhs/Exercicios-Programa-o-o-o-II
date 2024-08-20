import tkinter as tk
import os
from tkinter import messagebox, simpledialog

aplicativo = []

def listar_nomes_arquivos():
    return aplicativo

def adicionar_nome_arquivo(nome_arquivo):
    if nome_arquivo and nome_arquivo not in aplicativo:
        aplicativo.append(nome_arquivo)
        messagebox.showinfo("Sucesso", f"O aplicativo '{nome_arquivo}' foi adicionado com sucesso.")
    else:
        messagebox.showwarning("Aviso", f"O aplicativo '{nome_arquivo}' já está na lista ou o nome é inválido.")

def buscar_nome_arquivo(nome_arquivo):
    return nome_arquivo in aplicativo

def remover_nome_arquivo(nome_arquivo):
    
    if nome_arquivo in aplicativo:
        aplicativo.remove(nome_arquivo)
        messagebox.showinfo("Sucesso", f"O aplicativo '{nome_arquivo}' foi removido com sucesso.")
    else:
        messagebox.showwarning("Aviso", f"O aplicativo '{nome_arquivo}' não está na lista.")

def abrir_arquivo_exe(nome_arquivo):
    if os.startfile(nome_arquivo):
        messagebox.showinfo("Abrir Aplicativo", f"Abrindo o aplicativo '{nome_arquivo}'...")
    else:
        messagebox.showwarning("Aviso", f"O aplicativo '{nome_arquivo}' não está na lista.")

def listar_aplicativos():
    nomes = listar_nomes_arquivos()
    if nomes:
        messagebox.showinfo("Lista de Aplicativos", "\n".join(nomes))
    else:
        messagebox.showinfo("Lista de Aplicativos", "Nenhum aplicativo na lista.")

def menu():
    
    root = tk.Tk()
    root.title("Gerenciador de Aplicativos")
    
    Butao_listar = tk.Button(root, text="Listar Aplicativos", command=listar_aplicativos)
    Butao_adicionar = tk.Button(root, text="Adicionar Aplicativo", command=lambda: adicionar_nome_arquivo(simpledialog.askstring("Adicionar", "Digite o nome do aplicativo a ser adicionado:")))
    Butao_buscar = tk.Button(root, text="Buscar Aplicativo", command=lambda: buscar_nome_arquivo(simpledialog.askstring("Buscar", "Digite o nome do aplicativo a ser buscado:")))
    Butao_remover = tk.Button(root, text="Remover Aplicativo", command=lambda: remover_nome_arquivo(simpledialog.askstring("Remover", "Digite o nome do aplicativo a ser removido:")))
    Butao_abrir = tk.Button(root, text="Abrir Aplicativo", command=lambda: abrir_arquivo_exe(simpledialog.askstring("Abrir", "Digite o nome do aplicativo para abrir:")))
    Butao_sair = tk.Button(root, text="Sair", command=root.quit)

    
    Butao_listar.pack(pady=15)
    Butao_adicionar.pack(pady=15)
    Butao_buscar.pack(pady=15)
    Butao_remover.pack(pady=15)
    Butao_abrir.pack(pady=15)
    Butao_sair.pack(pady=15)

    root.mainloop()

if __name__ == '__main__':
    menu()