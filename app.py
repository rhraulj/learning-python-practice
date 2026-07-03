import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError  # Special tool to catch Gemini API errors

try:
    # 1. Load your API key from the hidden .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        # Manually trigger an error if the key is missing entirely
        raise ValueError("GEMINI_API_KEY is completely missing from your .env file!")

    # 2. Initialize the official Gemini Client
    client = genai.Client(api_key=api_key)

    # 3. Open and read your local note file
    print("📖 Reading 'my_note.txt'...")
    with open("my_note.txt", "r") as file:
        note_content = file.read()

    # 4. Construct the prompt
    prompt = f"""
    You are an advanced AI note organizer. Analyze the following note content:
    ---
    {note_content}
    ---
    Provide a 2-sentence summary of the note, followed by exactly 3 relevant hashtags.
    """

    print("🧠 Sending note to Gemini AI...")

    # 5. Call the Gemini model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )

    # 6. Print the result
    print("\n✨ --- AI Analysis Result --- ✨")
    print(response.text)

    # 7. APPEND the results to the bottom of your file
    print("💾 Writing tags back to 'my_note.txt'...")
    with open("my_note.txt", "a") as file:
        file.write("\n\n--- AI TAGS ---\n")
        file.write(response.text)

    print("🎉 Done! Open your my_note.txt file to see the results.")

# --- ERROR HANDLING BLOCKS ---
except FileNotFoundError:
    print("\n❌ Error: I couldn't find 'my_note.txt'. Please check that the file exists in this folder.")

except APIError as e:
    print(f"\n❌ Google Gemini API Error: Something went wrong on the cloud servers.\nDetails: {e}")

except ValueError as e:
    print(f"\n❌ Configuration Error: {e}")

except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")
