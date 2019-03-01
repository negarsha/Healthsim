import random
import json


N = 10

def myHealthcare():
    '''define a function that generates data for a thousand records '''
    create_user()
    with open('users.json') as file:
        data = json.loads(file.read())
    return data

'''create random numbers between two integers'''
def temperature():
    temp = random.randint(36, 39)
    return temp


def heart_rate():
    hr = random.randint(55,100)
    return hr


def pulse():
    pulse = random.randint(55,100)
    return pulse


def blood_pressure():
    bloodpr = random.randint(120,121)
    return bloodpr


def respiratory_rate():
    resrate = random.randint(11,17)
    return resrate


def oxygen_saturation():
    oxsat = random.randint(93,100)
    return oxsat


def ph():
    ph = round(random.uniform(7.1,7.7),1)
    return ph


'''ts?'''


def create_user():
    '''function to create a user with random attributes'''
    user_list = []
    for i in range(N):
        user = {'temp': temperature(), 'hr': heart_rate(),
                'pulse': pulse(), 'bloodpr': blood_pressure(),
                'resrate': respiratory_rate(), 'oxsat': oxygen_saturation(), 'ph': ph()}
        user_list.append(user)

    with open('users.json','w') as file:
        file.write(json.dumps(user_list))

    return user_list




