import courses

print(courses.__name__)
print(dir(courses))

courses.html.get_html()
courses.get_java()  # without java


courses.get_swift()
courses.js.get_js()

print(courses.doc.java_doc.java)
print(courses.doc.python_doc.python)