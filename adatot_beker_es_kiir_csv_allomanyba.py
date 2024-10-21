

a1 = str(input("Kérem adja meg az A1-es mező értékét! "))
b1 = str(input("Kérem adja meg az B1-es mező értékét! "))
a2 = str(input("Kérem adja meg az A2-es mező értékét! "))
b2 = str(input("Kérem adja meg az B2-es mező értékét! "))

with open("mintaoutput.csv","w",encoding="utf-8") as kimenet:
    kimenet.write(a1)
    kimenet.write(",")
    kimenet.write(b1)
    kimenet.write("\n")
    kimenet.write(a2)
    kimenet.write(",")
    kimenet.write(b2)