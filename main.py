# Smart Attendance System - Algorithm Prototype
import random

# Students in the class
students = ["S101", "S102", "S103", "S104"]
presence_count = {s: 0 for s in students}

TOTAL_DURATION = 60   # minutes
NUM_SAMPLES = 10

def generate_random_times(total_minutes, num_samples):
    """
    Generate unique random time points within total_minutes
    """
    return sorted(random.sample(range(total_minutes), num_samples))

sample_times = generate_random_times(TOTAL_DURATION, NUM_SAMPLES)

print("Random attendance check times (in minutes):")
print(sample_times)

