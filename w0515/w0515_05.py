# #### 네이버 항공권
# 김포, 제주 5/31 6/1 -> 
# 출발 비행기표 금액 110000원 이상 제외
# 김포출발시간 5/31 17:00 이후 제외
from datetime import datetime
standard_time = datetime(2025,5,31,17,00,00)
now_time = datetime(2025,5,31,15,00,00)

print(standard_time)
print(now_time)
print(standard_time>now_time)
