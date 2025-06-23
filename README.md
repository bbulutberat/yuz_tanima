Basit Yüz Algılama Projesi  
-Bu Python projesi, OpenCV kullanarak webcam üzerinden gerçek zamanlı yüz algılama işlemi yapar. Yüzler, Haar Cascade yöntemiyle tespit edilir ve ekranda dikdörtgen çerçevelerle gösterilir.  


Gereksinimler  
-Python 3.x  
-OpenCV  


Projeyi Çalıştırma  
-python yuz_algilama.py
 

Nasıl Çalışıyor?   
-cv2.VideoCapture(0) ile webcam başlatılır.  
-Her karede detectMultiScale() ile yüzler aranır.  
-Yüzler tespit edildiğinde, çerçeve içine alınır.  
-q tuşuna basıldığında kamera kapanır ve program sonlanır.  

Notlar  
-Webcam açılmazsa, başka bir uygulamanın kamerayı kullanmadığından emin olun.  
-Işık koşulları yüz tespit performansını etkileyebilir.  
-Bu proje sadece ön yüzdeki yüzleri tanır, dönen ya da ters yüzlerde çalışmayabilir.  


