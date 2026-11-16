import json
import os
from datetime import datetime
from models import Medication

class MedicationManager:
    def __init__(self, data_file="data/medications.json"):
        self.data_file = data_file
        self.medications = []
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.medications = [Medication.from_dict(item) for item in data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.medications = []
        else:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            self.save_data()
    
    def save_data(self):
        data = [med.to_dict() for med in self.medications]
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_medication(self, name, dosage, frequency, time_of_day, notes=""):
        for med in self.medications:
            if med.name.lower() == name.lower():
                return False, "Medication already exists!"
        
        medication = Medication(name, dosage, frequency, time_of_day, notes)
        self.medications.append(medication)
        self.save_data()
        return True, "Medication added successfully!"
    
    def remove_medication(self, name):
        for i, med in enumerate(self.medications):
            if med.name.lower() == name.lower():
                del self.medications[i]
                self.save_data()
                return True, f"Removed {name} successfully!"
        return False, f"Medication '{name}' not found!"
    
    def mark_taken(self, name):
        for med in self.medications:
            if med.name.lower() == name.lower():
                med.taken_today = True
                self.save_data()
                return True, f"Marked {name} as taken!"
        return False, f"Medication '{name}' not found!"
    
    def reset_daily(self):
        for med in self.medications:
            med.taken_today = False
        self.save_data()
        return "Daily status reset!"
    
    def get_all_medications(self):
        return self.medications
    
    def get_today_summary(self):
        taken = [med for med in self.medications if med.taken_today]
        not_taken = [med for med in self.medications if not med.taken_today]
        return taken, not_taken
    
    def search_medication(self, search_term):
        results = []
        search_term = search_term.lower()
        for med in self.medications:
            if search_term in med.name.lower() or search_term in med.notes.lower():
                results.append(med)
        return results
    
    def update_medication(self, old_name, new_name=None, dosage=None, 
                         frequency=None, time_of_day=None, notes=None):
        for med in self.medications:
            if med.name.lower() == old_name.lower():
                if new_name:
                    med.name = new_name
                if dosage:
                    med.dosage = dosage
                if frequency:
                    med.frequency = frequency
                if time_of_day:
                    med.time_of_day = time_of_day
                if notes is not None:
                    med.notes = notes
                self.save_data()
                return True, f"Updated {old_name} successfully!"
        return False, f"Medication '{old_name}' not found!"