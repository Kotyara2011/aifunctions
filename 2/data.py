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

def load_campaign_data(filename):
  # функция для загрузки данных о целях и метриках рекламной кампании из файла
  # принимает на вход имя файла в формате csv
  # возвращает датафрейм pandas
  campaign_data = pd.read_csv(filename) # читаем файл с помощью pandas
  return campaign_data

def preprocess_data(user_data, market_data, campaign_data):
  # функция для предобработки данных
  # преобразует категориальные признаки в числовые с помощью LabelEncoder
  # нормализует числовые признаки в диапазоне [0, 1] с помощью MinMaxScaler
  # объединяет данные о пользователях, рынке и кампании в один датафрейм
  # возвращает обработанный датафрейм pandas
  le = LabelEncoder() # создаем объект для кодирования категориальных признаков
  user_data = user_data.apply(le.fit_transform) # кодируем категориальные признаки пользователей
  market_data = market_data.apply(le.fit_transform) # кодируем категориальные признаки рынка
  campaign_data = campaign_data.apply(le.fit_transform) # кодируем категориальные признаки кампании
  data = pd.merge(user_data, market_data, on='user_id') # объединяем данные по id пользователя
  data = pd.merge(data, campaign_data, on='campaign_id') # объединяем данные по id кампании
  scaler = MinMaxScaler() # создаем объект для нормализации числовых признаков
  data = scaler.fit_transform(data) # нормализуем числовые признаки
  return data

def analyze_data(data):
  # функция для анализа данных
  # вычисляет основные статистические показатели по данным (среднее, медиана, стандартное отклонение и т.д.)
  # строит гистограммы и корреляционную матрицу по данным с помощью библиотек matplotlib и seaborn
  # возвращает словарь со статистическими показателями и графиками
  stats = {} # создаем пустой словарь для хранения статистических показателей
  stats['mean'] = data.mean() # вычисляем среднее по каждому столбцу
  stats['median'] = data.median() # вычисляем медиану по каждому столбцу
  stats['std'] = data.std() # вычисляем стандартное отклонение по каждому столбцу
  stats['min'] = data.min() # вычисляем минимум по каждому столбцу
  stats['max'] = data.max() # вычисляем максимум по каждому столбцу
  
  import matplotlib.pyplot as plt # библиотека для построения графиков
  import seaborn as sns # библиотека для построения красивых графиков
  
  # строим гистограммы по каждому столбцу
  plt.figure(figsize=(10,10)) # создаем фигуру с заданным размером
  for i in range(data.shape[1]): # проходим по каждому столбцу в цикле
    plt.subplot(3,3,i+1) # создаем подграфик в сетке 3x3
    sns.histplot(data.iloc[:,i]) # строим гистограмму с помощью seaborn
    plt.title(data.columns[i]) # добавляем заголовок с именем столбца
  plt.tight_layout() # подгоняем размеры графиков
  stats['histograms'] = plt # сохраняем фигуру с гистограммами в словаре
  
  # строим корреляционную матрицу по данным
  plt.figure(figsize=(10,10)) # создаем фигуру с заданным размером
  sns.heatmap(data.corr(), annot=True, cmap='Blues') # строим тепловую карту с помощью seaborn
  plt.title('Correlation matrix') # добавляем заголовок графика
  stats['correlation'] = plt # сохраняем фигуру с корреляционной матрицей в словаре
  
  return stats
