from flask import Blueprint, request, redirect, render_template, jsonify
from app import db
from app.models import ShortURL, ClickData
from app.utils import generate_short_code, preprocess_url
import uuid

bp = Blueprint('main', __name__)

@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.json['url']
    processed_url = preprocess_url(original_url)
    short_code = generate_short_code()
    short_url = ShortURL(original_url=processed_url, short_code=short_code)
    db.session.add(short_url)
    db.session.commit()
    return jsonify({
        'short_url': request.host_url + short_code,
        'processed_url': processed_url
    })

@bp.route('/<short_code>')
def redirect_to_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first_or_404()

    click_data = ClickData(
        short_url_id=short_url.id,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        referrer=request.referrer,
        unique_visitor_id=request.cookies.get('visitor_id', str(uuid.uuid4()))
    )
    db.session.add(click_data)
    db.session.commit()

    response = redirect(short_url.original_url)
    if 'visitor_id' not in request.cookies:
        response.set_cookie('visitor_id', click_data.unique_visitor_id, max_age=31536000)  # 1 year

    return response


@bp.route('/<short_code>/stats')
def show_stats(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first_or_404()

    total_clicks = ClickData.query.filter_by(short_url_id=short_url.id).count()
    unique_visitors = ClickData.query.filter_by(short_url_id=short_url.id).with_entities(
        ClickData.unique_visitor_id).distinct().count()
    recent_clicks = ClickData.query.filter_by(short_url_id=short_url.id).order_by(ClickData.timestamp.desc()).limit(
        10).all()

    return render_template('stats.html',
                           short_url=short_url,
                           total_clicks=total_clicks,
                           unique_visitors=unique_visitors,
                           recent_clicks=recent_clicks)