from app import create_app, db
from app.models import ShortURL, ClickData

def init_db():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if we already have any short URLs
        if ShortURL.query.first() is None:
            # Add some initial data
            initial_urls = [
                ('https://www.example.com', 'example'),
                ('https://www.google.com', 'google'),
                ('https://www.github.com', 'github')
            ]

            for url, code in initial_urls:
                short_url = ShortURL(original_url=url, short_code=code)
                db.session.add(short_url)

            db.session.commit()
            print("Initialized the database with some sample data.")
        else:
            print("Database already contains data, skipping initialization.")

if __name__ == '__main__':
    init_db()