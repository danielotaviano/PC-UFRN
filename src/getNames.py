def getNames(FileName):
  names = []
  f = open(FileName,'r')

  for name in f.read().split('\n'):
    names.append(name)

  return names

