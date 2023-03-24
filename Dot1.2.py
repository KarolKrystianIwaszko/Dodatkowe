def najbliżej_n(n):
    a = int(input('podaj a'))
    b = a-n
    if b < 0:
        b=b*-1
    najmniejsza_różnica = b
    najbliżej_n = a

    for i in range(4):
        a = int(input('podaj a'))
        b = a-n
        if b < 0:
            b=b*-1
        if b < najmniejsza_różnica:
            najmniejsza_różnica = b
            najbliżej_n = a
    return najbliżej_n
      
n = int(input('podaj n'))
print('najbliżej na osi liczbowej do',n,'jest',najbliżej_n(n))
