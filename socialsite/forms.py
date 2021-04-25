from django import  forms
# from .models import Posts
from .models import Post,Comment



class create_posts(forms.ModelForm):
	description=forms.CharField(required=False, widget=forms.Textarea(
									attrs={
											'class':'Eialids class',
											'rows': 15, #description er box size ta boro choto korar jnne rows and column guli use hoy.
											'cols':40,
											'placeholder':'Share your thought' 
										}
									)
	)	
	class Meta:
		model = Post
		fields = [
			'description'
		]


# comments

class create_comments(forms.ModelForm):
	comment_description=forms.CharField(required=False, widget=forms.Textarea(
									attrs={
											'class':'Eialids class',
											'rows': 5, #description er box size ta boro choto korar jnne rows and column guli use hoy.
											'cols':10,
											'placeholder':'write your comment' 
										}
									)
	)	
	class Meta:
		model = Comment
		fields = [
			'comment_description',
			'post'
		]