Questions = """
Как вы оцениваете свое самочувствие?
Есть ли у вас хронические заболевания?
Это физическое недомогание?
Связанно недомогание именно с этой болезнью?
Можете Вы определить примерное место недомогания?
Имеется ли отягощенная наследственность (наличие болезней у кровных родственников)?
Место локализации
Были у Вас травмы больного места?
Были ли у Вас колебания веса более 2 кг за последний год без специальных усилий?
Замечаете ли Вы у себя ухудшение аппетита?
Вы высыпаетесь?
Есть ли у Вас приступы немотивированной слабости (т.е. ухудшение общего самочувствия без причины)?
ИМТ
Вы старше 45 лет?
Как давно наблюдается такое самочувствие?
Вам есть 35 полных лет?
У Вас удаляли аппендицит?
Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)
Есть ли гинекологические проблемы? (нарушение цикла, выделения из половых путей)
Пол
Возраст
Есть ли при этом подъем температуры/ покраснение в месте болевого синдрома?
"""

Locations = """
Боль в сердце
Боль во 2 сегменте живота*
Боль в 5 сегменте живота*
Боль в 1, 3 сегментах живота*
Боль в 4, 6, 8 сегментах живота*
Боль в 9 сегменте живота*
Боль в 7 сегменте живота*
Боль/Дисфункция/Патологические выделения молочных/грудных желез
Боль/Дисфункция/Патологические выделения ротовой полости
Боль в позвоночнике 
Болевой синдром в костях/суставах
Боль в шее
Боль за лопаткой
Боль между лопатками
Головные боли
Боль/Дисфункция/Патологические выделения зрительных органов
Боль/Дисфункция/Патологические выделения ушей/носа/горла
Пятна/высыпания на кожных покровах
Болевой синдром кожных покровов
Боль/Дисфункция в областях заднего прохода/копчика/ягодиц
Дисфункция/Дискомфорт/патологические выделения половых органов
"""

Solutions = """
Плановая диспансеризация
Обращение к терапевту с ОАК
Обращение к диетологу/корректировка питания. Корректировка физ. нагрузки
Обращение к онкологу с ОАК
Обращение к кардиологу с ЭКГ
Обращение к гастроэнтерологу с ОАК, УЗИ, ФГС
Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости, Анализ кала на скрытую кровь
Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости
Обращение к урологу с ОАК, ОАМ, УЗИ почек, мочевого пузыря
Обращение к гинекологу с ОАК
Обращение к маммологу
Обращение к урологу с ОАК, ОАМ, Анализ крови на PSA, УЗИ почек, мочевого пузыря, простаты
Обращение к маммологу с маммографией
Обращение к проктологу с ОАК
Обращение к ортопеду
Обращение к ревматологу
Обращение к стоматологу
Обращение к хирургу с ОАК
Обращение к неврологу с МРТ
Обращение к неврологу
Обращение к офтальмологу
Обращение к ЛОРу
Обращение к дерматологу
"""
relationships = [
    {"name": "constGood",
     "relationship": "Постоянно хорошее"
     },
    {"name": "constBad",
     "relationship": "Часто плохое самочувствие"
     },
    {"name": "phBad",
     "relationship": "Ухудшение самочувствия при нагрузках"
     },
    {"name": "yes",
     "relationship": "Да"
     },
    {"name": "no",
     "relationship": "Нет"
     },
    {"name": "cantExplain",
     "relationship": "Не могу объяснить"
     },
    {"name": "for1to3year",
     "relationship": "в течение 1-3 лет"
     },
    {"name": "more3year",
     "relationship": "более 3 лет"
     },
    {"name": "strongLow",
     "relationship": "сильно пониженный"
     },
    {"name": "low/high",
     "relationship": "повышенный/пониженный"
     },
    {"name": "yesWithChronicDiseases",
     "relationship": "Да, есть хронические заболевания"
     },
    {"name": "yesWithCancelDiseases",
     "relationship": "Да, есть онкологические заболевания"
     },
    {"name": "localization",
     "relationship": "Локализация"
     },
    {"name": "man",
     "relationship": "мужской"
     },
    {"name": "woman",
     "relationship": "женский"
     },
    {"name": "more45age",
     "relationship": "Старше 45"
     },
    {"name": "from18to45age",
     "relationship": "от 18 до 45"
     },
    {"name": "yesWithInjury",
     "relationship": "Да, после травмы"
     },
    {"name": "noWithMan",
     "relationship": "Нет, (мужской)"
     },
    {"name": "noWithWoman",
     "relationship": "Нет, (женский)"
     },
    {"name": "yesWithMan",
     "relationship": "Да, (мужской)"
     },
    {"name": "yesWithWoman",
     "relationship": "Да, (женский)"
     },
    {"name": "yesWithoutInjury",
     "relationship": "Да, без травмы"
     },
]

q2q_triplets = [
    ('Как вы оцениваете свое самочувствие?', 'Часто плохое самочувствие', 'Есть ли у вас хронические заболевания?'),
    ('Как вы оцениваете свое самочувствие?', 'Ухудшение самочувствия при нагрузках', 'Это физическое недомогание?'),
    ('Есть ли у вас хронические заболевания?', 'Да', 'Связанно недомогание именно с этой болезнью?'),
    ('Есть ли у вас хронические заболевания?', 'Нет', 'Имеется ли отягощенная наследственность (наличие болезней у кровных родственников)?'),
    ('Связанно недомогание именно с этой болезнью?', 'Да', 'Место локализации'),
    ('Связанно недомогание именно с этой болезнью?', 'Нет', 'Можете Вы определить примерное место недомогания?'),
    ('Боль в 4, 6, 8 сегментах живота* ', 'Да', 'Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)'),
    ('Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)', 'Нет, (женский)', 'Есть ли гинекологические проблемы? (нарушение цикла, выделения из половых путей)'),
    ('Пол', 'женский', 'Возраст'),
    ('Боль/Дисфункция/Патологические выделения молочных/грудных желез', 'Да', 'Пол'),
    ('Болевой синдром в костях/суставах', 'Да, без травмы', 'Есть ли при этом подъем температуры/ покраснение в месте болевого синдрома?'),
    ('Это физическое недомогание?', 'Да', 'Вы можете определить место боли/дискомфорта?'),
    ('Это физическое недомогание?', 'Нет', 'Были ли у Вас колебания веса более 2 кг за последний год без специальных усилий?'),
    ('Это физическое недомогание?', 'Не могу объяснить',
     'Как давно наблюдается такое самочувствие?'),
    ('Вы можете определить место боли/дискомфорта?', 'Да', 'Были у Вас травмы больного места?'),
    ('Вы можете определить место боли/дискомфорта?', 'Нет', 'Были ли у Вас колебания веса более 2 кг за последний год без специальных усилий?'),
    ('Были у Вас травмы больного места?', 'Нет',
     'Имеется ли отягощенная наследственность (наличие болезней у кровных родственников)?'),
    ('Имеется ли отягощенная наследственность (наличие болезней у кровных родственников)?', 'Да, есть хронические заболевания', 'Место локализации'),
    ('Можете Вы определить примерное место недомогания?', 'Да', 'Место локализации'),
    ('Были ли у Вас колебания веса более 2 кг за последний год без специальных усилий?', 'Да', 'Замечаете ли Вы у себя ухудшение аппетита?'),
    ('Были ли у Вас колебания веса более 2 кг за последний год без специальных усилий?', 'Нет', 'ИМТ'),
    ('Замечаете ли Вы у себя ухудшение аппетита?', 'Нет', 'ИМТ'),
    ('Замечаете ли Вы у себя ухудшение аппетита?', 'Да', 'Вы высыпаетесь?'),
    ('Вы высыпаетесь?', 'Нет', 'ИМТ'),
    ('Вы высыпаетесь?', 'Да', 'Есть ли у Вас приступы немотивированной слабости (т.е. ухудшение общего самочувствия без причины)?'),
    ('Есть ли у Вас приступы немотивированной слабости (т.е. ухудшение общего самочувствия без причины)?', 'Да', 'ИМТ'),
    ('Есть ли у Вас приступы немотивированной слабости (т.е. ухудшение общего самочувствия без причины)?', 'Нет', 'Место локализации'),
    ('Как давно наблюдается такое самочувствие?','в течение 1-3 лет', 'ИМТ'),
    ('Как давно наблюдается такое самочувствие?', 'более 3 лет', 'Место локализации'),
    ('ИМТ', 'сильно пониженный', 'Вы старше 45 лет?'),
    ('Боль в 9 сегменте живота*', 'Да', 'Вам есть 35 полных лет?'),
    ('Вам есть 35 полных лет?', 'Нет', 'Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)'),
    ('У Вас удаляли аппендицит?', 'Да', 'Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)'),
]

q2s_triplets = [
    ('Как вы оцениваете свое самочувствие?', 'Постоянно хорошее', 'Плановая диспансеризация'),
    ('Можете Вы определить примерное место недомогания?', 'Нет', 'Обращение к терапевту с ОАК'),
    ('Имеется ли отягощенная наследственность (наличие болезней у кровных родственников)?', 'Да, есть онкологические заболевания', 'Обращение к онкологу с ОАК'),
    ('Вы старше 45 лет?', 'Да', 'Обращение к онкологу с ОАК'),
    ('Вы старше 45 лет?', 'Нет', 'Обращение к диетологу/корректировка питания. Корректировка физ. нагрузки'),
    ('Боль в сердце', 'Да', 'Обращение к кардиологу с ЭКГ'),
    ('Боль во 2 сегменте живота*', 'Да', 'Обращение к гастроэнтерологу с ОАК, УЗИ, ФГС'),
    ('Боль в 5 сегменте живота*', 'Да', 'Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости, Анализ кала на скрытую кровь'),
    ('Боль в 1, 3 сегментах живота*', 'Да', 'Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости'),
    ('Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)', 'Нет, (мужской)', 'Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости'),
    ('Есть ли нарушение мочеиспускания? (болевой синдром, учащение или урежение, изменение цвета мочи)', 'Да', 'Обращение к урологу с ОАК, ОАМ, УЗИ почек, мочевого пузыря'),
    ('Есть ли гинекологические проблемы? (нарушение цикла, выделения из половых путей)', 'Нет', 'Обращение к гастроэнтерологу с ОАК, УЗИ брюшной полости'),
    ('Есть ли гинекологические проблемы? (нарушение цикла, выделения из половых путей)', 'Да', 'Обращение к гинекологу с ОАК'),
    ('Пол', 'мужской', 'Обращение к маммологу'),
    ('Возраст', 'от 18 до 45', 'Обращение к маммологу'),
    ('Возраст', 'Старше 45', 'Обращение к маммологу с маммографией'),
    ('Дисфункция/Дискомфорт/патологические выделения половых органов', 'Да, (мужской)', 'Обращение к урологу с ОАК, ОАМ, Анализ крови на PSA, УЗИ почек, мочевого пузыря, простаты'),
    ('Дисфункция/Дискомфорт/патологические выделения половых органов', 'Да, (женский)', 'Обращение к гинекологу с ОАК'),
    ('Боль/Дисфункция в областях заднего прохода/копчика/ягодиц', 'Да', 'Обращение к проктологу с ОАК'),
    ('Есть ли при этом подъем температуры/ покраснение в месте болевого синдрома?', 'Да', 'Обращение к ревматологу'),
    ('Есть ли при этом подъем температуры/ покраснение в месте болевого синдрома?', 'Нет', 'Обращение к ортопеду'),
    ('Боль/Дисфункция/Патологические выделения ротовой полости', 'Да', 'Обращение к стоматологу'),
    ('У Вас удаляли аппендицит?', 'Нет', 'Обращение к хирургу с ОАК'),
    ('Боль в позвоночнике', 'Да, после травмы', 'Обращение к хирургу с ОАК'),
    ('Болевой синдром в костях/суставах', 'Да, после травмы', 'Обращение к хирургу с ОАК'),
    ('Боль в шее', 'Да, после травмы', 'Обращение к хирургу с ОАК'),
    ('Были у Вас травмы больного места?', 'Да', 'Обращение к хирургу с ОАК'),
    ('Боль в позвоночнике', 'Да, без травмы', 'Обращение к неврологу с МРТ'),
    ('Боль в шее', 'Да, без травмы', 'Обращение к неврологу с МРТ'),
    ('Боль за лопаткой', 'Да', 'Обращение к неврологу'),
    ('Боль между лопатками', 'Да', 'Обращение к неврологу'),
    ('Головные боли', 'Да', 'Обращение к неврологу'),
    ('Боль/Дисфункция/Патологические выделения зрительных органов', 'Да', 'Обращение к офтальмологу'),
    ('Боль/Дисфункция/Патологические выделения ушей/носа/горла', 'Да', 'Обращение к ЛОРу'),
    ('Пятна/высыпания на кожных покровах', 'Да', 'Обращение к дерматологу'),
    ('Болевой синдром кожных покровов', 'Да', 'Обращение к дерматологу')


]





def getRelation(relationship):
    for rel in relationships:
        if relationship == rel['relationship']:
            return rel

    return {}