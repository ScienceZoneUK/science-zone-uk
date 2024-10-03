# Week 4: Lists and Arrays - Class Activity

# Start by creating a variable to store data in a list
playlist = []
end = False

while (end != True):

    print("Manage the playlist")
    choice = input("Do you want to add, view or delete a song").lower()

    if choice == "add":
        song = input("What song do you want to add?")
        playlist.append(song)
      
    elif choice == "delete":
        song = input("What song do you want to delete?")
        playlist.remove(song)

    elif choice == "view":
        print(playlist)

    else:
        print("Please write the commands, add, view or delete")

