from django.urls import path
# from . import views
from . import views


app_name = "ktp_test_api"
urlpatterns = [
    # #########################
    # below is for class based view
    # #########################
    path('list/', views.InkhawmInchhiarnaBlogNewSerializer_list_create_view,
         name="inkhawm_list"),
    # below is the combine of list and create
    # path('', views.product_list_create_view, name="prod_list_create"),
    # belwo is for the create only
    # path('', views.product_create_view, name="prod_create")
    # update
    # path('<int:pk>/update/', views.ProductUpdateAPIview.as_view(), name="prod_update"),
    # # delete
    # path('<int:pk>/delete/', views.ProductDeleteAPIview.as_view(), name="prod_delete"),
]
