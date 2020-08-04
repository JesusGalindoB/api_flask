from . import db
from sqlalchemy import desc 

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(59), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime())
    create_at = db.Column(db.DateTime(), nullable=False, 
                          default=db.func.current_timestamp())

    def __str__(self):
        return self.title

    @classmethod
    def new(cls, title, description):
        return Task(title=title, description=description)

    @classmethod
    def get_by_page(cls, page, per_page=10):
        return Task.query.order_by(desc(Task.id)).paginate(page, per_page).items

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False 

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def serializer(self):
        return {
            "title": self.title, 
            "description": self.description,
            "deadline": self.deadline
        }