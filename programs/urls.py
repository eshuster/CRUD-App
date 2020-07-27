from django.conf.urls import url
from django.urls import path

from .controllers.ActivityController import ActivityController, ActivityListController
from .controllers.ContentController import ContentController, ContentListController
from .controllers.ContentItemController import ContentItemController, ContentItemListController
from .controllers.ProgramController import ProgramController, ProgramListController
from .controllers.SectionController import SectionController, SectionListController

urlpatterns = [
    path('', ProgramListController.as_view()),
    path('<int:pk>/', ProgramController.as_view()),
    path('activity/', ActivityListController.as_view()),
    path('activity/<int:pk>/', ActivityController.as_view()),
    path('section/<int:section_id>/activity/', ActivityListController.as_view()),
    path('activity/contentitem/', ContentItemListController.as_view()),
    path('activity/<int:activity_id>/contentitem/<int:pk>/', ContentItemController.as_view()),
    path('section/', SectionListController.as_view()),
    path('section/<int:pk>/', SectionController.as_view()),
    path('activity/<int:activity_id>/content/<int:pk>/', ContentController.as_view()),
    path('activity/content/', ContentListController.as_view())
]

