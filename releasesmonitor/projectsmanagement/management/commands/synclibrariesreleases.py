from django.core.management.base import BaseCommand
from ...models import Library

import feedparser
import re


class Command(BaseCommand):
    help = "Sync releases of libraries which we want to monitor"

    def get_last_library_release_version(self, library):
        releasesFeed = feedparser.parse("{}/releases.atom".format(library.repo_url))

        if releasesFeed and releasesFeed.entries:
            last_release = releasesFeed.entries[0]['id']
            release_version_match = re.search('v\d*\.\d*\.\d*$', last_release)

            if release_version_match:
                return release_version_match.group(0)
            else:
                self.stdout.write(self.style.ERROR("Library: {}, Repo: {} --- Does not follow Semantic Versioning format".format(library.name, library.repo_url)))
                return None
        else:
            self.stdout.write(self.style.ERROR("Library: {}, Repo: {} --- Does not have any release available".format(library.name, library.repo_url)))
            return None

    def handle(self, *args, **options):
        for library in Library.objects.all():
            try:
                library.last_version = self.get_last_library_release_version(library)
                if library.last_version != None:
                    library.save()
                    self.stdout.write(self.style.SUCCESS("Library: {}, Repo: {} --- Last release version: {}".format(library.name, library.repo_url, library.last_version)))
            except Exception as e:
                self.stdout.write(self.style.ERROR("[ERROR] Exception: {}".format(e.message)))
