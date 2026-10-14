
#Survey Feedback Analyzer

# Step 1: Preloaded Feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks

new_feedbacks = int(
    input("Enter the number of new feedbacks you want to add: ")
)

for i in range(new_feedbacks):

    name = input(f"Enter name for feedback {i + 1}: ")
    feedback = input(f"Enter written feedback {i + 1}: ")

    while True:
        try:
            rating = int(
                input(f"Enter rating for feedback {i + 1} (1-5): ")
            )
            if 1 <= rating <= 5:
                break
            else:
                print("Please enter a rating between 1 and 5.")

        except ValueError:
            print("Please enter a valid integer.")

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Text Cleaning

remove_punctuation = (".", ",", "!", "?")

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i].strip()

    for p in remove_punctuation:
        feedback = feedback.replace(p, "")

    feedback = ' '.join(feedback.lower().split())

    feedback_data['Feedback'][i] = feedback


# Step 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0
    word = word.lower()

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word in words:
            count += 1

    return count


print("\nStep 4: Word Count Insights")

print(
    "Number of feedbacks containing 'good':",
    count_word_in_feedbacks("good")
)

print(
    "Number of feedbacks containing 'poor':",
    count_word_in_feedbacks("poor")
)

print(
    "Number of feedbacks containing 'excellent':",
    count_word_in_feedbacks("excellent")
)


# Step 5: Final Summary and Insights

print("\nStep 5: Final Summary and Insights")

# Display the final cleaned feedback_data
print("\nFinal Cleaned Feedback Data:")
print(feedback_data)
# Calculate the average rating
average_rating = (
    sum(feedback_data['Rating']) / len(feedback_data['Rating'])
)
print(f"\nAverage Rating: {average_rating:.2f}")
# Find the feedback with the longest comment
longest_index = 0
for i in range(len(feedback_data['Feedback'])):
    if len(feedback_data['Feedback'][i].split()) > len(
        feedback_data['Feedback'][longest_index].split()
    ):
        longest_index = i
longest_feedback = feedback_data['Feedback'][longest_index]
print("\nFeedback with the Longest Comment:")
print("Name:", feedback_data['Name'][longest_index])
print("Feedback:", longest_feedback)
print("Word Count:", len(longest_feedback.split()))


# Find unique words across all feedbacks

unique_words = set()
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        unique_words.add(word)

print("\nList of Unique Words:")
print(sorted(list(unique_words)))


