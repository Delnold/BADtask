import timeit
import main
import main_1
from sample_text import generate_sample_text_array

text_count = 500
array_of_text = generate_sample_text_array(text_count, 1000)
print(array_of_text)


def v_approach(text):
    return main.uniqueChar(text)


def d_approach(text):
    return main_1.uniqueChar(text)

v_success = 0
d_success = 0
for text in array_of_text:
    time_taken_v = timeit.timeit('v_approach(text)', globals=globals(), number=1)
    time_taken_d = timeit.timeit('d_approach(text)', globals=globals(), number=1)
    if time_taken_v < time_taken_d:
        v_success+=1
    else:
        d_success+=1

print(f"Success by the v approach: {v_success} times out of {text_count}", sep="\n")
print(f"Success by the d approach: {d_success} times out of {text_count}")
