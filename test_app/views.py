from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm, UserUpdateForm, PublicationForm
from .models import Profile, Publication
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request):
    # Получаем или создаем профиль для пользователя
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user': request.user, 'profile': profile})

def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile
    })


@login_required
def upload_avatar(request):
    if request.method == 'POST':
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    return redirect('profile')

def feed_view(request):
    publications = Publication.objects.all().order_by('-created_at')
    return render(request, 'feed.html', {'publications': publications})

@login_required
def new_publication(request):
    # Получаем или создаем профиль для пользователя
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.profile = profile
            publication.save()
            return redirect('feed')
    else:
        form = PublicationForm()
    return render(request, 'new_publication.html', {'form': form})