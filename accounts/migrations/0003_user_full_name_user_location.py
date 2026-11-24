from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True
            ),
        ),
    ]