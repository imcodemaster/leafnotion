from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from autoslug import AutoSlugField
from django.db.models import Avg, Count, Min, Sum
# Create your models here.

feeling = [
                
                ('Happy', "Happy"),
                ('Sad', "Sad"),
                ('Inspired', "Inspired"),
                ('Bored', "Bored"),
                ('Empty', "Empty"),
                ('Anger', "Anger"),
                ('Crying', "Crying"),
                ('Blessed', "Blessed"),
                ('Awesome', "Awesome"),
                ('Cool', "Cool"),
                ('like a kid', "like a kid"),
                ('like a boss', "like a boss"),
                ('Tired' , "Tired"),
                ('Broken' , "Broken"),
                ('Lonely' , "Lonely"),

             
        ]


activity = [
                
                ('Dancing', "Happy"),
                ('Cooking', "Sad"),
                ('Reading', "Inspired"),
                ('Walking', "Bored"),
                ('Watching', "Watching"),
                ('Playing', "Playing"),
                ('Working', "Working"),
                ('Work-out', "Work-out"),
				('Thinking', "Thinking"),
                ('Sleeping', "Sleeping"),
                ('Dreaming', "Dreaming"),
             
        ]


reaction = [
                
                ('Nice', "Nice"),
                ('Great', "Great"),
                ('Innovative', "Innovative"),
                ('So what', "So what"),
                ('Trash', "Trash"),
                ('Why doing this ?', "Why doing this ?"),
                ('Happy for you', "Happy for you"),
                ('Thanks', "Thanks"),
                ('Kya majburi thi bhai ?', "Kya majburi thi bhai ?"),
                ('Cool', "Cool"),

             
        ]



class Post(models.Model):

	published = models.DateTimeField(default = timezone.now)
	image = models.FileField(upload_to ='media' , null= True , blank = True)	
	content = models.TextField( null= True , blank = True)
	slug = AutoSlugField(populate_from='author')
	feeling = models.CharField(max_length=100 , choices=feeling, blank=True, null= True)
	activity = models.CharField(max_length=100 , choices=activity, blank=True, null= True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
	likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
	like_count = models.BigIntegerField(default='0')		

	def total_likes(self):
		return self.likes.count()


	def __str__(self):
		return str(self.author.username)



	@property
	def mediaURL(self):
		try : 
			url = self.image.url
		except : 
			url = ''
		return url 






class video(models.Model):
	subject = models.CharField(max_length = 500)
	published = models.DateTimeField(default = timezone.now)
	video = models.FileField( max_length = 500, null= True , blank = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='videolike', default=None, blank=True)

	def total_likes(self):
		return self.likes.count()



	def __str__(self):
		return self.subject


	@property
	def mediaURL(self):
		try : 
			url = self.video.url
		except : 
			url = ''
		return url 



class PostComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='postcomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField( null= True , blank = True)
	reaction = models.CharField(max_length=100 , choices=reaction, blank=True, null= True)
	published = models.DateTimeField(default = timezone.now)




	def __str__(self):
		return self.user.username 



class VideoComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(video, related_name='videocomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField(null= True , blank = True)
	published = models.DateTimeField(default = timezone.now)


	def __str__(self):
		return self.user.username 


