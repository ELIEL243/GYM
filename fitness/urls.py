from django.urls import path
from .views import HomeView, ClientView, EquipementView, Login, Logout

urlpatterns = [
    path('', HomeView, name="home"),
    path('client/', ClientView, name="client"),
    path('equipement/', EquipementView, name="equipement"),
    path('logout/', Logout, name="logout"),
    path('login/', Login, name="login"),
]
