#-*- coding: utf-8 -*-
import facepy
import sys

vmro_id = '90137764259'
sdsm_id = '148427235188637'

with open('at', 'r') as f:
    at = f.readline()

f = facepy.GraphAPI(at)
profile_path = '?fields=name,likes'
post_path = '?fields=posts.limit(100){shares,link,message,likes.summary(true),comments.summary(true)}'
shares_path = '/sharedposts?limit=100'
def get_likes(id_):
    make_req = f.get(id_ + profile_path)
    yield make_req['likes']

def count_shares_of_posts(post_id):
    make_req = f.get(post_id + shares_path)
    count_shares = len(make_req['data'])
    while True:
        try:
            after = make_req['paging']['cursors']['after']
            make_req = f.get(post_id + shares_path + '&after=' + after)
            count_shares += len(make_req['data'])
        except KeyError:
            return count_shares
def get_posts(id_):
        make_req = f.get(id_ + post_path)
        for post in make_req['posts']['data']:
            if len(post['comments']['data']) > 0:
                for comment in post['comments']['data']:
                    author = comment['from']['name']
                    author_id = comment['from']['id']
                    comment_message = comment['message']
            post_id = post['id']
            num_shares = post['shares']['count']
            num_comments = post['comments']['summary']['total_count']
            num_likes = post['likes']['summary']['total_count']
            engagement = sum((num_likes, num_comments, num_shares))
# get_posts(vmro_id)