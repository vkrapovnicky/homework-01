# Homework-01

Использовал Google AI mode для отправки сообщения по SMTP. Он справился с первого раза. Мог сделать это через Cursor, но старался писать код самостоятельно, чтобы чему-нибудь научиться

Установка и запуск командами:
```bash
$ pip install -e .
Obtaining file:///home/vkrapovnicky/Work/homework-01
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: homework
  Building editable for homework (pyproject.toml) ... done
  Created wheel for homework: filename=homework-0.1.0-0.editable-py3-none-any.whl size=1192 sha256=42ea66389d82f95e3ca5e97728b863fc20af9acdeb8f28951b773571f2a89490
  Stored in directory: /tmp/pip-ephem-wheel-cache-24gbfy0g/wheels/04/fb/cf/024ccdd0d1b28db7dab060c5e2dac4cf2b44c06a182d0eab78
Successfully built homework
Installing collected packages: homework
  Attempting uninstall: homework
    Found existing installation: homework 0.1.0
    Uninstalling homework-0.1.0:
      Successfully uninstalled homework-0.1.0
Successfully installed homework-0.1.0
$ python src/homework/main.py 
1 <class 'int'>
1.0 <class 'float'>
True <class 'bool'>
hse <class 'str'>
['hse'] <class 'list'>
('hse',) <class 'tuple'>
{'hse'} <class 'set'>
{'hse': 'mag'} <class 'dict'>
Message sent successfully
```

Запуск тестов:
```bash
$ pytest -q -v
====================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/vkrapovnicky/Work/homework-01
configfile: pyproject.toml
collected 1 item                                                                                                                                                                                                                

tests/test_main.py .                                                                                                                                                                                                      [100%]

======================================================================================================= 1 passed in 0.04s =======================================================================================================
```