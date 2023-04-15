# Generated by Django 4.2 on 2023-04-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_project_users_alter_user_projects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.AlterField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='users_enrroled', to='core.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users_projects', to='core.user'),
        ),
    ]