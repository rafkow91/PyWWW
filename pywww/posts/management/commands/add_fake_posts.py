from django.core.management.base import BaseCommand

from posts.utils import create_posts


class Command(BaseCommand):
    help = 'Creating fake post'

    def handle(self, *args, **options):
        numbers_of_posts = options.get('number', 10)
        create_posts(numbers_of_posts)
        self.stdout.write(f'Created {numbers_of_posts} posts')

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, default=10, dest='number')
