# Importando do Paramiko:
import paramiko
import os

# Dados de acesso
address = '192.168.100.7' # IP do servidor
username = 'newman' # Usuario de acesso
password = 'newman' # Senha de acesso

# Criando a conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
sftp_client=ssh.open_sftp()

# Função com os Comandos
def Menu_Linguagens():

    print(30 * "-")

    print("""
|--Linguagens
|   |
|   |--Go
|   |
|   |--Java
|   |
|   |--Python
|   |
          """)

    print("1 --> Go")
    print("2 --> Java")
    print("3 --> Python")
    print("4 --> Sair")

    print(30 * "-")

loop = True

while loop:
    Menu_Linguagens()
    opcao = int(input("Selecione sua opção [1-4]: "))

    if  opcao == 1:
        # Executando...
        print("versões da linguagem disponiveis para instalar:\n")
        print("1 --> go1.18.6.windows-386.msi")
        print("2 --> go1.19.1.windows-amd64.msi")
        print("3 --> voltar\n")

        opcao_linguagem = int(input("Selecione sua opção [1-3]: "))

        if opcao_linguagem == 1:
            sftp_client.get('/home/public/Linguagens/Go/go1.18.6.windows-386.msi','go1.18.6.windows-386.msi')

        elif opcao_linguagem == 2:
            sftp_client.get('/home/public/Linguagens/Go/go1.19.1.windows-amd64.msi','go1.19.1.windows-amd64.msi')

        elif opcao_linguagem == 3:
            loop = True

        else:
            print("\nOpção incorreta. Tente novamente\n")

    elif opcao == 2:
        # Executando...
        print("versões da linguagem disponiveis para instalar:\n")
        print("1 --> JavaSetup8u341.exe")
        print("2 --> jre-7u64-winodws-i586.exe")
        print("3 --> voltar\n")

        opcao_linguagem = int(input("Selecione sua opção [1-3]: "))

        if opcao_linguagem == 1:
            sftp_client.get('/home/public/Linguagens/Java/JavaSetup8u341.exe','JavaSetup8u341.exe')

        elif opcao_linguagem == 2:
            sftp_client.get('/home/public/Linguagens/Java/jre-7u64-winodws-i586.exe','jre-7u64-winodws-i586.exe')

        elif opcao_linguagem == 3:
            loop = True

        else:
            print("\nOpção incorreta. Tente novamente\n")

    elif opcao == 3:
        # Executando...
        print("versões da linguagem disponiveis para instalar:\n")
        print("1 --> python-3.10.7-amd64.exe")
        print("2 --> python-3.9.6-amd64.exe")
        print("3 --> voltar\n")

        opcao_linguagem = int(input("Selecione sua opção [1-3]: "))

        if opcao_linguagem == 1:
            sftp_client.get('/home/public/Linguagens/Python/python-3.10.7-amd64.exe','python-3.10.7-amd64.exe')

        elif opcao_linguagem == 2:
            sftp_client.get('/home/public/Linguagens/Python/python-3.9.6-amd64.exe','python-3.9.6-amd64.exe')

        elif opcao_linguagem == 3:
            loop = True

        else:
            print("\nOpção incorreta. Tente novamente\n")

    elif opcao == 4:
        loop=False

    else:
        print('\nOpção incorreta. Tente novamente\n')

#Encerrando a conexão SSH
ssh.close()
os.remove("ancora.txt")

