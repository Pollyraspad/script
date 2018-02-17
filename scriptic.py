kotik = open("ccc.html")
 X = """<!DOCTYPE HTML PUBLIC>
<html>
 <head>
  <meta charset=utf-8">
  <title>Генерация </title>
 </head>
 <body>
<body bgcolor="#FFA07A"> 
  <h1>Страничка с котиком</h1>

<img src="https://78.media.tumblr.com/dd296920511563a60a062991b7b0ab32/tumblr_p484p2rMX71wfa5swo1_1280.jpg" > 
  
  <p><i> Тут просто кот!</i></p>
  
 </body>
</html>"""
kotik.write(X)
kotik.close()
 
