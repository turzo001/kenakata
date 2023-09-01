from django.urls import path
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
                        ############ dashboard ###### 

    #basic
    path('basiclogin/', views.basiclogin,name='basiclogin'),
    path('basicregister/', views.basicregister,name='basicregister'),
    path('basicresetpass/', views.basicresetpass,name='basicresetpass'),
    path('basicforgotpass/', views.basicforgotpass,name='basicforgotpass'),

    
    path('addnewprod/', views.AddProduct.as_view(),name='addnewprod'),
    path('productedit/<int:pk>', views.ProductEditView.as_view(), name='productedit'),
    path('productdelete/<int:pk>', views.ProductDeleteView.as_view(), name='productdelete'),
    path('ecommercecustomerdetails/<int:pk>', views.ecommercecustomerdetails.as_view(), name='ecommercecustomerdetails'),

    path('ecommercecustomers/', views.ecommercecustomers.as_view(),name='ecommercecustomers'),
    path('ecommerceorderdetails/<int:pk>', views.OrderPlaced.as_view(),name='ecommerceorderdetails'),
    path('ecommerceorders', views.ecommerceorder.as_view(),name='ecommerceorders'),
    path('ecommerceprod/', views.ProductListView.as_view(),name='ecommerceprod'),
        
    path('index/', views.dashboardindex.as_view(),name='index'),
        
    path('pageseditprofile/', views.pageseditprofile,name='pageseditprofile'),
    
    path('pageseror403/', views.pageseror403,name='pageseror403'),
    path('pageseror404/', views.pageseror404,name='pageseror404'),
    path('pageseror500/', views.pageseror500,name='pageseror500'),
    
    path('pricingtable/', views.pricingtable,name='pricingtable'),

    
    path('timeline/', views.timeline,name='timeline'),
    path('userprofile/', views.userprofile,name='userprofile'),
    
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)