
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RenameField(
                    model_name='order',
                    old_name='Customer',
                    new_name='customer',
                ),
                migrations.AlterField(
                    model_name='order',
                    name='customer',
                    field=models.ForeignKey(
                        db_column='Customer_id',
                        on_delete=models.CASCADE,
                        related_name='customer_orders',
                        to='accounts.user',
                    ),
                ),
                migrations.RenameField(
                    model_name='order',
                    old_name='quality',
                    new_name='quantity',
                ),
                migrations.AlterField(
                    model_name='order',
                    name='quantity',
                    field=models.PositiveIntegerField(db_column='quality'),
                ),
            ],
        ),
    ]
