from django.core.management.base import BaseCommand
from ...models import Library
import logging
import feedparser
import re

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Sync last releases versions of libraries which we want to monitor"

    def get_last_library_release_from_gitlab(self, library):
        releases_feed = feedparser.parse("{}/tags?format=atom".format(library.repo_url))

        if releases_feed and releases_feed.entries:
            last_release_version = releases_feed.entries[0]["title"]

            # Some repos like "https://gitlab.com/gitlab-org/gitlab/-/tags?format=atom"
            # does not contain the "updated" field (it is an open issue)
            if "updated" in releases_feed.entries[0]:
                last_release_date = releases_feed.entries[0]["updated"]
            else:
                # Repos that do not have "updated" value will use the default time
                last_release_date = None

            last_release = {"version": last_release_version,
                            "date": last_release_date}
            return last_release
        else:
            logger.error(
                "Library: {}, Repo: {} --- Does not have any release available".format(library.name, library.repo_url))
            return None

    def get_last_library_release_from_github(self, library):
        releases_feed = feedparser.parse("{}/releases.atom".format(library.repo_url))

        if releases_feed and releases_feed.entries:
            last_release_id = releases_feed.entries[0]['id']

            release_version_match = re.search(
                '(?<=\/)\D*(?P<mayor>\d*)\.(?P<minor>\d*)(\.(?P<patch>\d*))?.*$', last_release_id)

            if release_version_match:
                last_release = {"version": release_version_match.group(0), "date": releases_feed.entries[0]['updated']}
                return last_release
            else:
                logger.error(
                    "Library: {}, Repo: {} --- Does not follow Semantic Versioning format".format(library.name,
                                                                                                  library.repo_url))
                return None
        else:
            logger.error(
                "Library: {}, Repo: {} --- Does not have any release available".format(library.name, library.repo_url))
            return None

    def get_last_library_release(self, library):
        if library.repo_type == Library.GITHUB:
            return self.get_last_library_release_from_github(library)
        elif library.repo_type == Library.GITLAB:
            return self.get_last_library_release_from_gitlab(library)

    def handle(self, *args, **options):
        for library in Library.objects.all():
            try:
                last_release = self.get_last_library_release(library)

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
