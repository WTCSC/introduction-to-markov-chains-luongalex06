import random
import string


"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "The city skyline gleamed in the distance, its lights flickering like stars against the darkening sky. As she walked through the crowded streets, the noise of the city filled her senses—car engines humming, people chatting, the occasional horn honk. It was the kind of noise that once felt overwhelming but now felt oddly comforting, like a constant hum in the background of her life. She passed the familiar shops and restaurants, each holding its own memories. It was strange to think how much had changed in such a short time, yet how much stayed the same. The streets, the buildings, the people—all moving in a rhythm she’d come to recognize as part of the fabric of her everyday existence. But something was different tonight. There was a subtle shift in the air, a quiet anticipation that buzzed just below the surface. She couldn not put her finger on it, but she felt it in her chest, like the moment before a storm. Her thoughts drifted to the future, to what might lie ahead, and she realized that no matter how much she tried to predict it, life always found a way to surprise her. The unknown had a way of creeping up, catching her off guard, and she was not sure if she was ready for it."


"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
def pre_text(text):
    words = text.split()
    transitions = {}
    
    for i in range(len(words) - 1):
        current_word = words[i].strip(string.punctuation)
        next_word = words[i + 1].strip(string.punctuation)
    
    
        if current_word not in transitions:
            transitions[current_word] = []
        
        transitions[current_word].append(next_word)
    
    return transitions

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""
def generate_text(start_word, num_words, transitions):
    current_word = start_word
    result = [current_word]

    if current_word[0].lower() not in string.punctuation:
        current_word = current_word.capitalize()

    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)


            if next_word[-1] in '.!?':
                next_word = next_word.capitalize()
            
            
        else:
            break
        
        current_word = next_word
    
    return " ".join(result)

transitions = pre_text(text)

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
start_word = input('What is your starting word?: ')
num_words = int(input('How many number of words?: '))
random_sentence = generate_text(start_word, num_words, transitions)

print(random_sentence)

