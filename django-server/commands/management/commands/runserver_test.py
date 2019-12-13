from django.contrib.staticfiles.management.commands import runserver


def setup_test_data():
    from django.contrib.auth.models import User

    username = "root"
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email="",
            password="root1234",
            first_name="Mr",
            last_name="Root",
        )


class Command(runserver.Command):
    help = "Runs the server with test data"

    def run(self, **options):
        from django.core.management import call_command

        call_command("migrate")
        setup_test_data()
        super().run(**options)
