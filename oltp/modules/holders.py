from oltp.api import Holder

# Create Holder
# print(create_holder("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))

# Get Holder
# print(get_holder(email="alonssoreyes@gmail.com"))

# Update Holder
# print(update_holder(email="alonssoreyes@gmail.com",
#      new_values={'email': 'alonso.r@gmail.com'}))

# Delete Holder
# print(delete_holder(email="alonso.r@gmail.com"))
# print(get_holder(email="alonso.r@gmail.com"))


def create_holder(name, email, phone):
    try:
        holder = Holder(name=name, email=email, phone_number=phone)
        holder.save()
        return holder
    except:
        raise Exception('There has been an error in the system')


def get_holder(**kwargs):
    try:
        holder = Holder.objects.get(**kwargs)
        return holder
    except Exception as e:
        print(e)
        raise Exception('There has been an error in the system')


def update_holder(email, new_values):
    if not new_values:
        print("Invalid parameters")
        return None

    try:
        query = Holder.objects.update(new_values).where(email == email)
        query.execute()
        return 'Holder updated'

    except:
        raise Exception('There has been an error in the system')

    """ except ValueError as e:
        print('Holder could not be updated: ')
        print(e.args[0])
        return None """


def delete_holder(email):
    try:
        holder = Holder.get(email=email)
        holder.delete_instance()
        return 'Holder ' + email + ' deleted'
    except:
        raise Exception('There has been an error in the system')
