from .schema import Party, PartySchema, MainSchema
from marshmallow import pprint
from .models import Profile, Profile_Likes, Post, Comment
from . import db
import sqlalchemy
from sqlalchemy import func, desc
from datetime import datetime, timedelta, date
from app import SQLALCHEMY_DATABASE_URI
import pandas as pd

def get_names():
    return [profile.page_name for profile in Profile.query.all()]

def select_options():
    names = get_names()
    names.append('')
    name_index = [i for i in range(len(names))]
    select_options = list(zip(names, name_index))
    select_options = [{'children' : option[0], 'value' : option[1]} for option in select_options]
    return select_options

def calculate(page_id, column, days, calculation):
    days_before = date.today() - timedelta(days=days)
    try:
        return int(db.session.query(calculation(column)).filter(Post.post_created_time > days_before).filter_by(page_id=page_id).one()[0])    
    except TypeError as e:
        return 0
    

def get_likes(page_id, days):
    date_before = date.today() - timedelta(days=days)
    likes_before = Profile_Likes.query.filter(Profile_Likes.date == date_before).filter_by(page_id=page_id).all()[0].no_likes
    date_latest = db.session.query(func.max(Profile_Likes.date)).filter(Profile_Likes.page_id == page_id).all()[0][0]
    likes_latest = Profile_Likes.query.filter(Profile_Likes.date == date_latest).filter_by(page_id=page_id).all()[0].no_likes
    change = likes_latest - likes_before
    perc_change = round(((change / likes_before) * 100), 2)
    return likes_latest, change, perc_change, likes_before

def get_engagement(page_id, days):
    date_before = date.today() - timedelta(days=days)
    engagement = db.session.query(func.sum(Post.engagement)).filter(Post.page_id == page_id).filter(Post.post_created_time < datetime.now()).filter(Post.post_created_time > date_before).one()[0]
    likes = db.session.query(func.sum(Post.num_likes)).filter(Post.page_id == page_id).filter(Post.post_created_time < datetime.now()).filter(Post.post_created_time > date_before).one()[0]
    comments = db.session.query(func.sum(Post.num_comments)).filter(Post.page_id == page_id).filter(Post.post_created_time < datetime.now()).filter(Post.post_created_time > date_before).one()[0]
    shares = db.session.query(func.sum(Post.num_shares)).filter(Post.page_id == page_id).filter(Post.post_created_time < datetime.now()).filter(Post.post_created_time > date_before).one()[0]
    try:
        return int(engagement), int(likes), int(comments), int(shares)
    except TypeError:
        return 0, 0, 0, 0

def most_pop_post(page_id, days):
    date_before = date.today() - timedelta(days=days)
    try:
        return db.session.query(Post).filter(Post.post_link.like('%facebook.com%')).filter(Post.post_created_time  > date_before).filter_by(page_id=page_id).order_by(desc(Post.num_likes)).limit(1).one()
    except sqlalchemy.orm.exc.NoResultFound:
        return None

def most_shared_links(page_id, days):
    # Returns a sorted list
    date_before = date.today() - timedelta(days=days)
    return db.session.query(Post.post_link, func.count(Post.post_link)).filter(Post.page_id == page_id).group_by(Post.post_link).order_by(desc(func.count(Post.post_link))).all() 

def table_row(page_id, days):
    days_before = date.today() - timedelta(days=7)
    profile_likes, profile_likes_change, _, _ = get_likes(page_id, days)
    post_likes = calculate(page_id=page_id, days=days, calculation=func.sum, column=Post.num_likes)
    post_comments = calculate(page_id=page_id, days=days, calculation=func.sum, column=Post.num_comments)
    post_shares = calculate(page_id=page_id, days=days, calculation=func.sum, column=Post.num_shares)
    post_engagement = calculate(page_id=page_id, days=days, calculation=func.sum, column=Post.engagement)
    comment_authors = db.session.query(Comment.author_id).filter(Comment.page_id == page_id).filter(Comment.comment_created_time > days_before).distinct().count()
    links_shared = db.session.query(Post.post_link).filter(Post.page_id == page_id).filter(Post.post_created_time > days_before).count()
    post_links = post_links = db.session.query(Post.post_link).filter(Post.page_id == page_id).filter(Post.post_created_time > days_before).all()
    fb_links = len([x[0] for x in post_links if 'www.facebook' in x[0]])
    non_fb_links = len([x[0] for x in post_links if 'www.facebook' not in x[0]])
    page_name = Profile.query.filter_by(id=page_id).one().page_name
    return {'profile_likes' : profile_likes, 'profile_likes_change' : profile_likes_change,
            'post_likes' : post_likes, 'post_comments' : post_comments, 'post_shares' : post_shares,
            'post_engagement' : post_engagement, 'comment_authors' : comment_authors,
            'total_links_shared' : links_shared, 'fb_links' : fb_links, 'non_fb_links' : non_fb_links,
            'page_name' : page_name}

def table(days):
    ids = [x[0] for x in db.session.query(Profile.id).all()]
    rows = []
    for page_id in ids:
        rows.append(table_row(page_id, days))
    return rows

def get_party_stats(page_id, days):
    schema = {}
    likes_summary = get_likes(page_id, days)
    likes = dict(likesNow=likes_summary[0], likesChange=likes_summary[1],
                likesPercentageChange=likes_summary[2], likesBefore=likes_summary[3])
    schema['likesSummary'] = likes
    engagement_summary = get_engagement(page_id, days)
    engagement = dict(engagement=engagement_summary[0], likes=engagement_summary[1],
                    comments=engagement_summary[2], shares=engagement_summary[3])
    schema['engagementSummary'] = engagement
    pop_post = most_pop_post(page_id, days)
    try:
        most_pop_post_link = pop_post.post_link
    except AttributeError:
        most_pop_post_link = None
    name = db.session.query(Profile).filter(Profile.id == page_id).one().page_name
    schema['mostPopularLink'] = dict(name=name, link=most_pop_post_link)
    schema['name'] = name
    top_links = most_shared_links(page_id, days)[:3]
    top_links_summary = dict(one=top_links[0][0], two=top_links[1][0], three=top_links[2][0])
    schema['topLinks'] = top_links_summary
    options = select_options()
    for option in options:
        if option['children'] == name:
            schema['value'] = option['value']
    return schema

def get_csv(days, page_id, column):
    date_before = date.today() - timedelta(days=days)
    df = pd.read_sql(column, SQLALCHEMY_DATABASE_URI)
    if column == 'post':
        df = df.loc[(df.page_id == page_id) & (df.post_created_time > date_before)]
    elif column == 'comment':
        df = df.loc[(df.page_id == page_id) & (df.comment_created_time > date_before)]
    return df