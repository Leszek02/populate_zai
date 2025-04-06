import consts
import csv
import os
import random


def generate_custom_forms():
    if os.path.exists(consts.CUSTOM_FORMS_CSV):
        os.remove(consts.CUSTOM_FORMS_CSV)
    with open(consts.CUSTOM_FORMS_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(consts.CUSTOM_FORMS_HEADERS)
        for i in range(1, consts.events_num + 1):
             writer.writerow([
                  i,
                  "email",
                  "attendee",
                  "email",
                  "Email",
                  True,
                  True,
                  True,
                  0,
                  False,
                  False,
                  i,
                  0,
                  10,
                  False
             ])