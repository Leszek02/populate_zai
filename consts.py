
# File names
USERS_CSV = "./csv/users_data.csv"
EVENTS_CSV = "./csv/events_data.csv"
USERS_EVENTS_ROLES_CSV = "./csv/users_events_roles_data.csv"
TICKETS_CSV = "./csv/tickets_data.csv"


# Data headers
USERS_HEADERS = ["id", "_email", "_password", "reset_password", "salt", "is_super_admin", "is_admin", "is_sales_admin", 
                 "is_marketer", "is_verified", "is_blocked", "is_profile_public", "was_registered_with_order", "created_at"]

EVENTS_HEADERS = ["id", "identifier", "name", "starts_at", "ends_at", "timezone", "online", "latitude", "longitude", "stream_loop",
                  "stream_autoplay", "is_featured", "is_promoted", "is_demoted", "is_chat_enabled", "is_videoroom_enabled", 
                  "is_document_enabled", "show_remaining_tickets", "is_map_shown", "has_owner_info", "is_sessions_speakers_enabled",
                  "is_cfs_enabled", "privacy", "state", "is_announced", "schedule_published_on", "is_ticketing_enabled", "is_donation_enabled",
                  "is_ticket_form_enabled", "is_badges_enabled", "payment_country", "payment_currency", "is_tax_enabled", "is_billing_info_mandatory",
                  "can_pay_by_paypal", "can_pay_by_cheque", "can_pay_by_bank", "can_pay_by_invoice", "can_pay_onsite", "can_pay_by_omise",
                  "can_pay_by_alipay", "can_pay_by_paytm", "onsite_details", "created_at", "pentabarf_url", "ical_url", "xcal_url",
                  "is_sponsors_enabled", "is_stripe_linked"]

USERS_EVENTS_ROLES_HEADERS = ["id", "event_id", "user_id", "role_id"]

TICKETS_HEADERS = ["id", "name", "is_description_visible", "type", "quantity", "position", "price", "min_price", "max_price", "is_fee_absorbed",
                   "sales_starts_at", "sales_ends_at", "is_hidden", "min_order", "max_order", "is_checkin_restricted", "auto_checkin_enabled", "event_id"]


# Users parameters
BIG_ORGANIZERS_NUM = 100
SMALL_ORGANIZERS_NUM = 250


# Events parameters
CONCERTS_PER_BIG = 10
CONCERTS_PER_SMALL = 2
events_num = BIG_ORGANIZERS_NUM * CONCERTS_PER_BIG + SMALL_ORGANIZERS_NUM * CONCERTS_PER_SMALL


# Tickets parameters
BIG_ORGANIZERS_TICKETS = 4 * [50000] + 6 * [25000] # Hard coded number
SMALL_ORGANIZERS_TICKETS = [1000, 10001] # Range to pick random number rounded to thousands
INFINITE_TICKETS = pow(2, 31) - 1