#!/usr/bin/env bash

function compactar(){
echo "
----------------------------
Compactando os Diretórios...
----------------------------
"
sleep 1s
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

function organizar(){
cd ~
rm -rf Documents Videos Pictures
sudo mv Personal.zip ~/Desktop
unzip Personal
sudo mv Documents.zip Videos.zip Pictures.zip ~
unzip Documents.zip Videos.zip Pictures.zip
sudo mv Localhost.zip /var/www/
ln -s ~/Desktop/Personal/Calistenia calistenia
ln -s Desktop/Personal/Projetos projetos
ln -s ~/Desktop/Personal/Estudos estudos
#ln -s /var/www/html localhost
}

compactar
#organizar
