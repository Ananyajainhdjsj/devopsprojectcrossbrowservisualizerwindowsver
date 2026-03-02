from extensions import db
from datetime import datetime

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(200))
    browser = db.Column(db.String(50))
    status = db.Column(db.String(20))
    execution_time = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)