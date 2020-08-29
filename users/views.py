from django.shortcuts		 	import render,get_object_or_404
from django.views.generic 		import CreateView,UpdateView,DetailView
from django.contrib.auth.forms 	import (
										UserCreationForm,
										UserChangeForm,
										PasswordChangeForm,
										)
from django.urls 				import  reverse_lazy,reverse
from .forms 					import  (
										SignUpForm,
										ProfileSettingsForm,
										PasswordForm,
										ProfilePageForm,
										StatusForm,
										PhotosForm

										)
from blog.forms 				import PostUpdateForm
from django.contrib.auth.views 	import PasswordChangeView
from blog.models				import Profile,Comment,Article,PostUpdate,Photos
from django.http				import HttpResponseRedirect
from django.views.generic       import edit
# Create your views here.

class UserRegisterView(CreateView):
    form_class	 	=  SignUpForm
    template_name 	= 'registration/register.html'
    success_url 	= reverse_lazy('login')

# class UserLoginView():
# 	form_class  = LoginForm()

class ProfileSettingsView(UpdateView):
	form_class 		= ProfileSettingsForm
	template_name 	= 'registration/settings_profile.html'
	success_url 	= reverse_lazy('pages:home')

	def get_object(self):
		return self.request.user

class PasswordView(PasswordChangeView):
	form_class 		= PasswordForm
	template_name 	= 'registration/change_password.html'
	success_url 	= reverse_lazy('users:password_success')

def password_change_success(request):
	return render(request, 'registration/pass_success.html', {})


class ProfileUsers(DetailView):
	model 			= Profile
	template_name 	= 'registration/user_profile.html'
	form_class  	= PostUpdateForm
	status			= StatusForm
	photo_op		= PhotosForm

	def get_context_data(self,*args,**kwargs):
		# user_ob 	= Profile.objects.all()
		context 	= super(ProfileUsers, self).get_context_data(*args, **kwargs)
		user_pf 	= get_object_or_404(Profile,id = self.kwargs['pk'])
		articles	= Article.objects.filter(author =self.kwargs['pk']).order_by('-date')
		updates 	= PostUpdate.objects.filter(user_profile_id = self.kwargs['pk'] ).order_by('-date_time')
		photos		= Photos.objects.filter(user_profile_id = self.kwargs['pk']).order_by('-date_time')
		
		context['user_pf'] 	 = user_pf
		context['make_post'] = self.form_class
		context['status']	 = self.status
		context['articles']	 = articles	
		context['count'] 	 = 1
		context['updates']	 = updates
		context['photo_op']	 = self.photo_op
		context['photos']	 = photos

		
		return context



class EditProfileUsers(UpdateView):
	model 			= Profile
	form_class  	= ProfilePageForm
	template_name 	= 'registration/edit_profile.html'


	def form_valid(self,form):
		return super().form_valid(form)


	def get_object(self,*args,**kwargs):
		return get_object_or_404(Profile, id = self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		if 'form' not in kwargs:
			kwargs['form'] = self.get_form()
			return super().get_context_data(**kwargs)



	success_url 	= reverse_lazy('pages:home')



class CreateProfile(CreateView):

	model 			= Profile
	form_class 		= ProfilePageForm
	template_name 	= 'registration/create_profile.html'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	success_url = reverse_lazy('pages:home')


class UpdateStatusView(UpdateView):

	model = Profile
	form_class  = StatusForm


	def get_object(self,*args,**kwargs):
		return get_object_or_404(Profile, id = self.kwargs['id'])

	def form_valid(self,form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('users:profile-page', kwargs={'pk' : self.request.user.profile.id })
		

