
from django.urls import path
from  .import views


urlpatterns = [

    path('',views.starter,name="home"),
    path('home/',views.home,name="home"),
    path('hom/', views.hom, name="home"),
     path('programming/', views.programming, name="program"),
     path('products/', views.products, name="program"),
    path('malt-plot/', views.multi_plot, name="malt-plot"),

    path("combo/", views.combo, name="combo"),
]