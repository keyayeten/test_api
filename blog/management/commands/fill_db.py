import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Comment
from faker import Faker

class Command(BaseCommand):
    help = 'Наполняет базу данных фейковыми данными: пользователи, посты, комментарии'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Создаем фейковых пользователей
        num_users = 10
        users = []
        for _ in range(num_users):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Пользователь {user.username} создан'))

        # Создаем фейковые посты
        num_posts = 20
        posts = []
        for _ in range(num_posts):
            post = Post.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                author=random.choice(users)
            )
            posts.append(post)
            self.stdout.write(self.style.SUCCESS(f'Пост "{post.title}" создан'))

        # Создаем фейковые комментарии
        num_comments = 50
        for _ in range(num_comments):
            comment = Comment.objects.create(
                post=random.choice(posts),
                author=random.choice(users),
                text=fake.text()
            )
            self.stdout.write(self.style.SUCCESS(f'Комментарий создан: "{comment.text[:30]}..."'))
