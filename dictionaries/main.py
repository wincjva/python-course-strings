__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


def create_passport(name, dob, place, height, nationality):
    passport = dict(
        [
            ("name", name),
            ("date_of_birth", dob),
            ("place_of_birth", place),
            ("height", height),
            ("nationality", nationality),
        ]
    )
    return passport


def add_stamp(passport, country):
    if country == passport.get("nationality"):
        print(
            f"Welcome home! You do not need a stamp of {country} since this is your nationality"
        )
        return passport
    elif country in passport.get("stamps", []):
        name = passport.get("name")
        print(f"Welcome back to {country}, {name}! No stamp needed sir!")
        return passport
    else:
        list_of_stamps = passport.get("stamps", [])
        list_of_stamps.append(country)
        passport.update(stamps=list_of_stamps)
        print(f"Welcome to {country}! We've stamped your passport.")
        return passport


def check_passport(passport, destination, outgoing_allowed, incoming_forbidden):
    nationality = passport.get("nationality")
    approved_destinations = outgoing_allowed.get(nationality, [])
    banned_countries = incoming_forbidden.get(destination, [])
    if destination not in approved_destinations:
        print(f"{nationality} does not allow outgoing travel to {destination}")
        return False
    for stamp in passport.get("stamps", []):
        if stamp in banned_countries:
            print(f"People who travelled to {stamp} are not allowed into {destination}")
            return False
    add_stamp(passport, destination)
    return passport
