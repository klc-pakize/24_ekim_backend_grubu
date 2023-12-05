from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView

from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET', 'POST'])
def todo_list_create(request):

    if request.method == 'GET':
        todos = Todo.objects.all()  # queyset
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):

    if request.method == 'GET':
        # todo = Todo.objects.get(id=pk)  # queryset
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


    elif request.method == 'PUT':
        # todo = Todo.objects.get(id=pk)  # queryset
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        # todo = Todo.objects.get(id=pk)
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()
        message = {
            "message": "Todo Deleted"
        }
        return Response(message)
    


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer    