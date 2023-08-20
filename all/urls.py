from django.urls import path
from .views import HomePageView
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('user/register/', TelegramRegistrationView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<str:cat>/', ServiceListAPIView.as_view()),
    path('product/', Service2ListAPIView.as_view()),
    path('order/', OrderCreateView.as_view()),
    path('order/update/<int:pk>/', OrderUpdateAPIView.as_view()),
    path('order/<int:pk>/', OrderRetrieveAPIView.as_view()),
    path('user/<int:pk>/', UserListAPIView.as_view()),
    path('user/', UserListAPIView.as_view()),
    path('order/<int:pk>/', OrderListAPIView.as_view()),
    path('korzina/list/<int:pk>/', KorzinListView.as_view()),
    path('korzina/delete/<int:pk>/', KorzinaDestroyView.as_view()),
    path('korzina/clear/<int:user>/', KorzinaDelateAPIView),
    path('korzina/create/', KorzinCreateView.as_view()),
]
