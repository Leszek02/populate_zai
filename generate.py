from pathlib import Path

import faker
import argparse

from users import generate_users
from events import generate_events
from users_events_roles import generate_users_events_roles
from tickets import generate_tickets
from custom_forms import generate_custom_forms


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

    parser.add_argument(
        "--tickets", "-t",
        action="store_true",
        default=False,
        help="Generate 'tickets' table."
    )

    parser.add_argument(
        "--custom_forms", "-cf",
        action="store_true",
        default=False,
        help="Generate 'custom_forms' table."
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
        generate_tickets()
        generate_custom_forms()
    else:
        if args.users:
            generate_users(fake)
        if args.events:
            generate_events(fake)
        if args.users_events_roles:
            generate_users_events_roles()
        if args.tickets:
            generate_tickets()
        if args.custom_forms:
            generate_custom_forms()
        