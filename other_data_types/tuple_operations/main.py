# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Task 1: Convert the list of new shelf items to a tuple
shelf1_update_tuple = tuple(shelf1_update)

# Task 2: Concatenate the new tuple with the existing tuple
shelf1_concat = shelf1 + shelf1_update_tuple
print("Updated Shelf #1:", shelf1_concat)

# Task 3: Count the number of "celery" in the updated tuple
celery_count = shelf1_concat.count("celery")
print("Number of Celery:", celery_count)

# Task 4: Find the index of "celery" in the updated tuple
celery_index = shelf1_concat.index("celery")
print("Celery Index:", celery_index)