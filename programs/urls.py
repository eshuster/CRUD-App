from django.conf.urls import url
from django.urls import path

from .controllers.ActivityController import ActivityController, ActivityListController
from .controllers.AnswerController import AnswerController, AnswerListController
from .controllers.ContentHeaderController import ContentHeaderController, ContentHeaderListController
from .controllers.ContentItemController import ContentItemController, ContentItemListController
from .controllers.QuestionController import QuestionController, QuestionListController
from .controllers.ProgramController import ProgramController, ProgramListController
from .controllers.SectionController import SectionController, SectionListController

urlpatterns = [
    path('', ProgramListController.as_view()),
    path('<int:pk>/', ProgramController.as_view()),
    path('activity/', ActivityListController.as_view()),
    path('activity/<int:pk>/', ActivityController.as_view()),
    path('section/<int:section_id>/activity/', ActivityListController.as_view()),
    path('answer/', AnswerListController.as_view()),
    path('answer/<int:pk>/', AnswerController.as_view()),
    path('contentheader/', ContentHeaderListController.as_view()),
    path('<int:activity_id>/contentheader/<int:pk>/', ContentHeaderController.as_view()),
    path('contentitem/', ContentItemListController.as_view()),
    path('<int:activity_id>/contentitem/<int:pk>/', ContentItemController.as_view()),
    path('question/', QuestionListController.as_view()),
    path('question/<int:pk>/', QuestionController.as_view()),
    path('section/', SectionListController.as_view()),
    path('section/<int:pk>/', SectionController.as_view()),
]

