from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(count):
    koala_facts_list = []
    attempts = 0

    while (len(koala_facts_list) < count) and (attempts < 100):
        fact_to_be_added = random_koala_fact()
        if fact_to_be_added not in koala_facts_list:
            koala_facts_list.append(fact_to_be_added)
        else:
            attempts += 1
    return koala_facts_list


def num_joey_facts():
    koala_facts_list = []
    joey_facts = []
    fact_to_be_added = random_koala_fact()
    while koala_facts_list.count(fact_to_be_added) < 10:

        koala_facts_list.append(fact_to_be_added)
        if fact_to_be_added not in joey_facts and "joey" in fact_to_be_added:
            joey_facts.append(fact_to_be_added)
        fact_to_be_added = random_koala_fact()
    else:
        return len(joey_facts)


def koala_weight():
    random_fact = random_koala_fact()
    count = 0
    while count < 1000:
        random_fact = random_koala_fact()
        if "kg " in random_fact or "kg." in random_fact:
            break
        count += 1
    else:
        print("while loop ended with:", random_fact)
    weight_fact = random_fact.split("kg")
    weight = weight_fact[0].split()
    return int(weight[-1])


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(unique_koala_facts(3))
    print(num_joey_facts())
    print(koala_weight())
