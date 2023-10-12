#hangman

import random
secret_words = ["Ability", "Access", "Accident", "Account", "Act", "Action", "Activity", "Actor", "Ad", "Addition", "Address", "Administration", "Advantage", "Advertising", "Advice", "Affair", "Age", "Agency", "Agreement", "Air", "Airport", "Alcohol", "Ambition", "Amount", "Analysis", "Analyst", "Animal", "Answer", "Anxiety", "Apartment", "Appearance", "Apple", "Application", "Appointment", "Area", "Argument", "Army", "Arrival", "Art", "Article", "Aspect", "Assignment", "Assistance", "Assistant", "Association", "Assumption", "Atmosphere", "Attempt", "Attention", "Attitude", "Audience", "Aunt", "Average", "Awareness","Back", "Bad", "Balance", "Ball", "Bank", "Baseball", "Basis", "Basket", "Bath", "Bathroom", "Bedroom", "Beer", "Beginning", "Benefit", "Bird", "Birth", "Birthday", "Bit", "Blood", "Board", "Boat", "Body", "Bonus", "Book", "Boss", "Bottom", "Box", "Boy", "Boyfriend", "Bread", "Breath", "Brother", "Building", "Bus", "Business", "Buyer",
"Cabinet", "Camera", "Cancer", "Candidate", "Capital", "Car", "Card", "Care", "Career", "Case", "Cash", "Cat", "Category", "Cause", "Celebration", "Cell", "Championship", "Chance", "Chapter", "Charity", "Cheek", "Chemistry", "Chest", "Chicken", "Child", "Childhood", "Chocolate", "Choice", "Church", "Cigarette", "City", "Class", "Classroom", "Client", "Climate", "Clothes", "Coast", "Coffee", "Collection", "College", "Combination", "Committee","communication","Dad", "Data", "Database", "Date", "Day", "Dealer", "Death", "Debt", "Decision", "Definition", "Delivery", "Demand", "Department", "Departure", "Depression", "Depth", "Description", "Design", "Desk", "Development", "Device", "Diamond", "Difference", "Difficulty", "Dinner", "Direction", "Director", "Dirt", "Disaster", "Discipline", "Discussion", "Disease", "Disk", "Distribution", "Dog", "Drama", "Drawer", "Drawing", "Driver",
"Ear", "Earth", "Economics", "Economy", "Editor", "Education", "Effect", "Efficiency", "Effort", "Egg", "Election", "Elevator", "Emotion", "Emphasis", "Employee", "Employer", "Employment", "End", "Energy", "Engine", "Entertainment", "Enthusiasm", "Entry", "Environment", "Equipment", "Error", "Establishment", "Estate", "Event", "Exam", "Examination", "Example", "Exchange", "Excitement", "Exercise", "Experience", "Explanation", "Expression", "Extent", "Eye", "Face", "Fact", "Failure", "Family", "Farmer", "Fat", "Feature", "Feedback", "Field", "Figure", "Film", "Finding", "Fire", "Fish", "Flight", "Focus", "Food", "Football", "Force", "Form", "Fortune", "Foundation", "Frame", "Freedom", "Friendship", "Fun", "Funeral", "Future", "Game", "Garbage", "Garden", "Gate", "Gene", "Gift", "Girl", "Girlfriend", "Goal", "Government", "Grandmother", "Grocery", "Group", "Growth", "Guest", "Guidance", "Guide", "Guitar","Hair", "Half", "Hall", "Hand", "Hat", "Head", "Health", "Hearing", "Heart", "Heat", "Height", "Highway", "Historian", "History", "Home", "Homework", "Honey", "Hope", "Hospital", "Hotel", "House", "Housing",
"Ice", "Idea", "Image", "Imagination", "Impact", "Importance", "Impression", "Improvement", "Income", "Independence", "Indication", "Industry", "Inflation", "Information", "Initiative", "Injury", "Insect", "Inside", "Inspection", "Inspector", "Instance", "Instruction", "Insurance", "Intention", "Interaction", "Interest", "Internet", "Introduction", "Investment", "Issue", "Item",
"Job", "Judgment", "Key", "Kind", "King", "Knowledge","Lab", "Ladder", "Lady", "Lake", "Language", "Law", "Leader", "Leadership", "Length", "Level", "Library", "Life", "Light", "Line", "Link", "List", "Literature", "Location", "Loss", "Love",
"Machine", "Magazine", "Maintenance", "Mall", "Man", "Management", "Manager", "Manufacturer", "Map", "Market", "Marketing", "Marriage", "Material", "Math", "Matter", "Meal", "Meaning", "Measurement", "Meat", "Media", "Medicine", "Medium", "Member", "Membership", "Memory", "Menu", "Message", "Metal", "Method", "Midnight", "Mind", "Mixture", "Mode", "Model", "Mom", "Moment", "Money", "Month", "Mood", "Morning", "Mouse", "Movie", "Mud", "Music","Name", "Nation", "Nature", "Negotiation", "Network", "News", "Newspaper", "Night", "Note", "Nothing", "Number",
"Object", "Obligation", "Office", "Oil", "Operation", "Opinion", "Opportunity", "Orange", "Order", "Organization", "Outcome", "Outside", "Oven", "Owner","Page", "Paint", "Painting", "Paper", "Part", "Passenger", "Passion", "Patience", "Payment", "Penalty", "People", "Percentage", "Perception", "Performance", "Period", "Permission", "Person", "Personality", "Perspective", "Philosophy", "Phone", "Photo", "Physics", "Piano", "Picture", "Pie", "Piece", "Pizza", "Place", "Plan", "Platform", "Player", "Poem", "Poet", "Poetry", "Point", "Police", "Policy", "Politics", "Pollution", "Population", "Position", "Possession", "Possibility", "Post", "Pot", "Potato", "Power", "Practice", "Preference", "Preparation",
"Quality", "Quantity", "Queen", "Question", "Radio", "Range", "Rate", "Ratio", "Reaction", "Reality", "Reason", "Reception", "Recipe", "Recognition", "Recommendation", "Record", "Recording", "Reflection", "Refrigerator", "Region", "Relation", "Relationship", "Replacement", "Republic", "Reputation", "Requirement", "Research", "Resolution", "Resource", "Response", "Responsibility", "Restaurant", "Result", "Revenue", "Review", "Revolution", "Risk", "River", "Road", "Rock", "Role", "Room", "Rule",
"Safety", "Salad", "Salt", "Sample", "Satisfaction", "Scale", "Scene", "School", "Science", "Screen", "Secretary", "Section", "Sector", "Security", "Selection", "Sense", "Series", "Service", "Session", "Setting", "Shape", "Share", "Shirt", "Side", "Sign", "Signature", "Significance", "Singer", "Sir", "Sister", "Site", "Situation", "Size", "Skill", "Society", "Software", "Soil", "Solution", "Son", "Song", "Sound", "Soup", "Source", "Space", "Speaker", "Speech", "Sport", "Square", "Standard", "Star", "State", "Statement", "Steak", "Step", "Stock", "Storage", "Store", "Story", "Stranger", "Strategy", "Stress", "Structure", "Student", "Studio", "Study", "Style", "Subject", "Success", "Suggestion", "Sun", "Supermarket", "Surgery", "Sympathy", "System",
"Table", "Tale", "Task", "Tax", "Tea", "Teacher", "Technology", "Television", "Temperature", "Tennis", "Tension", "Term", "Test", "Thanks", "Theory", "Thing", "Thought", "Throat", "Time", "Tongue", "Tool", "Tooth", "Top", "Topic", "Town", "Trade", "Tradition", "Trainer", "Training", "Transportation", "Truth", "Two", "Type","War", "Warning", "Water", "Way", "Weakness", "Wealth", "Weather", "Web", "Wedding", "Week", "While", "Wife", "Wind", "Winner", "Woman", "Wood", "Word", "Work", "Worker", "World", "Writer", "Writing", "Year", "Youth"
]

v = []
win = True
g_limit = 5
guesses = 0
s_word = random.choice(secret_words)
len_s_word = len(s_word)
pos = len_s_word

for i in range(len_s_word):
    v.append('_')

n = input(' \n  \n  \n  \n Hi. What is your name?                               ')

print("""Hi """ + n + """. Lets play Hangman, but first we have to explain the game and its instructions so follow me:
      
      • You will have a blanked word. something like this '_ _ _'. And you need to guess the word.    
      • You will have only 5 guesses before you die.
      • Every letter you get right will be shown.
      • You can only type a word that has the same number of letter the blank has. Example:
          ' _ _ _ _ '. You can't type 'brown' but you can type 'bark'.
      
            ➡ Here is you word. Goodluck:
      
""")

print('            _____________ ')
print('            |          |')
print('            |          |')
print('            |         ⚫')
print('            |         /|\ ')
print('            |         / \ ')
print('           _|____________')










print(' \n  ')
print("                                      ", end="")
print(*v, sep=" ")


print(s_word)

try:
    while (win) and guesses != g_limit:
        user_inp = list(input(' \n   \n        ►  '))
        if user_inp == list(s_word):
                print(' \n  \n ')
                print("                                      ", end="")
                print(*v, sep="   ")
                print(' \n  \n  \n ➡  Exellent job. You guessed my word right!')  
                win = False 
        for pos in range(len_s_word):
            if user_inp[pos] == s_word[pos]:
                v[pos]=s_word[pos]
            else:
                print('')
        if (user_inp[pos] == s_word[pos] or user_inp[pos] != s_word[pos]) and user_inp != list(s_word):
                print('             ➡  You just lost a guess.')
                guesses +=1

        print(' \n  \n ')
        print("                                      ", end="")
        print(*v, sep=" ")
        
        if guesses == 1 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /|\ ')
                    print('            |         /  ')
                    print('           _|____________')
        elif guesses == 2 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /|\ ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses ==3 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |         /| ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses ==4 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         ⚫')
                    print('            |          | ')
                    print('            |           ')
                    print('           _|____________')
        elif guesses == 5 and user_inp != list(s_word):
                    print('            _____________ ')
                    print('            |          |')
                    print('            |          |')
                    print('            |         😵')
                    print('            |          ')
                    print('            |           ')
                    print('           _|____________')

                    print('   \n  \n                     Unfortunatly you lost the game. My word was '+ s_word)
                    win = False

except IndexError:
        print(' \n  \n  \n                 Type a word with the corresponding amount of letters. \n  \n  \n')
        win = False



