from business.activity_service import ActivityService
from business.impl.command.activity.find import Find
from business.impl.command.activity.find_by_context import FindByContext
from business.impl.command.activity.update import Update


class ActivityServiceImpl(ActivityService):

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find(self, activity):
        return Find(activity).execute()

    def update(self, activity):
        return Update(activity).execute()
