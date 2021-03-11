from django.db import models

# Create your models here.
class Faculty(models.Model):
    f_name = models.CharField(max_length=300)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.f_name

class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    branch_hod = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self):
        return self.branch_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=300)
    password = models.CharField(max_length=20)
    student_roll_no = models.IntegerField()
    student_photo = models.ImageField(upload_to="img/")
    student_photo_enc = models.FileField("enc/")
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    sem = models.IntegerField()
    def __str__(self):
        return self.student_name

class Subject(models.Model):
    sub_code = models.CharField(max_length=10)
    sub_name = models.CharField(max_length=100)
    f_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    sem = models.IntegerField()
    total_lecture = models.IntegerField()
    def __str__(self):
        return self.sub_name

class Attendance(models.Model):
    stud_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    date = models.DateTimeField()
    present = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="attend/%Y/%m/%d")
