from mongoengine import Document, fields, EmbeddedDocument
from datetime import datetime

class Subtask(EmbeddedDocument):
    name = fields.StringField(max_length=100, required = True)
    description = fields.StringField()
    is_complited = fields.BooleanField(default=False)
    created_date = fields.DateTimeField(default = datetime.now)
    complited_date = fields.DateTimeField(null=True)

    def task_comolited(self):
        self.is_complited = True
        self.date_complited = datetime.now()
        self.save()

    def task_pending(self):
        self.is_complited = False
        self.complited_date = None
        self.save()
    

class Task(Document):
    user_id = fields.ReferenceField('Users', required = True, reverse_delete_rule=1)
    name = fields.StringField(max_length= 100, required = True, unique = False)
    description = fields.StringField()
    date_created = fields.DateTimeField(default=datetime.now)
    date_updated = fields.DateTimeField(default=datetime.now)
    date_complited = fields.DateTimeField(null = True)
    due_date = fields.DateTimeField(null=True)
    is_complited = fields.BooleanField(default = True)
    status = fields.StringField(
        choices = ('panding', 'in_progress', 'complited'),
          default = 'panding'
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

    