import json


def get_posts_all():
    with open("data/posts.json",'r',encoding='utf-8') as file:
        data_posts=json.load(file)
    # print(data)
    return data_posts

def get_posts_by_user_name(user):
    data_posts=get_posts_all()
    user_name=[x for x in data_posts if x["poster_name"].lower()==user.lower()]
    return user_name


def get_comments_by_posts_id(post_id):
    with open("data/comments.json",'r',encoding='utf-8') as file:
        data_coments=json.load(file)
        posts_id_comennts=[x for x in data_coments if x['post_id']==post_id]
        # commeter_name=posts_id_comennts[0]['commenter_name']
    # print(posts_id_comennts)
    return posts_id_comennts

get_comments_by_posts_id(1)
def get_post_by_pk(pk):
    data_pk=get_posts_all()
    pk_data=[x for x in data_pk if x['pk']==pk]
    return pk_data
    # print(pk_data)

# get_post_by_pk(1)
