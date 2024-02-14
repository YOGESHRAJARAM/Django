from django.shortcuts import render
import datetime
import os
import qrcode


# Create your views here.

def indexpage(request):
    if request.method == 'POST':
        value=request.POST['qrcodelink']
        storpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename= str(datetime.datetime.now())
        newfilename= filename.replace("-","").replace(":","").replace(".","")
        trimed_text=newfilename.lstrip()
        trimed_text=trimed_text.replace(" ","_")
        finalstoringpath=trimed_text+".png"
        storepathimage= str(os.path.join(storpath,'static','images',finalstoringpath))
        print(storepathimage)
        print(trimed_text)
        img=qrcode.make(value)
        img.save(storepathimage)
        value_dis={'valuename':value,'qrcodeimg':finalstoringpath}
        return render(request,'index.html',context=value_dis)
    
    return render(request,'index.html')

