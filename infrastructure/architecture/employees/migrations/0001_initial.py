# Generated by Django 2.2.4 on 2019-08-28 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('department', models.CharField(choices=[('Ops', 'Operations'), ('HR', 'Human Resource'), ('Sales', 'Sales'), ('IT', 'IT'), ('Tech', 'Technology')], default='Ops', max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=False)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.Employee')),
            ],
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 18), ('age__gte', 70), _connector='OR'), name='invalid age'),
        ),
    ]
