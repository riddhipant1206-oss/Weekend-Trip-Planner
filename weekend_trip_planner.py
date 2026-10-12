
def show_plan(destination, stops, costs, total_cost, people, per_person):
    print("\n========== WEEKEND TRIP PLAN ==========")
    print("Destination:", destination)

    print("\nPlanned Stops:")

    for i in range(len(stops)):
        print(i + 1, ".", stops[i], "- ₹", costs[i])

    print("\nTotal Cost: ₹", total_cost)

    if people > 0:
        print("Number of People:", people)
        print("Cost Per Person: ₹", round(per_person, 2))


def save_plan(destination, stops, costs, total_cost, people, per_person):

    with open("trip_plan.txt", "w") as file:

        file.write("WEEKEND TRIP PLAN\n")
        file.write("========================\n")

        file.write("Destination: " + destination + "\n\n")

        file.write("Planned Stops:\n")

        for i in range(len(stops)):
            file.write(str(i + 1) + ". " + stops[i] +
                       " - ₹" + str(costs[i]) + "\n")

        file.write("\nTotal Cost: ₹" + str(total_cost) + "\n")

        if people > 0:
            file.write("Number of People: " + str(people) + "\n")
            file.write("Cost Per Person: ₹" +
                       str(round(per_person, 2)) + "\n")


print("===== WEEKEND TRIP PLANNER =====")

destination = input("Enter your destination: ")

stops = []
costs = []

num_stops = int(input("How many stops/activities? "))

for i in range(num_stops):

    stop = input("Enter stop/activity " + str(i + 1) + ": ")
    cost = float(input("Enter estimated cost: ₹"))

    stops.append(stop)
    costs.append(cost)

total_cost = sum(costs)

people = int(input("Enter number of people: "))

if people > 0:
    per_person = total_cost / people
else:
    per_person = 0

show_plan(destination, stops, costs,
          total_cost, people, per_person)

budget = float(input("Enter your total budget: ₹"))

if total_cost <= budget:
    print("Trip is within budget!")
    print("Remaining budget: ₹", budget - total_cost)
else:
    print("Trip is over budget!")
    print("Extra amount needed: ₹", total_cost - budget)

save_plan(destination, stops, costs,
          total_cost, people, per_person)

print("\nTrip saved successfully!")
