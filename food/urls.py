from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    # index page: /food/
    path('', views.index, name="index"),
    # show page: /food/1 (id)
    path('<int:item_id>/', views.detail, name="detail"),
    path('item/', views.item, name="item"),

]
