from django.shortcuts import render, redirect
from .models import one
from .forms import oneForm
from django.contrib import messages
import json
from django.core import serializers

from django.contrib.auth.models import User
from rest_framework import generics, permissions


from .models import one
from .serializers import UserSerializer, oneSerializer


def home(request):

    if request.method == 'POST':
        form = oneForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = one.objects.all
            messages.success(request, ('Item Has Been Added one'))
            return render(request, 'home.html', {'all_items': all_items})
        else:
            all_items = one.objects.all
            return render(request, 'home.html', {'all_items': all_items})


    else:
        all_items = one.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, one_id):
    print(("検証1")+ str(one_id))
    instance = one.objects.get(pk=one_id)
    print("検証2")
    instance.delete()
    messages.success(request, ('Item Has Been Deleted from one!'))
    return redirect('home')

def edit(request, one_id):
    print(2)
    if request.method == 'POST':
        print(3)
        instance = one.objects.get(pk=one_id)
        print(6)
        form = oneForm(request.POST or None, instance=instance)
        print(5)

        if form.is_valid():
            print(1)
            form.save()
            all_items = one.objects.all
            messages.success(request, ('Item Has Been Edited!'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        print(4)
        instance = one.objects.get(pk=one_id)
        return render(request, 'edit.html', {'item': instance})

def test(request):

    if request.method == 'POST':
        form = oneForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = one.objects.all
            messages.success(request, ('Item Has Been  one'))
            
            return render(request, 'home.html', {'all_items': all_items})
        else:
            all_items = one.objects.all
            return render(request, 'home.html', {'all_items': all_items})


    else:
        s = one.objects.order_by('?')[:5]
        post_list = serializers.serialize('json', s)
        print(s)
        return render(request, 'test.html', {'json_five_data': post_list})



#以下userのapi


class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


#以下oneのapi

class OneListCreate(generics.CreateAPIView):
    """ View to create a new one. Only accepts POST requests """
    print("検証1")
    queryset = one.objects.all()
    serializer_class = oneSerializer
    permission_classes = (permissions.IsAuthenticated, )


class oneRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a one or update one information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = one.objects.all()
    serializer_class = oneSerializer
    permission_classes = (permissions.IsAuthenticated, )