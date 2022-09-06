## Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


number = 0

while  number <=7:
   
 
    if number//2//2%2 == 1:
        x = True
    else:
        x = False

    if number//2%2 == 1:
        y = True
    else:
        y = False
    
    if number%2 == 1:
        z = True
    else:
        z = False

    number+=1

    c1 = not( x or y or z) #¬(X ⋁ Y ⋁ Z)
    c2 = (not x) and (not y) and (not z) # ¬X ⋀ ¬Y ⋀ ¬Z
    print( 'число =', number-1,'x =', x,'y =', y,'y =', z)

    if number == 8:
        print( )
        print ('Выражения ¬(X "⋁" Y "⋁" Z) и ¬X ⋀ ¬Y ⋀ ¬Z РАВНЫ для всех значений предиката')
        print( )
        
    if c1!= c2:
        print( )
        print('Выражения ¬(X "⋁" Y "⋁" Z) и ¬X ⋀ ¬Y ⋀ ¬Z Не РАВНЫ друг другу', '¬(X "⋁" Y "⋁" Z) = ',c1,'¬X ⋀ ¬Y ⋀ ¬Z = ', c2)
        print( )
        break

    