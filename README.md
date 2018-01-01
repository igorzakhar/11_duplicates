# Анти-Дупликатор

Скрипт ищет дублирующие файлы в указанной директории, при этом рекурсивно обходит все вложенные. Результат выводитится на стандартный вывод.
Дублирующие файлы – это два файла с одинаковым именем и размером.

# Как использовать

Скрипт принимает на вход путь до директории и проверяет является ли указанный путь директорией. 

Пример запуска в Linux, Python 3.5:
```#!bash
$ python duplicates.py <path>
```
Пример вывода результатов:

```#!bash
Filename: Default (Linux).sublime-keymap / size 4204 bytes / checksum 4531bec0288f08d9623c6408c2be7aa2
--------------------------------------------------
/home/user/Files/Default (Linux).sublime-keymap
/home/user/Files/Temp/Default (Linux).sublime-keymap
-------------------------------------------------- 

Filename: sublime-text_build-3083_amd64.deb / size 6334076 bytes / checksum 4531bec0288f08d9623c6408c2be7aa2
--------------------------------------------------
/home/user/Files/sublime-text_build-3083_amd64.deb
/home/user/Files/Temp/sublime-text_build-3083_amd64.deb
-------------------------------------------------- 
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
