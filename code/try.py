print('hello, Djangogirls')

if (3 > 2):
    print('coool!')

    name = 'ALex'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

nameN = 'Sonja'
def hi():
    if nameN == 'Ola':
        print('Hey Ola!')
    elif nameN == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
        print('Hi' + nameN)
        print('How are you?')

hi()

def hi(nameN):
    if nameN == 'Ola':
        print('Hey Ola!')
    elif nameN == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
        print('Hi' + nameN)
        print('How are you?')

hi('ALex')

def hey(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hey(name)
    print('Next girl')
