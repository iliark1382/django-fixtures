from django.core.management.base import AppCommand
from django.apps import AppConfig
from mimesis.locales import LIST_OF_LOCALES
from mockango.core.fixture import Fixture


class Command(AppCommand):

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='app_label', nargs='+', help='One or more application label.')
        parser.add_argument('--num', type=int, default=10, help='number of instances generate for each model')
        parser.add_argument('--format', type=str, default='json', choices=['json', 'yaml'], help='fixture file format')
        parser.add_argument('--locale', type=str, default='en', choices=LIST_OF_LOCALES,
                            help='locale to generate data in your native language')

    def handle_app_config(self, app_config: AppConfig, **options):
        for model in app_config.get_models():
            fixture = Fixture(model=model, num=options['num'], fixture_format=options['format'],
                              locale=options['locale'])
            self.stdout.write(fixture.create_fixtures_dir())
            self.stdout.write(fixture.create_fixture_file())