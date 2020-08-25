from src.frameworks_and_drivers.blueprints.registereds_blueprints import blueprints_store


def register_blueprints(app):
    """
    Register blueprints in flask app
    :param app:
    :return:
    """
    for _blu in blueprints_store:
        app.register_blueprint(_blu)
