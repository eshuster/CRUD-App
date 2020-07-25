from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, ContentHeader, Program, Section

class ContentHeaderTests(APITestCase):
    def setUp(self):
        self.program_1 = Program.objects.create(
            name="Cognitive Behavioral Therapy",
            category=Program.CategoryChoices.COGNITIVE_BEHAVIORAL_THERAPY,
            description="Part One"
        )

        self.section_1 = Section.objects.create(name="Mindfullness",
                                                description="Awarness of everything around oneself.",
                                                program=self.program_1, order_index=1)

        self.activity_1 = Activity.objects.create(name="Activity One",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.CONTENT,
                                                  section=self.section_1)


        self.content_header_1 = ContentHeader.objects.create(text="What Does Mindfulness Do?",
                                                             activity=self.activity_1)

    def test_get_content_header(self):
        res = self.client.get('/program/{}/contentheader/{}/'.format(self.activity_1.id, self.content_header_1.id))

        content_header = ContentHeader.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(content_header.id, self.content_header_1.id)

    def test_create_content_header(self):
        res = self.client.post('/program/contentheader/', data={
            "text": "What makes a good crepe?",
            "activity": self.activity_1.id
        }, format="json")

        newly_created_content_header = ContentHeader.objects.get(text="What makes a good crepe?",
                                                      activity_id=self.activity_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_content_header.id)
        self.assertEqual(ContentHeader.objects.count(), 2)

    def test_update_content_header(self):
        res = self.client.put('/program/{}/contentheader/{}/'.format(self.activity_1.id, self.content_header_1.id), data={
            "text": "What's up?"
        }, format='json')

        updated_content_header = ContentHeader.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_content_header.text, "What's up?")

    def test_delete_question(self):
        res = self.client.delete('/program/{}/contentheader/{}/'.format(self.activity_1.id, self.content_header_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ContentHeader.objects.count(), 0)
