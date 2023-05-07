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

DEBUG = False
if __name__ == '__main__':
    pic = cv2.imread('/home/ftp/manul.jpg')
    # cv2.imshow('МАНУЛ', pic)

    # Подготовим новые размеры
    final_wide = 800
    r = float(final_wide) / pic.shape[1]
    dim = (final_wide, int(pic.shape[0] * r))

    # уменьшаем изображение до подготовленных размеров
    resized = cv2.resize(pic, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Мелкий манул", resized)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    # # capture frames from a camera with device index=0
    # cap = cv2.VideoCapture(0)
    #
    # # loop runs if capturing has been initialized
    # while True:
    #     # захват
    #     ret, frame = cap.read()
    #     # отображение
    #     cv2.imshow('Camera', frame)
    #     # ждём нажатия 'q'
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # # отпускаем камеру
    # cap.release()
    #
    # # убираем окна
    # cv2.destroyAllWindows()