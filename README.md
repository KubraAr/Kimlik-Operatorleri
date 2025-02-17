# Kimlik-Operatorleri
## Python is Operatörü ve Nesne Kimliği

Görev 1: is Operatörü ve Nesne Kimliği
Bu projede, is operatörü kullanılarak iki değişkenin aynı nesneye işaret edip etmediği kontrol edilmiştir.
is operatörü, nesnelerin bellek adreslerini karşılaştırır ve nesnelerin gerçekten aynı bellek alanına sahip olup olmadığını kontrol eder.

Örnek 1:
a = 256 ve b = 256 gibi küçük tam sayılar için, Python bu sayıları önbelleğe alır ve aynı bellek adresini kullanır. Bu yüzden a is b ifadesi True döner.

Örnek 2:
c = 257 ve d = 257 gibi daha büyük sayılar için, Python bu sayıları önbelleğe almaz. Dolayısıyla her biri farklı bellek adreslerine sahip olur ve c is d ifadesi False döner.
Python, -5 ile 256 arasındaki tam sayıları önbellekte tutar. 257 ve üzeri sayılar için ise bu tutulum geçerli değildir.
