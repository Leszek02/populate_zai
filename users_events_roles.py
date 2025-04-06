from flask_scrypt import generate_password_hash, generate_random_salt

import consts
import math
import csv
import os


def generate_users_events_roles():
    if os.path.exists(consts.USERS_EVENTS_ROLES_CSV):
        os.remove(consts.USERS_EVENTS_ROLES_CSV)
    with open(consts.USERS_EVENTS_ROLES_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.USERS_EVENTS_ROLES_HEADERS)
        for i in range(1, consts.events_num + 1):
            if i <= consts.BIG_ORGANIZERS_NUM * consts.CONCERTS_PER_BIG:
                account = math.ceil(i / consts.CONCERTS_PER_BIG) - 1
            else:
                account = consts.BIG_ORGANIZERS_NUM + (math.ceil((i - consts.BIG_ORGANIZERS_NUM * consts.CONCERTS_PER_BIG) / 2)) - 1
            writer.writerow([
                i, # id
                i, # event_id
                account + 1, # user_id
                3 # role_id
            ])