from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"
       
    def get_questions(self):
        return self.question_set.all() 

class Question(models.Model):
    difficulty_choices =(
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),
    )
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=10, choices=difficulty_choices)
    quiz_id= models.ForeignKey("Quiz", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question_id = models.ForeignKey("Question", on_delete=models.CASCADE)
    # quiz_id = models.ForeignKey("Quiz", on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text