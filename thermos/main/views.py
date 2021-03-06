from flask import render_template

from thermos import login_manager
from thermos.main import main
from thermos.models import User, Bookmark, Tag


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@main.route("/")
@main.route("/index")
def index():
    return render_template("index.html", new_bookmarks=Bookmark.newest(5))


@main.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@main.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)
