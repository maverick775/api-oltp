# from database import db
# from models import User, Card, Account, Movements
# from .user import create_user, get_user
# from .account import create_account
# from .cards import assign_new_card

# # TODO: Create records for all tables


# def populate_all():
#     db.connect()

#     # Clean DB before populating it
#     db.drop_tables([User, Account, Card, Movements])

#     # Create new tables
#     db.create_tables([User, Account, Card, Movements])

#     def onboard_test_users(email, base_balance):
#         test_user = get_user(email=email)
#         acc = create_account(user=test_user, balance=base_balance)
#         card1 = assign_new_card(acc, test_user.name)
#         card2 = assign_new_card(acc, test_user.name)
#         print(f'New user: {test_user.name}\n Account ID: {acc}\n Balance: {acc.balance}\n Main card: {card1.card_number}\n Secondary card: {card2.card_number}')

#     print('****Create Users****')
#     print(create_user("Alonso Reyes", "alonso.reyes@gmail.com", "000000000"))
#     print(create_user("Pake Perez", "pake.perez@gmail.com", "0000000001"))
#     print(create_user("Jasmin Sanchez", "jasmin.sanchez@gmail.com", "0000000002"))
#     print(create_user("Erick Martinez", "erick.martinez@gmail.com", "0000000003"))
#     print(create_user("Mike Castañeda", "mike.castañeda@gmail.com", "0000000004"))

#     print()
#     print('****Create Accounts and Cards****')
#     onboard_test_users('alonso.reyes@gmail.com', 63000)
#     onboard_test_users('pake.perez@gmail.com', 100000)
#     onboard_test_users('jasmin.sanchez@gmail.com', 3000)
#     onboard_test_users('erick.martinez@gmail.com', 70000)
#     onboard_test_users('mike.castañeda@gmail.com', 3000000)

#     print('\n\n')
