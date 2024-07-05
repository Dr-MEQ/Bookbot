# Open the file in read mode
file_path = 'books/frankenstein.txt'  # Replace with your file path

def count_letter_frequency(filename):
    with open(filename) as file:
        text = file.read().lower()  # Read the entire file and convert to lowercase
        letter_freq = {}  # Initialize an empty dictionary for letter frequencies

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letter_freq[char] = letter_freq.get(char, 0) + 1

    return letter_freq


# Print the file to the screen
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()
        # Print the content
        # print("File Content:\n", file_content)
        
        # Count the words and print the word count to the screen
        
        # Split the data into separate words
        words = file_content.split()
        # Get the total number of words
        total_words = len(words)
        
        # Count the frequency for each letter that appears in the text
        # 
        filename = file_path  
        result = count_letter_frequency(filename)
        print(result)

        # Print a nice report from the letter frequency dictionary

        print("Letter Frequency Report for " + filename)
        print("==========================================")
        print("Total number of words: ", total_words)
        
        # Sort the dictionary by frequency in descending order

        sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

        # Print the sorted result
        for char, freq in sorted_result:
            print(f"The '{char}' was found {freq} times.")
            

        # End gracefully

        print("==========================================")
        print("End of Report")


        




    
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


