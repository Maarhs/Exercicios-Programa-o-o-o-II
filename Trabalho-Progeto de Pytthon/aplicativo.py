from funcoes import *


def menu():
    while True:

        print('''
              
    \\\\Menu////

1. Listar  aplicativo
2. Adicionar aplicativo
3. Buscar  aplicativo
4. Remover aplicativo
5. abrir aplicativo
5. sair..
              ''')
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            nomes = listar_nomes_arquivos()
            print("\nNomes de aplicativo na lista:")
            for nome in nomes:
                print(nome)
        
        elif opcao == '2':
            nome_arquivo = input("Digite o nome do aplicativo a ser adicionado: ")
            adicionar_nome_arquivo(nome_arquivo)
        
        elif opcao == '3':
            nome_arquivo = input("Digite o nome do aplicativo a ser buscado: ")
            encontrado = buscar_nome_arquivo(nome_arquivo)
            if encontrado:
                print(f"O nome '{nome_arquivo}' foi encontrado na lista.")
            else:
                print(f"O nome '{nome_arquivo}' não está na lista.")
        
        elif opcao == '4':
            nome_arquivo = input("Digite o nome do aplicativo a ser removido: ")
            remover_nome_arquivo(nome_arquivo)
        
        elif opcao == '5':
            nome_arquivo = input("Digite o nome do aplicativo para abrir: ")
            abrir_arquivo_exe(nome_arquivo)

        elif opcao == '6':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()