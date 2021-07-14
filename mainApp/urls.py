from django.urls import path
from . import views 

app_name = 'mainApp'



urlpatterns = [
    path('',views.loadMainPage,name = 'loadMainPage'),
    path('accounts/login/',views.loadLoginPage,name = 'loadLoginPage'),


 
    
    # path('print/<username>/', views.print_from_button ,name='printButton'),
    # path('ajax', views.answer_me, name='get_response'),
    path('authUser', views.authUser, name='authUser'),
    # path('logout', views.logout_req, name='logout'),
    # path('logoutSecured', views.logoutSecured_req, name='logoutSecured'),
]
