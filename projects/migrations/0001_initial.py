# Generated by Django 3.2.10 on 2022-01-08 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.basemodel')),
                ('name', models.CharField(db_index=True, max_length=31, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Menus',
                'verbose_name_plural': 'Menus',
                'db_table': 'menus',
            },
            bases=('projects.basemodel',),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.basemodel')),
                ('name', models.CharField(db_index=True, max_length=31, verbose_name='name')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='remark')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'project',
            },
            bases=('projects.basemodel',),
        ),
        migrations.CreateModel(
            name='MetaTable',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.basemodel')),
                ('table_name', models.CharField(max_length=31, verbose_name='Table Name')),
                ('status', models.IntegerField(choices=[('Undone', 0), ('Handled', 1)], default=0, verbose_name='status')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.menus')),
            ],
            options={
                'verbose_name': 'Meta-tables',
                'verbose_name_plural': 'Meta-tables',
                'db_table': 'meta_tables',
            },
            bases=('projects.basemodel',),
        ),
        migrations.CreateModel(
            name='MetaField',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.basemodel')),
                ('field_name', models.CharField(max_length=31, verbose_name='Field Name')),
                ('field_type', models.CharField(choices=[('CharField', 'CharField'), ('IntegerField', 'IntegerField'), ('DateTimeField', 'DateTimeField'), ('BooleanField', 'BooleanField')], max_length=31, verbose_name='Type')),
                ('max_length', models.IntegerField(verbose_name='max_length')),
                ('default_value', models.CharField(max_length=255, verbose_name='default_value')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.metatable')),
            ],
            options={
                'verbose_name': 'Meta-Fields',
                'verbose_name_plural': 'Meta-Fields',
                'db_table': 'meta_fields',
            },
            bases=('projects.basemodel',),
        ),
        migrations.AddField(
            model_name='menus',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together={('name', 'project')},
        ),
    ]
