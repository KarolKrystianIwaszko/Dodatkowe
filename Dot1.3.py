
def najbliżej_n(n):
  a = int(input('podaj a'))
  b = a-n
  if b < 0:
    b=b*-1
  najmniejsza_różnica = b
  najbliżej_n = a
  i=0
  while i < 4:
      a = int(input('podaj a'))
      b = a-n
      if b < 0:
        b=b*-1
      if b < najmniejsza_różnica:
        najmniejsza_różnica = b
        najbliżej_n = a
      i=i+1
    
    
n = int(input('podaj n'))
print('najbliżej na osi liczbowej do',n,'jest',najbliżej_n(n))
