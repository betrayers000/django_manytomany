from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor, related_name="patients")

    def __str__(self):
            return self.name
            

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient= models.ForeignKey(Patient, on_delete=models.CASCADE)
#     time = models.CharField(max_length=100)
#     location = models.CharField(max_length=100, default="3층")

#     def __str__(self):
#         return f"{self.doctor.name}의사 : {self.patient.name}환자"
