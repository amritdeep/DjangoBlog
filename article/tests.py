"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from article.models import Article #, get_upload_file_name
from django.utils import timezone
from time import time


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ArticleTest(TestCase):
	def create_article(self, title="test article", body="Blah Blah Blah Blah"):
		return Article.objects.create(title=title, 
									body=body, 
									pub_date=timezone.now(), 
									likes=0)

	def test_article_creation(self):
		a = self.create_article()
		self.assertTrue(isinstance(a, Article))
		self.assertEqual(a.__unicode__(), a.title)


	def test_get_upload_file_name(self):
		filename = "Cheese.txt"
		path = "uploaded_file/%s_%s" % (str(time()).replace('.', '_'), 
										filename)


		created_path = get_upload_file_name(self, filename)


















