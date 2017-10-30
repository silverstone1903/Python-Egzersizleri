from __future__ import division
def dortislem(sayi1=1, sayi2=1,op="+"):
    try:
        if op == "+":
            print sayi1 + sayi2
        elif op == "*" or op == "x":
            print sayi1 * sayi2
        elif op == "-":
            print sayi1 - sayi2
        elif op == "/" or op == ":":
            print float(sayi1) / sayi2
        else:
            print "Hatali islem!"
    except:
        print "Kullanim: Hatali giris yaptiniz. 4 islem yapiniz!"