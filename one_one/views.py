from django.shortcuts import render, redirect
from .models import one
from .forms import oneForm
from django.contrib import messages

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
    if request.method == 'POST':
        instance = one.objects.get(pk=one_id)
        form = oneForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()
            all_items = one.objects.all
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        instance = one.objects.get(pk=one_id)
        return render(request, 'edit.html', {'item': instance})