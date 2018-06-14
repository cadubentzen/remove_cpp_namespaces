import sys
import re
import subprocess
from remove_cpp_namespaces.brace import find_matching_brace, get_inner_text

def rm(text, namespace):
    ns = 'namespace %s' % namespace
    start = text.find(ns)
    while start != -1:
        start_bracket = -1
        for i in range(start + len(ns), len(text)):
            if not text[i] in [' ', '\n', '{']:
                break
            elif text[i] == '{':
                start_bracket = i

        if start_bracket == -1:
            start = text.find(ns, start + len(ns))
            continue

        end_bracket = find_matching_brace(text[start_bracket:])
        if end_bracket in [-1, 1]:
            break

        end_bracket = end_bracket + start_bracket

        text = text.replace(text[start:(end_bracket+1)], text[(start_bracket+1):end_bracket])
        start = text.find(ns)

    return text

def rm_comments(text, namespace):
    return text.replace('// namespace %s\n' % namespace, '')

def rm_using(text, namespace):
    text = text.replace('using %s;' % namespace, '')
    text = text.replace('using ::%s;' % namespace, '')
    text = re.sub(r'using ([:]{0,2})%s[^;]' % namespace, 'using \1', text)
    return text

def rm_file_save(name, namespaces, output=None, style=None, clang_format=None):
    text = ''
    with open(name, 'r') as f:
        text = f.read()

    if text == '':
        return

    for n in namespaces:
        text = rm_comments(text, n)
        text = rm(text, n)
        text = text.replace('%s::' % n, '')
        text = rm_using(text, n)

    # Remove remaining newlines in the beginning
    text = re.sub(r'^\n+', '', text)
    # Turn more than one blank line into one
    text = re.sub(r'[\n]{3,}', '\n\n', text)

    output = output if output else name
    with open(output, 'w') as f:
        f.write(text)

    clang_format = clang_format if clang_format else 'clang-format'
    style = style if style else 'file'
    subprocess.run([clang_format, '-i', '-style=%s' % style, output])
