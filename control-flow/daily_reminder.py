# daily_reminder.py

# prompt the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time_bound? (yes/no): ").strip().lower ()

#Use match_case to handle priority
match priority:
     case "high":
          reminder = f"Reminder: '{task}' is a high priority task"
     case "medium": 
          reminder = f"Reminder: '{task}' is a medium priority task"
     case "low":
          reminder =f"Note: '{task} is a low priority task"
     case _:
          reminder = f"Note: '{task}' has an unknown priority level"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
   if priority == "low":
        #low prioriity but time_bound(special message)
        reminder += "that should be addressed soon."
   else:
        reminder += "that requires immediate attention today!"
else:
     if priority == "low":
          reminder += ". Consider completing it when you have free time."
     else:
          reminder += "."
print("\n" + reminder)
      
#Bonus: Loop to confirm completion(optional)
while True:
      done = input("\nHave you completed this task? (yes/no): ").strip().lower()
      if done == "yes":
             print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
             print("\n🚀 Click here to tweet! 🚀")
             break
      elif done == "no":
                  print ("Keep going! You can do it!")
      else:
                    print("Please answer with 'yes' or 'no'.")
