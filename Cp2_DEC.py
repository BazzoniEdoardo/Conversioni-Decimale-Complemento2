def convertiCp(x):
  x = int(x)
  if x>0:
    x = bin(x).split("0b")
    x = str(x).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
    xlen = len(x)
    cm = 7-xlen
    if cm == 0:
      x = "0" + x
      return x
    elif cm < 0:
      return "Imposibile convertire con 8 bit"
    else:
      string = ""
      for i in range(cm):
        string = string + "0"
      x = string + x
      x = "0" + x
      return x
  elif x == -1:
    return 11111111
  else:
    lista = ["1"]
    x = x * (-1)
    x = bin(x).split("0b")
    x = str(x).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace(",", "")
    xlen = len(x)
    cm = 7-xlen
    if cm == 0:
      x = list(x)
      for i in range(len(x)):
        if x[i] == "1":
          x[i] = "0"
        else:
          x[i] = "1"

      if x[-1] == "0":
        x[-1] = "1"
        x = lista + x
        return "".join(x)
      else:
        x[-1] = "0"
        run = True
        i = 1
        while run:
          i += 1 
          if x[-i] == "1":
            x[-i] = "0"
          else:
            x[-i] = "1"
            run = False
        x = lista + x
        return "".join(x)
    elif cm < 0:
      return "Impossibile convertire con 8 bit"
    else:
      string = ""
      for i in range(cm):
        string = string + "0"
      x = string + x
      x = list(x)
      for i in range(len(x)):
        if x[i] == "1":
          x[i] = "0"
        else:
          x[i] = "1"
      
      if x[-1] == "0":
        x[-1] = "1"
        x = lista + x
        return "".join(x)
      else:
        x[-1] = "0"
        run = True
        i = 1
        while run:
          i += 1
          if x[-i] == "1":
            x[-i] = "0"
          else:
            x[-i] = "1"
            run = False
        x = lista + x
        return "".join(x)

 
res = input()
print(convertiCp(res))