from tracker import add_session, view_sessions
from analytics import show_summary

while True:
    print("\nStudyPulse")
    print("1. Add Study Session")
    print("2. View All Sessions")
    print("3. View Analytics")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Subject: ")
        duration = int(input("Duration (minutes): "))
        date = input("Date (YYYY-MM-DD): ")
        add_session(subject, duration, date)
        print("Session added")

    elif choice == "2":
        view_sessions()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
