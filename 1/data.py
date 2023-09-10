# data.py

# импортируем необходимые библиотеки
import pandas as pd # библиотека для работы с табличными данными
import numpy as np # библиотека для работы с числовыми данными
from sklearn.preprocessing import LabelEncoder, MinMaxScaler # библиотека для предобработки данных

def load_user_data(filename):
  # функция для загрузки данных о пользовательском поведении из файла
  # принимает на вход имя файла в формате csv
  # возвращает датафрейм pandas
  user_data = pd.read_csv(filename) # читаем файл с помощью pandas
  return user_data

def load_market_data(filename):
  # функция для загрузки данных о рынке и конкурентах из файла
  # принимает на вход имя файла в формате csv
  # возвращает датафрейм pandas
  market_data = pd.read_csv(filename) # читаем файл с помощью pandas
  return market_data

def preprocess_data(user_data, market_data):
  # функция для предобработки данных
  # преобразует категориальные признаки в числовые с помощью LabelEncoder
  # нормализует числовые признаки в диапазоне [0, 1] с помощью MinMaxScaler
  # объединяет данные о пользователях и рынке в один датафрейм
  # возвращает обработанный датафрейм pandas
  le = LabelEncoder() # создаем объект для кодирования категориальных признаков
  user_data = user_data.apply(le.fit_transform) # кодируем категориальные признаки пользователей
  market_data = market_data.apply(le.fit_transform) # кодируем категориальные признаки рынка
  data = pd.merge(user_data, market_data, on='user_id') # объединяем данные по id пользователя
  scaler = MinMaxScaler() # создаем объект для нормализации числовых признаков
  data = scaler.fit_transform(data) # нормализуем числовые признаки
  return data

def visualize_campaign(campaign):
  # функция для визуализации результатов кампании с помощью графиков и таблиц
  # принимает на вход объект кампании, содержащий информацию о размещенной рекламе и ее эффективности
  # использует библиотеки matplotlib, seaborn и pandas для построения графиков и таблиц
  import matplotlib.pyplot as plt # библиотека для построения графиков
  import seaborn as sns # библиотека для построения красивых графиков
  
  # график распределения бюджета по каналам
  plt.figure(figsize=(10,6)) # создаем фигуру с заданным размером
  sns.barplot(x=campaign['channel'], y=campaign['spend']) # строим столбчатый график с каналами по оси x и затратами по оси y
  plt.title('Budget distribution by channel') # добавляем заголовок графика
  plt.xlabel('Channel') # добавляем подпись оси x
  plt.ylabel('Spend') # добавляем подпись оси y
  plt.show() # показываем график

  # график распределения конверсий по каналам
  plt.figure(figsize=(10,6)) # создаем фигуру с заданным размером
  sns.barplot(x=campaign['channel'], y=campaign['conversions']) # строим столбчатый график с каналами по оси x и конверсиями по оси y
  plt.title('Conversions distribution by channel') # добавляем заголовок графика
  plt.xlabel('Channel') # добавляем подпись оси x
  plt.ylabel('Conversions') # добавляем подпись оси y
  plt.show() # показываем график

  # таблица сравнения метрик по каналам
  metrics = campaign.groupby('channel').agg({'spend': 'sum', 'conversions': 'sum', 'ROAS': 'mean'}) # группируем данные по каналам и агрегируем метрики
  metrics['CPA'] = metrics['spend'] / metrics['conversions'] # добавляем столбец с стоимостью за конверсию
  print(metrics) # выводим таблицу
