from django.conf.urls import url

from .controllers.ActivityController import ActivityController, ActivityListController
from .controllers.AnswerController import AnswerController, AnswerListController
from .controllers.QuestionController import QuestionController, QuestionListController
from .controllers.ProgramController import ProgramController, ProgramListController
from .controllers.SectionController import SectionController, SectionListController

urlpatterns = [
    url(r'^$', ProgramController.as_view()),
    url(r'^<int:pk>/$', ProgramListController.as_view()),
    url(r'^activity/$', ActivityListController.as_view()),
    url(r'^activity/<int:pk>/$', ActivityController.as_view()),
    url(r'^answer/$', AnswerListController.as_view()),
    url(r'^answer/<int:pk>/$', AnswerController.as_view()),
    url(r'^question/$', QuestionListController.as_view()),
    url(r'^question/<int:pk>/$', QuestionController.as_view()),
    url(r'^section/$', SectionListController.as_view()),
    url(r'^section/<int:pk>/$', SectionController.as_view()),
]