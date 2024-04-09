from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler404
from recipes.views import unknown

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', user_views.register, name="user-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
    path('profile/', user_views.profile, name="user-profile"),
    path('logout/', user_views.logout, name='logout'),
    path('set_language/', set_language, name='set_language'),
    
)

handler404 = 'recipes.views.unknown'