from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Program

class ProgramTests(APITestCase):
    def setUp(self):
        self.program_1 = Program.objects.create(
            name="Leadership Development",
            category=Program.CategoryChoices.LEADERSHIP_DEVELOPMENT,
            description="Part One"
        )

        self.program_2 = Program.objects.create(
            name="Cognitive Behavioral Therapy",
            category=Program.CategoryChoices.COGNITIVE_BEHAVIORAL_THERAPY,
            description="Part Two"
        )

    def test_get_program(self):
        res = self.client.get('/program/{}/'.format(self.program_1.id))

        program_1 = Program.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(program_1.id, self.program_1.id)

    def test_create_program(self):
        res = self.client.post('/program/', data={
                                                    "name":"Mindful Communication",
                                                    "category": Program.CategoryChoices.MINDFUL_COMMUNICATION,
                                                    "description": "Part Three"
                                                  }, format='json')

        newly_created_program = Program.objects.get(name="Mindful Communication",
                                                    category=Program.CategoryChoices.MINDFUL_COMMUNICATION)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_program.id)
        self.assertEqual(Program.objects.count(), 3)

    def test_update_program(self):
        res = self.client.put('/program/{}/'.format(self.program_1.id), data={
                                                "description": "Mindful Communication"
                                                }, format='json')

        updated_program = Program.objects.get(id=self.program_1.id)


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_program.description, "Mindful Communication")

    def test_delete_program(self):
        res = self.client.delete('/program/{}/'.format(self.program_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Program.objects.count(), 1)



