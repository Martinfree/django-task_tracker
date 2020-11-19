from django.test import TestCase
from django.urls import reverse
 
import nose.tools as nt

from nose.tools.nontrivial import raises

from rest_framework import status
from rest_framework.test import APITestCase

from board.models import Board, Task

from board.serializers import (BoardSerializer, TaskSerializer,
                               TaskCreateSerializer, TaskUpdateSerializer)

#testing vars
DICT = {
        'board_name': 'board',
        'task_head': 'Your task ',
        'task_description': 'Some description '
        }


# set up data for model and api endpoint testing
class BoardTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create all data for Testing models"""
        cls.board = Board.objects.create(name = DICT.get('board_name') )

        cls.task = Task.objects.create(head = DICT.get('task_head'),
                                        description = DICT.get('task_description'),
                                        board = cls.board )
        
class BoardAPITests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.board1 = Board.objects.create(name = '{}{}'.format(DICT.get('board_name'),1) )

        cls.board2 = Board.objects.create(name = '{}{}'.format(DICT.get('board_name'),2) )

        cls.board3 = Board.objects.create(name = '{}{}'.format(DICT.get('board_name'),3) )        
        
        cls.board4 = Board.objects.create(name = '{}{}'.format(DICT.get('board_name'),4) )        
        
        cls.task1 = Task.objects.create(head = '{}{}'.format(DICT.get('task_head'),1),
                                        description = '{}{}'.format(DICT.get('task_description'),1) )
        
        cls.task2 = Task.objects.create(head = '{}{}'.format(DICT.get('task_head'),2),
                                        description = '{}{}'.format(DICT.get('task_description'),2),
                                        board = cls.board1)
        
        cls.task3 = Task.objects.create(head = '{}{}'.format(DICT.get('task_head'),3),
                                        description = '{}{}'.format(DICT.get('task_description'),3),
                                        board = cls.board1 )
        
        cls.task4 = Task.objects.create(head = '{}{}'.format(DICT.get('task_head'),4),
                                        description = '{}{}'.format(DICT.get('task_description'),4),
                                        board = cls.board2 )

        cls.task5 = Task.objects.create(head = '{}{}'.format(DICT.get('task_head'),5),
                                        description = '{}{}'.format(DICT.get('task_description'),5),
                                        board = cls.board2 )






class BoardModelsTest(BoardTests):
    
    def test_board(self):
        nt.assert_equal(self.board.name, DICT.get('board_name')) 
        nt.assert_true(self.board.release_date)
        nt.assert_true(self.board.edit_at)
        nt.assert_equal(self.board.__str__(), self.board.name)
        
    def test_task(self):
        nt.assert_equal(self.task.head, DICT.get('task_head'))
        nt.assert_equal(self.task.description, DICT.get('task_description'))
        nt.assert_equal(self.task.board, self.board)
        nt.assert_true(self.task.release_date)
        nt.assert_true(self.task.edit_at)
 

class BoardAPITests(BoardAPITests):

    def test_get_boards(self):
        url = reverse('boards')

        query = Board.objects.all()
        serializer = BoardSerializer(query,many = True)

        response = self.client.get(url)
        
        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_board(self):
        url = reverse('board', args=[self.board1.id])

        query = Board.objects.get(id=self.board1.id)
        serializer = BoardSerializer(query)

        response = self.client.get(url)
        
        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)
    
    def test_get_bad_by_id_board(self):
        url = reverse('board', args=[9999999])

        response = self.client.get(url)
        
        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)
     

    def test_post_create_board(self):
        url = reverse('boards')

        data = {
            "name": "Board1"
            }

        response = self.client.post(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_bad_board(self):
        url = reverse('boards')

        data = {
                "namE": "Name"
            }

        response = self.client.post(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_one_board(self):
        url = reverse('board', args = [self.board1.id])

        response = self.client.post(url)

        nt.assert_equal(response.data, "METHOD_NOT_ALLOWED")
        nt.assert_equal(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_id_board(self):
        url = reverse('board', args = [self.board1.id])

        data = {
                "name": self.board1.name + " edited",
            }

        response = self.client.put(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_put_bad_id_board(self):
        url = reverse('board', args = [9999999])

        data = {
                "name": self.board1.name + " edited",
            }

        response = self.client.put(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bad_put_id_board(self):
        url = reverse('board', args = [self.board1.id])

        data = {
                "nam": self.board1.name + " edited",
            }

        response = self.client.put(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_board(self):
        url = reverse('board', args = [self.board4.id])

        response = self.client.delete(url)

        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_delete_bad_board(self):
        url = reverse('board', args = [99999])

        response = self.client.delete(url)

        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_tasks(self):
        url = reverse('tasks')

        query = Task.objects.all()
        serializer = TaskSerializer(query,many = True)

        response = self.client.get(url)
        
        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_task(self):
        url = reverse('task', args=[self.task1.id])

        query = Task.objects.get(id=self.task1.id)
        serializer = TaskSerializer(query)

        response = self.client.get(url)
        
        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)
    
    def test_get_bad_by_id_task(self):
        url = reverse('task', args=[9999999])

        response = self.client.get(url)
        
        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)
     

    def test_post_create_task(self):
        url = reverse('tasks')

        data = {
                "head": "Task1",
                "description": "Description1"
            }

        response = self.client.post(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_bad_task(self):
        url = reverse('tasks')

        data = {
                "namE": "Name"
            }

        response = self.client.post(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_one_task(self):
        url = reverse('task', args = [self.task1.id])

        response = self.client.post(url)

        nt.assert_equal(response.data, "METHOD_NOT_ALLOWED")
        nt.assert_equal(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_id_task(self):
        url = reverse('task', args = [self.task1.id])

        data = { 
                "head": self.task1.head,
                "name": self.task1.description + " edited",
                "status": True
            }

        response = self.client.put(url, data, format='json')
        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_put_bad_id_task(self):
        url = reverse('task', args = [9999999])

        data = {
                "name": self.task1.description + " edited",
            }

        response = self.client.put(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bad_put_id_task(self):
        url = reverse('task', args = [self.task1.id])

        data = {
                "nam": self.task1.description + " edited",
            }

        response = self.client.put(url, data, format='json')

        nt.assert_equal(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_task(self):
        url = reverse('task', args = [self.task5.id])

        response = self.client.delete(url)

        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_delete_bad_task(self):
        url = reverse('task', args = [99999])

        response = self.client.delete(url)

        nt.assert_equal(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_filter_tasks_by_board_id(self):
        url = reverse('task_filter', args=[self.board2.id])

        query = Task.objects.filter(board_id=self.board2.id)
        serializer = TaskSerializer(query,many = True)

        response = self.client.get(url)

        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)

    def test_filter_task_by_board_null_id(self):
        url = reverse('task_filter')

        query = Task.objects.filter(board__isnull=True)
        serializer = TaskSerializer(query,many=True)

        response = self.client.get(url)
        
        nt.assert_equal(response.data, serializer.data)
        nt.assert_equal(response.status_code, status.HTTP_200_OK)
