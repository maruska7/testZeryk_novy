from django.urls import path
from . import views
from .views import like, AddCommentView

#definice URL adres
urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),
    path('recipe/like/<int:pk>', like, name='like_post'),
    path('recipe/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('search/', views.search_recipes, name='search_recipes'),
]