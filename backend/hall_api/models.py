from django.db import models


from django.contrib.auth.models import AbstractUser

# --------------------
# Custom User Model
# --------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("EMPLOYEE", "Employee"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="EMPLOYEE")

    def __str__(self):
        return f"{self.username} ({self.role})"
    
# Hall master
class HallMaster(models.Model):
    off_code = models.CharField(max_length=100)
    hall_code = models.CharField(max_length=100, unique=True)
    hall_name = models.CharField(max_length=255)
    day_spoc_name = models.CharField(max_length=255)
    ngt_spoc_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    tables = models.IntegerField()
    chairs = models.IntegerField()
    white_board = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    audio = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

    def __str__(self):
        return self.hall_name

# admin master table
class AdminMaster(models.Model):
    empl_code = models.CharField(max_length=100)
    off_code = models.CharField(max_length=100)
    empl_name = models.CharField(max_length=255)
    desig = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)

    def __str__(self):
        return self.empl_name

# booking table
class Booking(models.Model):
    book_date = models.DateField()
    time_slot = models.TimeField()
    off_code = models.CharField(max_length=100)
    hall_code = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=255)
    empl_email_id = models.EmailField()
    empl_mobile_no = models.CharField(max_length=20)
    team_name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.emp_name} - {self.hall_code} on {self.book_date}"












