import face_recognition as fr
import numpy as np

def face(g_img_path,k_f_enc):
    g_img = fr.load_image_file(g_img_path) #img jisme check karna he
    f_l = fr.face_locations(g_img,number_of_times_to_upsample=2) #pehle faces ko locate karo. unka loc le lo
    f_e = fr.face_encodings(g_img,f_l,)  #fir usi loc pe faces ka encoding kar lo
    m = []
    for f_enc in f_e:
        matches = fr.compare_faces(k_f_enc,f_enc,tolerance=0.55)
        f_d = fr.face_distance(k_f_enc,f_enc)
        b_m_i = np.argmin(f_d)
        if matches[b_m_i]:
            m.append(b_m_i)
    return m


print(face(r".\img\1.jpg",[np.load("./img/1.npy"),np.load("./img/2.npy")]))
