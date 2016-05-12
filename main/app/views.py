from . import app, db
from .models import Profile_Likes, Comment, Post, Profile
from datetime import timedelta, date, datetime
from sqlalchemy import func, desc
from .test_schema import *
from flask import jsonify, Response
from io import StringIO
from app import SQLALCHEMY_DATABASE_URI

ids = [profile.id for profile in Profile.query.all()]
names = [profile.page_name for profile in Profile.query.all()]
days = 7

@app.route('/')
def index():
    schema = {}
    options = select_options()
    schema['select_menu'] = dict(menu=options)
    get_table = table(days)
    schema['table'] = get_table
    schema['analysis'] = []
    for id, name in list(zip(ids, names)):
        stats = get_party_stats(page_id=id, days=days)
        schema['analysis'].append(stats)
    return jsonify(schema)

@app.route('/csv/posts')
def serve_csv():
    df = get_csv(days, ids[2], 'post')
    output = StringIO()
    df.to_csv(output)
    return Response(output.getvalue(), mimetype="text/csv")