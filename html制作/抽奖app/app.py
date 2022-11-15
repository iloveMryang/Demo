# 让我们的电脑可以支持服务访问
# 需要一个web框架
# pip install Flask
from flask import Flask,render_template
app = Flask(__name__)   #创建一个web的应用

hero = [
    '亚瑟''妲己''蔡文姬''李白'
    '孙悟空''不知火舞''公孙离''孙策'
]

@app.route('/index')    #浏览器里返回index里return的内容
def index():
    return render_template("index.html",hero = hero)  #返回一个模板/index.html文件,将
                                                      #将hero赋值给index.html
app.run(debug=True)  #方便后续开发，后期更改代码时不用频繁打开关闭应用
