dict2 = {}
a = list()
yn = 'y'
o = 1
while yn == 'y':
    dict2.clear()
    x = input('Item ID?')
   
    if x in dict2:
        
    

        print(dict2[x])
    else:
        y = input('That ID doesn\'t exist. Could you tell me the name of the item?')
        z = input('Price of it?')
        a.append(y)
        a.append(z)
            
        dict2[x] = a
    yn = input('Do you still want to use this? y/n')
