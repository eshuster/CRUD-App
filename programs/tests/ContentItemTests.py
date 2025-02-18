from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, Content, ContentItem, Program, Section
class ContentItemTests(APITestCase):
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

        self.content_1 = Content.objects.create(text="What Does Mindfulness Do?",
                                                activity=self.activity_1)

        self.content_item_1 = ContentItem.objects.create(text="A",
                                                         content=self.content_1,
                                                         order_index=1)
        self.content_item_2 = ContentItem.objects.create(text="B",
                                                         content=self.content_1,
                                                         order_index=2)
        self.content_item_3 = ContentItem.objects.create(text="C?",
                                                         content=self.content_1,
                                                         order_index=3)

    def test_get_content_item(self):
        res = self.client.get('/program/activity/{}/contentitem/{}/'.format(self.activity_1.id, self.content_item_1.id))

        content_item = Content.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(content_item.id, self.content_item_1.id)

    def test_create_content_item(self):
        res = self.client.post('/program/activity/contentitem/', data={
            "text": "D?",
            "content": self.content_item_1.id,
            "order_index": 4
        }, format="json")

        newly_created_content_item = ContentItem.objects.get(text="D?",
                                                                 content=self.content_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_content_item.id)
        self.assertEqual(ContentItem.objects.count(), 4)

    def test_update_content_item(self):
        res = self.client.put('/program/activity/{}/contentitem/{}/'.format(self.activity_1.id, self.content_item_1.id),
                              data={
                                  "text": "E?"
                              }, format='json')

        updated_content_item = ContentItem.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_content_item.text, "E?")

    def test_delete_content_item(self):
        res = self.client.delete('/program/activity/{}/contentitem/{}/'.format(self.activity_1.id, self.content_item_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ContentItem.objects.count(), 2)

