from src.frameworks_and_drivers.database import db


def postgres_healthcheck():
    is_database_working = True
    output = 'postgres ok'

    try:
        session = db.session
        session.execute('SELECT 1')
    except Exception as e:
        output = str(e)
        is_database_working = False

    return is_database_working, output
