def sort_alphabets(input_string):
    return ''.join(sorted(input_string))

if __name__ == "__main__":
    input_string = "martialarts"
    sorted_string = sort_alphabets(input_string)
    print(f"Sorted alphabets: {sorted_string}")