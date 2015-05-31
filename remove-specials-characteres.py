#!/usr/bin/env python
# *-* coding: utf-8

import os
from os import walk

# Seta os nomes dos diretórios
initialDirectory = 'input'
finalDirectory = 'output'

# Caso, não existam os diretórios são criados
if not os.path.exists(initialDirectory):
    os.makedirs(initialDirectory)

if not os.path.exists(finalDirectory):
    os.makedirs(finalDirectory)

# Pega a lista de legendas
fileList = []
for (dirpath, dirnames, filenames) in walk(initialDirectory):
    fileList.extend(filenames)
    break

# Itera sobre as legendas, realizando a conversão
for x in range(1, len(fileList)):
    if x == 1:
        os.chdir(initialDirectory)
    else:
        os.chdir('../' + initialDirectory)

    subtitleFile = open(fileList[x], "rb")
    content = subtitleFile.read()

    # Apenas para visualizar a legenda corrente.
    print content

    content = content.replace("á", "a").replace("ã", "a").replace("à", "a").replace(" é ", " eh ").replace("é", "e").replace("ê", "e")
    content = content.replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ô", "o").replace("Ú", "U").replace("Ã", "A")
    content = content.replace("á", "A").replace(" É ", " Eh ").replace("Ê", "E").replace("Í", "I").replace("Ó", "O").replace("Ô", "O")
    content = content.replace("ç", "c")

    os.chdir('../' + finalDirectory)
    newFile = open(subtitleFile.name, "w")
    newFile.write(content)
