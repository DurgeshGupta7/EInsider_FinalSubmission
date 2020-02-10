from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.

#create file
def upload_file(request):
	if request.method == 'POST':
		form = FileForm(request.POST,request.FILES,instance=request.user)

		if form.is_valid():
			# instance = FileForm(file=request.FILES['file'])
			fileobj = File()
			user = User.objects.get(id = request.user.id)
			fileobj.user = user
			fileobj.title = form.cleaned_data['title']
			fileobj.file_type=form.cleaned_data['file_type']
			fileobj.file = form.cleaned_data['file']
			fileobj.save()
			return redirect('file_list')

	else:
 		form = FileForm()
	return render(request, 'uploadfile/upload_file.html',{'form':form})

#view file
def file_list(request):
	query = request.GET.get("q",None)
	files = File.objects.all()
	if query is not None:
		files=files.filter(
			Q(title__icontains=query) |
			Q(file_type__icontains=query)
			)

	return render(request, 'uploadfile/file_list.html',{
			'files': files
		})


#delete file
def delete_file(request, pk):
	if request.method == 'POST':
		file = File.objects.get(pk = pk)
		file.delete()
	return redirect('file_list')


#server side pagination
def  file_objects_pagination(request,PAGENO,SIZE):
	skip = SIZE *(PAGENO -1)
	files= File.objects.all() [skip:(PAGENO * SIZE)]
	dict = {
			"file":list(File.values("title","name"))
		}
	return JsonResponse(dict)