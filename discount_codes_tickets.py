import consts
import csv
import os
import random


def generate_discount_codes_tickets():
    if os.path.exists(consts.DISCOUNT_CODES_TICKETS_CSV):
        os.remove(consts.DISCOUNT_CODES_TICKETS_CSV)
    with open(consts.DISCOUNT_CODES_TICKETS_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.DISCOUNT_CODES_TICKETS_HEADERS)
        i = 1
        discount_id = 1
        while i < consts.EVENTS_NUM * 3 + 1:
            writer.writerow([
                discount_id,
                i
            ])
            discount_id += 1
            writer.writerow([
                discount_id,
                i
            ])
            discount_id += 1
            writer.writerow([
                discount_id,
                i
            ])
            discount_id += 1
            writer.writerow([
                discount_id,
                i
            ])
            discount_id += 1
            i += 3