Pyinstaller -F -w main.py 不带控制台

pyinstaller -F main.py 带控制台

切记-D这个参数一定要有，否则生成出来的exe不能在其他电脑上运行！

pyinstaller -i="h:\###.ico" -F -D ×××.py

pyinstaller -i="m4.ico" -F -w picture_download3.py

尽量把相关的东西放在GUI包下
