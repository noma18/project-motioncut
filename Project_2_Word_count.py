def count_words(input_string):
    """
    Counts the number of words in the input string.

    Args:
        input_string (str): The input string to count words from.

    Returns:
        int: The number of words in the input string.
    """
    # Split the input string into a list of words using spaces as separators
    words = input_string.split()
    # Return the number of words in the list
    return len(words)


def main():
    """
    The main function that prompts the user for input, counts the words, and displays the result.
    """
    # Prompt the user to enter a sentence or paragraph
    print("Enter a sentence or paragraph:")
    input_string = input()

    # Check for empty input
    if not input_string:
        print("Error: Input cannot be empty.")
        return

    # Count the words in the input string
    word_count = count_words(input_string)

    # Display the word count to the console
    print(f"The input contains {word_count} words.")


if __name__ == "__main__":
    main()
