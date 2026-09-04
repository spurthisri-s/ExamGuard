from faker import Faker
import random
import csv
from datetime import datetime, timedelta

fake = Faker()

# Event types given by mentor
event_types = [
    "face_absent",
    "face_detected",
    "tab_switched",
    "focus_loss",
    "question_answered"
]

# CSV file
filename = "log_generator.csv"

# Store generated data
data = []

# Generate data for 10 candidates
for i in range(10):

    session_id = f"SES{i + 1:03d}"
    candidate_name = fake.name()

    # Generate random number of events for each candidate
    number_of_events = random.randint(10, 20)

    start_time = datetime.now()

    for j in range(number_of_events):

        event_type = random.choice(event_types)

        timestamp = start_time + timedelta(
            seconds=random.randint(10, 300) * j
        )

        data.append([
            session_id,
            candidate_name,
            event_type,
            timestamp.strftime("%Y-%m-%d %H:%M:%S")
        ])


# Write data into CSV
with open(filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "session_id",
        "candidate_name",
        "event_type",
        "timestamp"
    ])

    # Data
    writer.writerows(data)


print(f"Successfully generated fake data for 10 candidates.")
print(f"Data saved to {filename}")