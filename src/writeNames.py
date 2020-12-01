def writeNames(names,outputNameFile):
  fs = open(outputNameFile, "w")
  for name in names:
    fs.write(name + '\n' )

  fs.close()