from django.core.management.base import BaseCommand, CommandError
from core.models.profile import Profile


class Command(BaseCommand):
    help = "This is commnad show profile"

    def add_arguments(self, parser):
        parser.add_argument("id", nargs="+", type=int)
        parser.add_argument("name", nargs="1", type=str)

    def handle(self, *args, **options):
        print(args)
        print(options)
        try:
            id = options.get("id")[0]
            profile = Profile.objects.get(id=id)
            print(profile.name)
        except Exception as e:
            raise CommandError(e)
