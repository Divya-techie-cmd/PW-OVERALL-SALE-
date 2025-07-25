import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

num_records = 10000

# Generate user IDs
user_ids = [f"PW{100000 + i}" for i in range(num_records)]

# Enrollment dates (random dates between 2019-01-01 and 2024-07-01)
enrollment_dates = pd.to_datetime(np.random.choice(pd.date_range('2019-01-01', '2024-07-01'), num_records))

# Course categories
course_categories = ['JEE', 'NEET', 'UPSC', 'Commerce', 'SSC', 'GATE', 'Skill Development']
courses = np.random.choice(course_categories, num_records, p=[0.3, 0.25, 0.1, 0.1, 0.1, 0.05, 0.1])

# Subscription types
subscription_types = ['Free', 'Paid Monthly', 'Paid Yearly']
subs_probs = [0.4, 0.4, 0.2]
subscriptions = np.random.choice(subscription_types, num_records, p=subs_probs)

# Revenue per user (₹)
def revenue(sub):
    if sub == 'Free':
        return 0
    elif sub == 'Paid Monthly':
        return random.choice([499, 699, 999])
    else:
        return random.choice([4999, 6999, 8999])

revenues = [revenue(sub) for sub in subscriptions]

# Cities (simplified tier classification)
cities_tier1 = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad', 'Kolkata']
cities_tier2 = ['Pune', 'Ahmedabad', 'Lucknow', 'Nagpur', 'Kanpur']
cities_tier3 = ['Varanasi', 'Gaya', 'Dehradun', 'Muzaffarpur', 'Jamshedpur']
cities = []
for _ in range(num_records):
    tier = np.random.choice(['Tier 1', 'Tier 2', 'Tier 3'], p=[0.4, 0.35, 0.25])
    if tier == 'Tier 1':
        cities.append(np.random.choice(cities_tier1))
    elif tier == 'Tier 2':
        cities.append(np.random.choice(cities_tier2))
    else:
        cities.append(np.random.choice(cities_tier3))

# User type
user_types = ['Online', 'Offline']
user_type_probs = [0.85, 0.15]
user_types_arr = np.random.choice(user_types, num_records, p=user_type_probs)

# Language
languages = ['Hindi', 'English', 'Regional']
lang_probs = [0.5, 0.3, 0.2]
languages_arr = np.random.choice(languages, num_records, p=lang_probs)

# Create DataFrame
df = pd.DataFrame({
    'user_id': user_ids,
    'enrollment_date': enrollment_dates,
    'course_category': courses,
    'subscription_type': subscriptions,
    'revenue_per_user': revenues,
    'city': cities,
    'user_type': user_types_arr,
    'language': languages_arr
})

# Save to CSV
df.to_csv('physics_wallah_synthetic_dataset.csv', index=False)

print("Synthetic dataset with 10,000 records generated and saved as 'physics_wallah_synthetic_dataset.csv'.")
