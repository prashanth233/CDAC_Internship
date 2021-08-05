import os,sys

try:
    import tinydb
except :
    os.system('pip install tinydb')
    import tinydb

db=tinydb.TinyDB('USERAUTH.DB')

def signup(username,password):
    userexists=0
    username=username.lower()
    for x in db:
        userexists= x['name']==username
        if userexists:
            break

    if userexists:
        print(f'WARNING: User "{username}" Already exists')
        return {'status':'user exists'}
    else:
        db.insert({'name': username, 'password': password})
        print(f'LOG: User Created {username}')
        return {'status':'success'}


def login(username,password):
    USER=tinydb.Query()
    userexists=db.search(USER.name == username)
    if userexists:
        print(f'LOG:user {username} exists attempting to login')
        correctPassword=userexists[0]['password']==password
        if correctPassword:
            return {'status':'success'}
        else:
            print(f'ERROR: invalid password for {username}')
            return {'status':'invalid password'}

    else:
        return {'status':'invalid user'}
    ...

signup ("admin", "admin123")


if __name__ == '__main__':
    # new sign up
    r=signup('prashanth','abcd1234')
    print(r,'\n')

    # signup after signup with different password
    r=signup('prashanth','scas!@#rfsdf')
    print(r,'\n')

    # signup 2nd user as test
    r=signup('dharam','prashi')
    print(r,'\n')

    # login incorrectly
    r=login('dharam','dharamprashi')
    print(r,'\n')

    # login correctly
    r=login('prashanth','abcd1234')
    print(r,'\n')

    # login correctly
    r=login('dharam','dharamprashi')
    print(r)