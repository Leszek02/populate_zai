import consts
import csv
import os
import random

def generate_tickets():
    if os.path.exists(consts.TICKETS_CSV):
        os.remove(consts.TICKETS_CSV)
    with open(consts.TICKETS_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.TICKETS_HEADERS)
        helper = 0
        ticket_id = 0
        for i in range(1, consts.events_num + 1):
            if i <= consts.BIG_ORGANIZERS_NUM * consts.CONCERTS_PER_BIG:
                quantity = consts.BIG_ORGANIZERS_TICKETS[helper]
                helper += 1
                helper %= 10
            else:
                quantity = random.choice(range(consts.SMALL_ORGANIZERS_TICKETS[0], consts.SMALL_ORGANIZERS_TICKETS[1], 1000))
            
            writer.writerow([  # Paid, limited tickets
                 ticket_id, # id
                 "Paid_ticket", # name
                 True, # is_description_visible
                 "paid", # type
                 quantity, # quantity
                 0, # position
                 15, # price
                 1, # min_price
                 0, # max_price
                 True, # is_fee_absorbed
                 "2025-04-04", # sales_starts_at
                 "2025-11-11", # sales_ends_at
                 False, # is_hidden
                 1, # min_order
                 100, # max_order
                 True, # is_checkin_restricted
                 False, # auto_checkin_enabled
                 i # event_id
            ])
            ticket_id += 1

            writer.writerow([  # Free, limited tickets
                 ticket_id, # id
                 "Free_ticket", # name
                 True, # is_description_visible
                 "free", # type
                 quantity, # quantity
                 1, # position
                 None, # price
                 1, # min_price
                 0, # max_price
                 True, # is_fee_absorbed
                 "2025-04-04", # sales_starts_at
                 "2025-11-11", # sales_ends_at
                 False, # is_hidden
                 1, # min_order
                 100, # max_order
                 True, # is_checkin_restricted
                 False, # auto_checkin_enabled
                 i # event_id
            ])
            ticket_id += 1
            
            writer.writerow([  # Free, unlimited tickets
                 ticket_id, # id
                 "Unlimited_ticket", # name
                 True, # is_description_visible
                 "free", # type
                 consts.INFINITE_TICKETS, # quantity
                 2, # position
                 None, # price
                 1, # min_price
                 0, # max_price
                 True, # is_fee_absorbed
                 "2025-04-04", # sales_starts_at
                 "2025-11-11", # sales_ends_at
                 False, # is_hidden
                 1, # min_order
                 100, # max_order
                 True, # is_checkin_restricted
                 False, # auto_checkin_enabled
                 i # event_id
            ])
            ticket_id += 1
