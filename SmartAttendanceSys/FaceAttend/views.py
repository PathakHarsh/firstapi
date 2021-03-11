from django.shortcuts import render,get_object_or_404
from .models import Student,Attendance,Subject,Faculty
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import datetime
import face_recognition as fr
import numpy as np
import os.path

def face(g_img_path,k_f_enc):
    g_img = fr.load_image_file(g_img_path) #img jisme check karna he
    f_l = fr.face_locations(g_img,number_of_times_to_upsample=2) #pehle faces ko locate karo. unka loc le lo
    f_e = fr.face_encodings(g_img,f_l,)  #fir usi loc pe faces ka encoding kar lo
    m = []
    for f_enc in f_e:
        matches = fr.compare_faces(k_f_enc,f_enc,tolerance=0.6)
        f_d = fr.face_distance(k_f_enc,f_enc)
        b_m_i = np.argmin(f_d)
        if matches[b_m_i]:
            m.append(b_m_i)
    return m

# Create your views here.
def take_attendance(request):
    return render(request,'FaceAttend/t_A.html')

def view_attendance(request):
    pass

def login(request):
    i_s = request.POST['user']
    if i_s == 's':
        k = Student.objects.get(pk=request.POST['username'])
    elif i_s == 'f':
        k = Faculty.objects.get(pk=request.POST['username'])
    if k.password == request.POST['password']:
        return HttpResponse('valid')
    else:
        return HttpResponse('invalid')
    

def do_attendance(request):
    k_s = Student.objects.filter(branch=request.POST['branch'],sem=request.POST['sem'])
    s = Subject.objects.get(id=request.POST['sub_id'])
    k_f = []
    k_f_id = []
    p = FileSystemStorage()
    p.save("1.jpg",request.FILES["A_img"])
    for k in k_s:
        k_f.append(np.load(os.path.dirname(__file__)+'/../media/enc/'+str(k.id)+'.npy'))
        k_f_id.append(k.id)
    m = face(os.path.dirname(__file__)+"/../media/1.jpg",k_f)
    for k in k_s:
        Attendance(stud_id=k,sub_id=s,date=datetime.datetime.now(),present= k_f_id.index(k.id) in m).save()
    return render(request,'FaceAttend/t_A.html')
