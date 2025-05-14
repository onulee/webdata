import smtplib
from email.mime.text import MIMEText


# 중요정보
recvEmail = "onulee@naver.com"
password = "HC4S4P5G2S2M" ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출
title = "웹스크래핑 이메일 보내기"
text = f"""
    <html>
    <body>
        <h2>{title}</h2>
        <p>메일 html전송</p>
    </body>
    </html>
    """

msg = MIMEText(text,'html')
msg['Subject'] = title
## 네이버주소메일이 아니면 에러
msg['From'] = "onulee@naver.com"
msg['To'] = recvEmail

s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("onulee",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
s.sendmail("onulee@naver.com",recvEmail,msg.as_string())
s.quit()

print("메일발송 완료")