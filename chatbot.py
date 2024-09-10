from crm import CRM
import random

# Initialize CRM system
crm_system = CRM()

# Predefined responses for basic questions
faq_responses = {
    "product": "We offer a variety of products including A, B, and C. Which one would you like to know more about?",
    "pricing": "Our pricing starts at $100 for basic packages. Would you like to know about advanced options?",
    "support": "Our support team is available 24/7. How can we assist you today?",
    "default": "I'm sorry, I don't understand your question. Can you please rephrase it?"
}

# Function to handle user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Respond based on keywords
    if "product" in user_input:
        return faq_responses["product"]
    elif "price" in user_input or "cost" in user_input:
        return faq_responses["pricing"]
    elif "support" in user_input:
        return faq_responses["support"]
    else:
        return faq_responses["default"]

# Function to collect lead information
def collect_lead_info():
    print("Great! We'd love to assist you further. Please provide your details:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    # Store lead in CRM
    crm_system.add_lead(name, email, phone)
    print("Thank you! Your information has been saved. Our team will reach out to you shortly.")

# Main chatbot loop
def run_chatbot():
    print("Welcome to our customer service chatbot! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
        # Ask for lead info if user is interested in product or pricing
        if "product" in user_input or "price" in user_input:
            collect_lead_info()

if __name__ == "__main__":
    run_chatbot()
