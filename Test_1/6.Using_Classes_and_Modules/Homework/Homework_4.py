def file_type(s):
    val = s.rfind('.')
    if (val == -1):
        return ""
    else:
        return s[val+1:]
    
s = ['foo.doc', 'foo.docx', 'foo.bar.docx', '', 'foo', 'foo.']

for x in s:
    print(file_type(x))