from flask import request,render_template,Blueprint
from utils import get_posts_by_user_name
user_feed_search_blueprint=Blueprint('user_feed_search',__name__)

@user_feed_search_blueprint.route("/user_feed/<s>")
def search_by_name(s):
    user_name=get_posts_by_user_name(s)
    return render_template("user-feed.html",user_name1=user_name)
