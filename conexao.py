# Importando Bibliotecas:
import paramiko
import os

# Dados de acesso
# OBS: No lugar dos '...' coleque:
address = '...' # IP do servidor
username = '...' # Usuario de acesso
password = '...' # Senha de acesso

# Criando a conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
sftp_client=ssh.open_sftp()

# Função com os Comandos
def Backup():

    print(30 * "-")

    print("""
|--Deretorios
|   |
|   |--Personal
|   |
|   |--Localhost
|   |
|   |--Documents
|   |
|   |--Pictures
|   |
|   |--Videos
|   |
          """)

    print("1 --> Personal")
    print("2 --> Localhost")
    print("3 --> Documents")
    print("4 --> Pictures")
    print("5 --> Videos")
    print("6 --> Todos")
    print("7 --> Sair")

    print(30 * "-")

loop = True

while loop:
    Backup()
    opcao = int(input("Selecione sua opção [1-7]: "))

    if opcao == 1:
        print("Transferindo Personal...\n")
        sftp_client.get('/home/public/backup/Personal.zip','Personal.zip')

    elif opcao_linguagem == 2:
        print("Transferindo Localhost...\n")
        sftp_client.get('/home/public/Backup/Localhost.zip','Localhost.zip')

    elif opcao_linguagem == 3:
        print("Transferindo Documents...\n")
        sftp_client.get('/home/public/Backup/Documents.zip','Documents.zip')

    elif opcao_linguagem == 4:
        print("Transferindo Pictures...\n")
        sftp_client.get('/home/public/Backup/Pictures.zip','Pictures.zip')

    elif opcao_linguagem == 5:
        print("Transferindo Videos...\n")
        sftp_client.get('/home/public/Backup/Videos.zip','Videos.zip')

    elif opcao_linguagem == 6:
        print("Transferindo Tudo...\n")
        sftp_client.get('/home/public/backup/Personal.zip','Personal.zip')
        sftp_client.get('/home/public/Backup/Localhost.zip','Localhost.zip')
        sftp_client.get('/home/public/Backup/Documents.zip','Documents.zip')
        sftp_client.get('/home/public/Backup/Pictures.zip','Pictures.zip')
        sftp_client.get('/home/public/Backup/Videos.zip','Videos.zip')

    elif opcao == 7:
        loop=False

    else:
        print("\nOpção incorreta. Tente novamente\n")
        loop = True

#Encerrando a conexão SSH
ssh.close()
os.remove("ancora.txt")
