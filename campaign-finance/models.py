from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime,
                           nullable=False,
                           server_default=db.func.now(),
                           onupdate=db.func.now())

## TODO: connecting users to filers - multiple users per fielr?

class Filer(BaseMixin, db.Model):
    __tablename__ = 'filers'

    type = db.Column(db.String(255), nullable=False) ## TODO: enum
    name = db.Column(db.String(255), nullable=False)
    candidate_supporting = db.Column(db.String(255))
    office = db.Column(db.String(255), nullable=False) ## TODO: enum or lookup table with constraint
    district_number = db.Column(db.Integer) ## TODO: lookup table with constraint
    party = db.Column(db.String(255)) ## TODO: lookup table with constraint
    county = db.Column(db.String(255)) ## TODO: lookup table with constraint
    phone = db.Column(db.String(255))
    address_line_1 = db.Column(db.String(255))
    address_line_2 = db.Column(db.String(255))
    city = db.Column(db.String(255)) ## TODO: lookup table with constraint
    state = db.Column(db.String(2)) ## TODO: lookup table with constraint
    zip_code = db.Column(db.String(10)) ## TODO: lookup table with constraint
    treasurer = db.Column(db.String(255)) 

class ElectionCycle(BaseMixin, db.Model):
    __tablename__ = 'election_cycles'

    name = db.Column(db.String(255))
    year = db.Column(db.Integer)

class Office(BaseMixin, db.Model):
    __tablename__ = 'offices'

    name = db.Column(db.String(255))

## TODO: use as through table?
class ElectionCycleOffice(db.Model):
    __tablename__ = 'election_cycle_offices'

    election_cycle_id = db.Column(db.Integer, db.ForeignKey('election_cycles.id'), primary_key=True)
    office_id = db.Column(db.Integer, db.ForeignKey('offices.id'), primary_key=True)

class ReportingCycle(BaseMixin, db.Model):
    __tablename__ = 'reporting_cycles'

    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

## TODO: use election_cycle_id and reporting_cycle_id as PK?
class ReportingCycleSchedule(BaseMixin, db.Model):
    __tablename__ = 'reporting_cycle_schedules'

    election_cycle_id = db.Column(db.Integer, db.ForeignKey('election_cycles.id'))
    reporting_cycle_id = db.Column(db.Integer, db.ForeignKey('reporting_cycles.id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    due_date = db.Column(db.Date)

class Report(BaseMixin, db.Model):
    __tablename__ = 'reports'

    filer_id = db.Column(db.Integer, db.ForeignKey('filers.id'))
    election_cycle_id = db.Column(db.Integer, db.ForeignKey('election_cycles.id'))
    reporting_cycle_id = db.Column(db.Integer, db.ForeignKey('reporting_cycles.id'))
    status = db.Column(db.String(255)) ## TODO: enum

class UnitemizedItems(BaseMixin, db.Model):
    __tablename__ = 'unitemized_items'

    report_id = db.Column(db.Integer, db.ForeignKey('reporting_cycle_schedules.id'))
    cash_contributions = db.Column(db.Numeric(scale=2))
    inkind_contributions = db.Column(db.Numeric(scale=2))

class Contribution(BaseMixin, db.Model):
    __tablename__ = 'contributions'

    contribution_type = db.Column(db.String(255)) ## TODO: enum - monetary or inkind
    contributor_type = db.Column(db.String(255)) ## TODO: enum
    full_name = db.Column(db.String(255)) ## TODO: entity table
    description = db.Column(db.String(2048))
    date = db.Column(db.Date)
    amount = db.Column(db.Numeric(scale=2))
    contributor_address_line_1 = db.Column(db.String(255)) ## TODO: addresses table?
    contributor_address_line_2 = db.Column(db.String(255))
    contributor_city = db.Column(db.String(255))
    contributor_state = db.Column(db.String(2))
    contributor_zip_code = db.Column(db.String(10))
    employer = db.Column(db.String(255))  ## TODO: entity table?
    occupation = db.Column(db.String(255))
    employer_address_line_1 = db.Column(db.String(255)) ## TODO: addresses table?
    employer_address_line_2 = db.Column(db.String(255))
    employer_city = db.Column(db.String(255))
    employer_state = db.Column(db.String(2))
    employer_zip_code = db.Column(db.String(10))
