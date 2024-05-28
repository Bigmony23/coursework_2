from flask import render_template,request,Blueprint
from utils import get_posts_all
search_blueprint=Blueprint('search_blueprint',__name__)

@search_blueprint.route("/search/", methods=['GET'])
def search_by_word():
    search=request.args.get("s")

    data=get_posts_all()
    has_word=[x for x in data if search.lower() in  x['content'].lower()]

    return render_template('search.html',has_word1=has_word, has_word_lendth=len(has_word),s=search)
