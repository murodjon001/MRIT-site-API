from django.test import TestCase, Client
from mrit_api.models.project import Projects
from mrit_api.serializer import ProjectsSerializer


class TestProjectsViewsQ(TestCase):

    def setUp(self) -> None:
        self.projet = Projects.objects.create(project_name='Test')
        self.client = Client()


    def test_get_all_albums(self):
        response = self.client.get('/projects/')
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['name'], 'Test')