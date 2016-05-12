import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, DECIMAL, UnicodeText, BigInteger, Date, Unicode, DateTime, ForeignKey
from sqlalchemy.orm import relationship

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://uanalyti_bozidar:acodelixjebemti@localhost/uanalyti_meta_fb'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profile'
    mysql_engine = 'InnoDB'
    mysql_charset = 'utf8mb4'
    id = Column(String(length=128), primary_key=True)
    page_name = Column(UnicodeText)
    # profile_pic = Column(String(length=265))
    profile_likes_rel = relationship('Profile_Likes', backref='profile', lazy='dynamic')
    post_rel = relationship('Post', backref='profile', lazy='dynamic')
    comment_rel = relationship('Comment', backref='profile', lazy='dynamic')

class Profile_Likes(Base):
    __tablename__ = 'profile_likes'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    id = Column(Integer, primary_key=True)
    no_likes = Column(BigInteger)
    date = Column(Date)
    page_id = Column(String(length=128), ForeignKey('profile.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    post_id = Column(Unicode(length=128), primary_key=True)
    post_link = Column(Unicode(length=512))
    post_message = Column(UnicodeText)
    post_created_time = Column(DateTime)
    num_shares = Column(BigInteger)
    num_likes = Column(BigInteger)
    num_comments = Column(BigInteger)
    engagement = Column(BigInteger)
    page_id = Column(String(length=128), ForeignKey('profile.id'), nullable=False)
    comment_rel = relationship('Comment', backref='post', lazy='dynamic')

class Comment(Base):
    __tablename__ = 'comment'
    mysql_engine='InnoDB'
    mysql_charset='utf8mb4'
    comment_id = Column(Unicode(length=128), primary_key=True)
    author = Column(Unicode(length=512))
    author_id = Column(BigInteger)
    comment_message = Column(UnicodeText)
    comment_created_time = Column(DateTime)
    page_id = Column(String(length=128), ForeignKey('profile.id'), nullable=False)
    post_id = Column(Unicode(length=128), ForeignKey('post.post_id'), nullable=False)

# Base.metadata.create_all(engine)