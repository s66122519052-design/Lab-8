#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dummy_zero2w.py
เวอร์ชันง่าย ๆ สำหรับ Raspberry Pi Zero 2 W (ไม่มีโมดูลกล้อง)
- แสดงข้อความจำลอง driver state
- ไม่โหลดโมเดล ไม่เปิดกล้อง
"""

import cv2
import numpy as np
import time
import itertools

WINDOW_NAME = "Driver Monitoring (Dummy Zero2W)"

# รายการสถานะจำลอง (อิงจาก paper: Safe, Distracted, Drowsy, Smartphone)
states = ["SafeDriving", "Distracted", "Drowsy", "Smartphone"]
colors = {
    "SafeDriving": (0, 255, 0),
    "Distracted": (0, 255, 255),
    "Drowsy": (0, 128, 255),
    "Smartphone": (0, 0, 255),
}

def main():
    # สร้างหน้าต่างเปล่า 480x320 (เหมือนกล้อง)
    frame_h, frame_w = 320, 480

    # วนซ้ำสถานะทีละ state
    for state in itertools.cycle(states):
        # สร้างภาพพื้นหลังสีดำ
        frame = np.zeros((frame_h, frame_w, 3), dtype=np.uint8)

        # วาดข้อความสถานะตรงกลาง
        color = colors.get(state, (255, 255, 255))
        cv2.putText(frame, f"STATE: {state}",
                    (30, frame_h // 2), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, color, 2, cv2.LINE_AA)

        # วาด FPS จำลอง
        cv2.putText(frame, "FPS: 10.0", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

        # แสดงผล
        cv2.imshow(WINDOW_NAME, frame)

        # หน่วงเวลา 1 วินาทีต่อ state
        key = cv2.waitKey(1000) & 0xFF
        if key in (27, ord('q')):  # ESC หรือ q ออก
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()