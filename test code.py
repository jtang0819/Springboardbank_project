def create_bank_account(accounttype="", userid=""):
    user_id = userid
    print(type(user_id))
    while type(user_id) != int:
        try:
            user_id = int(input('Please enter valid user id: '))
            print(type(user_id))
        except ValueError:
            user_id = int(input('Please enter valid user id(integer only): '))
            print(type(user_id))
        # finally:
        #     raise ValueError('Please enter int')
        #     print(type(user_id))



x = create_bank_account()

# a = balance(100)
# print(a)