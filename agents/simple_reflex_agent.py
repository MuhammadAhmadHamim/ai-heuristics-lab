'''
Build a simple Reflex Agent which takes temperature value as input from user and compare it with a certain threshold value stored in it. 
After comparing, it performs actions according to the result of that comparison.
'''

threshold = 30.0

def perceiveTemperature():
    t= input('Enter the temperature(°C):')
    t = float(t)  

    return t

def perceiveLight():
    l = input('Enter the level of light:')

    return l.lower()

def model():
    t = perceiveTemperature()

    if(t > threshold):
        print('Fan ON')
    else:
        print('Fan OFF')

    l = perceiveLight()

    if(l == 'low'):
        print('Light ON')
    else:
        print('Light OFF')

model()