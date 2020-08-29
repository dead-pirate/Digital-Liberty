from django.shortcuts 	import render,get_object_or_404
from django.http 		import HttpResponse
from blog.models 		import Profile,Article
from django.db.models   import Count
# Create your views here.

def home_view(request ,*args,**kwargs):
    #return HttpResponse('Hello There General Kenobi')
    user_pf     = Profile.objects.filter(id =request.user.id)
    recent_posts = Article.objects.all().order_by('-date')[:3]
    top_posts   = Article.objects.all().annotate(like_count = Count('likes')).order_by('-like_count')[:3]
    context = {

	    		   'user_pf'     :	user_pf,
                   'recent_posts' :  recent_posts,
                   'top_posts'    :  top_posts,
            
	    			}

    print(context)
    print(request.user.id)

    return render(request,"home.html",context) #{} --context

def about_view(request,*args,**kwargs):

    return render(request,"about.html",{})

def contact_view(request,*args,**kwargs):
    context = {

        'my_text' : 'Hello there',
        'my_phone': '+90390930039'

    }

    return render(request , "contact.html" ,context)
