from flask_admin.contrib.sqla import ModelView

class BaseView(ModelView):
    form_excluded_columns = ['created_at', 'updated_at']

class FilerView(BaseView):
    form_choices = {
        'type': [
            ('campaign', 'Campaign'),
            ('individual', 'Individual')
        ],
        'office': [
            ('mayor', 'Mayor'),
            ('council_member', 'Council Member')
        ]
    }

class ElectionCycleView(BaseView):
    pass

class OfficeView(BaseView):
    pass

class ReportingCycleView(BaseView):
    pass

class ReportingCycleScheduleView(BaseView):
    pass

class ReportView(BaseView):
    pass

class UnitemizedItemsView(BaseView):
    pass

class ContributionView(BaseView):
    pass
