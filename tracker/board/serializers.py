from rest_framework import serializers

from board.models import Board,Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Task
        fields = (
                '__all__'
                )

class BoardSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Board
        fields =(
                'name',
                )

