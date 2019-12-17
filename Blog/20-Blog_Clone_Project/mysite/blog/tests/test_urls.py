from django.test import SimpleTestCase
from django.urls import reverse,resolve
# from . import views
from blog.views import PostListView

class Testurl(SimpleTestCase):
	def test_list(self):
		url=reverse('post_list')
		self.assertEquals(resolve(url).func,PostListView.get_queryset())