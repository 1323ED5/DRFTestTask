from django.db import models


class RoleEnum(models.TextChoices):
    REPRESENT = 'represent'
    CLIENT = 'client'


class StatusEnum(models.TextChoices):
    CANCEL = 'cancel'
    WAITING = 'waiting'
    SUCCESS = 'success'
