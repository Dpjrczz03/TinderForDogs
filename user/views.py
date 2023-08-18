from django.shortcuts import render, redirect
from django.contrib import messages
from .forms1 import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, GenderForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = GenderForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            a=form2.save(commit=False)
            a.POST=request.POST
            a.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form1 = UserRegisterForm()
        form2 = GenderForm()
    return render(request, 'user/register.html', {'form1': form1, 'form2': form2})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context={'u_form': u_form, 'p_form': p_form}
    return render(request, 'user/profile.html',context)