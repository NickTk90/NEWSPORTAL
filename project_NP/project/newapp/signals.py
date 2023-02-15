from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import PostCategory
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, action, **kwargs):
    if action == 'post_add' and instance.__class__.__name__ == 'Post':
        for category in instance.postCategory.all():

            emails = User.objects.filter(
                subscriptions__category=category
            ).values_list('email', flat=True)
            print(emails)

            subject = f'Новый пост в категории: {category}'
            print(subject)

            text_content = (
                f'Пост: {instance.title}\n'
                # f'Цена: {instance.price}\n\n'
                f'Ссылка на пост: http://127.0.0.1{instance.get_absolute_url()}'
                )
            html_content = (
                f'Пост: {instance.title}<br>'
                # f'Цена: {instance.price}<br><br>'
                f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
                f'Ссылка на Пост</a>'
                )
            for email in emails:
                msg = EmailMultiAlternatives(subject, text_content, None, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()