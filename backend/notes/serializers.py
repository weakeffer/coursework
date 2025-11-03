from rest_framework import serializers
from .models import Task, Subtask

class SubtaskSerializer(serializers.Serializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class TaskSerializer(serializers.Serializer):
    subtasks = SubtaskSerializer(many=True, required = False)

    class Meta:
        model = Task
        fields = '__all__'