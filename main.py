# ЗАТРАХАЛСЯ ДОЛБАНЫЙ ОПЕНСИВИ СТАВИТЬ! Но всё поставилось и заработало. Уфф.
"""
Напишу, как ставил, пока не забыл.
1. Никаких пакетов через pip, библиотека OpenCV ставится только как внешняя сборка. Убедитесь, что никаких opencv, cv2
и прочего не установлено в свойствах интерпретатора PyCharm. Должно быть сухо и чисто, и вообще вся система обновлена.
2. Ставить строго и чётко по инструкции тут: https://pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/
(см. также README.md)
3. В конце в свойствах интерпретатора в PyCharm нужно будет обязательно указать полный путь к библиотеке 'cv2.so'
(Вы там по инструкции переименовывали длинное название в короткое 'cv2.so' - вот к ней и указывайте путь.)
"""
import cv2

if __name__ == '__main__':
    my_photo = cv2.imread('/home/ftp/test.jpeg')
    cv2.imshow('juj', my_photo)

    # Подготовим новые размеры
    final_wide = 200
    r = float(final_wide) / my_photo.shape[1]
    dim = (final_wide, int(my_photo.shape[0] * r))

    # уменьшаем изображение до подготовленных размеров
    resized = cv2.resize(my_photo, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
