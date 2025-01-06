# OR_saurin
В гите можно ознакомиться с полным кодом сервисов. Для каждого из них своя папка.
В каждый сервис были добавлены небольшие доработки для более удобного тестирования.

1. https://hub.docker.com/repositories/sjey666 - ссылка на dockerhub. Тут можно найти 2 нужных нам образа в публичном доступе.

2. Для скачивания образов необходимо прописать 2 команды
docker pull sjey666/short_url:latest
docker pull sjey666/todo_app:latest

3. Осталось запустить контейнер. Я проверил на 2ух разных машинах, на первой достаточно localhost/docs в браузере.
НО если вдруг не находит соединения, лечится пробросом портов:

docker run -p 8080:80 sjey666/short_url(в обычном терминале или докер для запуска контейнера)

и сервис доступен по адресу  http://localhost:8080/docs.

4. Кратко о сервисах
   SHORT_URL
   ![image](https://github.com/user-attachments/assets/eb3a9ac7-a902-48a4-afa4-169fbfa89faf)
/all - отдает все короткие урлы
  ![image](https://github.com/user-attachments/assets/7a4fd3fb-ba03-4c71-b096-6b06d3e3454c)
/shorten - позволяет нам запостить новую ссылку
![image](https://github.com/user-attachments/assets/4940d6fe-c5f1-4f61-8644-9d5ff16d2a10)
/{short_id} - редирект на страницу. В swagger нету прямого перехода для теста можно использовать localhost/<short-id ссылки>
![image](https://github.com/user-attachments/assets/0e691fc8-1ec3-410e-bc27-7942f104d847)
/stats/{short_id} - общее инфо о длинной ссылке по ее короткой
  TODO_APP
    ![image](https://github.com/user-attachments/assets/b7e16d7e-cff5-461b-97f2-1b786147476e)
   /items - отдает инфу о всех задачках в бд
   ![image](https://github.com/user-attachments/assets/c078402a-5e52-4906-b53c-ffd804f4224c)
   /items[post] - позволяет записать задачку ее статус и описание
   ![image](https://github.com/user-attachments/assets/180d1649-4cb4-44a3-a95d-4befc8d598fc)
Удалить, изменить, получить по ID задачки.
   
   

