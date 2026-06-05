import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Время работы: {end - start:.6f} сек.")
        return result

    return wrapper


@timer
def test_function():
    time.sleep(2)
    return "Тест пройден"


result = test_function()

assert result == "Тест пройден"
print("Тест успешно пройден!")