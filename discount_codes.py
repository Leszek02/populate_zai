import consts
import csv
import os
import math


def generate_discount_codes(custom_hex: list):
    if os.path.exists(consts.DISCOUNT_CODES_CSV):
        os.remove(consts.DISCOUNT_CODES_CSV)
    with open(consts.DISCOUNT_CODES_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.DISCOUNT_CODES_HEADERS)
        discount_id = 1
        for i in range(1, consts.EVENTS_NUM + 1):
            if i <= consts.BIG_ORGANIZERS_NUM * consts.CONCERTS_PER_BIG:
                account = math.ceil(i / consts.CONCERTS_PER_BIG) - 1
            else:
                account = consts.BIG_ORGANIZERS_NUM + (math.ceil((i - consts.BIG_ORGANIZERS_NUM * consts.CONCERTS_PER_BIG) / 2)) - 1

            writer.writerow([ # Unlimited 50% discount
                discount_id, # id
                "discount_unlimited_50", # code
                f'{consts.API_HOST}e/{custom_hex[i-1]}?code=discount_unlimited_50', # discount_url
                50, # value
                "percent", # type
                True, # is_active
                100000, # tickets_number
                1, # min_quantity
                100, # max_quantity
                "2025-04-04", # valid_from
                "2025-11-11", # valid_till
                i, # event_id
                "2025-04-04", # created_at
                account + 1, # marketer_id
                "ticket" # used_for
             ])
            discount_id += 1

            writer.writerow([ # Unlimited 100% discount
                discount_id, # id
                "discount_unlimited_100", # code
                f'{consts.API_HOST}e/{custom_hex[i-1]}?code=discount_unlimited_100', # discount_url
                100, # value
                "percent", # type
                True, # is_active
                100000, # tickets_number
                1, # min_quantity
                100, # max_quantity
                "2025-04-04", # valid_from
                "2025-11-11", # valid_till
                i, # event_id
                "2025-04-04", # created_at
                account + 1, # marketer_id
                "ticket" # used_for
             ])
            discount_id += 1

            writer.writerow([ # Unlimited 100% discount
                discount_id, # id
                "discount_limited_50", # code
                f'{consts.API_HOST}e/{custom_hex[i-1]}?code=discount_limited_50', # discount_url
                50, # value
                "percent", # type
                True, # is_active
                500, # tickets_number
                1, # min_quantity
                100, # max_quantity
                "2025-04-04", # valid_from
                "2025-11-11", # valid_till
                i, # event_id
                "2025-04-04", # created_at
                account + 1, # marketer_id
                "ticket" # used_for
             ])
            discount_id += 1

            writer.writerow([ # Unlimited 100% discount
                discount_id, # id
                "discount_limited_100", # code
                f'{consts.API_HOST}e/{custom_hex[i-1]}?code=discount_limited_100', # discount_url
                100, # value
                "percent", # type
                True, # is_active
                500, # tickets_number
                1, # min_quantity
                100, # max_quantity
                "2025-04-04", # valid_from
                "2025-11-11", # valid_till
                i, # event_id
                "2025-04-04", # created_at
                account + 1, # marketer_id
                "ticket" # used_for
             ])
            discount_id += 1