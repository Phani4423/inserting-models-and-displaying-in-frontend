from django.db import models

# Create your models here.
class dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)
class emp(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=7,decimal_places=2)
    comm = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    mgr = models.IntegerField()
    deptno = models.ForeignKey(dept,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.empno)
class salgrade(models.Model):
    grade = models.IntegerField(primary_key=True)
    losal = models.DecimalField(max_digits=7,decimal_places=2)
    hisal = models.DecimalField(max_digits=7,decimal_places=2)

