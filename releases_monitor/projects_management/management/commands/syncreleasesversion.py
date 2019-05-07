from django.core.management.base import BaseCommand
from ...models import Library
import logging
import feedparser
import re

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Sync last releases versions of libraries which we want to monitor"

    def get_last_library_release(self, library):
        releasesFeed = feedparser.parse("{}/releases.atom".format(library.repo_url))

        if releasesFeed and releasesFeed.entries:
            last_release_id = releasesFeed.entries[0]['id']

            release_version_match = re.search(
                '(?<=\/)\D*(?P<mayor>\d*)\.(?P<minor>\d*)(\.(?P<patch>\d*))?.*$', last_release_id)

            if release_version_match:
                last_release = {"version": release_version_match.group(0), "date": releasesFeed.entries[0]['updated']}
                return last_release
            else:
                logger.error(
                    "Library: {}, Repo: {} --- Does not follow Semantic Versioning format".format(library.name, library.repo_url))
                return None
        else:
            logger.error(
                "Library: {}, Repo: {} --- Does not have any release available".format(library.name, library.repo_url))
            return None

    def handle(self, *args, **options):
        for library in Library.objects.all():
            try:
                last_release = self.get_last_library_release(library)

                library.last_version = last_release["version"]
                library.last_version_date = last_release["date"]
                if library.last_version != None and library.last_version_date != None:
                    library.save()
                    logger.info("Library: {}, Repo: {} --- Last release version: {} (date: {})".format(
                        library.name, library.repo_url, library.last_version, library.last_version_date))
                else:
                    logger.error("[ERROR] Library: {}, Repo: {} --- VERSION or VERSION_DATE is empty".format(
                        library.name, library.repo_url))
            except Exception as e:
                logger.error("[ERROR] Exception: {}".format(e))
