from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile,Comment,Photos


class SignUpForm(UserCreationForm):

	email 		= forms.EmailField( required = True, 
									widget =  forms.EmailInput(attrs={
                             					'class': 'form-control',
                            					'placeholder':'john.doe@email.com'}))
	first_name  = forms.CharField( max_length = 200, required = True,
								   widget =forms.TextInput(attrs={
                            					'class': 'form-control',
                            					'placeholder':'John'}))
	last_name 	= forms.CharField( max_length = 200, required = True,
								   widget = forms.TextInput(attrs={
                            					'class': 'form-control',
                            					'placeholder':'Doe'}))

	class Meta:
		model = User
		fields = [

			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'

				] 

	def __init__(self,*args,**kwargs):
		super(SignUpForm, self).__init__(*args ,**kwargs)

		self.fields['username'].widget.attrs['class']  		 = 'form-control'
		self.fields['username'].widget.attrs['placeholder']  = 'john_doe21'
		self.fields['password1'].widget.attrs['class'] 		 = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['class'] 		 = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm'

class ProfileSettingsForm(UserChangeForm):

	email 			= forms.EmailField( required = True, 
									widget =  forms.EmailInput(attrs={
                             					'class': 'form-control',}))
	first_name  	= forms.CharField( max_length = 200, required = True,
								   widget =forms.TextInput(attrs={
                            					'class': 'form-control',}))
	last_name 		= forms.CharField( max_length = 200, required = True,
								   widget = forms.TextInput(attrs={
                            					'class': 'form-control',}))

	username    	= forms.CharField( max_length = 200, required = True,
								   widget = forms.TextInput(attrs={
                            					'class': 'form-control',}))
	# last_login  	= forms.CharField( max_length = 200, required = False,
	# 							   widget = forms.TextInput(attrs={
 #                            					'class': 'form-control',}))
	# is_superuser   	= forms.CharField( max_length = 200, required = False,
	# 							   widget = forms.CheckboxInput(attrs={
 #                            					'class': 'form-check',}))
	# is_staff   		= forms.CharField( max_length = 200, required = False,
	# 							   widget = forms.CheckboxInput(attrs={
 #                            					'class': 'form-check',}))
	# is_active    	= forms.CharField( max_length = 200, required = False,
	# 							   widget = forms.CheckboxInput(attrs={
 #                            					'class': 'form-check',}))
	# date_joined   	= forms.CharField( max_length = 200, required = False,
	# 							   widget = forms.TextInput(attrs={
 #                            					'class': 'form-control',}))

	class Meta:
		model = User
		fields = [

			'username',
			'first_name',
			'last_name',
			'email',

				] 

class PasswordForm(PasswordChangeForm):

	old_password 	= forms.CharField( required = True, 
									widget =  forms.PasswordInput(attrs={
                             					'class': 'form-control',
                            					'placeholder':'Old Password',
                            					'type' : 'password'}))
	new_password1   = forms.CharField( max_length = 200, required = True,
								   widget =forms.PasswordInput(attrs={
                            					'class': 'form-control',
                            					'placeholder':'New Password',
                            					'type' : 'password'}))
	new_password2 	= forms.CharField( max_length = 200, required = True,
								   widget = forms.PasswordInput(attrs={
                            					'class': 'form-control',
                            					'placeholder':'Confirm Password',
                            					'type' : 'password'}))

	class Meta:
		model = User
		fields = [
			'old_password',
			'password1',
			'password2'

				] 

class ProfilePageForm(forms.ModelForm):


	class Meta:
		model= Profile
		fields = [

				'bio',
				'gender',
			    'disp_pic',
			    'profession',
			    'fb',
			    'git_hub',
			    'insta',
			    'twitter',
			    'pinterest',
			    'linked_in',
			    'ex_link',

					]
		
		widgets = {

	            'bio' 			: forms.Textarea(attrs={
		                           	   'class'		 : 'form-control bg-white border-left-0 border-md',
		                           	   'placeholder' :'Tell something About Yourself'
	                                                    }),
	            'gender' 		: forms.Select(attrs={
				                    	'class'		 : 'form-control custom-select bg-white border-left-0 border-md',			                 
				                                        }),

	            'disp_pic' 		: forms.ClearableFileInput(attrs={
		                            # 'class': 'custom-file-input',
		                            
	                                                 }),
	            'profession' 	: forms.TextInput(attrs={
		                               'class'		 : 'form-control bg-white border-left-0 border-md',
		                           	   'placeholder':'Blogger,Programmer,Artist etc.'
	                                                    }),
	            'fb' 			: forms.TextInput(attrs={
		                               'class'		 : 'form-control bg-white border-left-0 border-md',
		                           	   'placeholder':'http://your_fb_link_here.com'
	                                                    }),
	            'git_hub'		: forms.TextInput(attrs={
		                           	   'class' 	 : 'form-control bg-white border-left-0 border-md',
		                          	   'placeholder':'http://your_git_link_here.com'
	                                                    }),
	            'insta' 		: forms.TextInput(attrs = {
	                           		   'class'      : 'form-control bg-white border-left-0 border-md',
	                           		   'placeholder':'http://your_insta_link_here.com'
	                                                     }),
	            'twitter'		: forms.TextInput(attrs={
				                	   'class'      : 'form-control bg-white border-left-0 border-md',
				                	   'placeholder':'http://your_twitter_link_here.com'
				                                    }),
	            'pinterest'		: forms.TextInput(attrs={
				                	   'class'      : 'form-control bg-white border-left-0 border-md',
				                	   'placeholder':'http://your_pin_here.com'
				                                    }),
	            'linked_in'		: forms.TextInput(attrs={
				                	   'class'      : 'form-control bg-white border-left-0 border-md',
				                	   'placeholder':'http://your_linkedin_here.com'
				                                    }),
	            'ex_link'		: forms.TextInput(attrs={
	                            	   'class'       : 'form-control bg-white border-left-0 border-md',
	                           		   'placeholder' :'http://your_link_here.com'
	                                                }),
					
					}

class StatusForm(forms.ModelForm):


	class Meta:

		model= Profile

		fields = [

				'status'

					]

		widgets ={

			'status' : forms.TextInput(attrs ={

							'class' : 'form-control'

				})

		}


class PhotosForm(forms.ModelForm):

	class Meta:

		model = Photos

		fields = [

			'pic',
			'caption'

		]

		widgets={

		# 'pic'		: forms.ClearableFileInput(attrs={
		#                             'class': 'custom-file-input',
		#                             }),
		'caption'	: forms.TextInput(attrs={

									'class' : 'form-control bg-white border-left-0 border-md',
									'placeholder': 'caption'
									})
		}