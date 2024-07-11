# Harry Potter'ın Görünmez Pelerini

Bu proje, Harry Potter filmlerindeki ünlü görünmez pelerini konseptini kullanarak bir gerçek zamanlı görüntü işleme uygulamasıdır. Kod, webcam'den alınan görüntüde mavi renk algılayarak bu bölgeleri arka planla değiştirir, böylece kullanıcıların mavi nesneleri (örneğin bir kumaş parçası) görünmez hale getirmelerine olanak tanır.

### Nasıl Çalışır?

- `cv2.VideoCapture` ile kamerayı açar ve arka planı yakalar.
- HSV renk uzayında mavi renk aralığını tanımlar ve bu renkleri maskelemek için kullanır.
- Maskeleme işlemi ile mavi nesneleri arka plan ile değiştirir.
- Görüntü işleme sürecini gerçek zamanlı olarak `cv2.imshow` ile görselleştirir.

### Kullanım

1. Projeyi çalıştırın ve mavi bir nesne (örneğin bir bez parçası) kameranın önüne getirin.
2. Mavi nesne görünmez hale gelene kadar sonucu gözlemleyin.
3. Çıkmak için 'q' veya 'Esc' tuşuna basın.

### Gereksinimler

- Python 3.x
- OpenCV (`pip install opencv-python` ile kurulabilir)

### Katkı

Katkıda bulunmak veya geri bildirimde bulunmak isterseniz, lütfen bir GitHub issue açın veya bir pull request gönderin!

