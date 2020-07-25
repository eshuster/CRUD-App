from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, Program, Section

class ActivityTests(APITestCase):
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

        self.activity_1 = Activity.objects.create(name="Activity One",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.CONTENT,
                                                  section=self.section_1)

        self.activity_2 = Activity.objects.create(name="Activity Two",
                                                  description="Activity for Section One",
                                                  type=Activity.TypeChoices.QUESTION_ANSWERS,
                                                  section=self.section_2)

    def test_get_activity(self):
        res = self.client.get('/program/activity/{}/'.format(self.activity_1.id))

        activity_1 = Activity.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(activity_1.id, self.activity_1.id)

    def test_get_activities_by_section_id(self):
        res = self.client.get('/program/section/{}/activity/'.format(self.section_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Activity.objects.filter(section_id=self.section_1.id).count(), len(res.data)) #2

    def test_create_activity(self):
        res = self.client.post('/program/activity/', data={
            "name": "Activity Three",
            "description": "Activity for Section Three",
            "type": Activity.TypeChoices.CONTENT,
            "section": self.section_1.id
        }, format="json")

        # unnecessary to query through program_id but demonstrating table relation for the
        # purposes of the assignment
        newly_created_activity = Activity.objects.get(name="Activity Three",
                                                    section__program_id=self.program_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_activity.id)
        self.assertEqual(Activity.objects.count(), 3)

    def test_update_activity(self):
        res = self.client.put('/program/activity/{}/'.format(self.activity_1.id), data={
            "description": "New activity description"
        }, format='json')

        updated_section = Activity.objects.get(id=self.activity_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_section.description, "New activity description")

    def test_delete_program(self):
        res = self.client.delete('/program/activity/{}/'.format(self.activity_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Activity.objects.count(), 1)