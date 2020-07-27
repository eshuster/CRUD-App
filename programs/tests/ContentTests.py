from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, Content, Program, Section

class ContentTests(APITestCase):
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

        self.activity_2 = Activity.objects.create(name="Activity Two",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.QUESTION_ANSWERS,
                                                  section=self.section_1)

        self.activity_3 = Activity.objects.create(name="Activity Three",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.QUESTION_ANSWERS,
                                                  section=self.section_1)

        self.activity_4 = Activity.objects.create(name="Activity Four",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.CONTENT,
                                                  section=self.section_1)

        self.content_1 = Content.objects.create(text="What Does Mindfulness Do?",
                                                             activity=self.activity_1)

        self.content_2 = Content.objects.create(text="What's Your Favorite Color?",
                                                             activity=self.activity_2)

    def test_get_content_html(self):
        res = self.client.get('/program/activity/{}/content/{}/'.format(self.activity_1.id, self.content_1.id))

        content = Content.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(content.id, self.content_1.id)

    def test_get_content_question_answers(self):
        res = self.client.get('/program/activity/{}/content/{}/'.format(self.activity_2.id, self.content_2.id))

        content = Content.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(content.id, self.content_2.id)

    def test_create_content_html(self):
        res = self.client.post('/program/activity/content/', data={
            "text": "What makes a good crepe?",
            "activity": self.activity_4.id
        }, format="json")

        newly_created_content = Content.objects.get(text="What makes a good crepe?",
                                                      activity__type=Activity.TypeChoices.CONTENT)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_content.id)
        self.assertEqual(Content.objects.count(), 3)

    def test_create_content_question_answers(self):
        res = self.client.post('/program/activity/content/', data={
            "text": "What is your favorite genre of music?",
            "activity": self.activity_3.id
        }, format="json")

        newly_created_content = Content.objects.get(text="What is your favorite genre of music?",
                                                      activity__type=Activity.TypeChoices.QUESTION_ANSWERS)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_content.id)
        self.assertEqual(Content.objects.count(), 3)

    # Will fail because Activity and Content is a OnetoOne
    def test_create_content_question_answers_fail(self):
        res = self.client.post('/program/activity/content/', data={
            "text": "What is your favorite genre of music?",
            "activity": self.activity_2.id
        }, format="json")


        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_content_html(self):
        res = self.client.put('/program/activity/{}/content/{}/'.format(self.activity_1.id, self.content_1.id), data={
            "text": "What's up?"
        }, format='json')

        updated_content_header = Content.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_content_header.text, "What's up?")

    def test_delete_content_html(self):
        res = self.client.delete('/program/activity/{}/content/{}/'.format(self.activity_1.id, self.content_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Content.objects.count(), 1)
