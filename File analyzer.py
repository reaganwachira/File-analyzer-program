from collections import Counter
import os

def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count the number of lines
        lines = content.splitlines()
        num_lines = len(lines)

        # Count the number of words
        words = content.split()
        num_words = len(words)

        # Count the number of characters
        num_chars = len(content)

        # Calculate the average word length
        if num_words > 0:
            avg_word_length = sum(len(word) for word in words) / num_words
        else:
            avg_word_length = 0

        # Find the most common word
        if num_words > 0:
            word_counts = Counter(words)
            most_common_word, most_common_word_count = word_counts.most_common(1)[0]
        else:
            most_common_word = None

        # Print the results
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
        print(f"Average word length: {avg_word_length:.2f}")
        if most_common_word:
            print(f"Most common word: {most_common_word} (appeared {most_common_word_count} times)")
        else:
            print("Most common word: None")
        
        # Write the results to analysis.txt
        with open('analysis.txt', 'w') as output_file:
            output_file.write(f"Number of lines: {num_lines}\n")
            output_file.write(f"Number of words: {num_words}\n")
            output_file.write(f"Number of characters: {num_chars}\n")
            output_file.write(f"Average word length: {avg_word_length:.2f}\n")
            if most_common_word:
                output_file.write(f"Most common word: {most_common_word} (appeared {most_common_word_count} times)\n")
            else:
                output_file.write("Most common word: None\n")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the name of the text file to analyze: ")
    analyze_file(filename)

if __name__ == "__main__":
    main()
