from models import User
from peewee import *


# Create User
# print(create_user("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))

# Get User
# print(get_user(email="alonssoreyes@gmail.com"))

# Update user
# print(update_user(email="alonssoreyes@gmail.com",
#      new_values={'email': 'alonso.r@gmail.com'}))

# Delete User
# print(delete_user(email="alonso.r@gmail.com"))
# print(get_user(email="alonso.r@gmail.com"))


def create_user(name, email, phone):
    try:
        user = User(name=name, email=email, phone_number=phone)
        user.save()
        return user
    except IntegrityError:
        # User already exists
        return f"{email} is already in use"


def get_user(**kwargs):
    try:
        user = User.get(**kwargs)
        return user
    except User.DoesNotExist:
        print("User does not exists in database")
        return None


def update_user(email, new_values):
    if not new_values:
        print("Invalid parameters")
        return None

    try:
        query = User.update(new_values).where(email == email)
        query.execute()
        return 'User updated'

    except User.DoesNotExist:
        print("User does not exists in database")
        return None

    except ValueError as e:
        print('User could not be updated: ')
        print(e.args[0])
        return None


def delete_user(email):
    try:
        user = User.get(email=email)
        user.delete_instance()
        return 'User ' + email + ' deleted'
    except User.DoesNotExist:
        print("User does not exists in database")
        return None
