
def najmniejsza(n):
    a=int(input('Wprowadź dane'))
    i=0
    minimum=a
    najmniejsza_reszta_z_dzielenia = a%n
    while i < 4:
        a=int(input('Wprowadź dane'))
        if najmniejsza_reszta_z_dzielenia > a%n:
            minimum=a
            najmniejsza_reszta_z_dzielenia = a%n
        i=i+1
    return minimum
n = int(input('Podaj dzielnik'))
na = najmniejsza(n)
print('Najmniejsza jest reszta z dzielenia',na,'przez',n,'równa',na%n )

