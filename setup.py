from setuptools import setup, find_packages

setup(
    name='url_shortener',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'psycopg2-binary',
        'gunicorn',
        'python-dotenv',
    ],
)