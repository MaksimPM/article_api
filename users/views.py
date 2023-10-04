import random
import string

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        token = ''.join(random.sample(string.digits + string.ascii_letters, 12))
        self.object.token = token
        self.object.is_active = False
        self.object.save()
        url = 'http://127.0.0.1:8000/users/verify/' + token

        if form.is_valid():
            send_mail(
                subject='Подтверждение регистрации',
                message=f"""Для подтверждения регистрации и присоединении к команде перейдите по ссылке: {url}
                        Внимание! Если вы не понимаете, почему Вам пришло это письмо, просто проигнорируйте его""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verify_email(request, token):
    user = User.objects.filter(token=token).first()
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('users:login')


def reset_password(request):
    if request.method == 'POST':
        input_email = request.POST.get('email')
        user = User.objects.filter(email=input_email).first()
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])
        send_mail(
            subject='Сброс пароля',
            message=f'''Вы успешно сбросили пароль для аккаунта {input_email}.\n Ваш новый пароль: {password}''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[input_email]
        )

    return render(request, 'users/reset_password.html')
