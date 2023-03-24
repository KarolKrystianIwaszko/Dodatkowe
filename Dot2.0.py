#usuń wszystkie "#" po przeczytaniu
# jeżeli zmieniasz zmienną pamiętaj zmienić ją w każdym miejscu
# nie zmieniaj zmiennej "n"
def najmniejsza(n):                      #def tworzy funkcje, najmniejsza to nazwa funkcji, zalecane jest zmienienie jej na np. najmniejsza_reszta_z_dzielenia albo na nrzd lub na coś innego
    a=int(input('Wprowadź dane'))           # nie trzeba zmieniać zmiennej "a", ale można, pamiętaj żeby zmienić ją w innych miejscach
    minimum = a                             # można zmienić zmienną "minimum", nie zmieniać jej na "min" bo niezadziała
    najmniejsza_reszta_z_dzielenia = a%n    #'najmniejsza_reszta_z_dzielenia' jest zmienną można ją zmienić, a%n daje reszte z dzielenia 'a' przez 'n'
    i=0                                     #tutaj nic nie zmieniać 
    while i < 4:                            #można zmienić na 4 > i, lepiej zostawić #jaby pan się pytał dlaczego tu jest 4 a nie 5 to dlatego bo linijki 5,6,7 robią to samo co jedna pętla
        a=int(input('Wprowadź dane'))       
        if najmniejsza_reszta_z_dzielenia > a%n:    #ta pętla if działa w następójący sposób - jeżeli reszta z dzielenia a przez n jest mniejsza od zmiennej to 
            minimum=a                               #ustawia "a" jako liczbę z najmniejszą resztą z dzielenia przez n
            najmniejsza_reszta_z_dzielenia = a%n    #ustawia reszte z dzielenia a przez n jako najmniejsza_reszta_z_dzielenia 
        i=i+1                                       #liczy ilość wykonania się pętli
    return minimum                                  #w linijce 17 funkcja "najmniejsza(e,n)" będzie traktowana jako wartość zmiennej minimum
n = int(input('Podaj dzielnik'))                    #nic nie zmieniać
na = najmniejsza(o,n)                               # zmień zmienną "na"
print('Najmniejsza jest reszta z dzielenia',na,'przez',n,'równa',na%n )

#!!! sprawdź czy trzymałeś się kroków z linijek 1,2,3
