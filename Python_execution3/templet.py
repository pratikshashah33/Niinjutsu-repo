import os

def get_template_path(path):
    file_path=os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a vaild template path %s"%(file_path))
    return file_path

def get_template(path):
    file_path=get_template_path(path)
    return open(file_path).read()

def render_context(template_string,context):
    return templete_string.format(**context)

file_ = "C:\Users\Pratiksha\Desktop\Templet\email_message.txt"
file_html = "C:\Users\Pratiksha\Desktop\Python_execution3\Templet\email_message.html"
template=get_template(file_)
template_html=get_template(file_html)
context={
    "name":"Pratiksha",
    "date":None,
    "total":None
}

print(render_context(template,context))
print(render_context(template_html,context))
    

