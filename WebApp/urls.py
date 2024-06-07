from django.urls import path
from WebApp import views

urlpatterns=[
        path('',views.homepage,name="Home"),
        path('About/',views.aboutpage,name="About"),
        path('Contact/',views.contactpage,name="Contact"),
        path('Our_products/',views.ourproducts,name="Our_products"),
        path('save_contact/',views.save_contact,name="save_contact"),
        path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
        path('single_productpage/<int:pro_id>/',views.single_productpage,name="single_productpage"),

        path('registration_page/',views.registration_page,name="registration_page"),
        path('save_registration/',views.save_registration,name="save_registration"),
        path('UserLogin/',views.UserLogin,name="UserLogin"),
        path('UserLogout/',views.UserLogout,name="UserLogout"),
        path('user_login_page/',views.user_login_page,name="user_login_page"),

        path('save_cart/',views.save_cart,name="save_cart"),
        path('cart_page/',views.cart_page,name="cart_page"),
        path('delete_item/<int:p_id>/',views.delete_item,name="delete_item"),
]