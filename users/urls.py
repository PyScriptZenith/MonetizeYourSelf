from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name


urlpatterns = [
    # path('', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', UserUpdateView.as_view(), name='profile'),
    # path('profile/genpassword', generate_new_password, name='generate_new_password'),
    # path('verify_email/<str:uidb64>/<str:token>/', verify_email, name='verify_email')
]
