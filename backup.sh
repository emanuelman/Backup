#!/usr/bin/env bash

#Esta funcao é pra ser utilizada antes de formatar o pc
function compactar(){
echo "
----------------------------
Compactando os Diretórios...
----------------------------
"
sleep 1s

caminho=~/Backup
if [ ! -d "$caminho" ]; then
    echo "O diretorio 'Backup' ainda não existe"
    echo "Criando diretorio Backup..."
    mkdir ~/Backup
    #echo "Diretorio não existe!"
else
    echo "O diretorio 'Backup' já existe"
    #echo "Diretorio existe"
fi

cd ~/Desktop
zip Personal.zip -r Personal -6
sudo mv Personal.zip ~/Backup
cd ~
zip Documents.zip -r Documents -6
zip Videos.zip -r Videos -6
zip Pictures.zip -r Pictures -6
sudo mv Documents.zip Videos.zip Pictures.zip ~/Backup
cd /var/www
sudo zip Localhost.zip -r html -6
sudo mv Localhost.zip ~/Backup
}

#Esta funcao é pra ser utilizada logo apos formatar o pc
function descompactar(){
#Personal
sudo mv ~/Backup/Personal.zip ~/Desktop
cd ~/Desktop
unzip Personal
#Documents, Videos e Pictures
cd ~
rm -rf Documents Videos Pictures
sudo mv ~/Backup/Documents.zip ~/Backup/Videos.zip ~/Backup/Pictures.zip ~
unzip Documents.zip Videos.zip Pictures.zip
#Localhost
sudo mv ~/Backup/Localhost.zip /var/www/html
cd /var/www/html
sudo unzip Localhost.zip
#Criar links simbolicos
ln -s ~/Desktop/Personal/Calistenia calistenia
ln -s Desktop/Personal/Projetos projetos
ln -s ~/Desktop/Personal/Estudos estudos
sudo ln -s /var/www/html localhost
}

compactar
descompactar
