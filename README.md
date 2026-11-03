# ESD2026
multiple servo control

## SW

1. gpio 설치
   
sudo apt update
sudo apt install pigpio python3-pigpio

2. RPI에서 GPIO 제어 요청을 처리하는 백그라운드 프로그램 실행
sudo pigpiod

3. 소스 코드 실행
python3 source.py
