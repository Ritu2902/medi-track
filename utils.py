import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_header(title):
    print("\n" + "="*60)
    print(f" {title} ".center(60, "="))
    print("="*60 + "\n")

def print_medication_list(medications, title="Current Medications"):
    if not medications:
        print("No medications to display.\n")
        return
    
    print(f"\n{title}:")
    print("-" * 60)
    for i, med in enumerate(medications, 1):
        print(f"{i}. {med}")
    print("-" * 60 + "\n")

def get_user_input(prompt, default=None):
    if default:
        user_input = input(f"{prompt} (default: {default}): ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def show_menu():
    print_header("MEDI-TRACK SYSTEM")
    print("1. View All Medications")
    print("2. Add New Medication")
    print("3. Mark Medication as Taken")
    print("4. Remove Medication")
    print("5. View Today's Summary")
    print("6. Search Medications")
    print("7. Update Medication")
    print("8. Reset Daily Status")
    print("9. Exit")
    print("\n" + "-"*60)