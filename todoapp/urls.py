from django.urls import path
from .views import TodoCreateView,TodoDetailView,TodoListView,TodosApiView
urlpatterns =[
path("create/", TodoCreateView.as_view(), name="create-todo"),
path("<uuid:pk>/", TodoDetailView.as_view(), name="detail-todo"),
path("todos/", TodosApiView.as_view(), name="list-todo"),

]