from django.shortcuts import render

def index(request):
    context={"text":"hello"}
    return render(request,'base.html',context)
