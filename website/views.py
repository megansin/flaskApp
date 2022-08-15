from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Clothing
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        type = request.form.get('type')
        color = request.form.get('color')
        storage = request.form.get('storage-choice')
        seasons = request.form.get('seasons')
        size = request.form.get('size')

        if len(type) < 1:
            flash('Type entry is too short!', category='error')
        elif len(color) < 1:
            flash('Color entry is too short!', category='error')
        elif len(storage) < 1:
            flash('Pick a storage unit!', category='error')
        elif len(seasons) < 1:
            flash('Pick at least one season!', category='error')
        elif len(size) < 1:
            flash('Size missing!', category='error')
        else:
            new_clothing = Clothing(color=color, type=type, storage=storage,
                seasons=seasons, size=size, user_id=current_user.id)
            db.session.add(new_clothing)
            db.session.commit()
            flash('Clothing added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/closet', methods=['GET', 'POST'])
@login_required
def closet_view():
    return render_template("closet.html", user=current_user)

@views.route('/delete-clothing', methods=['POST'])
def delete_clothing():
    clothing = json.loads(request.data)
    clothingId = clothing['clothingId']
    clothing = Clothing.query.get(clothingId)
    if clothing:
        if clothing.user_id == current_user.id:
            db.session.delete(clothing)
            db.session.commit()

    return jsonify({})