import os
import requests as re

def fetchpdb(pdb,dir):
    with open(os.join(dir,str(pdb)+'.pdb'),mode='wb') as f:
        resp = re.get('https://files.rcsb.org/download/'+str(pdb))
        f.write(resp.content)