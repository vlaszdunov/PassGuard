import cutie
from tabulate import tabulate


class Additional:
    """
    Вспомогательный класс.
    Служит для упрощения кода
    """
    def Confirmation(Question: str, ConfirmText: str = 'Да', RejectText: str = 'Нет') -> bool:
        """
        Запрос подтверждения

        Args:
            Question (str): Вопрос;
            ConfirmText (str): Текст для кнопки подтверждения.
                По умолчанию: "Да";
            RejectText (str): Текст для кнопки отмены.
                По умолчанию: "Нет;

        Returns:
            (bool) Булевое значение True или False
        """
        return cutie.prompt_yes_or_no(Question, yes_text=ConfirmText, no_text=RejectText, char_prompt=False, default_is_yes=True)

    def Select(Data: list, AdditionalElements: list = [], NonSelectableItems: list = []) -> int:
        """
        Выбор из списка

        Args:
            Data (list): Набор данных;
            AdditionalElements (list): Дополнительные элементы для выбора.
                Предназначен для элементов, не входящих в список Data;
            NonSelectableItems (list): Список индексов дополнительного набора данных,
            которые не должны иметь возможности выбора

        Return:
            (int): Индекс выбранного элемента из списка Data, включая дополнительные элементы;
        """
        Data.extend(AdditionalElements)
        return cutie.select(Data, caption_indices=NonSelectableItems)

    def CreateTable(Data: dict):
        """Создание и вывод данных в виде таблицы
        
        Args:
            Data (dict): Набор данных в виде словаря

        Returns:
            Данные в виде таблицы
        """
        Data = [list(Data.values())]
        print('\n'+tabulate(Data, headers=['Id', 'Сайт',
              'Логин', 'Пароль'], tablefmt='rounded_grid')+'\n')