from medication_manager import MedicationManager
from utils import *

def main():
    manager = MedicationManager()
    
    while True:
        show_menu()
        choice = get_user_input("Select an option (1-9)")
        
        if choice == "1":
            clear_screen()
            meds = manager.get_all_medications()
            print_medication_list(meds)
            input("Press Enter to continue...")
            
        elif choice == "2":
            clear_screen()
            print_header("ADD NEW MEDICATION")
            
            name = get_user_input("Medication name")
            if not name:
                print(" Name is required!")
                input("Press Enter to continue...")
                continue
                
            dosage = get_user_input("Dosage (e.g., 500mg)")
            frequency = get_user_input("Frequency (e.g., daily, twice daily, weekly)")
            time_of_day = get_user_input("Time of day (e.g., morning, evening, with meals)")
            notes = get_user_input("Notes (optional)")
            
            success, message = manager.add_medication(name, dosage, frequency, time_of_day, notes)
            print(f"\n{' ' if success else ''} {message}")
            input("Press Enter to continue...")
            
        elif choice == "3":
            clear_screen()
            print_header("MARK AS TAKEN")
            meds = manager.get_all_medications()
            if not meds:
                print("No medications to mark!")
                input("Press Enter to continue...")
                continue
                
            print_medication_list(meds)
            name = get_user_input("Enter medication name to mark as taken")
            if name:
                success, message = manager.mark_taken(name)
                print(f"{message}")
            input("Press Enter to continue...")
            
        elif choice == "4":
            clear_screen()
            print_header("REMOVE MEDICATION")
            meds = manager.get_all_medications()
            if not meds:
                print("No medications to remove!")
                input("Press Enter to continue...")
                continue
                
            print_medication_list(meds)
            name = get_user_input("Enter medication name to remove")
            if name:
                confirm = input(f"Are you sure you want to remove '{name}'? (y/n): ").lower()
                if confirm == 'y':
                    success, message = manager.remove_medication(name)
                    print(f"\n {message}")
                else:
                    print(" Operation cancelled")
            input("Press Enter to continue...")
            
        elif choice == "5":
            clear_screen()
            print_header("TODAY'S SUMMARY")
            taken, not_taken = manager.get_today_summary()
            
            print(f"\nTotal Medications: {len(taken) + len(not_taken)}")
            print(f"✓ Taken: {len(taken)}")
            print(f"✗ Not Taken: {len(not_taken)}")
            
            if taken:
                print_medication_list(taken, "✓ Medications Taken Today")
            if not_taken:
                print_medication_list(not_taken, "✗ Medications Not Taken Today")
            
            input("Press Enter to continue...")
            
        elif choice == "6":
            clear_screen()
            print_header("SEARCH MEDICATIONS")
            search_term = get_user_input("Enter search term (name or notes)")
            if search_term:
                results = manager.search_medication(search_term)
                if results:
                    print_medication_list(results, f"Search Results for '{search_term}'")
                else:
                    print(f" No results found for '{search_term}'")
            input("Press Enter to continue...")
            
        elif choice == "7":
            clear_screen()
            print_header("UPDATE MEDICATION")
            meds = manager.get_all_medications()
            if not meds:
                print("No medications to update!")
                input("Press Enter to continue...")
                continue
                
            print_medication_list(meds)
            old_name = get_user_input("Enter the name of the medication to update")
            if old_name:
                current_med = None
                for med in meds:
                    if med.name.lower() == old_name.lower():
                        current_med = med
                        break
                
                if current_med:
                    print(f"\nCurrent values for {old_name}:")
                    print(f"  Dosage: {current_med.dosage}")
                    print(f"  Frequency: {current_med.frequency}")
                    print(f"  Time of day: {current_med.time_of_day}")
                    print(f"  Notes: {current_med.notes}")
                    print("\n(Leave blank to keep current value)\n")
                    
                    new_name = get_user_input("New name", current_med.name)
                    dosage = get_user_input("New dosage", current_med.dosage)
                    frequency = get_user_input("New frequency", current_med.frequency)
                    time_of_day = get_user_input("New time of day", current_med.time_of_day)
                    notes = get_user_input("New notes", current_med.notes)
                    
                    success, message = manager.update_medication(
                        old_name, new_name, dosage, frequency, time_of_day, notes
                    )
                    print(f"\n {message}")
                else:
                    print(f" Medication '{old_name}' not found!")
            input("Press Enter to continue...")
            
        elif choice == "8":
            clear_screen()
            print_header("RESET DAILY STATUS")
            confirm = input("⚠️ Reset all 'taken' statuses for today? (y/n): ").lower()
            if confirm == 'y':
                message = manager.reset_daily()
                print(f" {message}")
            else:
                print(" Operation cancelled")
            input("Press Enter to continue...")
            
        elif choice == "9":
            # Exit
            clear_screen()
            print_header("THANK YOU!")
            print(" Your medication data has been saved.")
            print("Have a healthy day! \n")
            break
            
        else:
            print(" Invalid option! Please select 1-9")
            input("Press Enter to continue...")

if __name__ == "__main__":
    clear_screen()
    print(" Welcome to Medi-Track System! ")
    print("Your personal medication tracking assistant\n")
    input("Press Enter to start...")
    clear_screen()
    main()