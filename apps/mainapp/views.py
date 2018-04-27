from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import apps.mainapp.models as m

# Create your views here.

def index(request):
    if 'user_id' in request.session:
        posts = m.Post.objects.filter(user_wall_id=request.session['user_id']).order_by('-created_at')
        context = {
            'posts':posts
        }
        return render(request, 'mainapp/index.html', context)
    else:
        return render(request, 'mainapp/index.html')

def post(request):
    user_wall = request.POST['user_wall']
    post_contents = request.POST['html_post_contents']

    posting = m.Post.objects.create(
        author_id = request.session['user_id'],
        user_wall_id = user_wall,
        post_contents = post_contents
    )
    return redirect('mainapp:index')

def return_posts(request, posting):
    matching_posts = m.Post.objects.filter(user_wall_id=request.session['user_id'])
    list_of_posts = []
    
    for post in matching_posts:
        list_of_posts.append(post.id)

    context = {'posts':list_of_posts}

    return render(request, 'mainapp/index.html', context)    

def delete_post(request, post_id):
    post = m.Post.objects.get(id = post_id)
    post.delete()
    return redirect('mainapp:index')

def search_users(request):
    term = request.GET['html_query']
    return redirect('mainapp:results', term)

def results(request, term):
    matching_users = m.User.objects.filter(Q(username__icontains=term) | Q(email__icontains=term)).exclude(id=request.session['user_id'])
    users_being_followed = m.Following.objects.filter(follower_id=request.session['user_id'])
    matching_followed = []

    for follow in users_being_followed:
        matching_followed.append(follow.following_id)

    context = {
        'users':matching_users,
        'follows':matching_followed,
    }

    return render(request, 'mainapp/results.html', context)

def follow(request, following_id):
    print('****{}'.format(following_id))
    if 'user_id' in request.session == following_id:
        messages.error(request, 'You cannot follow yourself')
        return redirect('mainapp:index')
    else:
        following = m.Following.objects.create(
            follower_id = request.session['user_id'],
            following_id = following_id)
        
    return render(request, 'mainapp/index.html')

def unfollow(request, following_id):
    follow = m.Following.objects.get(following_id = following_id)
    follow.delete()
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




