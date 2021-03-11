import face_recognition as fr
import numpy as np

def l_img(x):
    a_img = fr.load_image_file(x)
    a_l = fr.face_locations(a_img,number_of_times_to_upsample=2)
    return fr.face_encodings(a_img,a_l)[0]


kfe = l_img(r'1.jpg') #known faces ka path. isko koi file me save kar sakte he enc. ko
np.save(r'1.npy',kfe)
