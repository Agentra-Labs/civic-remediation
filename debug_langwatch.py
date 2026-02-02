import langwatch
from dotenv import load_dotenv
load_dotenv()

try:
    prompt = langwatch.prompts.get("sentinel")
    print("\n--- Prompt Object ---")
    print(dir(prompt))
    print("\n--- Prompt Type ---")
    print(type(prompt))
    
    print("\n--- Formatted ---")
    formatted = prompt.format(query="TEST_QUERY")
    print(type(formatted))
    print(formatted)
    
    if isinstance(formatted, list):
        print("\n--- Message 0 ---")
        print(formatted[0])
        print(getattr(formatted[0], 'content', 'No content attr'))
except Exception as e:
    print(e)
