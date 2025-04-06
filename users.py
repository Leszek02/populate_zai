from flask_scrypt import generate_password_hash, generate_random_salt

import consts
import faker
import csv
import os
import random


def generate_users(fake: faker.Faker):
    if os.path.exists(consts.USERS_CSV):
        os.remove(consts.USERS_CSV)
    with open(consts.USERS_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.USERS_HEADERS)
        words = list(set(fake.get_words_list()))
        random.shuffle(words)
        words = words[:1000]
        for i in range(1, consts.BIG_ORGANIZERS_NUM + consts.SMALL_ORGANIZERS_NUM + 1):
            salt = str(generate_random_salt(), 'utf-8')
            hashed_password = str(generate_password_hash(words[i], salt), 'utf-8')
            hash_ = random.getrandbits(128)
            reset_password = str(hash_)
            writer.writerow([
                i,
                words[i]+"@gmail.com",
                hashed_password,
                reset_password,
                salt,
                False,
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                '2025-04-02'
            ])