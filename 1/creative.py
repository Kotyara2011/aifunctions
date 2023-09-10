# creative.py

# импортируем необходимые библиотеки
import nltk # библиотека для работы с естественным языком
import gensim # библиотека для работы с векторными представлениями слов
import transformers # библиотека для работы с предобученными нейронными сетями

def generate_creative(data):
  # функция для генерации креатива для рекламы
  # принимает на вход данные о пользователе, канале, формате и цели рекламы
  # использует модель GPT-2 из библиотеки transformers для генерации текста
  # возвращает текст креатива
  
  # загружаем предобученную модель GPT-2
  model = transformers.pipeline('text-generation', model='gpt2')
  
  # формируем начальный текст для генерации на основе данных
  prompt = f"User: {data['user']}\nChannel: {data['channel']}\nFormat: {data['format']}\nGoal: {data['goal']}\n\nCreative:\n"
  
  # генерируем текст креатива с помощью модели
  creative = model(prompt, max_length=100, do_sample=True)[0]['generated_text']
  
  # удаляем начальный текст из креатива
  creative = creative.replace(prompt, '')
  
  return creative

def personalize_creative(creative, user):
  # функция для персонализации креатива для рекламы
  # принимает на вход текст креатива и данные о пользователе
  # использует модель Word2Vec из библиотеки gensim для подбора синонимов и антонимов
  # возвращает персонализированный текст креатива
  
  # загружаем предобученную модель Word2Vec
  model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  
  # разбиваем текст креатива на токены (слова)
  tokens = nltk.word_tokenize(creative)
  
  # создаем пустой список для хранения персонализированных токенов
  personalized_tokens = []
  
  # проходим по каждому токену в цикле
  for token in tokens:
    # если токен является прилагательным и содержится в модели Word2Vec
    if nltk.pos_tag([token])[0][1] == 'JJ' and token in model:
      # если пользователь любит экстремальные эмоции, то подбираем синоним с большей интенсивностью
      if user['emotion'] == 'extreme':
        synonym = model.most_similar(token, topn=1)[0][0]
        personalized_tokens.append(synonym)
      # если пользователь любит спокойные эмоции, то подбираем антоним с меньшей интенсивностью
      elif user['emotion'] == 'calm':
        antonym = model.most_similar_negative(token, topn=1)[0][0]
        personalized_tokens.append(antonym)
      # иначе оставляем токен без изменений
      else:
        personalized_tokens.append(token)
    # иначе оставляем токен без изменений
    else:
      personalized_tokens.append(token)
  
  # объединяем персонализированные токены в текст
  personalized_creative = ' '.join(personalized_tokens)
  
  return personalized_creative
