"""
Append new blueprints
"""

from src.frameworks_and_drivers.blueprints.auth_blueprint import auth_blueprint
from src.frameworks_and_drivers.blueprints.index_blueprint import index_blueprint


blueprints_store = list()
blueprints_store.append(auth_blueprint)
blueprints_store.append(index_blueprint)
