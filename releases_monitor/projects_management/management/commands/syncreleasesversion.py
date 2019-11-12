from django.core.management.base import BaseCommand
from ...models import Library
import logging
from ...services.releases_service import ReleasesProvider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Sync last releases versions of libraries which we want to monitor"

    def handle(self, *args, **options):
        releases_service = ReleasesProvider()

        for library in Library.objects.all():
            try:
                last_release = releases_service.get_last_library_release(library)

                library.last_version = last_release["version"]
                library.last_version_date = last_release["date"]
                if library.last_version is not None:
                    library.save()
                    logger.info("Library: {}, Repo: {} --- Last release version: {} (date: {})".format(
                        library.name, library.repo_url, library.last_version, library.last_version_date))
                else:
                    logger.error("[ERROR] Library: {}, Repo: {} --- VERSION is empty".format(
                        library.name, library.repo_url))
            except Exception as e:
                logger.error("[ERROR] Exception: {}".format(e))
