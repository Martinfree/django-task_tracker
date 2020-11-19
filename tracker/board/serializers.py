from rest_framework import serializers

from board.models import Board,Task

class BoardSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Board
        fields ='__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects,many=False)

    class Meta(object):
        model = Task
        fields = ('head',
                'description',
                'release_date',
                'edit_at',
                'status',
                'board')
                
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
 
