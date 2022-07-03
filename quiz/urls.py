from rest_framework import routers
from django.urls import path, include
# from .views import question_list, question_detail, answer_list, category_list, quiz_list 
from .views import QuestionViewSet, AnswerViewSet, CategoryViewSet, QuizViewSet


# router = routers.DefaultRouter()
# router.register(r'question', question_list, basename='question')
# router.register(r'answer', answer_list, basename='answer')
# router.register(r'category', category_list, basename='category')
# router.register(r'quiz', quiz_list, basename='quiz')
# router.register(r'question/(?P<id>\d+)', question_detail, basename='question-detail')
router = routers.DefaultRouter()
router.register(r'category/model-viewset', CategoryViewSet)
router.register(r'model-viewset', QuizViewSet )
router.register(r'question/model-viewset', QuestionViewSet )
router.register(r'answer/model-viewset', AnswerViewSet )
urlpatterns = [
    # path('', home),
    # path('question/', question_list),
    # path('question/<int:id>/', question_detail),
    # path('answer/', answer_list),
    # path('category/', category_list),
    # path('quiz/', QuizViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('question/', QuestionViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('question/<int:id>/', QuestionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('answer/', AnswerViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('answer/<int:id>/', AnswerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<int:id>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('quiz/<int:id>/', QuizViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', include(router.urls)),


]

urlpatterns += router.urls