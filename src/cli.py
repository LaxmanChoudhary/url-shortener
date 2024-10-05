import click
from flask.cli import with_appcontext
from app import db
from app.models import ShortURL, ClickData

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    db.create_all()
    click.echo('Initialized the database.')

@click.command('populate-db')
@with_appcontext
def populate_db_command():
    """Add sample data to the database."""
    if ShortURL.query.first() is None:
        initial_urls = [
            ('https://www.example.com', 'example'),
            ('https://www.google.com', 'google'),
            ('https://www.github.com', 'github')
        ]

        for url, code in initial_urls:
            short_url = ShortURL(original_url=url, short_code=code)
            db.session.add(short_url)

        db.session.commit()
        click.echo('Added sample data to the database.')
    else:
        click.echo('Database already contains data, skipping population.')

def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)