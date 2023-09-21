import random
import string

def generate_sample_text_array(num_samples, text_length):
    sample_text_array = []

    for _ in range(num_samples):
        sample_text = generate_sample_text(text_length)
        sample_text_array.append(sample_text)

    return sample_text_array

def generate_sample_text(length):
    characters = string.ascii_letters + string.digits + ' '
    sample_text = ''.join(random.choice(characters + ' ') for _ in range(length))
    return sample_text
