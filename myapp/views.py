from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
# import requests
from . models import *
from .forms import *

from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

def index(request):
    #!tek bir sayfada calistigimizdan dolayi geri bir 
    #!return dondugunde sadece indexi gorur o yuzden dinamik
    #!olarak erismek icin butun nesneleri datanin icinde tut!
    
    data = {
        'features'      : Feature.objects.all(), 
        'contents'      : Content.objects.all(),
        'cards'         : Card.objects.all(),
        'values'        : Values.objects.all(),
        'portfolios'    : Portfolio.objects.all(),
        'designes'      : Design.objects.all(),
        'kartlar'       : Kartlar.objects.all()
    }

    

    
    
    return render(request,'index.html',data)
    
def about(request):
    
    return render(request,'_about.html',)




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {
            'name'      :name,
            'email'     :email,
            'subject'   :subject,
            'message'   :message 
        }
        # print(data['email'])

        #? -------  mesaj icerigi su sekilde gozukecek  ------------
        message = '''  
        New message: {}
        
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'sahil.mehdiyev2000@gmail.com',['sahil.mehdiyev2000@gmail.com'])
        

    return render(request,'partials/contact.html',{})
    # else:
    #     return render(request,'templates/partials/contact.html')



def downloadFile(request):
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 1. Dosyanın bulunduğu temel dizini belirle
    filename = 'Sahilcv.pdf'  # 2. Dosyanın adını belirle
    filepath = base_dir + '/Files/' + filename # 3. Dosyanın tam yolunu oluştur
    thefile = filepath # 4. İlgili dosya
    filename = os.path.basename(thefile) # 5. Dosyanın adını al
    chunk_size = 8192 # 6. İçerik parçacıklarının boyutu
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size),# 7. Dosyayı okuyarak bir StreamingHttpResponse oluştur
                                     content_type=mimetypes.guess_type(thefile)[0])
 
    response['Content-Length'] = os.path.getsize(thefile) # 8. Dosyanın boyutunu içeriğe ekleyerek Content-Length ayarla
    response['Content-Disposition'] = 'attachment; filename=%s' % filename  # 9. Dosyanın indirilirken kullanıcıya gösterilecek adını belirle

    return response


def downloadFilePptx(request):
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 1. Dosyanın bulunduğu temel dizini belirle
    filename = 'emesai-kullanim.pptx'  # 2. Dosyanın adını belirle
    filepath = base_dir + '/Files/' + filename # 3. Dosyanın tam yolunu oluştur
    thefile = filepath # 4. İlgili dosya
    filename = os.path.basename(thefile) # 5. Dosyanın adını al
    chunk_size = 8192 # 6. İçerik parçacıklarının boyutu
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size),# 7. Dosyayı okuyarak bir StreamingHttpResponse oluştur
                                     content_type=mimetypes.guess_type(thefile)[0])
 
    response['Content-Length'] = os.path.getsize(thefile) # 8. Dosyanın boyutunu içeriğe ekleyerek Content-Length ayarla
    response['Content-Disposition'] = 'attachment; filename=%s' % filename  # 9. Dosyanın indirilirken kullanıcıya gösterilecek adını belirle

    return response




        




    
    
    
    # return render(request,'partials/downloadFile.html')
