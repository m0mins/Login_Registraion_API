from django.urls import path
from .views import RegisterAPIView, LoginAPIView

#urlpatterns = [
    #path('register/', RegisterAPIView.as_view(), name='register'),
    #path('login/', LoginAPIView.as_view(), name='login'),
#]


from django.urls import path
from loginRegg.views import LoginAPIView,RegistrationAPIView

urlpatterns = [
    # User endpoints
    #path('users/', UserListCreateView.as_view(), name='user-list-create'),
    #path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    # Profile endpoints
    #path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    #path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
    path('registration',RegistrationAPIView.as_view() ,name='registration_api'),
    #path('registration',RegistrationAPIView.as_view()),

    path('login',LoginAPIView.as_view(), name='login_api'),
]

