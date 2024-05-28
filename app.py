from flask import Flask,render_template
from main.main import main_blueprint
from one_post.one_post import one_post_blueprint
from search.search import search_blueprint
from user_feed.user_feed import user_feed_search_blueprint
app=Flask(__name__)
app.register_blueprint(one_post_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_search_blueprint)

app.run(debug=True)
