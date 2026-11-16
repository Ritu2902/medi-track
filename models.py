class Medication:
    def __init__(self, name, dosage, frequency, time_of_day, notes=""):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency  
        self.time_of_day = time_of_day 
        self.notes = notes
        self.taken_today = False
    
    def to_dict(self):
        return {
            "name": self.name,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "time_of_day": self.time_of_day,
            "notes": self.notes,
            "taken_today": self.taken_today
        }
    
    @staticmethod
    def from_dict(data):
        med = Medication(
            data["name"],
            data["dosage"],
            data["frequency"],
            data["time_of_day"],
            data.get("notes", "")
        )
        med.taken_today = data.get("taken_today", False)
        return med
    
    def __str__(self):
        status = "✓ TAKEN" if self.taken_today else "✗ NOT TAKEN"
        return f"{self.name} | {self.dosage} | {self.frequency} | {self.time_of_day} | {status}"