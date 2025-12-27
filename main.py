# Smart Attendance System - Algorithm Prototype
import random

# Students in the class
students = ["S101", "S102", "S103", "S104"]
presence_count = {s: 0 for s in students}

TOTAL_DURATION = 60
NUM_SAMPLES = 10

def generate_random_times(total_minutes, num_samples):
    return sorted(random.sample(range(total_minutes), num_samples))

def mock_detected_students():
    """
    Simulate detected students in a time window.
    Some students may appear multiple times.
    """
    detections = []
    num_detections = random.randint(1, len(students))

    for _ in range(num_detections):
        detections.append(random.choice(students))

    return detections

sample_times = generate_random_times(TOTAL_DURATION, NUM_SAMPLES)

print("Attendance check times:", sample_times)
print("-" * 40)

for time_point in sample_times:
    detected = mock_detected_students()
    unique_students = set(detected)

    print(f"Minute {time_point}: detected -> {detected}")
    print(f"Unique counted -> {unique_students}")

    for student in unique_students:
        presence_count[student] += 1

    print("-" * 40)

print("Final presence counts:")
for student, count in presence_count.items():
    print(student, ":", count)


