from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, User
from .serializers import TaskSerializer, AssignTaskSerializer,UserSerializer

@api_view(['POST'])
def CreateUserView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateTaskView(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def AssignTaskView(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    user_ids = request.data.get('user_ids', [])
    if not isinstance(user_ids, list):
        return Response({"error": "user_ids must be a list"}, status=status.HTTP_400_BAD_REQUEST)
    users = User.objects.filter(id__in=user_ids)
    if not users.exists():
        return Response({"error": "No valid user IDs provided"}, status=status.HTTP_400_BAD_REQUEST)
    task.users.set(users)
    task.save()
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def UserTasksView(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    tasks = user.tasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
