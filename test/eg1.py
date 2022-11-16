# def login(shopping):
#     user_info={'admin':'admin','tom':'tom'}
#     user=input('Username: ' )
#     password=input('Password: ')
#     if user_info[user] == password:
#         print('%s log on  ...' % user)
#     else :
#         print('login fail,please enter the password ')
#         return login(shopping)
#
#     def new_fun(name):
#         shopping(name)
#     return new_fun
#
# @login
# def shopping(name):
#     print('%s is shopping'%name)
# shopping('admin')


def login(func):
    user_info={'admin':'admin','tom':'tom'}
    user=input('Username: ' )
    password=input('Password: ')
    if user_info[user] == password:
        print('%s log on  ...' % user)
    else :
        print('login fail,please enter the password ')
        return login(func)

    def new_fun():
        func()
    return new_fun

@login
def danceing():
    print('danceing....')

danceing()