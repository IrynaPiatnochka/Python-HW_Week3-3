
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Finding destinations that both airlines fly to.

common = our_routes.intersection(competitor_routes)
print(common)

# Finding destinations unique to your airline.

different = our_routes.difference(competitor_routes)
print(different)

# Finding destinations that neither airline shares.

not_shared = our_routes.symmetric_difference(competitor_routes)
print(not_shared)
