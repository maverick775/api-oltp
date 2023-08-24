from django.db import models

class Holder(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Holder {self.id}: {self.name} <{self.email}>"

    def get_email(self):
        return self.email
    class Meta:
        app_label = 'oltp'  

class Account(models.Model):
    holder = models.OneToOneField(Holder, on_delete=models.CASCADE, related_name='account')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        balance = "${:,.2f}".format(self.balance)
        return f"Account {self.id}: {self.holder.email} <{balance}>"
    class Meta:
        app_label = 'oltp'  

class Card(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cards')
    security_code = models.CharField(max_length=4, default='1111')
    card_number = models.CharField(max_length=16, unique=True)
    holder_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Card {self.id}: Account {self.account.id}, Holder Name: {self.holder_name}, Card Number: {self.card_number}, Security Code: {self.security_code}"
    class Meta:
        app_label = 'oltp'  

class Movement(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=10)  # Deposito or gasto
    date = models.DateTimeField()

    def __str__(self):
        return f"Movement {self.id}: Amount {self.amount}, Account: {self.account.holder.email}, Movement Type: {self.movement_type}, Date: {self.date}"
    class Meta:
        app_label = 'oltp'  
