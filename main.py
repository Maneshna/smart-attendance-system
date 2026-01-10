# Smart Attendance System - Algorithm Prototype
import random

# Students in the class, this can also be done as a data set, to be honest. i will add a real data set very soon. 
students = ["S101", "S102", "S103", "S104"]
presence_count = {s: 0 for s in students}

TOTAL_DURATION = 60  #in seconds
NUM_SAMPLES = 10
PRESENCE_THRESHOLD = 6 

def generate_random_times(total_minutes, num_samples):
    return sorted(random.sample(range(total_minutes), num_samples))

def mock_detected_students():
    """
    Simulate detected students in a time window.
    Might return an empty list 
    """
    detections = []
    num_detections = random.randint(0, len(students))

    for _ in range(num_detections):
        detections.append(random.choice(students))

    return detections

# check times? for random timings
sample_times = generate_random_times(TOTAL_DURATION, NUM_SAMPLES)

print("Attendance check times:", sample_times)
print("=" * 50)

# Present or not...more than 6 = present rest absent 
for time_point in sample_times:
    detected = mock_detected_students()
    unique_students = set(detected)

    print(f"Minute {time_point}: detected -> {detected}")
    print(f"Counted once -> {unique_students}")

    for student in unique_students:
        presence_count[student] += 1

    print("-" * 50)

# report for the attendance 
print("\nFINAL ATTENDANCE REPORT")
print("=" * 60)
print(f"{'Student':<10}{'Seen':<10}{'Status'}")  #for present or absent detection 
print("-" * 60)

for student, count in presence_count.items():
    status = "Present" if count >= PRESENCE_THRESHOLD else "Absent"
    print(f"{student:<10}{count}/10     {status}")



