from django.db import models

# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.FloatField()
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.ticker + " " + str(self.date)
    
