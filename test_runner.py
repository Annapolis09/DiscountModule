import sys

if "--v1" in sys.argv:
    from discount_service_v1 import DiscountModule
    VERSION = "v1 (черновик, до исправлений)"
else:
    from discount_service import DiscountModule
    VERSION = "финальная (discount_service.py)"



TEST_CASES = [
    ("TC-01", "Позитивный", "Действующий билет",               "12345678",   True,  15),
    ("TC-02", "Позитивный", "Другой действующий билет",        "87654321",   True,  15),
    ("TC-03", "Позитивный", "Номер передан числом",            12345678,     True,  15),
    ("TC-04", "Позитивный", "Пробелы по краям",                " 20240001 ", True,  15),
    ("TC-05", "Позитивный", "Ведущие нули в номере",           "00123456",   True,  15),

    ("TC-06", "Отказ",      "Билета нет в реестре",            "99999999",   False, 0),
    ("TC-07", "Отказ",      "Билет просрочен",                 "11111111",   False, 0),

    ("TC-08", "Негативный", "Текст вместо цифр",               "ABC-123",    False, 0),
    ("TC-09", "Негативный", "Пустая строка",                   "",           False, 0),
    ("TC-10", "Негативный", "None (номер не передан)",         None,         False, 0),
    ("TC-11", "Негативный", "Слишком короткий номер",          "1234",       False, 0),
    ("TC-12", "Негативный", "Очень длинная строка (1000 цифр)", "1" * 1000,  False, 0),
    ("TC-13", "Негативный", "Отрицательное число",             -12345678,    False, 0),
    ("TC-14", "Негативный", "Дробное число",                   12345678.9,   False, 0),
    ("TC-15", "Негативный", "Список вместо номера",            ["12345678"], False, 0),
    ("TC-16", "Негативный", "Логическое значение True",        True,         False, 0),
    ("TC-17", "Негативный", "Спецсимволы / инъекция",          "1234'; --",  False, 0),
]

def run_tests():
    module = DiscountModule()
    passed, failed = 0, []

    print(f"Тестируемая версия: {VERSION}\n")
    print(f"{'ID':<6} {'Группа':<11} {'Описание':<34} {'Итог':<5} Фактический результат")
    print("-" * 110)

    for case_id, group, title, data, exp_success, exp_percent in TEST_CASES:
        try:
            result = module.apply_student_discount(data)
            ok = (result["success"] == exp_success
                  and result["discount_percent"] == exp_percent)
            actual = f"{result['discount_percent']}% — {result['message']}"
        except Exception as error:
            ok = False
            actual = f"ПАДЕНИЕ: {type(error).__name__}: {error}"

        status = "PASS" if ok else "FAIL"
        print(f"{case_id:<6} {group:<11} {title:<34} {status:<5} {actual[:80]}")

        if ok:
            passed += 1
        else:
            failed.append(case_id)

    print("-" * 110)
    print(f"Итого: {len(TEST_CASES)} тестов, пройдено {passed}, провалено {len(failed)}")
    if failed:
        print("Провалены:", ", ".join(failed))
    return not failed


if __name__ == "__main__":
    sys.exit(0 if run_tests() else 1)
