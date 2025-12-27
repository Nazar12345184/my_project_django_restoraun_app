import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), '..', 'myapp', 'templates')

include_snippet = "{% include 'includes/back_button.html' %}"

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if include_snippet in content:
        return False
    if '</body>' in content:
        content = content.replace('</body>', include_snippet + '\n</body>', 1)
    else:
        content = content + '\n' + include_snippet
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def main():
    updated = []
    for root, dirs, files in os.walk(TEMPLATES_DIR):
        for name in files:
            if not name.endswith('.html'):
                continue
            rel = os.path.join(root, name)
            # skip the include file itself
            if os.path.normpath(rel).endswith(os.path.join('templates', 'includes', 'back_button.html')):
                continue
            if process_file(rel):
                updated.append(rel)
    print('Updated files:')
    for p in updated:
        print(p)

if __name__ == '__main__':
    main()
