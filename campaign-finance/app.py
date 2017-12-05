import os

from flask import Flask
from flask_admin import Admin

import models
import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_ALCHEMY_CONNECTION', 'postgresql://localhost/campaign_finance')

models.db.init_app(app)

admin = Admin(app, url='/', name='Campaign Finance', template_mode='bootstrap3')

# setup / lookup tables
admin.add_view(views.ElectionCycleView(models.ElectionCycle, models.db.session))
admin.add_view(views.OfficeView(models.Office, models.db.session))
admin.add_view(views.ReportingCycleView(models.ReportingCycle, models.db.session))
admin.add_view(views.ReportingCycleScheduleView(models.ReportingCycleSchedule, models.db.session))

# filer views
admin.add_view(views.FilerView(models.Filer, models.db.session))
admin.add_view(views.ReportView(models.Report, models.db.session))
admin.add_view(views.UnitemizedItemsView(models.UnitemizedItems, models.db.session))
admin.add_view(views.ContributionView(models.Contribution, models.db.session))

if __name__ == '__main__':
    with app.app_context():
        models.db.create_all()

    app.run()
