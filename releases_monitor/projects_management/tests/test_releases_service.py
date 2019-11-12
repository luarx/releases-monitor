import logging

from django.test import TestCase

from ..services.releases_service import ReleasesProvider

logger = logging.getLogger(__name__)


class TestReleasesService(TestCase):
    # TODO
    def test_get_last_release_version_gitlab(self):
        self.assertEqual(1, 1)
    # TODO
    def test_get_last_release_version_github(self):
        self.assertEqual(1, 1)


