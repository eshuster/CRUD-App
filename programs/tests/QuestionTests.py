from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, Answer, Program, Question, Section

class QuestionTests(APITestCase):
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
                                                  type=Activity.TypeChoices.QUESTION_ANSWERS,
                                                  section=self.section_1)

        # self.activity_2 = Activity.objects.create(name="Activity Two",
        #                                           description="Activity for Section One",
        #                                           type=Activity.TypeChoices.CONTENT,
        #                                           section=self.section_1)

        self.question_1 = Question.objects.create(text="What is your favorite color?",
                                                  activity=self.activity_1)

        self.answer_1 = Answer.objects.create(text="Red",
                                              question=self.question_1)
        self.answer_2 = Answer.objects.create(text="Blue",
                                              question=self.question_1)
        self.answer_3 = Answer.objects.create(text="Green",
                                              question=self.question_1)


    def test_get_question(self):
        res = self.client.get('/program/question/{}/'.format(self.question_1.id))

        question_1 = Question.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(question_1.id, self.question_1.id)


    def test_create_question(self):
        res = self.client.post('/program/question/', data={
            "text": "What's going on?",
            "activity": self.activity_1.id
        }, format="json")

        newly_created_question = Question.objects.get(text="What's going on?",
                                                      activity_id=self.activity_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_question.id)
        self.assertEqual(Question.objects.count(), 2)

    def test_update_question(self):
        res = self.client.put('/program/question/{}/'.format(self.question_1.id), data={
            "text": "What's up?"
        }, format='json')

        updated_question = Question.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_question.text, "What's up?")

    def test_delete_question(self):
        res = self.client.delete('/program/question/{}/'.format(self.question_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.count(), 0)
