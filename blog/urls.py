from django.urls import path
from .views import BlogListView, BlogInit

app_name="blog"

urlpatterns = [
    path('admon/', BlogListView.as_view(), name="home_Admin"),
    path('', BlogInit.as_view(), name="homes"),
]
