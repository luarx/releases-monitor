from django.core.management.base import BaseCommand
from ...models import ProjectLibrary, Environment
import logging

from django_slack import slack_message

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Notify project libraries that must be updated"

    def get_not_updated_libraries_of_environment(self, environment):
        return [project_library for project_library in ProjectLibrary.objects.filter(
            project__environment__name=environment.name) if not project_library.is_version_updated]

    def send_slack_notification(self, environment, project_libraries_not_updated):
        slack_message('slack/available_updates_notification.slack', {
            'environment': environment,
            'project_libraries_not_updated': project_libraries_not_updated,
        })

    def handle(self, *args, **options):
        for environment in Environment.objects.all():
            project_libraries_not_updated = self.get_not_updated_libraries_of_environment(
                environment)

            if project_libraries_not_updated:
                self.send_slack_notification(environment, project_libraries_not_updated)

            logger.info("Environment: {} --- NOT updated libraries: {}".format(
                environment.name, len(project_libraries_not_updated)))
