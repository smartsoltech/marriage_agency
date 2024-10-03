# profiles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, ProfileForm, GroomProfileForm, BrideProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile, GroomProfile, BrideProfile
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import get_backends
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from faker import Faker


def home(request):
    return render(request, 'profiles/home.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Аутентификация пользователя по email
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после успешного входа
        else:
            messages.error(request, 'Invalid email or password')  # Сообщение об ошибке
            return redirect('login')  # Перенаправление обратно на страницу входа при ошибке

    return render(request, 'profiles/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            fake = Faker()

            # Generate random username, first name, and last name
            random_username = fake.user_name()
            random_first_name = fake.first_name()
            random_last_name = fake.last_name()

            # Create user
            user = User.objects.create_user(
                username=random_username,
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )

            # Set the first and last name in the Profile model
            Profile.objects.create(
                user=user,
                first_name=random_first_name,
                last_name=random_last_name,
                date_of_birth=form.cleaned_data.get('date_of_birth')
            )

            # Log the user in after registration
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend
            auth_login(request, user)

            return redirect('create_profile')  # Redirect to the profile creation form

    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form': form})
@login_required
def create_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your profile has been created!'))
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/create_profile.html', {'form': form})


@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your profile has been updated!'))
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

from django.conf import settings
from django.utils import translation

def set_language(request):
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        if lang_code and lang_code in dict(settings.LANGUAGES).keys():
            translation.activate(lang_code)
            request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))


def profile_list(request):
    profiles = Profile.objects.all()

    user_type = request.GET.get('user_type')
    country = request.GET.get('country')
    city = request.GET.get('city')
    min_height = request.GET.get('min_height')
    max_height = request.GET.get('max_height')
    smoking = request.GET.get('smoking')
    children = request.GET.get('children')
    education = request.GET.get('education')

    if user_type:
        profiles = profiles.filter(user_type=user_type)
    if country:
        profiles = profiles.filter(country__icontains=country)
    if city:
        profiles = profiles.filter(city__icontains=city)
    if min_height:
        profiles = profiles.filter(height__gte=min_height)
    if max_height:
        profiles = profiles.filter(height__lte=max_height)
    if smoking:
        profiles = profiles.filter(smoking=smoking == 'true')
    if children:
        profiles = profiles.filter(children=children == 'true')
    if education:
        profiles = profiles.filter(education__icontains=education)

    return render(request, 'profiles/profile_list.html', {'profiles': profiles})    