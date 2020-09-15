# Generated by Django 3.1 on 2020-08-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoAppPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(help_text='The name of the page as displayed in the nav bar. Should not exceed 18 chars, as the string will be wider then the available space in the navbar.', max_length=18)),
                ('page_slug', models.SlugField(help_text='The name of the page used in the URL of it. Must be unique as two pages of this app cannot have the same url.', unique=True)),
                ('page_content', models.TextField(help_text="This is an example for some Content of the page that can be configured dynamically, i.e. by using Django's admin.")),
            ],
        ),
    ]