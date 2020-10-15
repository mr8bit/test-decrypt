### Дешифровка тестов 

1. **Определение склонности к отклоняющемуся поведению (А. Н. Орел)**

Методика диагностики склонности к отклоняющемуся поведению (Определение склонности к отклоняющемуся поведению
по А. Н. Орел) является стандартизированным тест-опросником, предназначенным для измерения готовности
(склонности) подростков к реализации различных форм отклоняющегося поведения. Опросник представляет собой
набор специализированных психодиагностических шкал, направленных на измерение готовности (склонности к
реализации отдельных форм отклоняющегося поведения.

2. **Суицидальная мотивация (Ю.Р.Вагин, 1998)**

Тест позволяет выявить и количественно оценить семь основных мотивационных аспектов суицидального поведения



Пример данных для обработки данных для теста №1

```json
[
  {
    "ФИО": "Иван Иванович",
    "gender": "m",
    "answer": [
      {
        "question": "Выберите ваш пол",
        "answer": 1
      },
      {
        "question": "Я стремлюсь в одежде следовать самой современной моде или даже опережать ее",
        "answer": 1
      } 
    ]
  }
]
```

Пример рабочего кода для обработки результатов для теста №1
```python

import pandas as pd
import json
from social_deviation import SocialDeviation

df = pd.read_csv("./data/api_test1.csv", delimiter=",", header=None)
df.columns = ['id','user_id', 'answer', 'gender']

index_db = 11
answer = df.iloc[index_db]['answer']
gender = df.iloc[index_db]['gender']
answer = json.loads(answer)

sd = SocialDeviation()
sd.process_answer(answer=answer, gender=gender)
results = sd.humanize_result()

for scale in results:
    print(scale['Scale'])
    print(scale['ScaleValue'])
    print(scale['Decryption'])
    print()
    print("="*30)





```


Пример данных для обработки данных для теста №2

```json
[
  {
    "ФИО": "Иван Иванович",
    "gender": "m",
    "answer": [
      {
        "question": "Совершали ли вы попытку/попытки самоубийства?",
        "answer": 1
      },
      {
        "question": "Думал, что если умру, то всем будет только лучше",
        "answer": 0
      } 
    ]
  }
]
```

Пример рабочего кода для обработки результатов для теста №2
```python
from suicidal_motivation import SuicidalMotivation
import pandas as pd
import json

df = pd.read_csv("./data/api_test2.csv", delimiter=",", header=None)
df.columns = ['id','user_id', 'answer', ]

index_db = 0
print(df.iloc[index_db])
answer = df.iloc[index_db]['answer']
answer = json.loads(answer)

sm = SuicidalMotivation()
sm.process_answer(answer=answer)
results = sm.humanize_result()

for scale in results:
    print(scale['Scale'])
    print(scale['ScaleValue'])
    print()
    print("="*30)

```