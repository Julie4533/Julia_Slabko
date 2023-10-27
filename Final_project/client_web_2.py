import requests
import numpy as np

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost:4000/predict', json={'features': [ 1,  2,  3,  4,  5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]})
    # выводим статус запроса
    print(r.status_code)
    
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print(r.json())
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)