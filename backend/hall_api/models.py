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

class HallMaster(models.Model):
    office_code = models.CharField(max_length=100)
    hall_code = models.CharField(max_length=100, unique=True)
    hall_name = models.CharField(max_length=255)
    day_spoc = models.CharField(max_length=255)
    mid_spoc = models.CharField(max_length=255)
    night_spoc = models.CharField(max_length=255)
    capacity = models.IntegerField()
    table = models.IntegerField()
    chairs = models.IntegerField()
    white_board = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    audio = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hall_name} ({self.hall_code})"
    
class SessionMaster(models.Model):
    session_code = models.CharField(max_length=100, unique=True)
    session_type = models.CharField(max_length=100)
    preferred_hall_1 = models.CharField(max_length=100, blank=True, null=True)
    preferred_hall_2 = models.CharField(max_length=100, blank=True, null=True)
    preferred_hall_3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.session_code} ({self.session_type})"

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

class Infrastructure(models.Model):
    infra_code = models.CharField(max_length=100, unique=True)
    infra_type = models.CharField(max_length=100)
    infra_item = models.CharField(max_length=255)
    nos_in_stock = models.CharField(max_length=100)  # Keeping as CharField per your schema

    def __str__(self):
        return f"{self.infra_code} - {self.infra_item}"
    

class Booking(models.Model):
    book_date = models.DateField()
    book_time = models.TimeField()
    office = models.CharField(max_length=100)
    hall = models.CharField(max_length=100)
    session_type = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=255)
    emp_email_id = models.EmailField()
    emp_mobile_no = models.CharField(max_length=20)
    team_name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.emp_name} - {self.hall} on {self.book_date}"

class StatusDate(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.status}"
    
class TimeSlot(models.Model):
    time = models.TimeField()
    slot = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    maintanance_status = models.BooleanField(default=False)

    def  __str__(self):
        return f"{self.slot} at {self.time}"





