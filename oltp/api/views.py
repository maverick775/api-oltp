from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import  Holder, Account, Card, Movement
from oltp.api.serializers import HolderSerializer, AccountSerializer, CardSerializer, MovementSerializer, UserSerializer, GroupSerializer
from oltp.modules.holders import create_holder, get_holder
from oltp.modules.account import get_account, update_acount
from oltp.modules.movements import create_movement
from oltp.modules.cards import assign_new_card
from django.http import HttpResponse
from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HolderViewSet(viewsets.ModelViewSet):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer

    def create(self, request):
        print(request)

        name = request.data.get('name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        
        create_holder(name,email,phone_number)
        return HttpResponse("Success")
    
    def retrieve(self,request, pk=None):
        holder = Holder.objects.get(pk=pk)
        return HttpResponse(holder)

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

        
        

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request):
        try:
            return Response(assign_new_card(**request.data))
        except Exception as e:
            return Response(str(e), 500)

class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    def create(self,request):
        try:
            holder = get_holder(email=request.data.get('account'))
            account = get_account(holder=holder)
            return Response(create_movement(request.data.get('amount'), request.data.get('movementType'), account, request.data.get('date')))
        except Exception as e:
            return Response(str(e), 500)

        

        
