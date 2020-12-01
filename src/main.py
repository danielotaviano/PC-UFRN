import sys
from getArgs import getArgs
from exceptions import raiseExceptions
from getNameFiles import getNameFiles
from getNames import getNames
from writeNames import writeNames


sys.argv.remove(sys.argv[0])
argv = sys.argv

if (len(argv) <= 1):
    raise Exception("Para executar o programa, passe os argumentos. ex: -i NomeDoArquivoDeOrigem.txt -o NomeDoArquivoDeSaida.txt") 

if ('-i' not in argv):
    raise Exception("Para execução do programa, é obrigatório a passagem do arquivo de origem como argumento. ex: -i NomeDoArquivoDeOrigem.txt") 

inputNameFile = ''
outputNameFile = ''

for i,e in enumerate(argv):
  if (e == '-i'):
    inputNameFile = argv[i+1]
  if (e == '-o'):
    outputNameFile = argv[i+1]

if (not outputNameFile):
  outputNameFile = 'sort_{a}'.format(a = inputNameFile)

names = []

f = open(inputNameFile,'r')

for name in f.read().split('\n'):
  names.append(name)

names.sort()

fs = open(outputNameFile, "w")
for name in names:
  fs.write(name + '\n' )

fs.close()

# args = getArgs()
# raiseExceptions(args)
# fileName, outputNameFile = getNameFiles(args)
# names = getNames(fileName)
# names.sort()
# writeNames(names,outputNameFile)

