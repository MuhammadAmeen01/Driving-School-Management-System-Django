# Generated by Django 4.0.3 on 2022-04-18 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customer_myteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='myteacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='accounts.teacher'),
        ),
    ]
