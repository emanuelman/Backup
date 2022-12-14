# Importando Bibliotecas:
import paramiko
import os

# Dados de acesso
# OBS: No lugar dos '...' coleque:
address = '...' # IP do servidor
username = '...' # Usuario de acesso
password = '...' # Senha de acesso

#variaveis para armazenar a ponte de diretorio do servidor
server_personal="/home/newman/Backup/Personal.zip"
server_localhost="/home/newman/Backup/Localhost.zip"
server_documents="/home/newman/Backup/Documents.zip"
server_pictures="/home/newman/Backup/Pictures.zip"
server_videos="/home/newman/Backup/Videos.zip"

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

    print("1 --> Personal.zip")
    print("2 --> Localhost.zip")
    print("3 --> Documents.zip")
    print("4 --> Pictures.zip")
    print("5 --> Videos.zip")
    print("6 --> Todos.zip")
    print("7 --> Sair")

    print(30 * "-")

loop = True

while loop:
    Backup()
    opcao_arquivo = int(input("Selecione sua opção [1-7]: "))

    if opcao_arquivo == 1:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_personal,'Personal.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Personal.zip',server_personal)

    elif opcao_arquivo == 2:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_localhost,'Localhost.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Localhost.zip',server_localhost)

    elif opcao_arquivo == 3:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_documents,'Documents.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Documents.zip',server_documents)

    elif opcao_arquivo == 4:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_pictures,'Pictures.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Pictures.zip',server_pictures)

    elif opcao_arquivo == 5:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_videos,'Videos.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Videos.zip',server_videos)

    elif opcao_arquivo == 6:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get(server_personal,'Personal.zip')
            sftp_client.get(server_localhost,'Localhost.zip')
            sftp_client.get(server_documents,'Documents.zip')
            sftp_client.get(server_pictures,'Pictures.zip')
            sftp_client.get(server_videos,'Videos.zip')

        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Personal.zip',server_personal)
            sftp_client.put('Localhost.zip',server_localhost)
            sftp_client.put('Documents.zip',server_documents)
            sftp_client.put('Pictures.zip',server_pictures)
            sftp_client.put('Videos.zip',server_videos)

    elif opcao_arquivo == 7:
        loop=False

    else:
        print("\nOpção incorreta. Tente novamente\n")
        loop = True

#Encerrando a conexão SSH
ssh.close()
#os.remove("ancora.txt")
