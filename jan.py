from operator import sub
import subprocess
subprocess.run(['py','san.py'])
# subprocess.run(['git','init'])
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-m','firstcommit'])
subprocess.run(['git', 'branch', '-M', 'main'])
# subprocess.run(['git','remote','add','origin','https://github.com/SANDHYA-R0910/sandy.git'])
subprocess.run(['git','remote'])
subprocess.run(['git', 'push', '-u', 'origin', 'main'])