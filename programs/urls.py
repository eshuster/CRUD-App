from django.conf.urls import url
from django.urls import path

from .controllers.ActivityController import ActivityController, ActivityListController
from .controllers.AnswerController import AnswerController, AnswerListController
from .controllers.QuestionController import QuestionController, QuestionListController
from .controllers.ProgramController import ProgramController, ProgramListController
from .controllers.SectionController import SectionController, SectionListController

urlpatterns = [
    path('', ProgramListController.as_view()),
    path('<int:pk>/', ProgramController.as_view()),
    url(r'^activity/$', ActivityListController.as_view()),
    url(r'^activity/<int:pk>/$', ActivityController.as_view()),
    url(r'^answer/$', AnswerListController.as_view()),
    url(r'^answer/<int:pk>/$', AnswerController.as_view()),
    url(r'^<int:section_id>/contentheader/$', AnswerListController.as_view()),
    url(r'^<int:section_id>/contentheader/<int:pk>/$', AnswerController.as_view()),
    url(r'^<int:section_id>/contentitem/$', AnswerListController.as_view()),
    url(r'^<int:section_id>/contentitem/<int:pk>/$', AnswerController.as_view()),
    url(r'^question/$', QuestionListController.as_view()),
    url(r'^question/<int:pk>/$', QuestionController.as_view()),
    path('section/', SectionListController.as_view()),
    path('section/<int:pk>/', SectionController.as_view()),
]

