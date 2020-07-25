from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Activity, Answer, Question, Program, Section

class AnswerTests(APITestCase):
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

        self.question_1 = Question.objects.create(text="What is your favorite color?",
                                                  activity=self.activity_1)

        self.answer_1 = Answer.objects.create(text="Red",
                                              question=self.question_1)
        self.answer_2 = Answer.objects.create(text="Blue",
                                              question=self.question_1)
        self.answer_3 = Answer.objects.create(text="Green",
                                              question=self.question_1)

    def test_get_answer(self):
        res = self.client.get('/program/answer/{}/'.format(self.answer_1.id))

        answer_1 = Answer.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(answer_1.id, self.answer_1.id)

    def test_create_answer(self):
        res = self.client.post('/program/answer/', data={
            "text": "Purple",
            "question": self.question_1.id
        }, format="json")

        newly_created_answer = Answer.objects.get(text="Purple",
                                                      question_id=self.question_1.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], newly_created_answer.id)
        self.assertEqual(Answer.objects.count(), 4)

    def test_update_answer(self):
        res = self.client.put('/program/answer/{}/'.format(self.answer_1.id), data={
            "text": "Orange"
        }, format='json')

        updated_answer = Answer.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_answer.text, "Orange")

    def test_update_answer_fail(self):
        res = self.client.put('/program/answer/{}/'.format(''), data={
            "text": "Orange"
        }, format='json')

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_answer(self):
        res = self.client.delete('/program/answer/{}/'.format(self.answer_1.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Answer.objects.count(), 2)