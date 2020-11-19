from rest_framework import serializers

from board.models import Board,Task

class BoardSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Board
        fields ='__all__'

class TaskSerializer(serializers.ModelSerializer):
    board = BoardSerializer()

    class Meta(object):
        model = Task
        fields = ('head',
                'description',
                'release_date',
                'edit_at',
                'status',
                'board')
 

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Task
        fields = ('head',
                'description',
                'release_date',
                'edit_at',
                'status',
                'board')


class TaskUpdateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Task
        fields = (
                'head',
                'description',
                'status'
                )

        extra_kwargs = {'board': {'required': False}}
            
    

