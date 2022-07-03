from email import message
from unicodedata import category
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, CategorySerializer
from .models import Quiz, Question, Answer, Category
# from .permission import IsStafforReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404


@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Question updated successfully'
            }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        data ={
            message: 'Question deleted successfully'
        }
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def answer_list(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        answer = AnswerSerializer(answers, many=True)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Answer created successfully'
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        answer.delete()

        data ={
            message: 'Answer deleted successfully'
        }
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Answer updated successfully'
            }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        category = CategorySerializer(categories, many=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Category created successfully'
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()

        data ={
            message: 'Category deleted successfully'
        }
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Category updated successfully'
            }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def quiz_list(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        quiz = QuizSerializer(quizzes, many=True)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Quiz created successfully'
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quiz.delete()

        data ={
            message: 'Quiz deleted successfully'
        }
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data ={
                message: 'Quiz updated successfully'
            }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
