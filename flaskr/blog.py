from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__,)

@bp.route('/index')
@login_required
def index():
    db = get_db()
    links = db.execute('SELECT webname, website FROM links').fetchall()
    events = db.execute('SELECT eventname, organization, link, deadline, fee FROM events').fetchall()
    return render_template('blog/index.html', links=links, events=events)

@bp.route('/addlink', methods=('GET', 'POST'))
@login_required
def addlink():
    if request.method == 'POST':
        webname = request.form['webname']
        website = request.form['website']
        error = None

        if not webname:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO links (webname, website)'
                ' VALUES (?, ?)',
                (webname, website)
            )
            db.commit()
            flash("Web Site saved successfully")
            return redirect(url_for('blog.index'))

    return render_template('blog/addlink.html')

@bp.route('/addevent', methods=('GET', 'POST'))
@login_required
def addevent():
    if request.method == 'POST':
        event = request.form['event']
        organization = request.form['organization']
        weblink = request.form['weblink']
        deadline = request.form['deadline']
        fee = request.form['fee']
        error = None

        if not event:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO events (eventname, organization, link, deadline, fee)'
                ' VALUES (?, ?, ?, ?, ?)',
                (event, organization, weblink, deadline, fee)
            )
            db.commit()
            flash("New Event saved successfully")
            return redirect(url_for('blog.index'))

    return render_template('blog/addevent.html')