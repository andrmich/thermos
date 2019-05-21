from flask import Blueprint

bookmarks = Blueprint('bookmarks', __name__)

from thermos.bookmarks import views
from thermos.bookmarks import forms