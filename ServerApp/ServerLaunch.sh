#!/bin/sh 
# 命令后面加 & 后台执行多个sh
sh /var/www/html/PythonCreator/ServerApp/AppleJWTToken.sh & 
sh /var/www/html/PythonCreator/ServerApp/AppVersion.sh & 

  
# vnc
# vncserver -kill :1
vncserver :1
# vncconfig  