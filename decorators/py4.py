

from sqlalchemy import func


users = [
    {
        'name': 'Charan T M',
        'email': 'charantm8787@gmail.com',
        'is_admin': True,
        'd_o_b': '2005-11-13'
    },
    {
        'name': 'Uday',
        'email': 'uday@gmail.com',
        'is_admin': False,
        'd_o_b': '2010-07-17'
    },
    {
        'name': 'Hardhik',
        'email': 'hardhik@gmail.com',
        'is_admin': False,
        'd_o_b': '2005-10-25'
    },
    {
        'name': 'shamanth',
        'email': 'shamanthhm@gmail.com',
        'is_admin': True,
        'd_o_b': '2005-08-18'
    }
]


# def func(**kwargs):
#     # print(kwargs.get('name'))
#     for i in range(1, len(user)+1):
#         if user[i]['name'] == kwargs.get('name') and user[i]['is_admin'] == True:

#             print(user[i]['name'])
#             break
#         else:
#             print('not auth')


def authorization(function):
    def checker(*args, **kwargs):

        username = None
        if args:
            username = args[0]
        elif kwargs:
            username = kwargs["name"]

        for user in users:
            db_user = user['name']
            if db_user.lower() == username.lower():

                if user["is_admin"]:
                    return function(*args, **kwargs)

                else:
                    return "Not authorized"

    return checker


@authorization
def game(*args, **kwargs):
    return 'Authorization checker: access granted'


print(game(name='Charan T M'))
