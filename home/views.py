from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,HttpResponse,redirect
import os

def index(request):
    return(render(request,"index.html"))

def modelform(request):

    try:


        if request.method == 'POST' and request.FILES['inpfile']:

            imagename="faceimage.jpg"
            if os.path.exists("./media/"+imagename):
                os.remove("./media/"+imagename)

            myfile = request.FILES['inpfile']
            fs = FileSystemStorage()
            filename = fs.save(imagename, myfile)
            print(filename)
            return render(request, "result.html")
        else:
            return render(request, "model.html")
    except:
        return render(request, "model.html")



def result(request):

    # Working of model here ==> to access image "./media/{imagename}.jpg"  (this will be path always)
    return render(request,"result.html")
