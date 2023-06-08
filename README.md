# Поиск объектов на фотографии

## Сборка и запуск проекта:

1. Склонировать репозиторий:

`git clone https://github.com/mark0wka/DeepLearning2023.git`

2. Перейдите в папку с проектом:

`cd DeepLearning2023`

3. Соберите Docker Image:

`docker build -t <IMAGE_NAME>`

4. Запустите контейнер:

`docker run <IMAGE_NAME>`

## Сохранение результатов локально:

1. Узнаем ID контейнера с проектом:

`docker ps -a`

2. Копируем файлы из контейнера в локальную файловую систему:

`docker cp <CONTAINER_ID>:/GroundingDINO/local_result.txt <YOUR_PATH>`
`docker cp <CONTAINER_ID>:/GroundingDINO/docker_result.txt <YOUR_PATH>`

### Результаты работы проекта:

В папке содержатся 2 файла - docker_results.txt - результаты, полученные при работе проекта в Докере. 
И local_results.txt - результаты, полученные при работе проекта на моей машине.
При запуске контейнера, последней строкой в логах выведется процент идентичности этих двух файлов.

## Ссылки:
+ [Страница проекта](https://paperswithcode.com/paper/grounding-dino-marrying-dino-with-grounded) на Papers With Code

+ [Ссылка](https://github.com/idea-research/groundingdino) на репозиторий