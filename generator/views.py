from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
	
def password(request):
    
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length','8'))
	
	# handle upper case
    if (request.GET.get('uppercase')):
	    characters.extend(list('ABCDEDFGHIJKLMNOPQRSTUVWXYZ'))
		
    if (request.GET.get('specialcharacters')):
	    characters.extend(list('@!£$%^&()'))
    if (request.GET.get('number')):
	    characters.extend(list('1234567890'))			
	
    password = ''	
    for x in range(length):
	    password+=random.choice(characters)
    return render(request,'generator/password.html',{'password':password})	
	
def about(request):
    return render(request,'generator/about.html')	