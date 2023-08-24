from oltp.api import Card
from peewee import *
import random
from .movements import save_movement
#General actions
# New card:
#   > Get User, User.name
#   > Get Account ID by User
#   assign_new_card(ACCOUNT_ID, USER.NAME, opt. security_code)
# Make purchase:
#   make_purchase(CARD_NUMBER, amount, security_code)
# Get card by number:
#   get_card_by_number(CARD_NUMBER)
# Update NIP:
#   update_nip(CARD_NUMBER, new_nip)
# Cancel card: 
#   cancel_card(CARD_ID)    




def assign_new_card(account_id, holder_name, security_code='1111'):
    def generate_card_number():
        return random.randint(10**13, 10**14 - 1)
    try:
        card = Card.objects.create(account=account_id, card_number=generate_card_number(), holder_name=holder_name, security_code=security_code)
        return card
    except Card.AccountDoesNotExist:
        raise ValueError("Account does not exist.")

def get_card_by_number(card_number):
    try:
        card = Card.objects.get(Card.objects.card_number == card_number)
        print(f'Card: {card.card_number} Holder:{card.holder_name} Account ID: {card.account.id}')
        return card
    except Card.DoesNotExist:
        print("Card does not exist.")
        return None

def make_purchase(card_number, amount, security_code):  #gasto
    try:
        card = Card.objects.get(Card.objects.card_number == card_number)
        if card.security_code != security_code:
            print("Invalid NIP")
            return False
        if card.account.balance >= amount:
            card.account.balance -= amount
            card.account.save()
            print("Payment succesful")
            return True
        else:
            print("Insuficcient funds")
            return False
    except Card.DoesNotExist:
        raise ValueError("Card does not exist.")
    
def deposit(card_number,amount):
    try:
        card = Card.objects.get(Card.objects.card_number == card_number)
        if card.account.balance >= amount:
            card.account.balance += amount
            card.account.save()
            save_movement(amount, 'Deposito', Card.objects.card_number)
            print("Payment succesful")
            return True
        else:
            print("Insuficcient funds")
            return False
    except Card.DoesNotExist:
        raise ValueError("Card does not exist.")


def update_nip(card_number, new_nip):
    try:
        card = Card.objects.get(Card.objects.card_number == card_number)
        card.security_code = new_nip
        print("NIP updated")
        card.save()
        return "NIP updated"
    except Card.DoesNotExist:
        print("Card does not exist.")
        return None

def cancel_card(card_id):
    try:
        card = Card.objects.get_by_id(card_id)
        card.delete_instance()
        print(f'Card {card_id} has been deleted')
        return f'Card {card_id} has been deleted'
    except Card.DoesNotExist:
        print("Card does not exist.")
        return None

