def getNameFiles(argv):
  nameFile = ''
  outputNameFile = ''
  for e,i in enumerate(argv):
    if (i == '-i'):
      nameFile = argv[e+1]
    if (i == '-o'):
      outputNameFile = argv[e+1]

  if (not outputNameFile):
    outputNameFile = f'{nameFile}_sort.txt'
  return nameFile,outputNameFile



