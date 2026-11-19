# Q2: Student Marks Analysis (no loops or functions used)

# 1. Create a list of five marks and convert it into a tuple
marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

# 2. Display both collections and their data types
print("Marks list :", marks_list, "->", type(marks_list))
print("Marks tuple:", marks_tuple, "->", type(marks_tuple))

# 3. Highest and lowest marks using built-in operations
highest = max(marks_list)
lowest = min(marks_list)
print("Highest mark:", highest)
print("Lowest mark :", lowest)

# 4. Count students who scored at least 40
# Each comparison gives True (1) or False (0), so adding them counts the passes
passed_count = (
    (marks_list[0] >= 40)
    + (marks_list[1] >= 40)
    + (marks_list[2] >= 40)
    + (marks_list[3] >= 40)
    + (marks_list[4] >= 40)
)
print("Students who scored at least 40:", passed_count)

# 5. Check that all marks are within 0 to 100
# If the lowest is >= 0 and the highest is <= 100, every mark is in range
all_valid = lowest >= 0 and highest <= 100
print("All marks within 0-100:", all_valid)

# 6. Changing one element in the list and one in the tuple
marks_list[1] = 45          # works fine
print("List after change :", marks_list)

# marks_tuple[1] = 45       # uncommenting this line raises:
#                           # TypeError: 'tuple' object does not support item assignment

# Observation: A list is mutable, so its elements can be changed after creation
# (marks_list[1] = 45 worked). A tuple is immutable, so its elements cannot be
# changed once created; trying to assign to marks_tuple[1] gives a TypeError.
# The tuple still holds the original values:
print("Tuple (unchanged) :", marks_tuple)
