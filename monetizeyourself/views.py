from django.urls import reverse_lazy
from django.views.generic import TemplateView, \
    CreateView, UpdateView, DetailView, ListView, DeleteView
import stripe
from monetizeyourself.forms import PostForm
from monetizeyourself.models import Post
from django.shortcuts import render, redirect

from payment.models import Payment



class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('monetizeyourself:post_list')

class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Post.objects.filter(is_free=True)

        return qs

class PayedPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'monetizeyourself/payed_post_list.html'

    inform_about_accout_pay = 0
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user


        payments = Payment.objects.filter(user=self.request.user)
        # print(payments)
        if not payments:
            self.inform_about_accout_pay = 1

        sessions = [payment.stripe_session_id for payment in payments]
        stripe.api_key = "sk_test_51OAXHdSFVg6LGnstWx1rKbLogFAh5PQI2VMhFuk9pIa5dr8urI2Ee838SmgFvdqdqW7roUbIVus4ha2A84uHo5pB00Lw6o6Xqp"

        for session in sessions:
            checkout_session_id = session
            checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)
            if checkout_session.payment_status == 'paid':
                return qs
            elif checkout_session.payment_status == 'unpaid':
                self.inform_about_accout_pay = 1

    def get_context_data(self, **kwargs):
        """Формируем данные для отображения в шаблоне"""
        context_data = super().get_context_data(**kwargs)
        if self.inform_about_accout_pay == 1:
            context_data["boo"] = "Ваш аккаунт не оплачен, пожалуйста, приобретите подписку !"

        return context_data




class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('monetizeyourself:post_list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('monetizeyourself:post_list')
