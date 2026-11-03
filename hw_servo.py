from adafruit_servokit import ServoKit
import time

# PCA9685 초기화 (16채널)
kit = ServoKit(channels=16)

# 실제 연결한 채널
SERVO1 = 0
SERVO2 = 4
SERVO3 = 8

servos = [SERVO1, SERVO2, SERVO3]

# 서보의 펄스 폭 범위 설정
for ch in servos:
    kit.servo[ch].set_pulse_width_range(1000, 2000)

try:
    # 1. 모든 서보 중앙
    print("모든 서보 중앙 이동")

    for ch in servos:
        kit.servo[ch].angle = 90

    time.sleep(2)

    # 2. 각각 다른 각도로 이동
    print("서보 개별 각도 제어")

    kit.servo[SERVO1].angle = 60
    kit.servo[SERVO2].angle = 120
    kit.servo[SERVO3].angle = 90

    time.sleep(2)

    # 3. 다른 위치로 이동
    kit.servo[SERVO1].angle = 120
    kit.servo[SERVO2].angle = 60
    kit.servo[SERVO3].angle = 120

    time.sleep(2)

    # 4. 중앙 복귀
    print("중앙 복귀")

    for ch in servos:
        kit.servo[ch].angle = 90

    time.sleep(2)

finally:
    # PWM 신호 중지
    for ch in servos:
        kit.servo[ch].angle = None

    print("프로그램 종료")
