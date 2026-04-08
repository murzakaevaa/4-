from typing import List, Optional
import re


# FIX_ME: добавлены две пустые строки между импортами и первым классом
# старый код: после импортов не было пустых строк
# новый код: добавлена одна пустая строка после импортов и две перед классом

class PersonName:
    # FIX_ME: длинная строка параметров разбита на несколько строк
    # старый код: def __init__(self, surname: Optional[str] = None, first_name: Optional[str] = None, patronymic: Optional[str] = None):
    def __init__(self, surname: Optional[str] = None,
                 first_name: Optional[str] = None,
                 patronymic: Optional[str] = None):
        self._surname = surname.strip() if surname and surname.strip() else None
        # FIX_ME: длинная строка разбита с использованием обратного слеша
        # старый код: self._first_name = first_name.strip() if first_name and first_name.strip() else None
        self._first_name = first_name.strip() if first_name and first_name.strip() \
            else None
        # FIX_ME: длинная строка разбита с использованием обратного слеша
        # старый код: self._patronymic = patronymic.strip() if patronymic and patronymic.strip() else None
        self._patronymic = patronymic.strip() if patronymic and patronymic.strip()\
            else None

    @property
    def surname(self) -> Optional[str]:
        return self._surname

    @surname.setter
    def surname(self, value: Optional[str]):
        self._surname = value.strip() if value and value.strip() else None

    @property
    def first_name(self) -> Optional[str]:
        return self._first_name

    @first_name.setter
    def first_name(self, value: Optional[str]):
        self._first_name = value.strip() if value and value.strip() else None

    @property
    def patronymic(self) -> Optional[str]:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value: Optional[str]):
        self._patronymic = value.strip() if value and value.strip() else None

    def __str__(self) -> str:
        parts = []
        if self._surname:
            parts.append(self._surname)
        if self._first_name:
            parts.append(self._first_name)
        if self._patronymic:
            parts.append(self._patronymic)
        return " ".join(parts) if parts else "Не указано"


# FIX_ME: добавлены две пустые строки между классами
# старый код: одна пустая строка между классами PersonName и Time
# новый код: две пустые строки

class Time:
    # FIX_ME: длинная строка параметров разбита на несколько строк
    # старый код: def __init__(self, seconds: int = 0, hours: int = 0, minutes: int = 0, seconds_part: int = 0):
    def __init__(self, seconds: int = 0,
                 hours: int = 0,
                 minutes: int = 0,
                 seconds_part: int = 0):
        if seconds > 0:
            self._total_seconds = seconds % 86400
        else:
            # FIX_ME: длинная строка разбита с использованием круглых скобок
            # старый код: self._total_seconds = (hours * 3600 + minutes * 60 + seconds_part) % 86400
            self._total_seconds = ((hours * 3600 + minutes * 60 + seconds_part)
                                   % 86400)

    @property
    def total_seconds(self) -> int:
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, value: int):
        self._total_seconds = value % 86400 if value >= 0 else 0

    @property
    def hours(self) -> int:
        return self._total_seconds // 3600

    @property
    def minutes(self) -> int:
        return (self._total_seconds % 3600) // 60

    @property
    def seconds(self) -> int:
        return self._total_seconds % 60

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes:02d}:{self.seconds:02d}"


# FIX_ME: добавлены две пустые строки между классами
# старый код: одна пустая строка между классами Time и Department
# новый код: две пустые строки

class Department:
    def __init__(self, name: str):
        self._name = name
        self._head = None
        self._employees = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def employees(self) -> List['Employee']:
        return self._employees.copy()

    def add_employee(self, employee: 'Employee'):
        if employee not in self._employees:
            self._employees.append(employee)
            employee.department = self

    # FIX_ME: длинная строка разбита на две строки через переменную
    # старый код: return f"Отдел: {self._name}, Начальник: {self._head.name if self._head else 'Не назначен'}"
    def __str__(self) -> str:
        head_name = self._head.name if self._head else 'Не назначен'
        return f"Отдел: {self._name}, Начальник: {head_name}"


# FIX_ME: добавлены две пустые строки между классами
# старый код: одна пустая строка между классами Department и Employee
# новый код: две пустые строки

class Employee:
    # FIX_ME: длинная строка параметров разбита на две строки
    # старый код: def __init__(self, name: PersonName, department: Optional[Department] = None):
    def __init__(self, name: PersonName,
                 department: Optional[Department] = None):
        self._name = name
        self._department = None
        if department:
            department.add_employee(self)

    @property
    def name(self) -> PersonName:
        return self._name

    @name.setter
    def name(self, value: PersonName):
        self._name = value

    @property
    def department(self) -> Optional[Department]:
        return self._department

    @department.setter
    def department(self, value: Optional[Department]):
        self._department = value

    def is_department_head(self) -> bool:
        return self._department is not None and self._department.head == self

    def get_department_employees(self) -> List['Employee']:
        return self._department.employees if self._department else []

    # FIX_ME: длинная строка разбита на несколько строк
    # старый код: return f"{self._name} работает в отделе {self._department.name}, начальник которого {self._department.head.name}"
    def __str__(self) -> str:
        if self.is_department_head():
            return f"{self._name} начальник отдела {self._department.name}"

        return (
            f"{self._name} работает в отделе {self._department.name}, "
            f"начальник которого {self._department.head.name}"
        )


# FIX_ME: добавлены две пустые строки между классами
# старый код: одна пустая строка между классами Employee и ExtendedTime
# новый код: две пустые строки

class ExtendedTime(Time):
    # FIX_ME: длинная строка параметров разбита на несколько строк
    # старый код: def __init__(self, seconds: int = 0, hours: int = 0, minutes: int = 0, seconds_part: int = 0):
    def __init__(self,
                 seconds: int = 0,
                 hours: int = 0,
                 minutes: int = 0,
                 seconds_part: int = 0):
        super().__init__(seconds, hours, minutes, seconds_part)

    def get_current_hour(self) -> int:
        return self.hours

    def get_minutes_since_hour(self) -> int:
        return self.minutes

    def get_seconds_since_minute(self) -> int:
        return self.seconds


# FIX_ME: добавлены две пустые строки между классом и функцией
# старый код: одна пустая строка между ExtendedTime и validate_positive_int
# новый код: две пустые строки

def validate_positive_int(prompt: str) -> int:
    """
    Проверка ввода положительного целого числа.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Ошибка! Введите неотрицательное число.")
        except ValueError:
            print("Ошибка! Введите целое число.")


# FIX_ME: добавлены две пустые строки между функциями
# старый код: одна пустая строка между validate_positive_int и validate_name_part
# новый код: две пустые строки

def validate_name_part(prompt: str) -> Optional[str]:
    """
    Ввод части имени с проверкой, что нет цифр.
    """
    while True:
        value = input(prompt).strip()
        if not value:
            return None

        # Проверяем, есть ли цифры в строке
        if re.search(r'\d', value):
            print("Ошибка! Имя не может содержать цифры. Попробуйте снова.")
            continue

        # Проверяем, что строка состоит только из букв, дефисов и пробелов
        if not re.match(r'^[а-яА-Яa-zA-Z\s\-]+$', value):
            # FIX_ME: длинная строка разбита на несколько строк
            # старый код: print("Ошибка! Имя может содержать только буквы, дефисы и пробелы. Попробуйте снова.")
            # новый код: сообщение разбито на две строки
            print(
                "Ошибка! Имя может содержать только буквы, "
                "дефисы и пробелы. Попробуйте снова."
            )
            continue

        return value


# FIX_ME: добавлены две пустые строки между функцией и main
# старый код: одна пустая строка между validate_name_part и main
# новый код: две пустые строки

def main():
    print("=== ЗАДАЧА 1: СУЩНОСТЬ ИМЯ ===\n")

    cleopatra = PersonName(first_name="Клеопатра")
    pushkin = PersonName("Пушкин", "Александр", "Сергеевич")
    mayakovsky = PersonName("Маяковский", "Владимир")

    print(f"Клеопатра: {cleopatra}")
    print(f"Пушкин: {pushkin}")
    print(f"Маяковский: {mayakovsky}")

    print("\n=== ЗАДАЧА 2: СУЩНОСТЬ ВРЕМЯ ===\n")

    time1 = Time(seconds=10)
    time2 = Time(seconds=10000)
    time3 = Time(seconds=100000)

    print(f"10 секунд: {time1}")
    print(f"10000 секунд: {time2}")
    print(f"100000 секунд: {time3}")

    print("\n=== ЗАДАЧА 3: СОТРУДНИКИ И ОТДЕЛЫ ===\n")

    it_department = Department("IT")

    petrov = Employee(PersonName("Петров"), it_department)
    kozlov = Employee(PersonName("Козлов"), it_department)
    sidorov = Employee(PersonName("Сидоров"), it_department)

    it_department.head = kozlov

    print(petrov)
    print(kozlov)
    print(sidorov)

    print("\n=== ЗАДАЧА 4: СПИСОК СОТРУДНИКОВ ОТДЕЛА ===\n")

    print(f"Сотрудники отдела {it_department.name}:")
    for emp in sidorov.get_department_employees():
        print(f"- {emp.name}")

    print("\n=== ЗАДАЧА 5: СОЗДАЕМ ВРЕМЯ (РАСШИРЕННОЕ) ===\n")

    ext_time1 = ExtendedTime(seconds=10000)
    ext_time2 = ExtendedTime(hours=2, minutes=3, seconds_part=5)

    print(f"10000 секунд: {ext_time1}")
    print(f"2 часа, 3 минуты, 5 секунд: {ext_time2}")

    print("\n=== ЗАДАЧА 6: СКОЛЬКО СЕЙЧАС ВРЕМЕНИ? ===\n")

    time34056 = 34056
    time4532 = 4532
    time123 = 123

    time34056_obj = ExtendedTime(seconds=time34056)
    time4532_obj = ExtendedTime(seconds=time4532)
    time123_obj = ExtendedTime(seconds=time123)

    # FIX_ME: длинные строки разбиты на несколько строк
    # старый код: print(f"Времени {time34056} секунд соответствует {time34056_obj.get_current_hour()} часов")
    print(
        f"Времени {time34056} секунд соответствует "
        f"{time34056_obj.get_current_hour()} часов"
    )
    # FIX_ME: длинные строки разбиты на несколько строк
    # старый код: print(f"Времени {time4532} секунд соответствует {time4532_obj.get_minutes_since_hour()} минут")
    print(
        f"Времени {time4532} секунд соответствует "
        f"{time4532_obj.get_minutes_since_hour()} минут"
    )
    # FIX_ME: длинные строки разбиты на несколько строк
    # старый код: print(f"Времени {time123} секунд соответствует {time123_obj.get_seconds_since_minute()} секунд")
    print(
        f"Времени {time123} секунд соответствует "
        f"{time123_obj.get_seconds_since_minute()} секунд"
    )

    print("\n=== ДЕМОНСТРАЦИЯ ПРОВЕРКИ ВВОДА ===\n")
    print("Введите время в секундах для демонстрации проверки ввода:")
    seconds = validate_positive_int("> ")

    custom_time = ExtendedTime(seconds=seconds)
    print(f"Введенное время: {custom_time}")
    print(f"Часы: {custom_time.get_current_hour()}")
    print(f"Минуты: {custom_time.get_minutes_since_hour()}")
    print(f"Секунды: {custom_time.get_seconds_since_minute()}")

    print("\n=== ДОБАВЛЕНИЕ НОВОГО СОТРУДНИКА В ОТДЕЛ IT ===\n")

    print("Введите данные нового сотрудника")

    surname = validate_name_part("Фамилия: ")
    first_name = validate_name_part("Имя: ")
    patronymic = validate_name_part("Отчество: ")

    if not any([surname, first_name, patronymic]):
        print("Ошибка! Должно быть введено хотя бы одно поле (фамилия, имя или отчество).")
    else:
        new_employee_name = PersonName(surname, first_name, patronymic)
        new_employee = Employee(new_employee_name, it_department)

        print(f"\nНовый сотрудник успешно добавлен в отдел {it_department.name}!")
        print(f"Информация о сотруднике: {new_employee}")

        print(f"\nОбновлённый список сотрудников отдела {it_department.name}:")
        print(f"Начальник отдела: {it_department.head.name}")
        print("Сотрудники:")
        for i, emp in enumerate(it_department.employees, 1):
            if emp.is_department_head():
                print(f"  {i}. {emp.name}")
            else:
                print(f"  {i}. {emp.name}")

        print(f"\nВсего сотрудников в отделе: {len(it_department.employees)}")


if __name__ == "__main__":
    main()