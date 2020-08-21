from django  import forms

from .models import Article,Category,Comment,PostUpdate

choices = Category.objects.all().values_list('name' , 'name')

choice_list =[]

for i in choices:
    choice_list.append(i)

class create_form(forms.ModelForm):

    class Meta:
        model = Article
        fields =[
        'post_no',
        'title',
        'author',
        'category',
        'content',
        'image',
        'snippet'
        

        ]

        widgets = {
            'post_no' : forms.NumberInput(attrs={
                            'class': 'form-control'
                                                }),
            'title' : forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder':'YOUR TITLE'
                                                }),
            'content' : forms.Textarea(attrs={
                            'class'      : 'form-control custom-select bg-white border-left-0 border-md',
                            'placeholder':'YOUR CONTENT',
                                                }),
            'author' : forms.TextInput(attrs={
                            'class' : 'form-control',
                            'value' : '',
                            'id'    : 'auth',
                            'type'  : 'hidden'
                                                }),
            'category' : forms.Select(choices = choice_list,attrs = {
                            'class' : 'form-control custom-select bg-white border-left-0 border-md'
                                                }),
            'snippet' : forms.Textarea(attrs={
                            'class'      : 'form-control',
                            'placeholder':'Add a snippet for the post'
                                                }),
}

    # def cleaned_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not 'abc' in title:
    #         return 'hey'
    #     else:
    #         return forms.ValidationError('hey u')
#
# class Rawcreate_form(forms.Form):
#     post_no  = forms.IntegerField()
#     title    = forms.CharField()
#     content  = forms.CharField(widget = forms.Textarea(
#                 attrs={
#                 'rows': 20,
#                 'columns': 100
#                 }
#                         ))
#     author   = forms.CharField()

class update_form(forms.ModelForm):

    class Meta:
        model = Article
        fields =[

        'title',
        'category',
        'content',
        'snippet'
        

        ]

        widgets = {

            'title' : forms.TextInput(attrs={
                            'class': 'form-control bg-white border-left-0 border-md',
                            
                                                }),
            'content' : forms.Textarea(attrs={
                            'class'      : 'form-control custom-select bg-white border-left-0 border-md', 
                            
                                                }),
            'category' : forms.Select(choices = choice_list,attrs = {
                            'class' : 'form-control custom-select bg-white border-left-0 border-md'
                                                }),
            'snippet' : forms.Textarea(attrs={
                            'class' :   'form-control bg-white border-left-0 border-md',
                            'cols'  :   '150', 
                            'rows'  :   '5',
                            
                                    }),
            }


class AddCommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = [

                'name',
                'email',
                'body',

                ]

        widgets={

                'name'  : forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder':'Your Name',
                                    'style':'border:none;'
                                                    }),
                'email' : forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder':'Your email won\'t be displayed or shared',
                                'required'   : 'True'
                                                    }),
                'body'  : forms.Textarea(attrs={
                                'class' : 'form-control',
                                'placeholder':'Add your comment '
                                                    }),
                }

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = PostUpdate

        fields = [
                    'post',
                    'pic_1'
        ]


        widgets = {

                    'post' : forms.Textarea(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'what\'s you been upto'
                        })



        }