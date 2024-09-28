import json
import os

class StakeholderCommunicationTool:
    def _init_(self, filename='stakeholder_data.json'):
        self.filename = filename
        self.stakeholders = []
        self.communication_logs = []
        self.meetings = []
        self.outcomes = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.stakeholders = data.get("stakeholders", [])
                self.communication_logs = data.get("communication_logs", [])
                self.meetings = data.get("meetings", [])
                self.outcomes = data.get("outcomes", [])

    def save_data(self):
        data = {
            "stakeholders": self.stakeholders,
            "communication_logs": self.communication_logs,
            "meetings": self.meetings,
            "outcomes": self.outcomes,
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_stakeholder(self, name):
        stakeholder = {"id": len(self.stakeholders) + 1, "name": name}
        self.stakeholders.append(stakeholder)
        self.save_data()
        return stakeholder

    def create_communication_log(self, stakeholder_id, method, summary, date_time):
        if not self.get_stakeholder(stakeholder_id):
            print("Error: Stakeholder ID not found.")
            return None
        
        log = {
            "id": len(self.communication_logs) + 1,
            "stakeholder_id": stakeholder_id,
            "method": method,
            "summary": summary,
            "date_time": date_time,
        }
        self.communication_logs.append(log)
        self.save_data()
        return log

    def schedule_meeting(self, stakeholder_id, date_time, agenda):
        if not self.get_stakeholder(stakeholder_id):
            print("Error: Stakeholder ID not found.")
            return None
        
        meeting = {
            "id": len(self.meetings) + 1,
            "stakeholder_id": stakeholder_id,
            "date_time": date_time,
            "agenda": agenda,
        }
        self.meetings.append(meeting)
        self.save_data()
        return meeting

    def log_outcome(self, communication_log_id, description):
        if not self.get_communication_log(communication_log_id):
            print("Error: Communication log ID not found.")
            return None
        
        outcome = {
            "id": len(self.outcomes) + 1,
            "communication_log_id": communication_log_id,
            "description": description,
        }
        self.outcomes.append(outcome)
        self.save_data()
        return outcome

    def get_stakeholder(self, stakeholder_id):
        for stakeholder in self.stakeholders:
            if stakeholder["id"] == stakeholder_id:
                return stakeholder
        return None

    def get_communication_log(self, log_id):
        for log in self.communication_logs:
            if log["id"] == log_id:
                return log
        return None

    def get_meeting(self, meeting_id):
        for meeting in self.meetings:
            if meeting["id"] == meeting_id:
                return meeting
        return None

    def get_outcome(self, outcome_id):
        for outcome in self.outcomes:
            if outcome["id"] == outcome_id:
                return outcome
        return None

    def display_menu(self):
        print("\n--- Stakeholder Communication Tool Menu ---")
        print("1. Create Stakeholder")
        print("2. Create Communication Log")
        print("3. Schedule Meeting")
        print("4. Log Outcome")
        print("5. Retrieve Stakeholder")
        print("6. Retrieve Communication Log")
        print("7. Retrieve Meeting")
        print("8. Retrieve Outcome")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-9): ")

            if choice == '1':
                name = input("Enter stakeholder name: ")
                stakeholder = self.create_stakeholder(name)
                print("Stakeholder created:", stakeholder)

            elif choice == '2':
                stakeholder_id = int(input("Enter stakeholder ID: "))
                method = input("Enter communication method (e.g., email, phone): ")
                summary = input("Enter communication summary: ")
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
                log = self.create_communication_log(stakeholder_id, method, summary, date_time)
                print("Communication Log created:", log)

            elif choice == '3':
                stakeholder_id = int(input("Enter stakeholder ID: "))
                date_time = input("Enter meeting date and time (YYYY-MM-DD HH:MM:SS): ")
                agenda = input("Enter meeting agenda: ")
                meeting = self.schedule_meeting(stakeholder_id, date_time, agenda)
                print("Meeting scheduled:", meeting)

            elif choice == '4':
                communication_log_id = int(input("Enter communication log ID: "))
                description = input("Enter outcome description: ")
                outcome = self.log_outcome(communication_log_id, description)
                print("Outcome logged:", outcome)

            elif choice == '5':
                stakeholder_id = int(input("Enter stakeholder ID: "))
                retrieved_stakeholder = self.get_stakeholder(stakeholder_id)
                print("Retrieved Stakeholder:", retrieved_stakeholder)

            elif choice == '6':
                log_id = int(input("Enter communication log ID: "))
                retrieved_log = self.get_communication_log(log_id)
                print("Retrieved Communication Log:", retrieved_log)

            elif choice == '7':
                meeting_id = int(input("Enter meeting ID: "))
                retrieved_meeting = self.get_meeting(meeting_id)
                print("Retrieved Meeting:", retrieved_meeting)

            elif choice == '8':
                outcome_id = int(input("Enter outcome ID: "))
                retrieved_outcome = self.get_outcome(outcome_id)
                print("Retrieved Outcome:", retrieved_outcome)

            elif choice == '9':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

# Run the menu-driven tool
tool = StakeholderCommunicationTool()
tool.run()
