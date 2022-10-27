from django.shortcuts import render, redirect
from diary.form import MemoryForm
from diary.models import Memory

def memory_list(request):
    list_qs = Memory.objects.all().order_by('-pk')
    
    return render(
        request, 
        'blog/memory_list.html',
        {   
            'list_qs' : list_qs
        }
        )

def memory_detail(request, pk):
    post = Memory.objects.get(pk=pk)

    return render(
        request,
        'blog/memory_detail.html',
        {
            'post':post
        }
    )

def memory_new(request):
    # print("request.method=", request.method)
    # print("request.Post=", request.Post)
    if request.method == "GET":
        form=MemoryForm()
    else:
        form=MemoryForm(request.POST)
        if form.is_valid():
            #form.cleaned_data
            post = form.save()
            #return redirect(f"/blog/{post.pk}/")
            #return redirect("/blog/")
            return redirect(post)

    return render(request, 'blog/memory_new.html', {
        "form": form,
    })
