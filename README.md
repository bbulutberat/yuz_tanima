# Basit Yüz Algılama Projesi  
-Bu Python projesi, OpenCV kullanarak webcam üzerinden gerçek zamanlı yüz algılama işlemi yapar. Yüzler, Haar Cascade yöntemiyle tespit edilir ve ekranda dikdörtgen çerçevelerle gösterilir.  


## Gereksinimler  
-Python 3.x  
-OpenCV  

## Haar Cascade Algoritması  
--
Haar Cascade algoritması, Bir görüntüdeki veya gerçek zamanlı bir 
videodaki yüzleri tanımlamak için kullanılan bir Nesne Algılama 
Algoritmasıdır. Algoritmaya, yüzlerden oluşan çok sayıda olumlu görüntü ve 
üzerlerinde eğitilecek herhangi bir yüzden oluşmayan çok sayıda olumsuz 
görüntü verilir. Bu eğitimden oluşturulan model, OpenCV GitHub 
deposunda mevcuttur.  

**Avantajları**  
-Çok hızlıdır. Düşük işlem gücüne sahip sistemlerde bile gerçek zamanlı yüz tespiti yapılabilir.  
-Webcam veya canlı video akışlarında sorunsuz şekilde kullanılabilir.  
-Derin öğrenme tabanlı modellere göre çok daha az RAM ve işlemci gücü tüketir.  
-OpenCV ile birlikte gelen önceden eğitilmiş .xml modeller sayesinde doğrudan kullanılabilir.  
-Sadece yüz değil, göz, burun, araç plakası, el hareketleri gibi farklı nesneler için de model eğitilebilir.  
-scaleFactor, minNeighbors, minSize gibi birkaç temel parametre ile iyi sonuçlar elde edilebilir.  

**Dezavantajları**  
-Aydınlık ortamlarda iyi çalışırken, gölgeli veya gece ortamlarında çoğu zaman başarısız olur.  
-Yüz yalnızca cepheden bakıldığında doğru şekilde tespit edilebilir.  
-Derin öğrenme tabanlı yöntemler (örneğin CNN, MTCNN, RetinaFace, Mediapipe) ile kıyaslandığında:  
    -Doğruluğu daha düşüktür.  
    -Yalnızca sınırlı türde nesne tespiti yapılabilir.  
-Görüntüyü gri tona çevirerek çalışır. Renkli bilgiyi (ten rengi, sıcaklık vb.) kullanmaz. Bu da renk temelli nesneleri algılamada yetersizliğe neden olur.
    
----------------------------------------------------------------------------------------------------------------------------------------

## KOD AÇIKLAMASI  
```
import cv2
import numpy as np

class YuzAlgila():

   def __init__(self):
        # Haar Cascade modeli yüklenir.
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  

        # Webcam açılır.
        self.cap = cv2.VideoCapture(0)

   def kamera(self):
        while True:
            
            # Kameradan her frame görüntüsü tek tek alınır.
            ret, self.frame = self.cap.read()

            face_rect = self.Algila()
            self.Cizdir(face_rect)

            #Görüntü kullanıcıya gösterilir.
            cv2.imshow("Yuz_Algilama", self.frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
               self.cap.release()
                break
    
   def Algila(self):
        
        # Yüzler tespit edilir. ScaleFactor ve minNeighbors parametreleri ile hassasiyet ve doğruluk ayarlanır.
        return self.face_cascade.detectMultiScale(self.frame, scaleFactor=1.2, minNeighbors=5)

   def Cizdir(self, face_rect):

        # Tespit edilen yüzler dikdörtgen içine alınır.
        for (x, y, w, h) in face_rect:
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 255, 255), 10)


if __name__ == "__main__":
    baslat = YuzAlgila()
    baslat.kamera()
    cv2.destroyAllWindows()
```
----------------------------------------------------------------------------------------------------------------------------------------

## Parametreler
-ScaleFactor = Görüntüyü küçültme oranı. Daha düşük değerler daha hassas ama yavaş olur.  
-MinNeighbors = Bir bölgenin yüz olarak kabul edilmesi için gereken komşuluk sayısı.  

**Önerilen Değerler**
-scaleFactor=1.2: Gerçek zamanlı uygulamalar için dengeli hız ve doğruluk sağlar.  
-minNeighbors=5: Yanlış pozitifleri azaltır, daha kararlı sonuç verir.

## Projeyi Çalıştırma  
-python yuz_algilama.py
 
## Nasıl Çalışıyor?   
-cv2.VideoCapture(0) ile webcam başlatılır.  
-Her karede detectMultiScale() ile yüzler aranır.  
-Yüzler tespit edildiğinde, çerçeve içine alınır.  
-q tuşuna basıldığında kamera kapanır ve program sonlanır.  

## Notlar  
-Webcam açılmazsa, başka bir uygulamanın kamerayı kullanmadığından emin olun.  
-Işık koşulları yüz tespit performansını etkileyebilir.  
-Bu proje sadece ön yüzdeki yüzleri tanır, dönen ya da ters yüzlerde çalışmayabilir.  


