from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Program, Section

class SectionTests(APITestCase):
    def setUp(self):
        self.program_1 = Program.objects.create(
            name="Cognitive Behavioral Therapy",
            category=Program.CategoryChoices.COGNITIVE_BEHAVIORAL_THERAPY,
            description="Part One"
        )

        self.section_1 = Section.objects.create(name="Mindfullness",
                                                description="Awarness of everything around oneself.",
                                                program=self.program_1, order_index=1)

        self.section_2 = Section.objects.create(name="Values",
                                                description="Concepts that are important to us.",
                                                program=self.program_1, order_index=2)

    def test_get_section(self):
        res = self.client.get('/program/section/{}/'.format(self.section_1.id))

        section_1 = Section.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(section_1.id, self.section_1.id)

    def test_get_section_by_program_id(self):
        res = self.client.get('/program/section/{}/'.format(self.section_1.id))

        sections = Section.objects.filter(program_id=self.section_1.program.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(sections), 2)

    def test_create_section(self):
        res = self.client.post('/program/section/', data={
                                                    "name": "Action",
                                                    "description": "Mindful Communication",
                                                    "program": self.program_1.id,
                                                    "order_index": 3
                                                  }, format="json")

        newly_created_section = Section.objects.get(name="Action",
                                                    program_id=self.program_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_section.id)
        self.assertEqual(Section.objects.count(), 3)

    def test_create_section_with_invalid_order_index(self):
        res = self.client.post('/program/section/', data={
                                                    "name": "Action",
                                                    "description": "Mindful Communication",
                                                    "program": self.program_1.id,
                                                    "order_index": 2
                                                  }, format="json")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Section.objects.count(), 2)

    def test_update_program(self):
        res = self.client.put('/program/section/{}/'.format(self.section_1.id), data={
                                                "description": "New section description"
                                                }, format='json')

        updated_section = Section.objects.get(id=self.section_1.id)


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_section.description, "New section description")

    def test_delete_program(self):
        res = self.client.delete('/program/section/{}/'.format(self.section_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Section.objects.count(), 1)
