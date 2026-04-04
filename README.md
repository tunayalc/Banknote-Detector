# Banknote-Detector

N Kolay Ödeme Kuruluşu A.Ş. stajım sırasında geliştirdiğim banknot tespit projesi

## Genel Bakış

`Banknote-Detector`, görüntü işleme ve nesne tespiti alanında çalıştığım staj projelerinden biri. Proje, banknotların görüntü üzerinden tespit edilmesi için veri hazırlığı, etiketleme, eğitim ve canlı inference adımlarını aynı akış içinde ele alıyor.

## Proje Kapsamı

| Katman | İçerik |
| --- | --- |
| Veri Hazırlığı | görselleri düzenleme ve sınıflandırma |
| Etiketleme | yarı otomatik label üretimi |
| Dataset Sonlandırma | train / val / test düzeni |
| Model Eğitimi | YOLOv8 tabanlı object detection |
| Canlı Çalıştırma | webcam üzerinden gerçek zamanlı tespit |

## Dosya Bazlı Yapı

### `organize.py`

Ham veri setini daha düzenli bir yapıya çekmek için kullanılan dosya. Veri toplama ile eğitim arasındaki ilk köprüyü kuruyor.

### `auto_labeler.py`

Etiketleme sürecinin bir bölümünü otomatikleştirerek veri hazırlığını hızlandırmayı amaçlayan bileşen.

### `finalize_dataset.py`

Veri setini model eğitimine uygun nihai formata yaklaştıran son hazırlık adımı.

### `train.py`

YOLOv8 model eğitiminin merkezini oluşturan script.

### `detect_live.py`

Eğitilen modelin canlı kamera akışı üzerinde test edilmesini sağlayan inference katmanı.

### `data.yaml`

Sınıf isimleri ve dataset yolları gibi eğitim konfigürasyonunu tanımlayan dosya.

## Repo Yapısı

```text
Banknote-Detector/
|-- auto_labeler.py
|-- data.yaml
|-- detect_live.py
|-- finalize_dataset.py
|-- organize.py
|-- train.py
|-- requirements.txt
`-- README.md
```

## Kullanılan Teknolojiler

- Python
- Ultralytics YOLOv8
- OpenCV
- object detection yaklaşımı
- görüntü işleme
