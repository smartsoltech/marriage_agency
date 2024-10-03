# verification/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VerificationForm
from .models import ProfileVerification
from django.contrib import messages

@login_required
def upload_verification(request):
    try:
        verification = request.user.profileverification
    except ProfileVerification.DoesNotExist:
        verification = None

    if request.method == 'POST':
        form = VerificationForm(request.POST, request.FILES, instance=verification)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.profile = request.user
            verification.save()
            messages.success(request, _('Your documents have been uploaded for verification.'))
            return redirect('profile_detail', pk=request.user.profile.pk)
    else:
        form = VerificationForm(instance=verification)
    return render(request, 'verification/upload_verification.html', {'form': form})
