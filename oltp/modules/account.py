from oltp.api import Account
from peewee import *

# Create account
# test_user = get_user(email='alonso.reyes@gmail.com')
# print(create_account(holder=test_user, balance=63000))
# print(create_user("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))

# Get account
# print(get_account(holder=test_user))

# Update account
# print(update_acount(holder=test_user, new_values={'balance': 5000}))
# print(get_account(holder=test_user))

# Delete account
# print(delete_account(holder=test_user))
# print(get_account(holder=test_user))


def create_account(holder, balance):
    try:
        acc = Account(holder=holder, balance=balance)
        acc.save()
        return acc
    except IntegrityError:
        # Account already exists
        return "User already has an account"


def get_account(**kwargs):
    try:
        acc = Account.objects.get(**kwargs)
        return acc
    except Account.DoesNotExist:
        print("Account does not exists in database")
        return None


def update_acount(holder, new_values):
    if not new_values:
        print("Invalid parameters")
        return None

    try:
        query = Account.objects.update(new_values).where(holder == holder)
        query.execute()

        return 'Account updated'

    except Account.DoesNotExist:
        print("Account does not exists in database")
        return None

    except ValueError as e:
        print('Account could not be updated: ')
        print(e.args[0])
        return None


def delete_account(holder):
    try:
        acc = Account.objects.get(holder=holder)
        acc.delete_instance()
        return 'Account for ' + holder.get_email() + ' deleted'
    except Account.DoesNotExist:
        print("User does not exists in database")
        return None
