from crypt import methods
from unicodedata import name
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Clothing as clt, Image
from . import db
import json
import os


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        
        print('home1')
        type = request.form.get('type')
        color = request.form.get('color')
        storage = request.form.get('storage-choice')
        size = request.form.get('size')

        if len(type) < 1:
            flash('Type entry is too short!', category='error')
        elif len(color) < 1:
            flash('Color entry is too short!', category='error')
        elif len(storage) < 1:
            flash('Pick a storage unit!', category='error')
        elif len(size) < 1:
            flash('Size missing!', category='error')
        else:
            print('home2')
            new_clothing = clt(color=color, type=type, storage=storage, size=size, user_id=current_user.id)
            db.session.add(new_clothing)
            db.session.commit()
            flash('Clothing added to closet!', category='success')

            id = new_clothing.id
            pic = request.files['image_file']

            if not pic:
                flash('Clothing added, but no image uploaded', category='error')

            else:
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype
                print('here')

                img = Image(img=pic.read(), mimetype=mimetype, name=filename, clothing_id=id)
                
                db.session.add(img)
                db.session.commit()
                flash("Image saved successfully", category='success')    

            return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user)

@views.route('/closet', methods=['GET', 'POST'])
@login_required
def closet_view():
    return render_template("closet.html", user=current_user)

@views.route('/delete-clothing', methods=['POST'])
def delete_clothing():

    clothing = json.loads(request.data)
    clothingId = clothing['clothingId']
    clothing = clt.query.get(clothingId)
    img = clt.query.get(clothingId)

    if clothing:
        if clothing.user_id == current_user.id:
            db.session.delete(clothing)
            db.session.delete(img)
            db.session.commit()

    return jsonify({})

    