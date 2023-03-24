
n = int(input('Podaj dzielnik'))


a=int(input('Wprowadź dane'))
minimum = a
najmniejsza_reszta_z_dzielenia = a%n
i=0
while i < 4:
  a=int(input('Wprowadź dane'))
  if najmniejsza_reszta_z_dzielenia > a%n:
    minimum=a
    najmniejsza_reszta_z_dzielenia = a%n
  i=i+1

print('Najmniejsza jest reszta z dzielenia',na,'przez',n,'równa',na%n )
