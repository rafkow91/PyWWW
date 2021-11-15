from django.core.management.base import BaseCommand

from books.utils import create_books


class Command(BaseCommand):
    help = 'Creating fake books'

    def handle(self, *args, **options):
        numbers_of_books = options.get('number', 10)
        create_books(numbers_of_books)
        self.stdout.write(f'Created {numbers_of_books} posts')

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, default=10, dest='number')