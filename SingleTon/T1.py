class Singleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Создаём экземпляр
singleton1 = Singleton.getInstance()

# Пытаемся создать другой экземпляр
singleton2 = Singleton.getInstance()

# Проверяем, что оба "экземпляра" на самом деле один и тот же объект
assert singleton1 is singleton2  # Это один и тот же объект
print(hash(singleton1), hash(singleton2))  # Хеши будут одинаковыми
