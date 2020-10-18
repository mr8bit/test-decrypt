from .data_keys import suicidal_keys


class SuicidalMotivation():
    """
        Тест: "Суицидальная мотивация" (Ю.Р.Вагин, 1998)
        Назначение: тест позволяет выявить и количественно оценить семь основных мотивационных аспектов суицидального поведения:
        1. Альтруистическая мотивация (смерть ради других)
        2. Анемическая мотивация (потеря смысла жизни)
        3. Анестетическая мотивация (невыносимость страдания)
        4. Инструментальная мотивация (манипуляция другими)
        5. Аутопунитическая мотивация (самонаказание)
        6. Гетеропунитическая мотивация (наказание других)
        7. Поствитальная мотивация (надежда на что-то лучшее после смерти).
    """

    def __init__(self):
        self.suicidal_keys = suicidal_keys
        self.result = []
        self.raw_result = []
        self.gender = ''
        self.scale = [
            'Альтруистическая мотивация (смерть ради других)',
            'Аномическая мотивация (потеря смысла жизни)',
            'Анестетическая мотивация (невыносимость страдания) ',
            'Инструментальная мотивация (манипуляция другими) ',
            'Аутопунитическая мотивация (самонаказание) ',
            'Гетеропунитическая мотивация (наказание других) ',
            'Поствитальная мотивация (надежда на что-то лучшее после смерти).'
        ]

    # 0% -  20%  низкий показатель;
    # 21% -  40%  пониженный показатель;
    # 41% -  60%  средний показатель;
    # 61% -  80%  повышенный показатель;
    # 81% - 100%  высокий показатель.

    def get_procent_value(self):
        max_value = 15
        max_precent = 100
        for x in self.raw_result:
            self.result.append((x * max_precent) / max_value)

    def humanize_result(self):
        humonize = []
        for index, x in enumerate(self.result):
            humonize.append({
                'Scale': self.scale[index],
                'ScaleValue': self.result[index],
                'RawValue': self.raw_result[index],
            })
        return humonize

    def results(self):
        return [x for x in self.result]

    def process_answer(self, answer):
        for keys in self.suicidal_keys:
            scale_answer = 0
            for check_index in keys:
                ans = answer[check_index]['answer']
                if ans == 1:
                    scale_answer += 3
                if ans == 0.75:
                    scale_answer += 2
                if ans == 0.25:
                    scale_answer += 1
                if ans == 0:
                    scale_answer += 0

            self.raw_result.append(scale_answer)
        self.get_procent_value()
