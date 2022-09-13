from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        dob = form.cleaned_data.get('birth_date')
        self.object = form.save(commit=False)
        self.object.save()
        self.object.profile.birth_date = dob
        self.object.save()
        return super().form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            return redirect('accounts:login')
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})
