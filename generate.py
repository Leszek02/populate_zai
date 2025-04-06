from flask_scrypt import generate_password_hash, generate_random_salt
from pathlib import Path
from datetime import datetime

import faker
import argparse
import csv
import os
import random
import math


# File names
users_csv = "./csv/users_data.csv"
events_csv = "./csv/events_data.csv"
users_events_roles_csv = "./csv/users_events_roles.csv"


# Data headers
users_headers = ["id", "_email", "_password", "reset_password", "salt", "is_super_admin", "is_admin", "is_sales_admin", 
                 "is_marketer", "is_verified", "is_blocked", "is_profile_public", "was_registered_with_order", "created_at"]

events_headers = ["id", "identifier", "name", "starts_at", "ends_at", "timezone", "online", "latitude", "longitude", "stream_loop",
                  "stream_autoplay", "is_featured", "is_promoted", "is_demoted", "is_chat_enabled", "is_videoroom_enabled", 
                  "is_document_enabled", "show_remaining_tickets", "is_map_shown", "has_owner_info", "is_sessions_speakers_enabled",
                  "is_cfs_enabled", "privacy", "state", "is_announced", "schedule_published_on", "is_ticketing_enabled", "is_donation_enabled",
                  "is_ticket_form_enabled", "is_badges_enabled", "payment_country", "payment_currency", "is_tax_enabled", "is_billing_info_mandatory",
                  "can_pay_by_paypal", "can_pay_by_cheque", "can_pay_by_bank", "can_pay_by_invoice", "can_pay_onsite", "can_pay_by_omise",
                  "can_pay_by_alipay", "can_pay_by_paytm", "onsite_details", "created_at", "pentabarf_url", "ical_url", "xcal_url",
                  "is_sponsors_enabled", "is_stripe_linked"]

users_events_roles_headers = ["id", "event_id", "user_id", "role_id"]


# Users parameters
big_organizers_num = 100
small_organizers_num = 250


# Events parameters
concerts_per_big = 10
concerts_per_small = 2
events_num = big_organizers_num * concerts_per_big + small_organizers_num * concerts_per_small



def generate_users(fake: faker.Faker):
    if os.path.exists(users_csv):
        os.remove(users_csv)
    with open(users_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(users_headers)
        words = list(set(fake.get_words_list()))
        random.shuffle(words)
        words = words[:1000]
        for i in range(1, big_organizers_num + small_organizers_num + 1):
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


def generate_events(fake: faker.Faker):
    if os.path.exists(events_csv):
        os.remove(events_csv)
    with open(events_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(events_headers)
        for i in range(1, events_num + 1):
            date = datetime.strftime(fake.date_time_this_decade(), "%B %d, %Y")
            random_words = fake.words(random.randrange(2, 6))
            title = ''.join(word + " " for word in random_words)
            writer.writerow([
                i, # id
                fake.hexify(text='^^^^^^^^'), # identifier
                title, # name
                "2025-11-11", # starts_at
                "2025-12-12", # ends_at
                "Europe/Warsaw", # timezone
                True, # online
                0, # latitude
                0, # longitude
                False, # stream_loop
                False, # stream_autoplay
                False, # is_featured
                False, # is_promoted
                False, # is_demoted
                False, # is_chat_enabled
                False, # is_videoroom_enabled
                True, # is_document_enabled
                False, # show_remaining_tickets
                True, # is_map_shown
                False, # has_owner_info
                False, # is_sessions_speakers_enabled
                False, # is_cfs_enabled
                "public", # privacy
                "published", # state
                False, # is_announced
                "1970-01-01", # schedule_published_on
                False, # is_ticketing_enabled
                False, # is_donation_enabled
                False, # is_ticket_form_enabled
                False, # is_badges_enabled
                "Poland", # payment_country
                "USD", # payment_currency
                False, # is_tax_enabled
                False, # is_billing_info_mandator
                False, # can_pay_by_paypal
                False, # can_pay_by_cheque
                False, # can_pay_by_bank
                False, # can_pay_by_invoice
                True, # can_pay_onsite
                False, # can_pay_by_omise
                False, # can_pay_by_alipay
                False, # can_pay_by_paytm
                "Frogs are friends", # onsite_details
                "2024-10-10", # created_at
                "http://localhost/static/media/exports/4/pentabarf/MmtBd3o1OT/pentabarf.xml", # pentabarf_url
                "http://localhost/static/media/exports/4/ical/LzRwU2FkNj/event_ical.ics", # ical_url
                "http://localhost/static/media/exports/4/xcal/MEVnQlo2T0/xcal.xcs", # xcal_url
                False, # is_sponsors_enabled
                False, # is_stripe_linked
            ])


def generate_users_events_roles():
    if os.path.exists(users_events_roles_csv):
        os.remove(users_events_roles_csv)
    with open(users_events_roles_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(users_events_roles_headers)
        for i in range(1, events_num + 1):
            if i <= big_organizers_num * concerts_per_big:
                account = math.ceil(i / concerts_per_big) - 1
            else:
                account = big_organizers_num + (math.ceil((i - big_organizers_num * concerts_per_big) / 2)) - 1
            writer.writerow([
                i, # id
                i, # event_id
                account + 1, # user_id
                3 # role_id
            ])


def parse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Fossasia open-event database population", description="Script generating fake data for testing purposes."
    )

    parser.add_argument(
        "--custom", "-c",
        action="store_false",
        default=True,
        help="Use this flag for selective generating."
    )

    parser.add_argument(
        "--users", "-u",
        action="store_true",
        default=False,
        help="Generate 'users' table."
    )

    parser.add_argument(
        "--events", "-e",
        action="store_true",
        default=False,
        help="Generate 'events' table."
    )

    parser.add_argument(
        "--users_events_roles", "-uer",
        action="store_true",
        default=False,
        help="Generate 'users_events_roles' table."
    )

    return parser



if __name__ == "__main__":
    parser = parse()
    args = parser.parse_args()
    fake = faker.Faker()

    Path("./csv").mkdir(parents=True, exist_ok=True)

    if args.custom:
        generate_users(fake)
        generate_events(fake)
        generate_users_events_roles()
    else:
        if args.users:
            generate_users(fake)
        if args.events:
            generate_events(fake)
        if args.users_events_roles:
            generate_users_events_roles()
        