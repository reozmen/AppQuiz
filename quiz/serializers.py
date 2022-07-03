from ast import Delete
from rest_framework import serializers
from .models import Quiz, Question, Answer, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category_id',
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer_text',
            'is_right',
            'question_id',
        )


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = serializers.StringRelatedField()
    quiz_id = serializers.IntegerField(source='quiz.id',write_only=True)


    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'difficulty',
            'quiz_id',
            'answer',
            'quiz',
        )




class StaffQuizSerializer(serializers.ModelSerializer):
    Question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category_id',
            'Question',

        )
