import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    raise RuntimeError("pigpio 데몬 연결 실패")
  
# servo별 gpio 연결에 따라 수정
SERVO1 = 17
SERVO2 = 18
SERVO3 = 22

def move_servos(pulse):
    # 서보 1: 정방향
    pi.set_servo_pulsewidth(SERVO1, pulse)

    # 서보 2: 반대 방향
    pi.set_servo_pulsewidth(SERVO2, 3000 - pulse)

    # 서보 3: 절반 범위로 이동
    pi.set_servo_pulsewidth(SERVO3, 1500 + (pulse - 1500) // 2)

try:
    move_servos(1500)
    time.sleep(1)

    while True:
        # 왼쪽 -> 오른쪽
        for pulse in range(1200, 1801, 10):
            move_servos(pulse)
            time.sleep(0.03)

        # 오른쪽 -> 왼쪽
        for pulse in range(1800, 1199, -10):
            move_servos(pulse)
            time.sleep(0.03)

except KeyboardInterrupt:
    print("서보 제어 종료")

finally:
    for gpio in [SERVO1, SERVO2, SERVO3]:
        pi.set_servo_pulsewidth(gpio, 0)

    pi.stop()
