from django.urls import path
from .views import (
					UserRegisterView,
					ProfileSettingsView,
					PasswordView,
					ProfileUsers,
					EditProfileUsers,
					CreateProfile,
                                        UpdateStatusView
						)
# from django.contrib.auth import views as auth_views
from . import views
from blog.views  import UpdatePostView ,PhotosUpload
 
app_name = 'users'

urlpatterns = [
        # path('login/',UserLoginView.as_view(),name = 'login'),
        path('register/',UserRegisterView.as_view(),name = 'register'),
        path('settings/',ProfileSettingsView.as_view(),name = 'settings-profile'),
        # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),name = 'password-change'),
        path('password/',PasswordView.as_view(),name = 'password-change'),
        path('password/success',views.password_change_success,name = 'password_success'),
        path('profile/<int:pk>',ProfileUsers.as_view(),name = 'profile-page'),
        path('profile/<int:pk>/update',EditProfileUsers.as_view(),name = 'edit-profile-page'),
        path('profile/create',CreateProfile.as_view(),name = 'create-profile-page'),
        path('profile/newpost/<int:pk>' , UpdatePostView.as_view(),name = 'make-post'),
        # path('profile/posts', UpdatePostList.as_view(), name='users-update'),
        path('profile/update/<int:id>', UpdateStatusView.as_view(), name='status-update'),
        path('profile/pic/<int:id>', PhotosUpload.as_view(), name='pic-upload')

]
