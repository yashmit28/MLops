def run() :
  tweakrunNO = open('/mlops/tweakrun.txt','r')
  tweakrun = int(tweakrunNO.read())
  tweakrunNO.close()
  if tweakrun == 0:
    x = [0,0,0,0,0]
    tweakrun = tweakrun + 1
    tweakrunNO = open('/mlops/tweakrun.txt','w')
    tweakrunNO.write(str(tweakrun))
    tweakrunNO.close()
  else :
    p = accuracyCompare()
    if p == 0 :
      x = [0,0,0,0,0]
    elif p == 1 :
      x = values(tweakrun)
      tweakrun = tweakrun + 1
      tweakrunNO = open('/mlops/tweakrun.txt','w')
      tweakrunNO.write(str(tweakrun))
      tweakrunNO.close()
  return x

#function to geet the tweaking parameters
def values(no_of_layers) :
  y = []
  if no_of_layers == 1:
    y.append(1)
    y.append(50)
    y.append(5)
    y.append(2)
    y.append(2)
  else:
    y = [0,0,0,0,0]
  return y


#function to compare the accuracy
def accuracyCompare():
  accuracyStored = open('/mlops/accuracy.txt','r')
  accuracy = float(accuracyStored.read())
  if accuracy < 0.988888 :
    return 1
  elif accuracy >= 0.988888:
    return 0