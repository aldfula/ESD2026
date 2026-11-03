# ESD2026
multiple servo control

## SW

1. gpio 설치
   
   - sudo apt update
   - sudo apt install pigpio python3-pigpio

2. RPI에서 GPIO 제어 요청을 처리하는 백그라운드 프로그램 실행
   - sudo pigpiod

3. 소스 코드 실행
   - python3 sw_servo_control.py


## HW
1. I2C 활성화
   - sudo raspi-config
   - Interface Options -> I2C -> Yes
   - sudo reboot

2. PCA 연결 확인
   - sudo apt update
   - sudo apt install -y i2c-tools
   - sudo i2cdetect -y 1

3. Python 라이브러리 설치

   - **Adafruit Blinka: Raspberry Pi에서 CircuitPython 기반 라이브러리를 사용할 수 있도록 지원**
   - **Adafruit ServoKit: PCA9685로 서보 모터의 각도를 제어**
   1. Python 가상환경 준비
      - sudo apt install -y python3-venv python3-pip
      - 작업 폴더 생성
      - python3 -m venv .venv
      - source .venv/bin/activate
   2. 라이브러리 설치
      - python -m pip install adafruit-blinka adafruit-circuitpython-servokit
