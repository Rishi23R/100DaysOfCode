from django.db import models

# Create your models here.

class Students(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    DateOfBirth = models.DateField()
    EnrollmentDate = models.DateField()

class Teachers(models.Model):
    TeacherID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    HireDate = models.DateField()
    Department = models.CharField(max_length=250)

class Courses(models.Model):
    CourseID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Code=models.CharField(max_length=200)
    TeacherID = models.ForeignKey(Teachers, on_delete=models.CASCADE)

class Enrollments(models.Model):
    EnrollmentID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    DateEnrolled = models.DateField()
class Attendances(models.Model):
    AttendanceID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    DateAttended = models.DateField()
    Status = models.CharField(max_length=200)

class Grades(models.Model):
    GradeID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Students, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Grade = models.FloatField()



