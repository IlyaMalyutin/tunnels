Simple python-script to control ssh-tunnels.

If you use ssh-tunnels, once there may be too many of them. They can fall off. They need to be restarted and so on.
A simple python script runs tunnels in separated processes and periodically pings the ports to which they are routed.
If something is wrong (fell off wi-fi, restarted vpn, etc.) - the tunnel restarts.

To start you need to go to the project directory:

`cd tunnels`

Create new config file:

`cp config_example.py config.py`

Add your tunnels and ports as in the example from config_example.py

`vi config.py`

You can then run the script:

`python 3 start.py`




Простой python-скрипт для контроля ssh-туннелей.

Если вы испльзуете ssh-туннели, то в какой-то момент их может стать слишком много. Они могут отваливаться. Их нужно перезапускать и тд.
Простой python-скрипт запускает туннули в отдельных процессах и периодически пингует порты, на которые они проброшены.
Если что-то не так (отвалилися wi-fi, перезапустился vpn и тд) - туннель перезапускается.

Для старта нужно перейти в дирикторию проекта:

`cd tunnels`

Создать новый файл с конфигом:

`cp config_example.py config.py`

Добавить свой туннель и порт как в примере из config_example.py

`vi config.py`

После этого можно запустить скрипт:

`python3 start.py`
