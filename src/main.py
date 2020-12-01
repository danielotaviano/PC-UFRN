import sys
from exceptions import raiseExceptions
from getNameFiles import getNameFiles

def getArgs():
  sys.argv.remove(sys.argv[0])
  return sys.argv
def excep (argv):
  if (len(argv) <= 1):
    raise Exception("Para executar o programa, passe os argumentos. ex: -i NomeDoArquivoDeOrigem.txt -o NomeDoArquivoDeSaida.txt") 

  if ('-i' not in argv):
    raise Exception("Para execução do programa, é obrigatório a passagem do arquivo de origem como argumento. ex: -i NomeDoArquivoDeOrigem.txt") 
  
inputNameFile = ''
outputNameFile = ''

def getNamesFiles(argv):
  nameFile = ''
  outputNameFile = ''

  for i,e in enumerate(argv):
    if (e == '-i'):
      inputNameFile = argv[i+1]
    if (e == '-o'):
      outputNameFile = argv[i+1]

  if (not outputNameFile):
    outputNameFile = 'sort_{nameFile}'.format(nameFile = inputNameFile)
  return nameFile,outputNameFile

def getNames(FileName):
  names = []
  f = open(FileName,'r',encoding = 'utf8')

  for name in f.read().split('\n'):
    names.append(name)
  return names  

def writeNames(names,outputNameFile):
  fs = open(outputNameFile,'w',encoding = 'utf8')
  for name in names:
    fs.write(name + '\n' )
  fs.close()

args = getArgs()
excep(args)
fileName, outputNameFile = getNameFiles(args)
names = getNames(fileName)
names.sort()
writeNames(names,outputNameFile)

