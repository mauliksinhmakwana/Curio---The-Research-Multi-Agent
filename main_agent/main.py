from dotenv import load_dotenv
from agents import app
from tools import save_to_file

# Load API Keys
load_dotenv()

def main():
    print("✨ Welcome to Curio: Your Empathetic Research Team ✨")
    topic = input("What would you like us to research for you today? (e.g., 'The future of AI agents'): ")
    
    initial_state = {
        "topic": topic,
        "plan": [],
        "research_notes": [],
        "final_report": ""
    }
    
    # Run the Multi-Agent System
    result = app.invoke(initial_state)
    
    # Output the result
    print("\n" + "="*50)
    print("📜 FINAL REPORT FROM CURIO")
    print("="*50 + "\n")
    print(result['final_report'])
    
    # Use Tool to Save
    save_to_file.invoke(result['final_report'])
    print("\n✅ Process Complete! Check 'research_report.md'.")

if __name__ == "__main__":
    main()
