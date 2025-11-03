from mongoengine import Document, fields, EmbeddedDocument
from datetime import datetime

class Subtask(EmbeddedDocument):
    name = fields.StringField(max_length=100, required = True)
    description = fields.StringField()
    is_completed = fields.BooleanField(default=False)
    created_date = fields.DateTimeField(default = datetime.now)
    completed_date = fields.DateTimeField(null=True)

    def task_comolited(self):
        self.is_completed = True
        self.date_completed = datetime.now()
        self.save()

    def task_pending(self):
        self.is_completed = False
        self.completed_date = None
        self.save()
    

class Task(Document):
    user_id = fields.ReferenceField('Users', required = True, reverse_delete_rule=1)
    name = fields.StringField(max_length= 100, required = True, unique = False)
    description = fields.StringField()
    date_created = fields.DateTimeField(default=datetime.now)
    date_updated = fields.DateTimeField(default=datetime.now)
    date_completed = fields.DateTimeField(null = True)
    due_date = fields.DateTimeField(null=True)
    is_completed = fields.BooleanField(default = False)
    status = fields.StringField(
        choices = ('pending', 'in_progress', 'complited'),
          default = 'pending'
    )

    priority = fields.StringField(
        choices = ('low', 'medium', 'high'),
        default = 'low'
    )

    subtasks = fields.EmbeddedDocumentListField(Subtask, default = list)

    meta = {
        'collection' : 'tasks',
        'indexes': [
            'user_id',
            'status',
            'priority',
            'due_date',
            {'fields' : ['user_id', 'status']},
            {'fields' : ['user_id', 'due_date']}
        ],
        'ordering' : ['-date_created']
    }

    