from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from .models import Post,Book
from .forms import PostForm

def home(request):
	return render(request, 'gamapp/home.html',{})


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'gamapp/post_list.html',{'posts': posts })

def post_details(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if (post.tags == "#books"):
		return render(request,'gamapp/book_details.html', {'post':post})
	elif (post.tags == "#travel"):
		return render(request,'gamapp/travel_details.html', {'post':post})
	elif (post.tags == "#food"):
		return render(request,'gamapp/food_details.html', {'post':post})
	elif (post.tags == "#technology"):
		return render(request,'gamapp/technology_details.html', {'post':post})
	elif (post.tags == "#fashion"):
		return render(request,'gamapp/fashion_details.html', {'post':post})
	
def post_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm()
	return render (request, 'gamapp/post_edit.html',{'form':form})
	
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('gamapp.views.post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gamapp/post_edit.html', {'form': form})
	
def book_list(request):
	posts = Post.objects.filter(tags__contains="#books")
	return render(request, 'gamapp/book_list.html',{'posts': posts })

def book_details(request,pk):
	post = get_object_or_404(Book, pk=pk)
	return render(request,'gamapp/book_details.html', {'post':post})
	
def book_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(initial={'tags': '#books'})
	return render (request, 'gamapp/book_edit.html',{'form':form})
	
def book_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'gamapp/book_edit.html', {'form': form})
	
def food_list(request):
	posts = Post.objects.filter(tags__contains="#food")
	return render(request, 'gamapp/food_list.html',{'posts': posts })

def food_details(request,pk):
	post = get_object_or_404(Food, pk=pk)
	return render(request,'gamapp/food_details.html', {'post':post})
	
def food_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(initial={'tags': '#food'})
	return render (request, 'gamapp/food_edit.html',{'form':form})
	
def food_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'gamapp/food_edit.html', {'form': form})
	
def technology_list(request):
	posts = Post.objects.filter(tags__contains="#technology")
	return render(request, 'gamapp/technology_list.html',{'posts': posts })

def technology_details(request,pk):
	post = get_object_or_404(Technology, pk=pk)
	return render(request,'gamapp/technology_details.html', {'post':post})
	
def technology_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(initial={'tags': '#technology'})
	return render (request, 'gamapp/technology_edit.html',{'form':form})
	
def technology_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'gamapp/technology_edit.html', {'form': form})
	
def travel_list(request):
	posts = Post.objects.filter(tags__contains="#travel")
	return render(request, 'gamapp/travel_list.html',{'posts': posts })

def travel_details(request,pk):
	post = get_object_or_404(Travel, pk=pk)
	return render(request,'gamapp/travel_details.html', {'post':post})
	
def travel_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(initial={'tags': '#travel'})
	return render (request, 'gamapp/travel_edit.html',{'form':form})
	
def travel_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'gamapp/travel_edit.html', {'form': form})
	
def fashion_list(request):
	posts = Post.objects.filter(tags__contains="#fashion")
	return render(request, 'gamapp/fashion_list.html',{'posts': posts })

def fashion_details(request,pk):
	post = get_object_or_404(Fashion, pk=pk)
	return render(request,'gamapp/fashion_details.html', {'post':post})
	
def fashion_new(request):
	if (request.method == "POST"):
		form=PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(initial={'tags': '#fashion'})
	return render (request, 'gamapp/fashion_edit.html',{'form':form})
	
def fashion_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('gamapp.views.post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'gamapp/fashion_edit.html', {'form': form})
	
def about_us(request):
	return render(request, 'gamapp/aboutus.html',{})

def rewards(request):
	return render(request, 'gamapp/rewards.html',{})
	
def contact_us(request):
	return render(request, 'gamapp/contactus.html',{})

