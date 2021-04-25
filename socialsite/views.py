from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

# from .forms import create_posts
from .forms import create_posts,create_comments
from .models import Post,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
# 	return HttpResponse('<h1> microblog </h1>')

def home(request):
	return render(request, 'socialsite/index.html')

@login_required(login_url='/accounts/login/')
def create_post(request):

	
	product_instance=create_posts(request.POST or None)  #forms.py file er create_product class tar ekta instance create korchi


	if product_instance.is_valid(): # checking if user entered data are valid or not
		product_instance.save() #creating objects in database
		product_instance=create_posts()

	queryset=Post.objects.all()
	# create_comments

	# comment_instance=create_comments(request.POST or None)  #forms.py file er create_product class tar ekta instance create korchi

	# if comment_instance.is_valid(): # checking if user entered data are valid or not
	# 	comment_instance.save() #creating objects in database
	# 	comment_instance=create_comments()
		
	forms={
		'product_form':product_instance,
		'product':queryset
		# 'comment': comment_instance

	}
	return render(request, 'socialsite/home.html', forms)


# def create_comment(request,id):

# 	# get the post using the id
# 	comment_instance=get_object_or_404(Comment,id=id)
# 	forms={
# 		'comment':comment_instance
# 	}
# 	# convert it into context dictionary
# 	return render(request, 'socialsite/comment_page.html',forms)



# def login(request):
# 	# return render(request, 'socialsite/login.html')
# 	return render()

@login_required(login_url='/accounts/login/')
def comment(request):
	comment_instance=create_comments(request.POST or None)
	if comment_instance.is_valid(): # checking if user entered data are valid or not
		comment_instance.save() #creating objects in database
		comment_instance=create_comments()

	allComments=Comment.objects.all()
	# create_comments

	# comment_instance=create_comments(request.POST or None)  #forms.py file er create_product class tar ekta instance create korchi

	# if comment_instance.is_valid(): # checking if user entered data are valid or not
	# 	comment_instance.save() #creating objects in database
	# 	comment_instance=create_comments()
		
	forms={
		'comment_box':comment_instance,
		'comments': allComments
		# 'comment': comment_instance

	}



	return render(request,"socialsite/comment_page.html",forms)

