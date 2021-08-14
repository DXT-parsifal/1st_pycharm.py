# 引入smtplib 模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 配置邮箱信息
sender = '511757085@qq.com'  # 发件人的地址
password = 'gitagjzxtonibiga'  # 此处是我们刚刚在邮箱中获取的授权码
receivers = ['511757085@qq.com', ]  # 邮件接受方邮箱地址，可以配置多个，实现群发

# 邮件内容设置
message = MIMEText('你好呀，邮箱', 'plain', 'utf-8')
# 邮件标题设置

message['Subject'] = '来自pycharm的问候'

# 发件人信息
message['From'] = sender

# 收件人信息
message['To'] = receivers[0]

# 通过授权码,登录邮箱,并发送邮件
try:
    server = smtplib.SMTP('smtp.qq.com')  # 配置126邮箱的smtp服务器地址
    server.login(sender, password)
    server.sendmail(sender, receivers, message.as_string())
    print('发送成功')
    server.quit()

except smtplib.SMTPException as e:
    print('error', e)

# 添加图片附件
try:
    imageFile = r"QQpicture20200430203406.jpg"
    imageApart = MIMEMultipart(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename="love.jpg")
    message.attach(imageApart)
except Exception as e:
    print('图片附加添加失败')

server = zmail.server('511757085@qq.com', 'gitagjzxtonibiga')
mail = server.get_latest()
zmail.show(mail)