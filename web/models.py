
from django.db import models

# Create your models here.
class Agent(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    mobile = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    phone = models.CharField(
        max_length=20,

    )
    email = models.CharField(
        max_length=20,
    )

    address1 = models.CharField(
        max_length=200,
    )
    address2 = models.CharField(
        max_length=200,
    )

    national_id = models.CharField(
        max_length=10,
    )

    city = models.CharField(
        max_length=20,
    )
    zip_code = models.CharField(
        max_length=10,
    )
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("Created at"))
    update_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=_("Updated at"))

class Installer(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    mobile = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    birthday = models.DateTimeField()
    national_id = models.CharField(
        max_length=10,
    )
    city = models.CharField(
        max_length=20,
    )
    zip_code = models.CharField(
        max_length=10,
    )
    address1 = models.CharField(
        max_length=200,
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)

class Customer(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    mobile = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    birthday = models.DateTimeField()
    national_id = models.CharField(
        max_length=10,
    )
    city = models.CharField(
        max_length=20,
    )
    zip_code = models.CharField(
        max_length=10,
    )
    address1 = models.CharField(
        max_length=200,
    )
    installer = models.ForeignKey(Installer, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(Agent, on_delete= models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)


class Installation(models.Model):
    device_serial = models.CharField(max_length= 50)
    device_model = models.CharField(max_length= 50)
    city = models.CharField(max_length= 50)
    address = models.CharField(max_length= 100)
    installer = models.ForeignKey(Installer, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(Agent, on_delete= models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete= models.DO_NOTHING)
    started_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)