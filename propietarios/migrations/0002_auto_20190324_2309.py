# Generated by Django 2.1.7 on 2019-03-25 04:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('propietarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='soporte_documento',
            field=models.FileField(default=1, upload_to='propietarios/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propietario',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propietario',
            name='numero_documento',
            field=models.CharField(max_length=15, unique=True, verbose_name='número de documento'),
        ),
    ]
