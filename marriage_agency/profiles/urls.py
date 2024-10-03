from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница профилей
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.login, name='login'),  # Вход
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profiles', views.profile_list, name='view_profiles'),
    path('profile/create/', views.create_profile, name='create_profile'),  # Создание профиля
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),  # Детали профиля
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # Редактирование профиля
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
