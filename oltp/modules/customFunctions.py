from .holders import get_holder
from .account import get_account, update_acount
from rest_framework.response import Response

def trasnsfer(self, request):
    try:
        sender_mail = request.data.get('sender')
        receiver_mail = request.data.get('receiver')
        amount = request.data.get('amount')
        sender = get_holder(email=sender_mail)
        sender_acc = get_account(holder=sender)
        if sender_acc.balance >= amount:
            receiver = get_holder(email=receiver_mail)
            receiver_acc = get_account(holder=receiver)
            update_acount(holder=sender, new_values={'balance':sender_acc.balance - amount})
            update_acount(holder=receiver, new_values={'balance':receiver_acc.balance + amount})
        else:
            return Response(str('Not sufficient funds'), 400)
    except Exception as e:
        return Response(str(e), 500)