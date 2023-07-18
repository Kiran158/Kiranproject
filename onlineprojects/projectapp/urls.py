from django.urls import path
from .views import HomePage, SignUpView, CustomLoginView

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]