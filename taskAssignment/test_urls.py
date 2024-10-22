from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import CreateUserView, CreateTaskView, AssignTaskView, UserTasksView

class TestUrls(SimpleTestCase):

    def test_create_user_url_is_resolved(self):
        url = reverse('create-user')
        self.assertEqual(resolve(url).func, CreateUserView)

    def test_create_task_url_is_resolved(self):
        url = reverse('create-task')
        self.assertEqual(resolve(url).func, CreateTaskView)

    def test_assign_task_url_is_resolved(self):
        url = reverse('assign-task', args=[1])
        self.assertEqual(resolve(url).func, AssignTaskView)

    def test_user_tasks_url_is_resolved(self):
        url = reverse('user-tasks', args=[1])
        self.assertEqual(resolve(url).func, UserTasksView)