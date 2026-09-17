items = ['Rock','Pogo Stick','Wand']
levels = [1,2,3]
#print('You can get a',items[0],'at level 1')
#print('You can get a',items[1],'at level 1')
#print('You can get a',items[2],'at level 2')
#print('You can get a',items[1],'at level 2')
#print('You can get a',items[2],'at level 3')
#print('You can get a',items[0],'at level 3')
#print('You can get a',items[1],'at level 3')

for level in levels:
    for item in items:
        if level == 2 and item == 'Rock':
            continue
        else:
            print(f'You can get a {item} at level {level}.')

