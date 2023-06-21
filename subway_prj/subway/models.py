from django.db import models

# Create your models here.
# class Station(models.Model):
#     Station_Name = models.CharField(max_length=100) # 제목
#     Station_Code = models.IntegerField
#     Line = models.CharField(max_length=100)
#     Out_Code = models.CharField(max_length=100)
#     Lat = models.FloatField
#     Lng = models.FloatField

class Line(models.Model):
    serial_number = models.IntegerField(db_column='Serial_Number', primary_key=True)
    line = models.CharField(db_column='Line', unique=True, max_length=100, blank=True, null=True)
    upend_station = models.CharField(db_column='UpEnd_Station', max_length=100, blank=True, null=True)
    downend_station = models.CharField(db_column='DownEnd_Station', max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'line'

class Station(models.Model):
    station_name = models.CharField(db_column='Station_Name', max_length=100, blank=True, null=True)
    station_code = models.IntegerField(db_column='Station_Code', primary_key=True)
    line = models.ForeignKey(Line, models.PROTECT, to_field='line', db_column='Line', blank=True, null=True)
    out_code = models.CharField(db_column='Out_Code', max_length=100, blank=True, null=True)
    lat = models.FloatField(db_column='Lat', blank=True, null=True)
    lng = models.FloatField(db_column='Lng', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Congestion(models.Model):
    serial_number = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    day_of_week_division = models.CharField(max_length=6, blank=True, null=True)
    line_name = models.CharField(max_length=6)
    station_code = models.ForeignKey(Station, models.PROTECT, db_column='station_code')
    departure_station = models.CharField(max_length=50, blank=True, null=True)
    division_name = models.CharField(max_length=4)
    congestion_5_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_6_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_6_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_7_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_7_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_8_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_8_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_9_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_9_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_10_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_10_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_11_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_11_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_12_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_12_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_13_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_13_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_14_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_14_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_15_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_15_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_16_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_16_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_17_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_17_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_18_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_18_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_19_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_19_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_20_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_20_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_21_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_21_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_22_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_22_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_23_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_23_30 = models.CharField(max_length=10, blank=True, null=True)
    congestion_00_00 = models.CharField(max_length=10, blank=True, null=True)
    congestion_00_30 = models.CharField(max_length=10, blank=True, null=True)
    remark_dc = models.CharField(db_column='REMARK_DC', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subway_congestion'
        unique_together = (('serial_number', 'line_name', 'division_name'),)


class Tourspot(models.Model):
    serial_number = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    tourspot_name = models.CharField(db_column='Tourspot_Name', max_length=100, blank=True, null=True)
    station_name = models.CharField(db_column='Station_Name', max_length=100, blank=True, null=True)
    station_code = models.ForeignKey(Station, models.PROTECT, db_column='Station_Code')
    line = models.CharField(db_column='Line', max_length=100, blank=True, null=True)
    exit_number = models.CharField(db_column='Exit_Number', max_length=100, blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourspots'

