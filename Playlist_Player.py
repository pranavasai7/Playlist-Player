#Subrahmanya Sree Pranava Sai Maganti
#Creative Idea Assignment
#PlayMusic
#Music Player
#Project-1

""" The below written code works on reading the text file with the list mp3 music files stored in the computer.
After reading the text file, upon running the code, it prints the list of songs. It then plays the song that has been selected.
To make the code complex, I have also put in the pause, resume and stop options which work like pausing, resuming from the pasued spot, and stopping the currently playing song.
I have used pygame module to play the mp3 music files stored into different folders with the respective artist name.
Upon selection of the song in the terminal after the list is printed, firstly it prints the song that is played alongwith the name of the artist.
To avoid error in the code while using in different device, I used the relative path feature which afvoids the use of the entire path of the code.
"""

from pygame import mixer

#This section of the code below read all the line in the text file and separate the entire text with  (comma ','). 
#It also prints the number of lines in the text file by reading the entire file and in the main function asks to select one song from the list. 
#The empty list is created to append each element in the text file.

def loadFile(fileName):
    fileName = "." + fileName
    with open(fileName, 'r') as f:
        contents = f.readlines()

    data = []
    #row = 0
    for line in contents:
        line = line[:len(line)-1]
        line = line.split(',')
        line1 = []
        for element in line:
            element = element.strip()
            line1.append(element)
        #row += 1
        # if row == 1:
        #     pass
        # else:
        data.append(line1)
    return data

#This function is created to read and print the list of songs for selection among all of them.

def display(songs):
    print()
    for music in songs:
        print(music[0],',',music[1],',',music[2])
        print()

#This function is created for playing the song from the relative path mentioned in the code. 
#It not only plays the song, but it also prints the name of the song and that of the artist. 
#This section of code also has a 'while' section wherein it is used to pause or stop the current playing song and resume the song the song from the spot where it was paused. 
#If any other option apart from the [p]ause, [r]esume or [s]top are given, it prints out "Invalid Statement" .
#Also, I have used the (lower) string function which is used to convert the choice [p], [r], and [s] if given in uppercase to lowercase.
    
def playSong(songPath,songName,songArtist,fileName):
    print()
    print("Now Playing",songName,"by",songArtist)

    mixer.init()
    mixer.music.load(songPath)
    mixer.music.play()

    choice1 = ''
    while True:
        print()

        if choice1 == "":
            choice1 = input("Do you wish [p]ause the current song? or [s]top playing the song or [f]restart the song ?")

        else:
            choice1 = input("Do you wish [r]esume the current song? or [s]top playing the song?")

        choice1 = choice1.lower()
        if choice1 == "p":
            mixer.music.pause()
        
        elif choice1 == "r":
            mixer.music.unpause()
            choice1 = ''
        
        elif choice1 == "f":
            mixer.music.rewind()
            choice1 = ''
        
        elif choice1 == "s":
            mixer.music.stop()
            break

        else:
            print("Invalid input... Please try again")
            choice1 = ""
    
 #The main function in the code has code that loads the text file with the list of songs, prints the list of songs. 
 #It also has a section of code that asks for input of the choice for which song to play among the specified range in the terminal upon running. 
 #In the choice section, if the choice is 0, the code breaks and anything else in the range, it prints out the song name, artist and plays the song.
def main():
    print("Welcome to Musical Party")
    print()

    
    print("By: <Subrahmanya Sree Pranava Sai Maganti>")
    print("[COM S 127 <section F & Lab Section 1>]")
    print()

    fnSongs = loadFile("/songs.txt")
    totalSongs = (len(fnSongs)-1)

    while True:
        display(fnSongs)
        print()
        try:
            choice = int(input("Select a song from the List Displayed [1]-[" + str(totalSongs) + "], [0]quit : "))
        except:
            print("Invalid Input !!!")
            print("Please enter an input between the mentioned range above !!! Try Again")
            choice = int(input("Select a song from the List Displayed [1]-[" + str(totalSongs) + "], [0]quit : "))
            
        if choice == 0:
            print("Good Bye !!!")
            break
        else:
            playSong(fnSongs[choice][3],fnSongs[choice][2],fnSongs[choice][1],fnSongs)

        
if __name__ == "__main__":
    main()