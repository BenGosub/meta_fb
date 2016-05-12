import facepy
import sqlalchemy
from models import Profile
from . import db

ids = {}
ids['vmro'] = '90137764259'
ids['sdsm'] = '148427235188637'
ids['dui'] = '114081605319234'
ids['dpa'] = '130194893722510'

with open('at', 'r') as f:
    at = f.readline()

f = facepy.GraphAPI(at)
profile_path = '?fields=name,likes'

def insert_profile(id):
    req = f.get(id + profile_path)
    name = req['name']
    profile = Profile(id=id, page_name=name)
    db.session.add(profile)
    db.session.commit()
    db.session.close()

for id in ids.values():
    insert_profile(id)