import ckan.model as model
import ckan.plugins.toolkit as tk
import db


def is_adquired(pkg_dict):

    if db.package_allowed_users_table is None:
        db.init_db(model)

    if tk.c.user:
        return len(db.AllowedUser.get(package_id=pkg_dict['id'], user_name=tk.c.user)) > 0
    else:
        return False


def is_owner(pkg_dict):
    if tk.c.userobj:
        return tk.c.userobj.id == pkg_dict['creator_user_id']
    else:
        return False


def get_allowed_users_str(users):
    if users:
        return ','.join([user for user in users])
    else:
        return ''
