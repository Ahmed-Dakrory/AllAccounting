from django.urls import path
from . import views 

app_name = 'accountingApp'

urlpatterns = [
    path('',views.loadMainPageForaccounting,name = 'loadMainPage'),



    
    path('qyod/',views.qyod,name = 'qyod'),
    path('qyodUSA/',views.qyodUSA,name = 'qyodUSA'),
    path('qyodReport/',views.qyodReport,name = 'qyodReport'),

    
    path('dalel/',views.dalel,name = 'dalel'),
    path('arseda/',views.arseda,name = 'arseda'),

    
    path('treeOfMain/',views.treeOfMain,name = 'treeOfMain'),
    path('treeOfMainAll/',views.treeOfMainAll,name = 'treeOfMainAll'),
    path('delete_treeElement/',views.delete_treeElement,name = 'delete_treeElement'),
    path('getElementParametersOfTree/',views.getElementParametersOfTree,name = 'getElementParametersOfTree'),
    path('getAllElementsRelatedToTreeElementAndType/',views.getAllElementsRelatedToTreeElementAndType,name = 'getAllElementsRelatedToTreeElementAndType'),
    path('getTransactionDetails/',views.getTransactionDetails,name = 'getTransactionDetails'),



    
    # path('print/<username>/', views.print_from_button ,name='printButton'),
    # path('ajax', views.answer_me, name='get_response'),
    # path('auth', views.authUser, name='authUser'),
    # path('logout', views.logout_req, name='logout'),
    # path('logoutSecured', views.logoutSecured_req, name='logoutSecured'),
]
