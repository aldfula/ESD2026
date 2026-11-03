from adafruit_servokit import ServoKit
import time
import math

# PCA9685 초기화
kit = ServoKit(channels=16)

# 서보 채널
SERVO1 = 0
SERVO2 = 4
SERVO3 = 8

SERVOS = [SERVO1, SERVO2, SERVO3]

# 펄스 폭 설정 (1000~2000μs)
for ch in SERVOS:
    kit.servo[ch].set_pulse_width_range(1000, 2000)

# 왕복 운동 주기 (초)
PERIOD = 4.0

# 업데이트 간격 (초)
INTERVAL = 0.02

try:
    # 초기 위치 설정
    for ch in SERVOS:
        kit.servo[ch].angle = 90

    time.sleep(1)

    start_time = time.monotonic()

    while True:
        # 경과 시간
        t = time.monotonic() - start_time

        # -1 ~ 1 범위의 사인파
        wave = math.sin(2 * math.pi * t / PERIOD)

        # 각 서보의 목표 각도
        angle1 = 90 + 30 * wave
        angle2 = 90 - 30 * wave
        angle3 = 90 + 15 * wave

        # 서보 모터 제어
        kit.servo[SERVO1].angle = angle1
        kit.servo[SERVO2].angle = angle2
        kit.servo[SERVO3].angle = angle3

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\n서보 제어 종료")

finally:
    # PWM 출력 중지
    for ch in SERVOS:
        kit.servo[ch].angle = None

    print("프로그램 종료")
