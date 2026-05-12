import json
import sys
import os

def fix_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    metadata = nb.get('metadata', {})
    widgets = metadata.get('widgets', None)

    if widgets is not None:
        # Fix: add 'state' key if missing
        if 'state' not in widgets:
            metadata['widgets']['state'] = {}
            print(f"Fixed 'state' key in: {filepath}")
        else:
            print(f"No fix needed: {filepath}")
    else:
        print(f"No widgets metadata found: {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Fix specific files passed as arguments
        for path in sys.argv[1:]:
            fix_notebook(path)
    else:
        # Fix all notebooks in current directory
        for fname in os.listdir('.'):
            if fname.endswith('.ipynb'):
                fix_notebook(fname)
