from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime,date
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField


# Create your models here.
class Article(models.Model):
    post_no  = models.PositiveIntegerField(primary_key = True)
    title    = models.CharField(max_length=300 )
    # content  = models.TextField()
    content  = RichTextField(blank=True,null=True)
    image    = models.ImageField(blank=True, null=True,upload_to ='images/')
    author   = models.ForeignKey(User , on_delete=models.CASCADE)
    date     = models.DateField(auto_now_add = True)
    category = models.CharField(max_length =20)
    snippet  = models.CharField(max_length =100 )
    likes    = models.ManyToManyField(User, related_name='post_likes')

    def total_likes(self):
    	return self.likes.count()


    def get_absolute_url(self):
        return reverse("blog:article-detail",kwargs={'id':self.post_no})

    def __str__(self):
        return self.title + '|' + str(self.author)

    @property
    def get_image(self):
        if self.image and hasattr(self.image,'url'):
            return self.image
        else:
            self.image = 'images/profile/default_post_image.jpg'
            return self.image

    


class Category(models.Model):

	name = models.CharField(max_length =200)

	def get_absolute_url(self):
		return reverse("blog:article-list")

	def __str__(self):
		return self.name 

class Profile(models.Model):

    GENDER_CHOICES =[

                     ('Male' ,'Male'),
                     ('Female','Female'),
                     ('NonBinary','NonBinary')

                    ]

    user         = models.OneToOneField(User , null = True , on_delete = models.CASCADE)
    disp_pic     = models.ImageField(blank = True , null = True , upload_to = 'images/profile/',default = 'images/profile/default_dp_nb.png' )
    cover_pic    = models.ImageField(blank = True , null = True , upload_to = 'images/profile/',default = 'images/profile/default_cover.jpg' )
    bio          = models.TextField(blank = True , null=True)
    gender       = models.CharField(max_length = 10 ,  null = True,  blank = True, choices = GENDER_CHOICES)
    profession   = models.CharField(max_length = 30 ,  null = True , blank = True)
    status       = models.CharField(max_length = 500 , null = True , blank = True)
    fb           = models.CharField(max_length = 500 , null = True , blank = True)
    git_hub      = models.CharField(max_length = 500 , null = True , blank = True)
    insta        = models.CharField(max_length = 500 , null = True , blank = True)
    ex_link      = models.CharField(max_length = 500 , null = True , blank = True)
    twitter      = models.CharField(max_length = 500 , null = True , blank = True)
    pinterest    = models.CharField(max_length = 500 , null = True , blank = True)
    linked_in    = models.CharField(max_length = 500 , null = True , blank = True)
    # check  = models.FileField(blank = True , null = True , upload_to = 'images/profile/')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("user:profile-page")

    @property
    def get_disp_pic(self):

        def_url = {

                    'Male'      : 'images/profile/default_dp_male.png',
                    'Female'    : 'images/profile/default_dp_female.png',
                    'NonBinary' : 'images/profile/default_dp_nb.png',
                        }
        if self.disp_pic and hasattr(self.disp_pic,'url'):
            return self.disp_pic
        else:
            if self.gender == None:
                self.gender = 'NonBinary'
            self.disp_pic = def_url[self.gender]
            return self.disp_pic

    @property
    def get_status(self):

        if self.status:
            return self.status
    
        else:
            return 'Hello There General Kenobi'

    @property
    def get_cover_pic(self):

        if self.cover_pic and hasattr(self.cover_pic,'url'):
            return self.cover_pic
        else:
            self.cover_pic = 'images/profile/default_cover.jpg'
            return self.cover_pic

    
    
 



class Comment(models.Model):
    post       = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    body       = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' %(self.post.title , self.name)


    # def get_absolute_url(self):
    #     return reverse("blog:article-detail",kwargs=)



class PostUpdate(models.Model):
    """docstring for PostUpdate"""
    user_profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'posts')
    post         = models.TextField(blank=True,null=True)
    pic_1        = models.ImageField(blank = True, null = True,upload_to = 'images/profile/')
    date_time    = models.DateTimeField(auto_now_add=True)

class Photos(models.Model):

    user_profile = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'pics')
    pic          = models.ImageField(upload_to = 'images/profile/')
    caption      = models.TextField(blank=True, null=True)
    date_time    = models.DateTimeField(auto_now_add=True)