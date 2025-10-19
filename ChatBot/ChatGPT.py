import google.generativeai as genai

# Configure the API key
# It's generally not recommended to hardcode API keys directly in your script.
# Consider using environment variables or a secure configuration management system.
genai.configure(api_key="AIzaSyCyj2wCeevB2xkKVHItw3nbCtBYX4F8WEc")  # Replace "YOUR_API_KEY" with your actual API key

# Initialize the Generative Model
# The class name should be 'GenerativeModel', not 'GenerativeAiModel'
model = genai.GenerativeModel(
    "gemini-2.5-flash")  # 'gemini-2.0-flash' is not a valid model name, 'gemini-1.5-flash' is a current option.

# Start a chat session
chat = model.start_chat(history=[])  # It's good practice to explicitly pass an empty history for a new chat


#response = chat.send_message("analyse these sentances into xphrases and words starting with the words and building up into phrases as bullet points format with - instead of *.  ")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    try:
        #response = chat.send_message("analyse these sentances into x-phrases and words using syntactic rules starting with the words and building up into phrases only the words and phrases without labeling or redundant syntactic units as bullet points format with - instead of *." + user_input)
        #response = chat.send_message("devide this text into visual meaningful xphrases as bullet points format with - instead of *." + user_input)

        #poetry is testing your ability to groot yourself
        response = chat.send_message("Perform a bottom-up syntactic constituency analysis on the given sentences. Begin by identifying each word as its own constituent. Then, iteratively combine adjacent words and/or existing constituents *only when they form a larger, syntactically valid phrase*. Each combination must strictly adhere to the rules of English syntax, ensuring that every derived phrase functions as a cohesive grammatical unit. The output should exclusively list these derived words and phrases, starting with the words building up the phrases, strictly without any explicit grammatical category labels (e.g., NP, VP, PP) or any redundant sub-phrases (i.e., if 'a red car' is a phrase, do not also list 'red car' separately, as 'a red car' is the more complete nominal unit for that span). Format the analysis as a bulleted list, using a hyphen (-) for each entry." + user_input)
        #response = chat.send_message("Then the first layer of phrases until it ends up with the sentence separating each level, perform a bottom-up syntactic constituency analysis on the given sentences. Begin by identifying each word as its own constituent. From these initial constituents, iteratively combine adjacent words and/or existing constituents *only when they form a larger, syntactically valid phrase*. Each combination must strictly adhere to the rules of English syntax, ensuring that every derived phrase functions as a cohesive grammatical unit. The output should exclusively list these derived words and phrases, ordered by their length and complexity (from individual words to the full sentence), strictly without any explicit grammatical category labels (e.g., NP, VP, PP) or any redundant sub-phrases (i.e., if 'a red car' is a phrase, do not also list 'red car' separately, as 'a red car' is the more complete nominal unit for that span). Format the analysis as a bulleted list, using a hyphen (-) for each entry." + user_input)
        #response = chat.send_message(user_input)
        print("Gemini: ", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your API key is correct and the model name is valid.")