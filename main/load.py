import facepy
import sqlalchemy
from app.models import Profile_Likes, Comment, Post, Profile
import datetime
from app import db
import dateutil.parser

page_ids = db.session.query(Profile.id).all()
page_ids = [id for (id, ) in page_ids]

with open('at', 'r') as f:
    at = f.readline()

f = facepy.GraphAPI(at)
profile_path = '?fields=name,likes'
post_path = '?fields=posts.limit(50){created_time,shares,link,message,likes.summary(true),comments.summary(true)}'
post_fields = 'posts.limit(50){created_time,shares,link,message,likes.summary(true),comments.summary(true)}'

def get_since_timestamp(page_id):
    most_recent_post_time = Post.query.filter_by(page_id=page_id).order_by \
    (Post.post_created_time.desc()).all()[0].post_created_time.timestamp()
    return most_recent_post_time

def convert_to_datetime(created_at):
    created_at = dateutil.parser.parse(created_at)
    created_at = created_at.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    return created_at


def insert_profile_likes(page_id):
    make_req = f.get(page_id, fields=['name', 'likes'])
    today = datetime.date.today()
    likes = make_req['likes']
    likes_insert = Profile_Likes(no_likes=likes, date=today, page_id=page_id)
    db.session.add(likes_insert)
    db.session.commit()

def insert_posts_and_comments(page_id, since):
    make_req = f.get(page_id, fields=[post_fields], since=since)
    for post in make_req['posts']['data']:
        post_id = post['id'].split('_')[1]
        try:
            post_link = post['link']
        except KeyError:
            post_link=''
        try:
            post_message = post['message']
        except KeyError:
            post_message =''
        post_created_time = convert_to_datetime(post['created_time'])
        try:
            num_shares = post['shares']['count']
        except KeyError:
            num_shares = 0
        num_comments = post['comments']['summary']['total_count']
        try:
            num_likes = post['likes']['summary']['total_count']
        except KeyError:
            num_likes = 0
        engagement = sum((num_likes, num_comments, num_shares))
        post_insert = Post(post_id=post_id, post_link=post_link,
                            post_message=post_message, post_created_time=post_created_time,
                            num_shares=num_shares, num_likes=num_likes,
                            num_comments=num_comments, engagement=engagement,
                            page_id=page_id)
        db.session.add(post_insert)
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            pass
        if len(post['comments']['data']) > 0:
            for comment in post['comments']['data']:
                comment_id = comment['id']
                author = comment['from']['name']
                author_id = comment['from']['id']
                comment_message = comment['message']
                comment_created_time = convert_to_datetime(comment['created_time'])
                comments_insert = Comment(author=author, author_id=author_id, 
                                            comment_message=comment_message, comment_created_time=comment_created_time,
                                            comment_id=comment_id, page_id=page_id,
                                            post_id=post_id)

                db.session.add(comments_insert)
                try:
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                    pass
                db.session.close()

def insert_into_db(id_):
    make_req = f.get(id_ + profile_path)
    profile = Profile(id=id_, page_name=make_req['name'])
    today = datetime.date.today()
    likes = make_req['likes']
    likes_insert = Profile_Likes(no_likes=likes, date=today, page_id=id)

    db.session.add(likes_insert)
    db.session.commit()

    make_req = f.get(id_ + post_path)
    for post in make_req['posts']['data']:
        post_id = post['id'].split('_')[1]
        try:
            post_link = post['link']
        except KeyError:
            post_link=''
        try:
            post_message = post['message']
        except KeyError:
            post_message =''
        post_created_time = convert_to_datetime(post['created_time'])
        try:
            num_shares = post['shares']['count']
        except KeyError:
            num_shares = 0
        num_comments = post['comments']['summary']['total_count']
        try:
            num_likes = post['likes']['summary']['total_count']
        except KeyError:
            num_likes = 0
        engagement = sum((num_likes, num_comments, num_shares))
        post_insert = Post(post_id=post_id, post_link=post_link,
                            post_message=post_message, post_created_time=post_created_time,
                            num_shares=num_shares, num_likes=num_likes,
                            num_comments=num_comments, engagement=engagement,
                            page_id=id)
        db.session.add(post_insert)
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            pass
        db.session.close()
        if len(post['comments']['data']) > 0:
            for comment in post['comments']['data']:
                comment_id = comment['id']
                author = comment['from']['name']
                author_id = comment['from']['id']
                comment_message = comment['message']
                comment_created_time = convert_to_datetime(comment['created_time'])
                comments_insert = Comment(author=author, author_id=author_id, 
                                            comment_message=comment_message, comment_created_time=comment_created_time,
                                            comment_id=comment_id, page_id=id,
                                            post_id=post_id)

                db.session.add(comments_insert)
                try:
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                    pass
                db.session.close()
for page_id in page_ids:
    insert_profile_likes(page_id)
    since = get_since_timestamp(page_id)
    insert_posts_and_comments(page_id, since)

