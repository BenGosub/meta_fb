from app import db

class Profile(db.Model):
    __tablename__ = 'profile'
    mysql_engine = 'InnoDB'
    mysql_charset = 'utf8mb4'
    id = db.Column(db.String(length=128), primary_key=True)
    page_name = db.Column(db.UnicodeText)
    # profile_pic = db.Column(db.String(length=265))
    profile_likes_rel = db.relationship('Profile_Likes', backref='profile', lazy='dynamic')
    post_rel = db.relationship('Post', backref='profile', lazy='dynamic')
    comment_rel = db.relationship('Comment', backref='profile', lazy='dynamic')

class Profile_Likes(db.Model):
    __tablename__ = 'profile_likes'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    id = db.Column(db.Integer, primary_key=True)
    no_likes = db.Column(db.BigInteger)
    date = db.Column(db.Date)
    page_id = db.Column(db.String(length=128), db.ForeignKey('profile.id'), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    post_id = db.Column(db.Unicode(length=128), primary_key=True)
    post_link = db.Column(db.Unicode(length=512))
    post_message = db.Column(db.UnicodeText)
    post_created_time = db.Column(db.DateTime)
    num_shares = db.Column(db.BigInteger)
    num_likes = db.Column(db.BigInteger)
    num_comments = db.Column(db.BigInteger)
    engagement = db.Column(db.BigInteger)
    page_id = db.Column(db.String(length=128), db.ForeignKey('profile.id'), nullable=False)
    comment_rel = db.relationship('Comment', backref='post', lazy='dynamic')

class Comment(db.Model):
    __tablename__ = 'comment'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    comment_id = db.Column(db.Unicode(length=128), primary_key=True)
    author = db.Column(db.Unicode(length=512))
    author_id = db.Column(db.BigInteger)
    comment_message = db.Column(db.UnicodeText)
    comment_created_time = db.Column(db.DateTime)
    page_id = db.Column(db.String(length=128), db.ForeignKey('profile.id'), nullable=False)
    post_id = db.Column(db.Unicode(length=128), db.ForeignKey('post.post_id'), nullable=False)

# db.create_all()