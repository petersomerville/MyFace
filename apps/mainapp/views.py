from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import apps.mainapp.models as m

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def register(request):
    if 'user_id' in request.session:
        return redirect('mainapp:index')
    if request.method == 'POST':
        if len(request.POST['html_email']) > 0 and request.POST['html_password'] == request.POST['html_confirm']:
            try:
                user = m.User.objects.create(
                    username = request.POST['html_username'],
                    email = request.POST['html_email'], 
                    password = request.POST['html_password'])
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                request.session['email'] = user.email
            except:
                raise
                messages.error(request,'Account already in use, Bitches')
                return redirect('mainapp:register')

        return redirect('mainapp:index')
    return render(request, 'mainapp/register.html')

def login(request):
    if 'user_id' in request.session:
        return redirect('mainapp:index')
    if request.method == 'POST':
        try:
            user = m.User.objects.get(email = request.POST['html_email'])
            if request.POST['html_password'] == user.password:
                request.session['username'] = user.username
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('mainapp:index')
            else:
                messages.error(request, 'Invalid login')
                return redirect('mainapp:login')
        except:
            messages.error(request, 'Invalid login')    
            return redirect('mainapp:login')

    return render(request, 'mainapp/login.html')

    
def logout(request):
    request.session.clear()
    return redirect('mainapp:index')

def search_users(request):
    term = request.GET['html_query']
    return redirect('mainapp:results', term)

def results(request, term):
    context = {
        'users' : m.User.objects.filter(Q(username__icontains=term) | Q(email__icontains=term))
    }
    print(context)
    return render(request, 'mainapp/results.html', context)

def follow(request):
    pass

def unfollow(request):
    pass
