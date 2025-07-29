# Gerçek Zamanlı Banknot Tanıma Projesi (YOLOv8)

## 1. Projenin Amacı ve Özeti

Bu projenin temel amacı, bir bilgisayarın standart bir webcam aracılığıyla Türk Lirası banknotlarını gerçek zamanlı olarak tanımasını ve sınıflandırmasını sağlamaktır. Proje, modern bir nesne tespit modeli olan YOLOv8 kullanılarak geliştirilmiştir. Süreç, veri toplama, veri hazırlama, otomatik etiketleme, model eğitimi ve gerçek zamanlı uygulama adımlarını kapsamaktadır.

## 2. Kullanılan Teknolojiler

- **Model:** YOLOv8n (Ultralytics)
- **Kütüphaneler:** PyTorch (CUDA ile), OpenCV, Pillow
- **Dil:** Python
- **Veri Seti:** 900 adet resimden oluşan, projeye özel hazırlanmış bir veri seti (`dataset.zip`).

## 3. Eğitim ve Test Sonuçları

Model, NVIDIA GeForce GTX 1650 Ti GPU üzerinde 50 epoch boyunca eğitilmiştir. Eğitim sonunda, modelin daha önce hiç görmediği **Test Veri Seti** üzerinde elde edilen başarı metrikleri aşağıdaki gibidir:

- **mAP50 (Mean Average Precision @ IoU=0.50):** `0.995`
- **mAP50-95 (Mean Average Precision @ IoU=0.50:0.95):** `0.887`

**Bu ne anlama geliyor?**
- `mAP50` skorunun **%99.5** olması, modelimizin banknotları **neredeyse mükemmel bir doğrulukla** tespit edebildiğini gösterir.
- `mAP50-95` skorunun **%88.7** olması ise, modelin sadece banknotları bulmakla kalmayıp, aynı zamanda onların **konumlarını da çok hassas bir şekilde** çerçeveleyebildiğini kanıtlar.

## 4. Proje Akışı: Fikirden Ürüne Giden Yol

Bu proje, bir makine öğrenmesi modelinin sıfırdan nasıl hayata geçirildiğini adım adım gösterir. İzlenen yol, veri kaosuyla başlayıp, çalışan bir uygulamayla son bulmuştur.

1.  **Veri Toplama ve İsimlendirme:** Farklı banknotların resimleri toplandı ve dosya isimleri sınıfı belirtecek şekilde (`5(1).jpg`, `10(1).jpg` vb.) düzenlendi.
2.  **Veri Organizasyonu (`organize_and_chunk_images.py`):** Ham resimler, sınıflarına göre ayrılıp, etiketleme sürecini kolaylaştırmak için 100'lük gruplara bölündü.
3.  **Otomatik Etiketleme (`auto_labeler.py`):** Parçalanmış resimlerin her birine, merkezlerini baz alarak YOLO formatında (`.txt`) etiket dosyaları otomatik olarak oluşturuldu.
4.  **Veri Seti Finalizasyonu (`finalize_dataset.py`):** Otomatik etiketlenmiş tüm resim grupları birleştirildi, rastgele karıştırıldı ve makine öğrenmesi standardı olan `%70 Eğitim`, `%20 Doğrulama`, `%10 Test` oranlarında `dataset` klasörüne ayrıldı.
5.  **Model Eğitimi (`train.py`):** Hazırlanan `dataset` ve `data.yaml` konfigürasyon dosyası kullanılarak, önceden eğitilmiş `yolov8n.pt` modeli üzerinde "ince ayar" (fine-tuning) yapıldı. Eğitim sonucunda projenin asıl ürünü olan `best.pt` modeli elde edildi.
6.  **Gerçek Zamanlı Uygulama (`detect_live.py`):** Eğitilmiş `best.pt` modeli kullanılarak, webcam'den gelen görüntüleri anlık işleyen ve banknotları tespit eden son kullanıcı uygulaması yazıldı.

## 5. Proje Dosyalarının Detaylı Açıklamaları

- **`best.pt`**: **Projenin Çıktısı.** Kendi veri setimizle eğittiğimiz, en başarılı ve kullanıma hazır model dosyası.
- **`yolov8n.pt`**: **Eğitimin Başlangıç Noktası.** Eğitime sıfırdan başlamak yerine kullandığımız, önceden eğitilmiş temel model.
- **`data.yaml`**: **Eğitimin Pusulası.** YOLO'ya `dataset` klasörünün nerede olduğunu, kaç sınıf olduğunu ve bu sınıfların isimlerini (`5-lira`, `10-lira` vb.) bildiren yapılandırma dosyası.
- **`requirements.txt`**: **Projenin Reçetesi.** Projenin çalışması için gereken tüm Python kütüphanelerini listeleyen dosya.
- **`train.py`**: **Modelin Öğretmeni.** `data.yaml` ve `dataset`'i kullanarak `yolov8n.pt` modelini eğiten ve `best.pt`'yi üreten script.
- **`detect_live.py`**: **Uygulamanın Kendisi.** `best.pt` modelini kullanarak gerçek zamanlı tespiti başlatan script.
- **`organize_and_chunk_images.py`**, **`auto_labeler.py`**, **`finalize_dataset.py`**: **Veri Hazırlama Araçları.** Ham resimleri alıp, adım adım işleyerek eğitime hazır hale getiren yardımcı scriptler.
