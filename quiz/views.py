from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer, CategorySerializer, QuizSerializer, StaffQuizSerializer
from .models import Question, Answer, Category, Quiz
from rest_framework import viewsets
# from .permission import IsStafforReadOnly

# from requests import request


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = (IsStafforReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffQuizSerializer
        return serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter()

class QuizViewSetDetail(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = (IsStafforReadOnly,)

    def get_serializer_class(self, *args, **kwargs):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffQuizSerializer
        return serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter()
    
    

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = (IsStafforReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter()


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = (IsStafforReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsStafforReadOnly,)