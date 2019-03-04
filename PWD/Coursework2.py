import random
import json
import pandas as pd


N = 10

# def myHealthcare():
#     '''define a function that generates data for a thousand records '''
#     create_user()
#     with open('users.json') as file:
#         data = json.loads(file.read())
#     return data

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
    ph = round(random.uniform(7.1, 7.7), 1)
    return ph


def create_user():
    '''function to create a user with random attributes'''
    user_list = []
    for i in range(N):
        user = {'ts': i+1, 'temp': temperature(), 'hr': heart_rate(),
                'pulse': pulse(), 'bloodpr': blood_pressure(),
                'resrate': respiratory_rate(), 'oxsat': oxygen_saturation(), 'ph': ph()}
        user_list.append(user)

    with open('users.json','w') as file:
        file.write(json.dumps(user_list))

    return user_list


url = "/Users/negarsh/Documents/PWD/users.json"
df = pd.read_json(url, orient='rows')
df = df[['ts','temp','hr','pulse','bloodpr','resrate','oxsat','ph']]
print (df.to_string(index=False))

print (df.sample(n=5))

#abnormal_pulse = df['pulse'].where(df['pulse']==100 or df['pulse']<60)
#print (abnormal_pulse)
#print (df.loc[df['pulse'] > 50])
#def abnormalSignAnalytics():

# def abnormal_sign_analytics():
#     myfile=
#     userinfo=getJSON(myfile)
#     key,value = find(userinfo)



def getjson(file):
    with open('users.json') as file:
        data = json.loads(file.read())
    dict={}
    count=0
    for i in data:
        dict[count]=i
        count += 1
    return dict

# file = '/Users/negarsh/Documents/PWD/users.json'

with open('users.json') as file:
    data = json.loads(file.read())
for i in range (5):



