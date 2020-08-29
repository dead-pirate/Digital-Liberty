from django.shortcuts           import render , get_object_or_404
from django.urls                import reverse,reverse_lazy
from .forms                     import ( 
                                        create_form ,
                                         update_form, 
                                         AddCommentForm,
                                         PostUpdateForm
                                         )
from django.contrib.auth.models import User
from .models                    import Article , Category,Comment ,PostUpdate,Photos
from django.http                import HttpResponseRedirect,Http404
from django.views.generic       import (
                                        CreateView,
                                        DetailView,
                                        ListView,
                                        UpdateView,
                                        DeleteView,
                                        edit
                                        )
from users.forms                 import  PhotosForm
# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'blogposts/create_post.html'
    form_class = create_form
    model = Article
    # queryset = Article.objects.all()
    # fields = '__all__'
    # success_url ='/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView):
    model = Article
    # queryset = Article.objects.all()
    template_name = 'blogposts/posts_list.html'
    tags          = Category.objects.all()
    ordering      = [ '-date']

    def get_context_data(self , *args ,**kwargs):
        tags_menu    = Category.objects.all()
        count        = 1
        context      = super(ArticleListView,self).get_context_data(*args,**kwargs)
        context["tags_menu"] = tags_menu
        context["count"]     = count
        return context

class ArticleDetailView(edit.FormMixin,DetailView):
    # model = Article
    template_name   = 'blogposts/post.html'
    form_class      = AddCommentForm
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article,post_no = id)

    
    def get_context_data(self,*args,**kwargs):
        ob = self.get_object()
        is_liked = False
        context = super().get_context_data(*args, **kwargs)

        if ob.likes.filter(id = self.request.user.id).exists():
            is_liked = True
        else:
            is_liked = False

        context['likes'] = ob.total_likes()
        context['is_liked'] = is_liked
        context['form'] = self.form_class
        return context

class ArticleUpdateView(UpdateView):
    template_name = 'blogposts/update_post.html'
    form_class = update_form
    queryset = Article.objects.all()
    success_url = '/'


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article,post_no = id)

    def form_valid(self, form):
        return super().form_valid(form)



class ArticleDeleteView(DeleteView):

    template_name = 'blogposts/post_delete.html'
    success_url = reverse_lazy('blog:article-list')
    #
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article,post_no = id)

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('blog:article-list')


def  CategoryView(request , tag):

    category_posts = Article.objects.filter(category=tag)


    context = {

            'tag'   : tag,
            'posts' : category_posts,
            'count' : 1,


                }

    return render(request , 'blogposts/category.html' , context )

def TagNavView(request,*args,**kwargs):
    tags = Category.objects.all()
    context= {

            'tags' : tags
                }
    return render(request,'blogposts/taglist.html',context)


def LikeView(request,id):
    post  = get_object_or_404(Article,post_no=id)
    is_liked = False

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(reverse('blog:article-detail', args=[str(id)]))

# def AddCommentView(request, **kwargs):
#     post = get_object_or_404(Article, post_no=id)

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm


    def form_valid(self, form):
        form.instance.post_id = self.kwargs['id']
        return super().form_valid(form)
 
    # success_url = reverse_lazy('blog:article-detail', kwargs={'id' :})
    def get_success_url(self):
        return reverse('blog:article-detail', kwargs={'id' : self.kwargs['id']})

class UpdatePostView(CreateView):
    model       = PostUpdate
    form_class  = PostUpdateForm


    def form_valid(self,form):
        form.instance.user_profile = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:profile-page', kwargs={'pk' : self.kwargs['pk']})

    

class PhotosUpload(CreateView):
    model       = Photos
    form_class  = PhotosForm


    def form_valid(self,form):
        form.instance.user_profile = self.request.user
        return super().form_valid(form)  

    def get_success_url(self):
        return reverse('users:profile-page', kwargs={'pk' : self.kwargs['id']})

# class UpdatePostDetail(DetailView):

#     model  = PostUpdate

# class UpdatePostDelete(DeleteView):

#     model = PostUpdate


    
# def post_view(request):
#
#     obj = Article.objects.get(post_no = 1)
#     # context ={ 
#     #         'title'   : obj.title,
#     #         'content' : obj.content,
#     #         'author'  : obj.author
#     #
#     #             }
#     context ={
#
#         'object' : obj
#
#             }
#     return render(request, 'blogposts/posts.html',context)
#
#
# def create_post(request):
#     form = Rawcreate_form()
#
#     if request.method == 'POST':
#         form = Rawcreate_form(request.POST or None)
#         if form.is_valid():
#             Article.objects.create(**form.cleaned_data)
#             print(form.cleaned_data)
#
#     context ={
#                 'form' : form
#     }
#     return render(request, 'blogposts/create_post.html',context)
#
#     def list_contents(request):
#         pass
