<h1> Финальный проект: «Модель прогнозирования стоимости жилья для агентства недвижимости»</h1>

Цель проекта — разработать моделья прогнозирования стоимости недвижимости и запустить веб-сервис, предсказывающий цену объекта по его характеристикам

В моей работе представлены 3 файла:

<h2> Final</h2>
файл, в котором составляется модель

## 1. Обработка и очистка данных, разведывательный анализ

>разведывательный анализ начну сразу проводить в этом пункте

### 1.1 Признаки fireplace, private pool, PrivatePool, mls-id

### 1.2 Обработка признака status

### 1.3. обработка признака propertyType

### 1.4 Признак street

### 1.5 Обработка признака baths

### 1.6 Обработка признака homeFacts

#### 1.6.1 извлечем год постройки дома

#### 1.6.2.извлечем тип отопления

#### 1.6.3 извлечем тип парковки из признака homeFacts

### 1.7 Обработка признака schools

#### 1.7.1 извлечем количество школ из признака schools

#### 1.7.2 посчитаем средний рейтинг школ

### 1.8 преобразуем признак sqft

### 1.9 преобразуем признак beds

### 1.10 признак state

### 1. 11 признак city

### 1.12 преобразуем признак stories

### 1.13 целевой признак target

## 2. обработка пропусков и выбросов

## 3. Разведывательный анализ данных

## 4. Построение модели

### 4.1 Подготовка данных

### 4.2 Модель случайного леса. 

### 4.3 Замена целевой переменной. 

### 4.4 Оптимизация гиперпараметров модели случайного леса

### 4.5 Отбор признаков с помощью SelectKBest

### 4.6 создание пайплайна и сериализация модели

<h2> wep_app_2</h2>
файл, в котором составляется сервер для приложения

<h2> client_web_2</h2>
файл, в котором составляется клиент приложения