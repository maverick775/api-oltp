from models import Card, Movements
from peewee import *

#General Actions
#Depositos
#Gastos

def save_movement(amount, movementType, account): #se puede quitar o no usar
    card = Card.get(Card.card_number==account)
    movement = Movements(amount = amount, movementType=movementType, account = account)
    movement.save()
    print(f'Movement from Account: {movement} Amount :{amount} Movement Type: {movementType}')
    pass

def create_movement(amount, movementType, account, date):
    try:
        movement = Movements(amount = amount, movementType=movementType, account = account, date = date)
        movement.save()
        return movement
    except:
        return "Something went wrong"

    
def get_movement(**kwargs):
    try:
        movement = Movements.get(**kwargs)
        return movement
    except Movements.DoesNotExist:
        print("Movement does not exists in database")
        return None
    
def update_movement(account, date, new_values):
    if not new_values:
        print("Invalid parameters")
        return None

    try:
        query = Movements.update(new_values).where((account == account) & (date == date))
        query.execute()

        return 'Movement updated'

    except Movements.DoesNotExist:
        print("Movement does not exists in database")
        return None

    except ValueError as e:
        print('Movement could not be updated: ')
        print(e.args[0])
        return None


def delete_movement(account, date):
    try:
        mov = Movements.get((account == account) & (date == date))
        mov.delete_instance()
        return f'Movement {mov.id} deleted'
    except Movements.DoesNotExist:
        print("Movement does not exists in database")
        return None