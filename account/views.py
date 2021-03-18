from django.shortcuts import render
from .forms import ProfileForm, UserCreateForm

# Create your views here.
def register(request):
    registered = False

    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST)
        user_form = UserCreateForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.web_user = user
            profile.save()
            registered = True
        else:
            print(profile_form.errors,user_form.errors)
    else:
        profile_form = ProfileForm()
        user_form = UserCreateForm()
    context = {
        'registered':registered,
        'user_form':user_form,
        'profile_form':profile_form,
    }

    return render(request,'account/register.html',context=context) 
