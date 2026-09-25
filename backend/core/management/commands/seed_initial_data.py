from pathlib import Path
import runpy

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Seed production-safe reference data after database migrations.'

    SEED_SCRIPTS = (
        'populate/populate_school_ownership_types.py',
        'backend/populate_categories.py',
        'populate/populate_zone.py',
        'populate/populate_districts.py',
        'populate/populate_clubs.py',
        'populate/populate_schools.py',
    )

    def handle(self, *args, **options):
        project_root = Path(settings.BASE_DIR).parent
        for relative_path in self.SEED_SCRIPTS:
            script_path = project_root / relative_path
            if not script_path.is_file():
                raise CommandError(f'Required seed script not found: {script_path}')

            self.stdout.write(f'Running {relative_path}')
            runpy.run_path(str(script_path), run_name='__main__')

        self.stdout.write(self.style.SUCCESS('Initial production data is ready.'))