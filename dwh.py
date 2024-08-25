import argparse
import json
import sys
import tempfile

storage_file=os.path.join(tempfile.gettempdir(), 'storage.json')
# это изменение в файле dwh.py для учета в git. Это ветка DEV