#!/bin/bash

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
white="\033[1;37m"
nc="\033[0m"

export LANG=C # ensuring english once we expect the word "LISTEN" on grep

check_port(){
    printf "$yellow[PORT $1] -> $white$2 ...$nc"
    killarg=`echo $@ | egrep '[-]{2}kill'`
    has_permission_to_kill=$?

    if [ -z has_permission_to_kill ]; then
        (netstat -na | egrep "[:.]$1.*LISTEN" 2>&1 > /dev/null) 2>&1 || printf "$green OK$nc\n"
        pid=`sudo lsof -i :$1 | awk '{ print $2 }' | grep -vi PID`
        if [ ! -z "$pid" ]; then
            (sudo kill -9 $pid 2>&1 > /dev/null) 2>&1 > /dev/null && printf "$yellow KILLED$nc\n" || printf "$red impossible. $white Maybe it's been already killed somehow\n$nc\n"
        fi;
    else
        (netstat -na | egrep "[:.]$1.*LISTEN" 2>&1 > /dev/null) 2>&1 && printf "$red BUSY\n$nc\n" && exit 1 || printf "$green OK$nc\n"
    fi;

}

echo
check_port 9999 "for supervisord control panel"
check_port 8000 "for frontend's nginx"
check_port 7000 "for django server"
check_port 6379 "for redis"
check_port 7777 "for socketio server"
check_port 8080 "for socketio (public facing) port"
echo
