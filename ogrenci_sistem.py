
note=0
#Not Ortalamasnın Hesaplandıgı fonksiyon
def final_score(m,n,p) :
    score = 0.3 * m + 0.5 * f + 0.2*p
    print("Not Ortalaması: "+str(score))
    note=score
    return score
#HArf Notunun hesaplandıgı fonksiyon
def letter_grade(note) :

    if 90 <= note <= 100:
        print("Harf notunuz:AA")
        
    elif 70 <= note < 90:
        print("Harf notunuz:BB")
        
    elif 50 <= note < 70:
        print("Harf notunuz:CC")
       
    elif 30 <= note < 50:
        print("Harf notunuz:DD")
        
    else:
        print("Harf notunuz:FF")
      
    return letter_grade

print("Öğrenci Sistemine Hosgeldiniz")
#Kimlik bilgisinin dogrulugunun belirlendigi fonksiyon
def get_input():

    keywords = ['Ayse Celik', 'Ali Ozdemir', 'Ozlem Demirci']
    user_input = None
    while True:
        false=0
        user_input = input("isim giriniz:")
        if user_input in keywords:
            break
        else:
            
            false=false+1
            print(str(false)+"kere yanlıs girdiniz")
            if false == 3:
                print("3 kere yanlıs girdiniz. Sonra tekrar deneyin")
                break
    return user_input
user=get_input()

Ders_sayisi=int(input("Kac ders sececeksiniz?(En az 3, En fazla 5 ders alabilirsiniz"))
#Alınacak ders sayısının 3-5 arasında kalmasını saglayan fonksiyon
def secim(Ders_sayisi):
    
        if Ders_sayisi<3:
            print("En az 3, en fazla 5 ders alabilirsiniz.Tekrar deneyin")
            
        elif Ders_sayisi>5:
            print("En fazla 5 ders seçebilirsiniz. Tekrar deneyin")
            
        else :
            print(str(Ders_sayisi)+" dersi secebilirsiniz.Başarılar")
            

secim(Ders_sayisi)           

print(user+" derslere asagıda bakıp basındaki ders kodunu yazarak secebilirsin.")
#Dersler Listesi ve Ders Kodları
Lessons=["Math","Python","İngilizce","Fizik","Kimya","Etik"]
print("Dersler:0)"+str(Lessons[0]) +" 1)"+str(Lessons[1]) +" 2)"+str(Lessons[2])
     +" 3)"+str(Lessons[3])+" 4)"+str(Lessons[4])+" 5)"+str(Lessons[5]))

choosen_lessons=[]
#Secilen derserimizi ekledigimiz liste

#Derslerimizi listeye ekledigimiz kısım
for i in range(Ders_sayisi): 
    if i<=Ders_sayisi :  
        i = int(input("Ders kodunu girin: "))
        choosen_lessons.append(Lessons[i]) # adding the element 
        print(choosen_lessons)
print(str(Ders_sayisi)+ " ders aldınız")
#Secilen derslerden Hangisinin not ortalamasına bakılacagını gosteren kısım
selected_lesson=str(input("Notlarınızın ekleneceği dersi yazın:"))

m=int(input("Midterm notunuzu giriniz"))
p=int(input("Proje notunuzu giriniz")) 
f=int(input("Final notunuzu giriniz"))
d={"midterm":m,"project":p,"final":f}
print(d)
print(selected_lesson+" Dersi Sonuçları:")
final_score(m,p,f)
letter_grade(a)