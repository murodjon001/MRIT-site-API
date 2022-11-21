from django.test import Client,TestCase
from mrit_api.models.project import Projects
from mrit_api.serializer import ProjectsSerializer

class TestSerializer(TestCase):
    def setUp(self) -> None:
        self.projects_name = Projects.objects.create(projec_name='Test_project')
        self.projects_name1 = Projects.objects.create(project_name='Test2',images='media/media/glavni.jpg',project_url='https://t.me/developer_sam_city')
        def test_data(self):
            data = ProjectsSerializer(self.projects_name).data
            data1 = ProjectsSerializer(self.projects_name1).data

            assert data['id'] is not None
            assert data1['project_url'] is not None


