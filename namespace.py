import sys
import re
import subprocess
from brace import find_matching_brace, get_inner_text


def rm(text, namespace):
    start = text.find('namespace %s' % namespace)
    while start != -1:
        i = text.find('{', start)
        if i == -1:
            break

        j = i + find_matching_brace(text[i:])
        if j == i - 1 or j == i + 1:
            break

        text = text.replace(text[start:(j+1)], text[(i+1):j])
        start = text.find('namespace %s' % namespace)

    return text

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
