from faker import Faker
from random import randint
from books.models import Book


def create_books(n=10):
    fake = Faker('pl_PL')
    for _ in range(n):
        fake_date = fake.date_time()
        fake_author = fake.name().split()
        book = Book(
            title=fake.text(randint(20, 100)),
            author_first_name=fake_author[0],
            author_last_name=fake_author[1],
            description=fake.text(randint(100, 300)),
            publication_year=randint(-1000, 2021),
            publication_city=fake.city(),
            created_at=fake_date,
            modified_at=fake_date + fake.time_delta(5),
            available=fake.boolean(),
        )

        book.save()
