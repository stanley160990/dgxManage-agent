#!/bin/bash

hari=$1


systemctl stop nvsm
systemctl stop nvidia-dcgm

nvidia-smi -i 0 -mig 0
nvidia-smi -i 1 -mig 0
nvidia-smi -i 2 -mig 0
nvidia-smi -i 3 -mig 0
nvidia-smi -i 4 -mig 0
nvidia-smi -i 5 -mig 0
nvidia-smi -i 6 -mig 0
nvidia-smi -i 7 -mig 0

nvidia-smi -i 0 -mig 1
nvidia-smi -i 1 -mig 1
nvidia-smi -i 2 -mig 1
nvidia-smi -i 3 -mig 1
nvidia-smi -i 4 -mig 1
nvidia-smi -i 5 -mig 1
nvidia-smi -i 6 -mig 1
nvidia-smi -i 7 -mig 1

case $hari in
    "1")
        echo "senin\n"
        nvidia-smi mig -i 0 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 1 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 2 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 3 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 4 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 5 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 7 -cgi 19,19,19,19,19,19,19 -C
        ;;
    "2")
        echo "selasa\n"
        nvidia-smi mig -i 0 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 1 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 2 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 3 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 4 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 5 -cgi 19,19,19,19,19,19,19 -C
        nvidia-smi mig -i 7 -cgi 19,19,19,19,19,19,19 -C
        ;;
    "3")
        echo "rabu\n"
        nvidia-smi mig -i 0 -cgi 14,14,14 -C
        nvidia-smi mig -i 1 -cgi 14,14,14 -C
        nvidia-smi mig -i 2 -cgi 14,14,14 -C
        nvidia-smi mig -i 3 -cgi 14,14,14 -C
        nvidia-smi mig -i 4 -cgi 14,14,14 -C
        nvidia-smi mig -i 5 -cgi 14,14,14 -C
        nvidia-smi mig -i 6 -cgi 14,14,14 -C
        nvidia-smi mig -i 7 -cgi 14,14,14 -C
        ;;
    "4")
        echo "kamis\n"
        nvidia-smi mig -i 0 -cgi 9,9 -C
        nvidia-smi mig -i 1 -cgi 9,9 -C
        nvidia-smi mig -i 2 -cgi 9,9 -C
        nvidia-smi mig -i 3 -cgi 9,9 -C
        nvidia-smi mig -i 4 -cgi 9,9 -C
        nvidia-smi mig -i 5 -cgi 9,9 -C
        nvidia-smi mig -i 6 -cgi 9,9 -C
        nvidia-smi mig -i 7 -cgi 9,9 -C
        ;;
    "5")
        echo "jumat\n"
        nvidia-smi mig -i 0 -cgi 0 -C
        nvidia-smi mig -i 1 -cgi 0 -C
        nvidia-smi mig -i 2 -cgi 0 -C
        nvidia-smi mig -i 3 -cgi 0 -C
        nvidia-smi mig -i 4 -cgi 0 -C
        nvidia-smi mig -i 5 -cgi 0 -C
        nvidia-smi mig -i 6 -cgi 0 -C
        nvidia-smi mig -i 7 -cgi 0 -C
        ;;
    "10")
        echo "penelitian\n"
        nvidia-smi mig -i 0 -cgi 9,9 -C
        nvidia-smi mig -i 1 -cgi 9,9 -C
        nvidia-smi mig -i 2 -cgi 9,9 -C
        nvidia-smi mig -i 3 -cgi 9,9 -C
        nvidia-smi mig -i 4 -cgi 9,9 -C
        nvidia-smi mig -i 5 -cgi 9,9 -C
        nvidia-smi mig -i 6 -cgi 9,9 -C
        nvidia-smi mig -i 7 -cgi 9,9 -C
    *)
        echo "salah"
esac

systemctl start nvsm
systemctl start nvidia-dcgm