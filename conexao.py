# Importando Bibliotecas:
import paramiko
import os

# Dados de acesso
# OBS: No lugar dos '...' coleque:
address = '192.168.100.7' # IP do servidor
username = 'newman' # Usuario de acesso
password = 'newman' # Senha de acesso

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
            sftp_client.get('/home/newman/Backup/Personal.zip','Personal.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Personal.zip','/home/newman/Backup/Personal.zip')

    elif opcao_arquivo == 2:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get('/home/newman/Backup/Localhost.zip','Localhost.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Localhost.zip','/home/newman/Backup/Localhost.zip')

    elif opcao_arquivo == 3:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get('/home/newman/Backup/Documents.zip','Documents.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Documents.zip','/home/newman/Backup/Documents.zip')

    elif opcao_arquivo == 4:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get('/home/newman/Backup/Pictures.zip','Pictures.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Pictures.zip','/home/newman/Backup/Pictures.zip')

    elif opcao_arquivo == 5:
        print("1 --> Upload")
        print("2 --> Download")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("downloading...\n")
            sftp_client.get('/home/newman/Backup/Videos.zip','Videos.zip')
        elif opcao_transferir == 2:
            print("uploading...")
            sftp_client.put('Videos.zip','/home/newman/Backup/Videos.zip')

    elif opcao_arquivo == 6:
        print("1 --> Download")
        print("2 --> Upload")
        opcao_transferir = int(input("Selecione sua opção [1-2]: "))
        if opcao_transferir == 1:
            print("Download...\n")
            sftp_client.get('/home/newman/Backup/Personal.zip','Persona.zip')
            sftp_client.get('/home/newman/Backup/Localhost.zip','Localhost.zip')
            sftp_client.get('/home/newman/Backup/Documents.zip','Documents.zip')
            sftp_client.get('/home/newman/Backup/Pictures.zip','Pictures.zip')
            sftp_client.get('/home/newman/Backup/Videos.zip','Videos.zip')

        elif opcao_transferir == 2:
            print("downloading...")
            sftp_client.get('Personal.zip','/home/newman/Backup/Personal.zip')
            sftp_client.get('Localhost.zip','/home/newman/Backup/Localhost.zip')
            sftp_client.get('Documents.zip','/home/newman/Backup/Documents.zip')
            sftp_client.get('Pictures.zip','/home/newman/Backup/Pictures.zip')
            sftp_client.get('Videos.zip','/home/newman/Backup/Videos.zip')

    elif opcao_arquivo == 7:
        loop=False

    else:
        print("\nOpção incorreta. Tente novamente\n")
        loop = True

#Encerrando a conexão SSH
ssh.close()
#os.remove("ancora.txt")
