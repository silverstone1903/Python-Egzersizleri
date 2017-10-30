# main sinifi ekleme

class Vektor:
    '''
    Vektore ait girilen x, y ve aci ile 
        '''
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
          
    def boy(self):
        from math import sqrt
        return sqrt((self.x ** 2) + (self.y ** 2))
    
    def __repr__(self):
        return ("%si + %sj" %(self.x, self.y))
    
    #def yazdir(self):
        #return ("%si + %sj" %(self.x, self.y))
        # ayni gorevi goren fonksiyon ozel isimle kullanilabilir.
        
    def toplama(self, oteki): # vektorlerin x ve y'lerini toplama
        return Vektor(self.x + oteki.x, self.y + oteki.y)
    
    #def __add__(self, oteki): # alternatif
     #   return Vektor(self.x + oteki.x, self.y + oteki.y)
        
    def aci(self): # vektorlerin arasindaki aciyi hesaplama
        from math import atan, pi
        return round(atan(float(self.y)/self.x) * 180 / pi)
    
if __name__ == "__main__": # 
    a = input("Vektorun x degerini giriniz: ")
    b = input("Vektorun y degerini giriniz: ")
    c = Vektor(a,b)
    print "Vektor:", c.__repr__()
    print "Aralarindaki aci:", c.aci(), "\n"
    
    from DortIslem import *
    d = DortIslem(a,b)
    print "DortIslem sinifi ile toplama islemi:", d.toplama()
    print "DortIslem sinifi ile cikarma islemi:", d.cikarma()
    print "DortIslem sinifi ile bolme islemi:", d.bolme()
    print "DortIslem sinifi ile carpma islemi:", d.carpma()