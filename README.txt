# my_first_jango_project
 Make my first project on Django

Команды терминала:
  pip3 list
  python3                     #откывает терминал под Python
  contol+d                    #zakryvaet Python
  python3 -m venv venv        #установка Виртуального пространства (второй 'venv' - название папки)
  source venv/bin/activate   #активация виртуального пространства
  deactivate                  #выход из ВП

  pip3 install Django        #installing Django

  django-admin              #запуск админа Django
    Available subcommands:
     [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

  python3 manage.py runserver      #запуск сервера на localhost:8000
  python3 manage.py runserver 4000 #запуск сервера на localhost:4000
  python3 manage.py runserver 192.168.0.1:4000  #запуск сервера на ip:192.168.0.1  port:8000

  python3 manage.py startapp  # создание приложения

  #далее регистрируем созданное приложение в фаиле settings.py в папке сайта в папке 'venv'





