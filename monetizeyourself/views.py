from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView,
)
import stripe
from monetizeyourself.forms import PostForm
from monetizeyourself.models import Post

from payment.models import Payment


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("monetizeyourself:post_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):

    """Главная страница сервиса с бесплатным контентом"""

    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Post.objects.filter(is_free=True)

        return qs


class PayedPostListView(ListView):

    """Страница с платным контентом"""

    model = Post
    context_object_name = "posts"
    template_name = "monetizeyourself/payed_post_list.html"

    inform_about_accout_pay = 0

    def get_queryset(self):
        qs = super().get_queryset()

        # Делаем выборку по платежам пользователя

        payments = Payment.objects.filter(user=self.request.user)

        # Если истории платежей нет, то информируем пользователя
        if not payments:
            self.inform_about_accout_pay = 1

        # Достаем id платежной сессии из истории платежей
        sessions = [payment.stripe_session_id for payment in payments]
        stripe.api_key = settings.STRIPE_API_KEY

        # Проверяем пользователя на оплату подписки

        for session in sessions:
            checkout_session_id = session
            checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

            # Если оплатил - то показываем объекты страницы платного контента
            if checkout_session.payment_status == "paid":
                return qs

            # Если нет, то необходимо проинформировать
            elif checkout_session.payment_status == "unpaid":
                self.inform_about_accout_pay = 1

    def get_context_data(self, **kwargs):
        """Формируем данные для отображения в шаблоне страницы платного контента"""

        context_data = super().get_context_data(**kwargs)

        # Если оплата не произведена - выводим информационное сообщение
        if self.inform_about_accout_pay == 1:
            context_data[
                "need_to_purchase_account"
            ] = "Ваш аккаунт не оплачен, пожалуйста, приобретите подписку !"

        return context_data


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("monetizeyourself:post_list")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("monetizeyourself:post_list")
