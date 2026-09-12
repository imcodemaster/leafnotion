from django import forms
from .models import PostComment, Post , video , VideoComment

class PostForm(forms.ModelForm):

	content = forms.CharField(
		label =  '', 
		widget =  forms.Textarea(attrs = {
			'rows' : '3',
			'placeholder' : "Post your stories .."
			}))

	image = forms.ImageField(required = False , label = 'Add Picture :')

	class Meta:
		model = Post
		fields = ['content', 'feeling', 'activity' , 'image']




class PostUpdateForm(forms.ModelForm):

	content = forms.CharField(
		label =  '', 
		widget =  forms.Textarea(attrs = {
			'rows' : '3',
			'placeholder' : "Share your Today's  stories .."
			}))

	image = forms.ImageField(required = False , label = 'Add Picture :')
	
	

	class Meta:
		model = Post
		fields = ['content', 'feeling', 'activity' , 'image']






class PostCommentForm(forms.ModelForm):

	comment_content = forms.CharField(
		label =  '', 
		required = False,
		widget = forms.Textarea(attrs = {
			'rows' : '3',
			'placeholder' : 'Add your comment.. '
			}))
	

	class Meta:
		model = PostComment
		fields = ['comment_content' , 'reaction']



class VideoForm(forms.ModelForm):

	subject = forms.CharField(
		label =  '', 
		required = False,
		widget =  forms.Textarea(attrs = {
			'rows' : '3',
			'placeholder' : "What's happening or your Notion.."
			}))

	video = forms.FileField(required = False , label = 'Add Your Video')

	class Meta:
		model = video
		fields = ['subject', 'video']



class VideoCommentForm(forms.ModelForm):

	comment_content = forms.CharField(
		label =  '', 
		required = False,
		widget = forms.Textarea(attrs = {
			'rows' : '3',
			'placeholder' : 'Add your comment.. '
			}))
	

	class Meta:
		model = VideoComment
		fields = ['comment_content']
