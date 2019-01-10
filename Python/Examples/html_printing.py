import webbrowser
 
f = open('helloworld.html','w')
 
message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
 
f.write(message)
f.close()
 
#Change path to reflect file location
filename = 'file:///C:/Users/venkat/Documents/PythonDocs/' + 'helloworld.html'
webbrowser.open_new_tab(filename)


