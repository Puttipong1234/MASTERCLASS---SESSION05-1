# f(x) = x + 1
# f(1) = 1 + 1 = 2
# f(2) = 2 + 1 = 3

def cal_fx(x):
        return x + 1

print(cal_fx(10))
print(cal_fx(100))
print(cal_fx(20000))


def เอาทุนออก(จำนวนที่ซื้อ):
        จำนวนBTCที่ผมซื้อ = จำนวนที่ซื้อ # btc 0.001223 doge 0.0000032131
        ราคาที่ผมซื้อ = 20000 # บาทต่อbtc
        ราคาbtcวันนี้ = 60000 # บาทต่อbtc

        # string : กลุ่มตัวอักษรหรือเดี่ยว เชื่อม string เข้าหากัน

        ผมชื่อว่า = "mr.pybott"

        ต้นทุนผมเป็นจำนวนเงิน = จำนวนBTCที่ผมซื้อ * ราคาที่ผมซื้อ
        มูลค่าBTCในวันนี้ = ราคาbtcวันนี้ * จำนวนBTCที่ผมซื้อ

        จำนวนที่ผมต้องขายเพื่อเอาทุนออก = ต้นทุนผมเป็นจำนวนเงิน / ราคาbtcวันนี้ 

        print("\n")

        print(ผมชื่อว่า + " ต้องทำการขาย BTC จำนวน : " + str(จำนวนที่ผมต้องขายเพื่อเอาทุนออก) + " BTC เพื่อเอาทุนออก")

        print("คุณ " + ผมชื่อว่า + " จะเหลือ BTC อยู่จำนวน : " + str(จำนวนBTCที่ผมซื้อ - จำนวนที่ผมต้องขายเพื่อเอาทุนออก) + " BTC")

        print("\n")
        
        return จำนวนBTCที่ผมซื้อ - จำนวนที่ผมต้องขายเพื่อเอาทุนออก

import math

คงเหลือ = เอาทุนออก(จำนวนที่ซื้อ = 5)
print(math.floor(คงเหลือ * 100) / 100) # 3.33
print(math.floor(คงเหลือ * 1000) / 1000) # 3.333
เอาทุนออก(จำนวนที่ซื้อ = 20)
เอาทุนออก(จำนวนที่ซื้อ = 60)
เอาทุนออก(จำนวนที่ซื้อ = 100)