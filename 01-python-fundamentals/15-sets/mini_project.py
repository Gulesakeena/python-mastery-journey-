'''Mini Project
Unique Visitor Tracker

Store website visitors using a set.

Menu

1 Add Visitor

2 Check Visitor

3 Remove Visitor

4 Display Visitors

5 Total Unique Visitors

6 Exit

Rules

Do not allow duplicate visitors.
Display visitors in sorted order when showing all visitors.'''

"""
Mini Project: Unique Visitor Tracker

Features:
1. Add Visitor
2. Check Visitor
3. Remove Visitor
4. Display Visitors (Sorted)
5. Total Unique Visitors
6. Exit
"""

visitors = set()

while True:
    print("\n" + "=" * 40)
    print("        UNIQUE VISITOR TRACKER")
    print("=" * 40)
    print("1. Add Visitor")
    print("2. Check Visitor")
    print("3. Remove Visitor")
    print("4. Display Visitors")
    print("5. Total Unique Visitors")
    print("6. Exit")
    print("=" * 40)

    try:
        option = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # -------------------- Add Visitor --------------------
    if option == 1:
        name = input("Enter visitor name: ").strip().title()

        if name == "":
            print("❌ Visitor name cannot be empty.")

        elif name in visitors:
            print("⚠ Visitor already exists.")

        else:
            visitors.add(name)
            print(f"✅ {name} added successfully.")

    # -------------------- Check Visitor --------------------
    elif option == 2:
        name = input("Enter visitor name to search: ").strip().title()

        if name in visitors:
            print(f"✅ {name} is already in the visitor list.")
        else:
            print(f"❌ {name} not found.")

    # -------------------- Remove Visitor --------------------
    elif option == 3:
        name = input("Enter visitor name to remove: ").strip().title()

        if name in visitors:
            visitors.remove(name)
            print(f"✅ {name} removed successfully.")
        else:
            print(f"❌ {name} not found.")

    # -------------------- Display Visitors --------------------
    elif option == 4:

        if len(visitors) == 0:
            print("⚠ No visitors available.")

        else:
            print("\nRegistered Visitors")
            print("-" * 25)

            for index, visitor in enumerate(sorted(visitors), start=1):
                print(f"{index}. {visitor}")

    # -------------------- Total Visitors --------------------
    elif option == 5:
        print(f"\nTotal Unique Visitors: {len(visitors)}")

    # -------------------- Exit --------------------
    elif option == 6:
        print("\nThank you for using Unique Visitor Tracker.")
        break

    # -------------------- Invalid Choice --------------------
    else:
        print("❌ Invalid choice. Please select between 1 and 6.")