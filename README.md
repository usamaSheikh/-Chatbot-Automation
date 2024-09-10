### Running the Project:

Install Required Dependencies:

For this simple project, only Python's built-in libraries like sqlite3 are used. There's no need for external libraries.

### Run the Chatbot:

Start the chatbot by running chatbot.py:
  python chatbot.py
  
### User Interaction:

The user interacts with the chatbot by asking questions about products, pricing, or support.
If the user shows interest in products or pricing, the bot collects lead information and stores it in the CRM.

### Check CRM Data:

After interacting with the chatbot, you can retrieve the stored leads by adding a function to display them, or by checking the SQLite database directly.

### Example code to retrieve leads from the database:

  from crm import CRM
  
  crm_system = CRM()
  leads = crm_system.get_all_leads()
  
  print("Stored Leads:")
  for lead in leads:
      print(lead)
