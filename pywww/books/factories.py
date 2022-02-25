from random import randint

import factory
from faker import Factory

faker = Factory.create()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'books.Author'

    first_name = factory.LazyAttribute(lambda x: faker.name().split()[0])
    last_name = factory.LazyAttribute(lambda x: faker.name().split()[1])
    birth_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    birth_city = factory.LazyAttribute(lambda x: faker.city())
    death_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    death_city = factory.LazyAttribute(lambda x: faker.city())
    bio = factory.LazyAttribute(lambda x: faker.text(200))


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'books.Book'

    title = factory.LazyAttribute(lambda x: faker.text(randint(20, 100)))
    description = factory.LazyAttribute(lambda x: faker.text(randint(100, 250)))
    available = factory.LazyAttribute(lambda x: faker.boolean())
    publication_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    publication_city = factory.LazyAttribute(lambda x: faker.city())

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)
