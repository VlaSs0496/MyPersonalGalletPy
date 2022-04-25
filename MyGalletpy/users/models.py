from enum import unique
from tkinter import CASCADE
from turtle import ondrag
from unicodedata import name
from unittest import addModuleCleanup
from django.db import models
from urllib3 import ProxyManager

# Create your models here.
class User(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class Transaction(models.Model):
    class Meta:
        models.UniqueConstraint(fields=['id_transaction', 'id_user'], name='transaction_pk')

    id_transaction = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_transaction = models.DateField()
    type_transaction = models.BooleanField(default=True)
    amount = models.FloatField()

class Pocket(models.Model):
    class Meta:
        models.UniqueConstraint(fields=['id_pocket', 'id_user'], name='pocket_pk')

    id_pocket = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_pocket = models.CharField(max_length=30)
    balance_pocket = models.FloatField()

class Pocket_transaction(models.Model):
    class Meta:
        models.UniqueConstraint(fields=['id_pocket', 'id_transaction'], name='pocket_transaction_pk')

    id_pocket = models.BigAutoField(primary_key=True)
    id_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

class Normal_transaction(models.Model):
    class Meta:
        models.UniqueConstraint(fields=['id_transaction','id_user'], name='normal_transaction_pk')

    id_transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)