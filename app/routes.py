import datetime
from flask import Blueprint, render_template, request, redirect, url_for, abort
from app.models import Link, get_db

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET'])
def home():
    """Render the home page with form and recent links."""
    db = get_db()
    recent_links = db.query(Link).order_by(Link.created_at.desc()).limit(5).all()
    return render_template('home.html', recent_links=recent_links)

@main_bp.route('/create', methods=['POST'])
def create_link():
    """Handle URL submission and redirect back to home."""
    original_url = request.form.get('original_url')
    if not original_url:
        return redirect(url_for('main.home'))

    db = get_db()
    new_link = Link.create(original_url)
    db.add(new_link)
    db.commit()

    return redirect(url_for('main.home'))

@main_bp.route('/<code>')
def redirect_link(code):
    """Redirect short code to original URL, updating click stats."""
    db = get_db()
    link = db.query(Link).filter_by(code=code).first()
    if link is None:
        abort(404)
    # Update stats
    link.click_count += 1
    link.last_accessed = datetime.datetime.utcnow()
    db.commit()
    return redirect(link.original_url)

@main_bp.route('/stats/<code>')
def stats(code):
    """Show statistics for a given short code."""
    db = get_db()
    link = db.query(Link).filter_by(code=code).first()
    if link is None:
        abort(404)
    return render_template('stats.html', link=link)