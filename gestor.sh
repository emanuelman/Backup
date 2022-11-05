#!/bin/sh
# Gerencia o arquivo 'conexao.py'

python "conexao.py"

while :
do

    if [[ -e go1.18.6.windows-386.msi ]]; then
        # go1.18.6.windows-386.msi /quiet
        echo "arquivo instalado"
        #rm -f go1.18.6.windows-386.msi
    fi

    if [[ -e go1.19.1.windows-amd64.msi ]]; then
        # go1.19.1.windows-amd64.msi /quiet
        echo "arquivo instalado"
        #rm -f go1.19.1.windows-amd64.msi
    fi

    if [[ -e JavaSetup8u341.exe ]]; then
        # JavaSetup8u341.exe /quiet
        echo "arquivo instalado"
        #rm -f JavaSetup8u341.exe
    fi

    if [[ -e jre-7u67-windows-i586.exe ]]; then
        # jre-7u67-windows-i586.exe /quiet
        echo "arquivo instalado"
        #rm -f jre-7u67-windows-i586.exe
    fi

    if [[ -e python-3.10.7-amd64.exe ]]; then
        # python-3.10.7-amd64.exe /quiet
        echo "arquivo instalado"
        #rm -f python-3.10.7-amd64.exe
    fi

    if [[ -e python-3.9.6-amd64.exe ]]; then
        # python-3.9.6-amd64.exe /quiet
        echo "arquivo instalado"
        #rm -f python-3.9.6-amd64.exe
    fi

    if [[ -e ancora.txt ]]; then
        echo ""
    else
        break;
    fi

done

touch ancora.txt
echo "Execucao finalizada!"

