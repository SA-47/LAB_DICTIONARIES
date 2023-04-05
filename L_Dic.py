def get_owner(phone_number):
    phone_book = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983": "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla",

    }
    
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is an invalid number"
    owner = phone_book.get(phone_number)
    if owner is not None:
        return owner
    else:
        return "Sorry, the number is not found"

# Receive phone number input from the user
phone_number = input("Please enter the phone number: ")
# Get the owner and print the result
result = get_owner(phone_number)
print(result)
def move_zeros_to_end(arr):
    non_zeros = [x for x in arr if x != 0]  # Filter out non-zero elements
    zeros = [0] * arr.count(0)  # Create a list of zeros with the same count as in the original list
    return non_zeros + zeros  # Concatenate the non-zero elements with the zero


# Input list
numbers = [5, 0, 34, 9, 0, 13, 8]
# Call the function and print the rearranged list
arranged_list = move_zeros_to_end(numbers)
print(arranged_list)