#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. 

a=int(input('Numarul  curent al primului elev este: ')) 
x=int(input('punctajul acestuia este: '))
b=int(input('Numarul curent la al doilea elev este: '))
y=int(input('punctajul acestuia este: '))
c=int(input('Numarul curent la al treilea elev este: ')) 
z=int(input('punctajul acestuia este: '))
if (x>y) and (x>z):
    print('Punctajul maxim îl deține elevul cu numarul ', a)
elif (y>x) and (y>z):
    print('Punctajul maxim îl are elevul cu numarul ', b)
elif (z>x) and (z>y):
    print('Punctajul maxim îl are elevul cu numarul ', c)
else:
    print("error")
