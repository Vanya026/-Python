#todo 1: создайте модуль serializer
import pickle
import json
import yaml

# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
def to_pickle(obj, file):
    pass
    with open(file, 'wb') as fd:
        pickle.dump(obj, fd, pickle.HIGHEST_PROTOCOL)
    
    # ваш код

#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
def to_json(obj, file):
    pass
    with open(file, 'wt') as fd:
        json.dump(obj, fd, indent=4)

    # ваш код

# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
def to_yaml(obj, file):
    pass
    with open(file, 'wt') as fd:
        yaml.dump(obj, file, indent=4)

    # ваш код


#todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    pass
    with open(file, 'wd') as fd:
        return pickle.load(fd)
    
    # ваш код

# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    pass
    with open(file, 'rt') as fd:
        return json.load(fd)
    
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    pass
    with open(file, 'rt')as fd:
        return yaml.load(fd)
    
    # ваш код

#todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.

from serdes import serializer, deserializer
serializer.to_yaml(1, 2)
deserializer.from_yaml(1, 2)