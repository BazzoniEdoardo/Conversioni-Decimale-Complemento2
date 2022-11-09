def convertiDec(x):
    if len(x) > 8:
        return "Impossibile convertire con 8 bit"
    elif len(x) < 0:
        return "Numero non convertito in Complemento 2"
    else:
        if int(str(x[0])) == 1:
            x = list(x)
            del x[0]
            if x[-1] == "1":
                x[-1] = "0"
                for i in range(len(x)):
                    if x[i] == "1":
                        x[i] = "0"
                    else:
                        x[i] = "1"
                x = "".join(x)
                x = int(x)
                x = int(str("0b") + str(x), 2)
                x = x * (-1)
                return x
            else:
                x[-1] = "1"
                run = True
                i = 1
                while run:
                    i += 1
                    if x[-i] == "0":
                        x[-i] = "1"
                    else:
                        x[-i] = "0"
                        run = False
                i = 0
                for i in range(len(x)):
                    if x[i] == "1":
                        x[i] = "0"
                    else:
                        x[i] = "1"
                x = "".join(x)
                x = int(x)
                x = int(str("0b") + str(x), 2)
                x = x * (-1)
                return x
        else:
            x = int(x)
            x = int(str("0b") + str(x), 2)
            return x
            

res = input()
print(convertiDec(res))