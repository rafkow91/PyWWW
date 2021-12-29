from faker import Faker
from random import randint

from posts.models import Post


def create_posts(n=10):
    fake = Faker('pl_PL')
    for _ in range(n):
        fake_date = fake.date_time()
        post = Post(
            title=fake.text(randint(20, 100)),
            content=fake.text(randint(100, 500)),
            published=fake.boolean(),
            created=fake_date,
            modified=fake_date + fake.time_delta(5),
            sponsored=fake.boolean(),
            author=3
        )

        post.save()
