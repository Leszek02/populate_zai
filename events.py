from flask_scrypt import generate_password_hash, generate_random_salt

import consts
import faker
import csv
import os
import random


def generate_events(fake: faker.Faker):
    if os.path.exists(consts.EVENTS_CSV):
        os.remove(consts.EVENTS_CSV)
    with open(consts.EVENTS_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.EVENTS_HEADERS)
        for i in range(1, consts.events_num + 1):
            random_words = fake.words(random.randrange(2, 6))
            title = ''.join(word + " " for word in random_words)
            writer.writerow([
                i, # id
                fake.hexify(text='^^^^^^^^'), # identifier
                title, # name
                "2025-11-11", # starts_at
                "2025-11-15", # ends_at
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