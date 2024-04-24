
# Create a function for data analysis of customers id's.

def id_set():
    customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
    # print each id separately and without a duplicate.
    for id in set(customer_ids):
        print(id)
    # return a set of unique id's.
    set_list = set(customer_ids)
    customer_ids = list(set_list)
    print(customer_ids)

id_set()
