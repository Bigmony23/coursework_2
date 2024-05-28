from flask import Flask,render_template,Blueprint
from utils import get_comments_by_posts_id

one_post_blueprint=Blueprint("one_post_blueprint",__name__)

@one_post_blueprint.route("/posts/<int:id>")
def one_post_comments(id):
    one_post_comment=get_comments_by_posts_id(id)
    spisok_userov=[x for x in one_post_comment if x['post_id']==id]
    return render_template("post.html",one_post=one_post_comment,comment_lendth=len(one_post_comment),spisok=spisok_userov)
