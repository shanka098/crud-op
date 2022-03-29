from django.shortcuts import render,redirect
from groceryapp.models import supermarket
from groceryapp.forms import supermarketForm

def retrieve_view(request):
    a = supermarket.objects.all()
    return render(request, 'groceryapp/index.html', { 'supermarket': a })

def create_view(request):
    print("a")
    forms = supermarketForm()
    if request.method == 'POST':
       form = supermarketForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('/check')
    return render(request , 'groceryapp/create.html', {'supermarket': forms})

def addlist(request):
   forms = supermarketForm()
   #context = form
   return render(request , 'groceryapp/create.html', {'supermarket': forms})



def delete_view(request,id):
   c = supermarket.objects.get(id=id)
   c.delete()
   return redirect('/check')

def update_view(request ,id):
   form= supermarket.objects.get(id=id)
   if request.method == 'POST':
       form1 = supermarketForm(request.POST, instance=form)
       print("valid form",form)
       if form1.is_valid():
          form1.save()
       return redirect('/check')
   return render(request , 'groceryapp/update.html', {'supermarket': form })
 
  