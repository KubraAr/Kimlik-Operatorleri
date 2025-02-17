#Görev1
a = 256
b = 256
print(a is b)  # Sonuç:True 
               # Neden? Çünkü Operatör belleğinde is aynı nesneyi gösterdiğini kontrol ettikten sonra True olarak döner
               # Nesne aynılığı bellek konumunu kontrol etmektir.
c = 257
d = 257
print(c is d)  # Sonuç:False
               # Neden? Çünkü Python 256'dan büyük tam sayıları önbellekte tutmaz . Bu nedenle 257 sayıları farklı belleklerde saklanır.
               # Aynı nesneye işaret vermediğini anladığımız için False olarak döner.
               # (Python -5 ile 256 sayıları arasındaki tamsayıları ön bellekte tutar.)
