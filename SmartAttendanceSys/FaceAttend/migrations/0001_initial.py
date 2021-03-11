# Generated by Django 3.1.7 on 2021-03-02 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_code', models.CharField(max_length=10)),
                ('sub_name', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('total_lecture', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.branch')),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=300)),
                ('student_roll_no', models.IntegerField()),
                ('student_photo', models.ImageField(upload_to='img/')),
                ('student_photo_enc', models.FileField(upload_to='', verbose_name='enc/')),
                ('sem', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_hod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.faculty'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('present', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to='attend/%Y/%m/%d')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.student')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceAttend.subject')),
            ],
        ),
    ]
