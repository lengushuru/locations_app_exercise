from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LocationForm
from django.contrib import messages
from .models import Location
from .models import parent_loc
from .forms import ParentLocationForm, LocationForm

def home(request):

    # location = Location.objects.select_related('parent').all()
    parent_locs = parent_loc.objects.prefetch_related('location_set').all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authoticate user
        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            messages.success(request,'you are logged in')
            return redirect('home')
        else:
            messages.success(request,"username or email is not correct, please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'parent_locs':parent_locs})

#logout user
def logout_user(request):
    logout(request)
    messages.success(request,'you are logged out')
    return redirect('home')

def  location_record(request, pk):
    if request.user.is_authenticated:
        loc = parent_loc.objects.get(id=pk)
        return render(request, 'location_record.html', {'loc':loc})

def  delete_record(request, pk):
    if request.user.is_authenticated:
        delete_loc = parent_loc.objects.get(id=pk)
        delete_loc.delete()
        return redirect('home')
def  delete_child(request, pk):
    if request.user.is_authenticated:
        delete_loc = Location.objects.get(id=pk)
        delete_loc.delete()
        return redirect('location_record')

def add_record_parent(request):
   if request.method == 'POST':
        form = ParentLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_record_parent')  # Replace 'success' with the URL name of the success page
        else:
            form = ParentLocationForm()
            return redirect('add_record_parent')
   else:
        form = ParentLocationForm()
        return render(request, 'add_record_parent.html', {'form': form})

def add_record(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_record')  # Replace 'success' with the URL name of the success page
    else:
        form = LocationForm()
    return render(request, 'add_record.html', {'form': form})

