from django.urls import path, include
from . import views
from appBooks.views import BookList, BookCreate, Book1

urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>/', Book1.as_view())
]
