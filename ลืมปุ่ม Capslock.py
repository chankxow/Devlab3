#เกิดความผิดพลาดในการพิมพ์โดยระหว่างพิมพ์ได้ลืมกดปุ่ม Capslock 
# ค้างไว้ทำให้ข้อความที่เข้ามาเกิดการสลับกันระหว่างตัวอักษรพิมพ์ใหญ่และตัวอักษรพิมพ์เล็ก
#  ทำให้ไม่สามารถนำไปใช้งานต่อได้ ให้เราเขียนโปรแกรมเพื่อทำการแปลงข้อความกลับเป็นเหมือนเดิม

s = str(input(''))
ans = s.swapcase()    
print(ans)