# Generated by Django 2.2.16 on 2021-02-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0049_resourcebase_resource_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesaurus',
            name='about',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ThesaurusLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=3)),
                ('label', models.CharField(max_length=255)),
                ('thesaurus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_thesaurus', to='base.Thesaurus')),
            ],
            options={
                'verbose_name_plural': 'Thesaurus Labels',
                'ordering': ('lang',),
                'unique_together': {('thesaurus', 'lang')},
            },
        ),
    ]
