from random import *


word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
            'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец',
            'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец',
            'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон', 'война',
            'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья',
            'число', 'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство',
            'начало', 'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица', 'вечер',
            'качество', 'мысль', 'дорога', 'мать', 'действие', 'месяц', 'государство', 'язык', 'любовь', 'взгляд',
            'мама', 'век', 'школа', 'цель', 'общество', 'деятельность', 'организация', 'президент', 'комната',
            'порядок', 'момент', 'театр', 'письмо', 'утро', 'помощь', 'ситуация', 'роль', 'рубль', 'смысл', 'состояние',
            'квартира', 'орган', 'внимание', 'тело', 'труд', 'сын', 'мера', 'смерть', 'рынок', 'программа', 'задача',
            'предприятие', 'окно', 'разговор', 'правительство', 'семья', 'производство', 'информация', 'положение',
            'центр', 'ответ', 'муж', 'автор', 'стена', 'интерес', 'федерация', 'правило', 'управление', 'мужчина',
            'идея', 'партия', 'совет', 'счет', 'сердце', 'движение', 'вещь', 'материал', 'неделя', 'чувство', 'глава',
            'наука', 'ряд', 'газета', 'причина', 'плечо', 'цена', 'план', 'речь', 'точка', 'основа', 'товарищ',
            'культура', 'данные', 'мнение', 'документ', 'институт', 'ход', 'проект', 'встреча', 'директор', 'срок',
            'палец', 'опыт', 'служба', 'судьба', 'девушка', 'очередь', 'лес', 'состав', 'член', 'количество', 'событие',
            'объект', 'зал', 'создание', 'значение', 'период', 'шаг', 'брат', 'искусство', 'структура', 'номер',
            'пример', 'исследование', 'гражданин', 'игра', 'начальник', 'рост', 'тема', 'принцип', 'метод', 'тип',
            'фильм', 'край', 'гость', 'воздух', 'характер', 'борьба', 'использование', 'размер', 'образование',
            'мальчик', 'кровь', 'район', 'небо', 'армия', 'класс', 'представитель', 'участие', 'девочка', 'политика',
            'герой', 'картина', 'доллар', 'спина', 'территория', 'пол', 'поле', 'изменение', 'направление', 'рисунок',
            'течение', 'церковь', 'банк', 'сцена', 'население', 'большинство', 'музыка', 'правда', 'свобода', 'память',
            'команда', 'союз', 'врач', 'договор', 'дерево', 'факт', 'хозяин', 'природа', 'угол', 'телефон', 'позиция',
            'двор', 'писатель', 'самолет', 'объем', 'род', 'солнце', 'вера', 'берег', 'спектакль', 'фирма', 'способ',
            'завод', 'цвет', 'журнал', 'руководитель', 'специалист', 'оценка', 'регион', 'песня', 'процент', 'родитель',
            'море', 'требование', 'основание', 'половина', 'роман', 'круг', 'анализ', 'стихи', 'автомобиль',
            'экономика', 'литература', 'бумага', 'поэт', 'степень', 'господин', 'надежда', 'предмет', 'вариант',
            'министр', 'граница', 'дух', 'модель', 'операция', 'пара', 'сон', 'название', 'ум', 'повод', 'старик',
            'миллион', 'успех', 'счастье', 'ребята', 'кабинет', 'магазин', 'пространство', 'выход', 'удар', 'база',
            'знание', 'текст', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник', 'участок',
            'пункт', 'линия', 'желание', 'папа', 'доктор', 'губа', 'дочь', 'среда', 'председатель', 'представление',
            'солдат', 'художник', 'волос', 'оружие', 'соответствие', 'ветер', 'парень', 'зрение', 'генерал', 'огонь',
            'понятие', 'строительство', 'ухо', 'грудь', 'нос', 'страх', 'услуга', 'содержание', 'радость',
            'безопасность', 'продукт', 'комплекс', 'бизнес', 'сад', 'сотрудник', 'лето', 'курс', 'предложение', 'рот',
            'технология', 'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'река',
            'продукция', 'сумма', 'техника', 'здание', 'сфера', 'необходимость', 'фонд', 'подготовка', 'лист',
            'республика', 'хозяйство', 'воля', 'бюджет', 'снег', 'деревня', 'мужик', 'элемент', 'обстоятельство',
            'немец', 'победа', 'источник', 'звезда', 'выбор', 'масса', 'итог', 'сестра', 'практика', 'проведение',
            'карман', 'слава', 'кухня', 'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан',
            'работник', 'обеспечение', 'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'бой', 'теория',
            'зона', 'отдел', 'зуб', 'разработка', 'личность', 'гора', 'товар', 'метр', 'праздник', 'влияние',
            'читатель', 'удовольствие', 'актер', 'слеза', 'ответственность', 'учитель', 'акт', 'боль', 'множество',
            'особенность', 'показатель', 'корабль', 'звук', 'впечатление', 'частность', 'детство', 'вывод', 'профессор',
            'доля', 'норма', 'прошлое', 'командир', 'коридор', 'поддержка', 'рамка', 'враг', 'этап', 'черт', 'дед',
            'собрание', 'прием', 'болезнь', 'клетка', 'кожа', 'заявление', 'попытка', 'сравнение', 'расчет', 'депутат',
            'комитет', 'знак', 'дядя', 'учет', 'хлеб', 'чай', 'режим', 'целое', 'вирус', 'выражение', 'здоровье',
            'зима', 'десяток', 'глубина', 'сеть', 'студент', 'секунда', 'скорость', 'поиск', 'суть', 'налог', 'ошибка',
            'доход', 'режиссер', 'поверхность', 'ощущение', 'карта', 'клуб', 'станция', 'революция', 'колено',
            'министерство', 'стекло', 'этаж', 'высота', 'бабушка', 'трубка', 'газ', 'мастер', 'поведение', 'столица',
            'механизм', 'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'кино',
            'сожаление', 'заместитель', 'ресурс', 'акция', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист',
            'сосед', 'фраза', 'фигура', 'субъект', 'реакция', 'список', 'фотография', 'журналист', 'май', 'нарушение',
            'заседание', 'толпа', 'больница', 'существо', 'свойство', 'долг', 'поколение', 'животное', 'схема',
            'усилие', 'отличие', 'остров', 'противник', 'волна', 'реализация', 'страница', 'формирование', 'житель',
            'красота', 'птица', 'растение', 'тень', 'явление', 'храм', 'запах', 'водка', 'наличие', 'ужас', 'одежда',
            'кресло', 'больной', 'поезд', 'университет', 'традиция', 'адрес', 'декабрь', 'ладонь', 'сведение', 'цветок',
            'лидер', 'октябрь', 'занятие', 'сентябрь', 'помещение', 'январь', 'зритель', 'редакция', 'стиль', 'весна',
            'фактор', 'август', 'известие', 'зависимость', 'охрана', 'оборудование', 'концерт', 'отделение', 'расход',
            'выставка', 'милиция', 'переход', 'эпоха', 'запад', 'произведение', 'родина', 'собственность', 'тайна',
            'трава', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'март', 'клиент', 'дама', 'фронт',
            'отрасль', 'стул', 'беседа', 'законодательство', 'продажа', 'повышение', 'музей', 'след', 'полковник',
            'сомнение', 'понимание', 'апрель', 'князь', 'рыба', 'дума', 'кодекс', 'сутки', 'чудо', 'шея', 'судья',
            'крыша', 'настроение', 'поток', 'должность', 'преступление', 'мозг', 'честь', 'пост', 'еврей', 'июнь',
            'сотня', 'дождь', 'лестница', 'дача', 'установка', 'появление', 'получение', 'образец', 'труба', 'главное',
            'осень', 'костюм', 'баба', 'ценность', 'обязанность', 'пьеса', 'таблица', 'вино', 'воспоминание', 'лошадь',
            'коллега', 'организм', 'ученик', 'учреждение', 'открытие', 'том', 'черта', 'характеристика', 'выполнение',
            'оборона', 'выступление', 'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан',
            'километр', 'спор', 'вкус', 'признак', 'промышленность', 'американец', 'лоб', 'заключение', 'восток',
            'исключение', 'ключ', 'постановление', 'слой', 'бок', 'июль', 'перевод', 'секретарь', 'кусок', 'слух',
            'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина', 'зарплата',
            'билет', 'подарок', 'тюрьма', 'ящик', 'конкурс', 'книжка', 'изучение', 'просьба', 'царь', 'публика', 'смех',
            'сообщение', 'угроза', 'беда', 'блок', 'достижение', 'назначение', 'реклама', 'портрет', 'масло', 'стакан',
            'урок', 'часы', 'крик', 'творчество', 'телевизор', 'инструмент', 'концепция', 'лейтенант', 'экран', 'дно',
            'реальность', 'канал', 'мясо', 'знакомый', 'щека', 'конфликт', 'переговоры', 'запись', 'вагон', 'площадка',
            'последствие', 'сотрудничество', 'зеркало', 'тон', 'академия', 'палата', 'потребность', 'ноябрь',
            'увеличение', 'дурак', 'поездка', 'обед', 'потеря', 'февраль', 'мероприятие', 'парк', 'принятие',
            'устройство', 'вещество', 'категория', 'сезон', 'гостиница', 'издание', 'объединение', 'темнота',
            'человечество', 'колесо', 'опасность', 'разрешение', 'воздействие', 'коллектив', 'камера', 'запас',
            'следствие', 'длина', 'крыло', 'округ', 'фон', 'кандидат', 'родственник', 'давление', 'присутствие',
            'взаимодействие', 'доска', 'партнер', 'двигатель', 'шум', 'достоинство', 'грех', 'нож', 'полет', 'страсть',
            'испытание', 'истина', 'оплата', 'разница', 'водитель', 'пакет', 'снижение', 'формула', 'живот', 'капитал',
            'мост', 'новость', 'эффект', 'вход', 'губернатор', 'доклад', 'смена', 'убийство', 'эксперт', 'автобус',
            'платье', 'кадр', 'тетя', 'общение', 'психология', 'лев', 'порог', 'проверка', 'процедура', 'рабочий',
            'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'буква',
            'доказательство', 'признание', 'постель', 'штаб', 'владелец', 'компьютер', 'инженер', 'старуха', 'лодка',
            'ракета', 'серия', 'шутка', 'вершина', 'выпуск', 'кулак', 'лед', 'торговля', 'нефть', 'молодежь', 'цифра',
            'корпус', 'недостаток', 'сапог', 'сущность', 'талант', 'эффективность', 'кофе', 'полоса', 'основное',
            'рассмотрение', 'сбор', 'штат', 'следователь', 'жилье', 'мешок', 'описание', 'куст', 'отказ', 'замок',
            'редактор', 'дворец', 'забота', 'пиво', 'диван', 'столик', 'эксперимент', 'печать', 'кольцо', 'пистолет',
            'воспитание', 'начальство', 'профессия', 'ворота', 'добро', 'дружба', 'покой', 'риск', 'окончание', 'дым',
            'брак', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кость', 'спорт', 'кредит', 'господь',
            'майор', 'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'отдых', 'ручка', 'металл',
            'молоко', 'прокурор', 'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'мечта', 'село', 'еда',
            'зло', 'подразделение', 'сюжет', 'рубеж', 'сигнал', 'атмосфера', 'крест', 'вес', 'взрыв', 'контакт',
            'сигарета', 'восторг', 'золото', 'почва', 'премия', 'король', 'подъезд', 'шанс', 'автомат', 'заказ',
            'мальчишка', 'очки', 'миг', 'штука', 'чтение', 'поселок', 'свидетель', 'ставка', 'сумка', 'удивление',
            'хвост', 'песок', 'поворот', 'возвращение', 'мгновение', 'статус', 'озеро', 'строй', 'параметр', 'сказка',
            'тенденция', 'вина', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'дочка', 'танец',
            'эксплуатация', 'коммунист', 'пенсия', 'приятель', 'объяснение', 'набор', 'производитель', 'пыль',
            'философия', 'мощность', 'обязательство', 'уход', 'горло', 'кризис', 'указание', 'плата', 'яблоко',
            'препарат', 'действительность', 'москвич', 'остаток', 'изображение', 'сделка', 'сочинение',
            'покупатель', 'танк', 'затрата', 'строка', 'единица']
guessed_words = []

def get_word():
    word = choice(word_list).upper()
    if word in guessed_words:
        word_list.remove(word)
        return get_word()
    return word


def display_hangman(tries, hangman):

    if tries == 6:
        return hangman
    elif tries == 0:
        hangman = hangman[:869] + '$$' + hangman[871:]
        hangman = hangman[:930] + '$$' + hangman[932:]
        hangman = hangman[:990] + '$$' + hangman[992:]
        hangman = hangman[:1050] + '$$' + hangman[1052:]
        hangman = hangman[:1110] + '$$' + hangman[1112:]
        return hangman
    elif tries == 1:
        hangman = hangman[:866] + '$$' + hangman[868:]
        hangman = hangman[:925] + '$$' + hangman[927:]
        hangman = hangman[:985] + '$$' + hangman[987:]
        hangman = hangman[:1045] + '$$' + hangman[1047:]
        hangman = hangman[:1105] + '$$' + hangman[1107:]
        return hangman
    elif tries == 2:
        hangman = hangman[:571] + '$' + hangman[572:]
        hangman = hangman[:631] + '$$' + hangman[633:]
        hangman = hangman[:692] + '$' + hangman[693:]
        hangman = hangman[:752] + '$' + hangman[753:]
        hangman = hangman[:812] + '$' + hangman[813:]
        return hangman

    elif tries == 3:
        hangman = hangman[:565] + '$' + hangman[566:]
        hangman = hangman[:624] + '$$' + hangman[626:]
        hangman = hangman[:684] + '$' + hangman[685:]
        hangman = hangman[:744] + '$' + hangman[745:]
        hangman = hangman[:804] + '$' + hangman[805:]
        return hangman
    elif tries == 4:
        hangman = hangman[:626] + '$$$$$' + hangman[631:]
        hangman = hangman[:686] + '$$$$$' + hangman[691:]
        hangman = hangman[:746] + '$$$$$' + hangman[751:]
        hangman = hangman[:806] + '$$$$$' + hangman[811:]
        return hangman
    elif tries == 5:
        hangman = hangman[:507] + '$$$' + hangman[510:]
        hangman = hangman[:446] + '$$$$$' + hangman[451:]
        hangman = hangman[:387] + '$$$' + hangman[390:]
        return hangman



def play(word):
    hangman = ''' 
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    ____ZZZZZ_________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                '''
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    tries = 6  # количество попыток
    print('Давайте играть в Угадайку слов!')
    temp = display_hangman(tries, hangman)
    print(temp)
    hangman = temp
    print(f'У вас есть {tries} попыток!')
    print(word_completion)
    print('Я загадал слово, попоробуйте его угадать! Назовите букву.')
    while True:
        letter = input('Введите букву: ')
        if letter.lower() in guessed_letters:
            print('Такая буква уже была, введите другую!')
        else:
            guessed_letters.append(letter.lower())
            if letter.isalpha() == False:
                print('Вы ввели не букву, повторите.')
            elif len(letter) > 1:
                print('Введите ОДНУ букву.')
            else:
                if letter.upper() in word.upper():
                    print('Да, такая буква есть!')
                    for j in range(len(word)):
                        if word[j].upper() == letter.upper():
                            word_completion = word_completion[:j] + letter + word_completion[j + 1:]
                    print(word_completion.upper())
                    if word_completion.isalpha() == True:
                        print('Поздравляю, вы победили и избежали повешения!')
                        guessed_words.append(word)
                        endgame = True
                        break
                else:
                    tries -= 1
                    temp = display_hangman(tries, hangman)
                    print(temp)
                    hangman = temp
                    if 1 < tries < 5:
                        print(f'К сожалению, такой буквы в слове нет. У вас осталось {tries} попытки.')
                        print(word_completion.upper())
                    elif tries == 1:
                        print(f'К сожалению, такой буквы в слове нет. У вас осталось {tries} попытка.')
                        print(word_completion.upper())
                    elif tries == 5:
                        print(f'К сожалению, такой буквы в слове нет. У вас осталось {tries} попыток.')
                        print(word_completion.upper())
                    elif tries == 0:
                        temp = display_hangman(tries, hangman)
                        print(temp)
                        print("К сожалению, вы проиграли. Не расстраивайтесь, в следующий раз повезёт!")
                        print(f'Слово было таким: {word}')
                        guessed_words.append(word)
                        endgame = True
                        break
    if endgame:
        while True:
            print('Хотите сыграть ещё раз? (Да/Нет)')
            answer2 = input().lower()
            if answer2 == 'да':
                print('Отлично!')
                play(get_word())
            elif answer2 == 'нет':
                print('Чтож, очень жаль. В таком случае до встречи!')
                return print('Спасибо за игру!')


            else:
                print('Я не понимаю, введите "да" или "нет"')






play(get_word())