from flask import render_template, session, redirect, url_for

from . import main
from .forms import TicketForm

@main.route('/', method=['GET', 'POST'])
def index():
    form = TicketForm()
    if form.validate_on_submit():
        #
        return redirect(url_for('.index'))
    return render_template('index.html', form=form)
