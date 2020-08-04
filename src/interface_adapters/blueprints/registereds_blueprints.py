"""
Append new blueprints
"""

from src.interface_adapters.blueprints.auth_blueprint import auth_blueprint
from src.interface_adapters.blueprints.index_blueprint import index_blueprint


blueprints_store = list()
blueprints_store.append(auth_blueprint)
blueprints_store.append(index_blueprint)
