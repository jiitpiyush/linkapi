# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class ForgotPassOp(models.Model):
    lb_umail = models.CharField(primary_key=True, max_length=50)
    pin = models.CharField(max_length=6)
    pin_time = models.DateTimeField()
    w_a = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forgot_pass_op'


class LbEngg(models.Model):
    lb_id = models.CharField(max_length=25,primary_key=True)
    lb_maincate = models.CharField(max_length=25)
    lb_cate = models.CharField(max_length=25)
    lb_sub = models.CharField(max_length=30, blank=True, null=True)
    lb_head = models.CharField(max_length=30)
    lb_name = models.CharField(max_length=100)
    lb_link = models.TextField()
    l_desc = models.TextField()
    u_vote = models.BigIntegerField(blank=True, null=True)
    lb_ut = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lb_engg'

class LbLogin(models.Model):
    lb_id = models.CharField(max_length=25,primary_key=True)
    lb_ufname = models.CharField(max_length=50, blank=True, null=True)
    lb_ulname = models.CharField(max_length=50, blank=True, null=True)
    lb_user = models.CharField(unique=True, max_length=20)
    lb_umail = models.CharField(unique=True, max_length=50)
    u_salt = models.CharField(max_length=150)
    lb_upass = models.TextField()
    pass_real = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lb_login'
