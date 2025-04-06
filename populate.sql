-- Clear all previously populated tables
TRUNCATE users CASCADE;

-- Populate users table
COPY users (id, _email, _password, reset_password, salt, is_super_admin, is_admin, is_sales_admin, is_marketer, is_verified, is_blocked, is_profile_public, was_registered_with_order, created_at) FROM '/csv/users_data.csv' CSV HEADER;

COPY events (id, identifier, name, starts_at, ends_at, timezone, online, latitude, longitude, stream_loop,
                  stream_autoplay, is_featured, is_promoted, is_demoted, is_chat_enabled, is_videoroom_enabled, 
                  is_document_enabled, description, after_order_message, show_remaining_tickets, is_map_shown, has_owner_info, is_sessions_speakers_enabled,
                  is_cfs_enabled, privacy, state, is_announced, schedule_published_on, is_ticketing_enabled, is_donation_enabled,
                  is_ticket_form_enabled, is_badges_enabled, payment_country, payment_currency, is_tax_enabled, is_billing_info_mandatory,
                  can_pay_by_paypal, can_pay_by_cheque, can_pay_by_bank, can_pay_by_invoice, can_pay_onsite, can_pay_by_omise, 
                  can_pay_by_alipay, can_pay_by_paytm, onsite_details, created_at, pentabarf_url, ical_url, xcal_url, 
                  is_sponsors_enabled, is_stripe_linked) FROM '/csv/events_data.csv' CSV HEADER;

COPY users_events_roles (id, event_id, user_id, role_id) FROM '/csv/users_events_roles_data.csv' CSV HEADER;

COPY tickets (id, name, is_description_visible, type, quantity, position, price, min_price, max_price, is_fee_absorbed,
                   sales_starts_at, sales_ends_at, is_hidden, min_order, max_order, is_checkin_restricted, auto_checkin_enabled, event_id) FROM '/csv/tickets_data.csv' CSV HEADER;

COPY custom_forms (id, field_identifier, form, type, name, is_required, is_included, is_fixed, position, is_public, 
                        is_complex, event_id, min, max, is_allow_edit) FROM '/csv/custom_forms_data.csv' CSV HEADER;

COPY discount_codes (id, code, discount_url, value, type, is_active, tickets_number, min_quantity, max_quantity, valid_from, 
                          valid_till, event_id, created_at, marketer_id, used_for) FROM '/csv/discount_codes_data.csv' CSV HEADER;

COPY discount_codes_tickets (discount_code_id, ticket_id) FROM '/csv/discount_codes_tickets_data.csv' CSV HEADER;