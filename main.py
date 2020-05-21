points = 0
solved_challenges = [""]
all_challenges = ["Warm up", "Bases", "Bases_again", "VaultDoor0", "VaultDoor1", "VaultDoor2", "The numbers", "Caesar", "Easy Crypto"]
def sequence8() :
    print("So you like drawing..\nHow many test cases of diamonds do you want?\n")
    t = int(input())
    for i in range(t):
        row = int(input("Enter the number of rows: "))
        col = int(input("Enter the number of columns: "))
        size = int(input("Enter the size (height) of the diamonds: "))
        size=size*2 # for the pattern as 1 diamond takes up 2 cols and 2 rows
        row=row*size # ^2 cause o the bottom half of the diamond
        col=col*size # because of the size of each diamond

        for j in range(row):
            a=size/2-1-j%size
            b=size/2+j%size
            if (j%size>=size/2):
                b=0
            for k in range(col):
                if abs((k+j))%size==size/2-1 :
                    print("/", end = "")
                    if (j%size<size/2):
                        b+=size
                    else:
                        b=a+1

                elif (abs((k-j))%size==size/2) :
                    print("\\", end = "")
                    if (j%size<size/2):
                        a+=size
                    else :
                        a=b+size-1

                elif (j%size==0 or (j+1)%size==0):
                    print(".", end = "")
                else:
                    if j%size<size/2:
                        if k>a and k<b:
                            print("*", end = "")
                        else:
                            print(".", end = "")
                    else:
                        if k>b and k<a:
                            print("*", end = "")
                        else:
                            print(".", end = "")


            print("\n")

def general_skills():
    option = 0
    global points # to modify the points variable
    while option!=4:
        try:
            print("\nLet's see what you can do. I got you 3 challenges:")
            print("1. Warm up (50 points)")
            print("2. Bases (100 points)")
            print("3. Bases_again (150 points)")
            print("4. Return to general skills menu")
            option = int(input("Choose a challenge: "))
            if option > 4 or option < 1:
                print("Invalid option!!\n")
            else:
                if option == 1:
                    answer = input("\n[*] If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? ")
                    if answer == "p":
                        if "Warm up" not in solved_challenges:
                            print("That is correct! You've gained 50 points!!\n")
                            solved_challenges.append("Warm up")
                            points += 50

                        else:
                            print("That is correct! However, you've already solved the problem\n")
                    else:
                        print("Too bad. Try again next time!\n")
                elif option == 2:
                    print("\n[*] What does this mean? I think it has something to do with bases:\nbDNhcm5fdGgzX3IwcDM1\n")
                    answer = input("Answer: ")
                    if answer == "l3arn_th3_r0p35":
                        if "Bases" not in solved_challenges:
                            print("That is correct! You've gained 100 points!!\n")
                            solved_challenges.append("Bases")
                            points += 100
                        else:
                            print("That is correct! However, you've already solved the problem\n")
                    else:
                        print("Too bad. Try again next time!\n")
                elif option == 3:
                    print("Check this one out. They seem to be random: ")
                    print("\n226833785f336e433064316e675f6172336e27745f744861545f6241645f72316748543f22")
                    print("[*] Hint: Hmm... It seems like the characters don't exceed a certain range. Also, think about all the bases that you know!\n")
                    answer = input("Answer: ")
                    if answer == "h3x_3nC0d1ng_ar3n't_tHaT_bAd_r1gHT?":
                        if "Bases_again" not in solved_challenges:
                            print("That is correct! You've gained 150 points!!\n")
                            solved_challenges.append("Bases_again")
                            points+=150
                        else:
                            print("That is correct! However, you've already solved the problem\n")
                    else:
                        print("Too bad. Try again next time!\n")
        except ValueError:
            print("Invalid option!!\n\n")

 # Reverse Engineering
def reverse():
    option = 0
    global points
    while option!=4:
        try:
            print("\nReverse engineering is quite annoying. Dare coming here, you must be good.")
            print("If you don't know some java, this is gonna be a pain in the *ss. But I'll show mercy, I've cut out most of the programs @@. \nJust gonna give you the most important snippets of the code :)")
            print("Let's see your skills: ")
            print("1. VaultDoor0 (50 points)")
            print("2. VaultDoor1 (100 points)")
            print("3. VaultDoor2 (150 points)")
            print("4. Return to  reverse engineering menu")
            option = int(input("Choose a challenge: "))
            if option > 4 or option <1:
                print("Invalid option!!\n\n")
                continue
            elif option == 2:
                print("\nCan you mange this? It's quite messed up tho: \n")
                print("""public boolean checkPassword(String password) {
                return password.length() == 32 &&
                password.charAt(0)  == 'd' &&
                password.charAt(29) == '3' &&
                password.charAt(4)  == 'r' &&
                password.charAt(2)  == '5' &&
                password.charAt(23) == 'r' &&
                password.charAt(3)  == 'c' &&
                password.charAt(17) == '4' &&
                password.charAt(1)  == '3' &&
                password.charAt(7)  == 'b' &&
                password.charAt(10) == '_' &&
                password.charAt(5)  == '4' &&
                password.charAt(9)  == '3' &&
                password.charAt(11) == 't' &&
                password.charAt(15) == 'c' &&
                password.charAt(8)  == 'l' &&
                password.charAt(12) == 'H' &&
                password.charAt(20) == 'c' &&
                password.charAt(14) == '_' &&
                password.charAt(6)  == 'm' &&
                password.charAt(24) == '5' &&
                password.charAt(18) == 'r' &&
                password.charAt(13) == '3' &&
                password.charAt(19) == '4' &&
                password.charAt(21) == 'T' &&
                password.charAt(16) == 'H' &&
                password.charAt(27) == 'd' &&
                password.charAt(30) == '8' &&
                password.charAt(25) == '_' &&
                password.charAt(22) == '3' &&
                password.charAt(28) == '0' &&
                password.charAt(26) == '9' &&
                password.charAt(31) == 'f';
                }\n""")
                print("Hint: Look up the charAt() method online.\n")
                answer = input("Can you solve this? Show me your flag: ")
                if answer == "d35cr4mbl3_tH3_cH4r4cT3r5_9d038f":
                    if "VaultDoor1" not in solved_challenges:
                        print("That is correct! You've gained 100 points!!\n")
                        solved_challenges.append("VaultDoor1")
                        points += 100
                    else:
                        print("That is correct! However, you've already solved this problem\n")
                else:
                    print("Thought you were good.... But you couldn't manage this problem :(\n")
            elif option == 1:
                print("\nAlright. I'll go easy on you with this one: \n")
                print("""\npublic boolean checkPassword(String password) {
                return password.equals("w4rm1ng_Up_w1tH_jAv4_fcb79c48f5b");
                } \n""")
                answer = input("It's very easy right? Now give me the flag: ")
                if answer == "w4rm1ng_Up_w1tH_jAv4_fcb79c48f5b":
                    if "VaultDoor0" not in solved_challenges:
                        print("Told ya it was easy! You've gained 50 points\n")
                        solved_challenges.append("VaultDoor0")
                        points += 50
                    else:
                        print("That is correct! However, you've already solved the problem\n")
                else:
                    print("IT'S RIGHT THERE MATEEEEE! HOW COULD YOU GET THIS WRONG...\n")
            elif option == 3:
                print("\nThis is your last one. Ready for it? Don't think you gonna get it tho: ")
                print("""

                        // Each character can be represented as a byte value using its
                        // ASCII encoding. Each byte contains 8 bits, and an int contains
                        // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
                        // example: if the hex string is "01ab", then those can be
                        // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
                        // bytes are represented as binary, they are:
                        //
                        // 0x30: 00110000
                        // 0x31: 00110001
                        // 0x61: 01100001
                        // 0x62: 01100010
                        //
                        // If we put those 4 binary numbers end to end, we end up with 32
                        // bits that can be interpreted as an int.
                        //
                        // 00110000001100010110000101100010 -> 808542562
                        //
                        // Since 4 chars can be represented as 1 int, the 32 character password can
                        // be represented as an array of 8 ints.
                        //
                        // - Minion #7816
                        public int[] passwordToIntArray(String hex) {
                            int[] x = new int[8];
                            byte[] hexBytes = hex.getBytes();
                            for (int i=0; i<8; i++) {
                                x[i] = hexBytes[i*4]   << 24
                                     | hexBytes[i*4+1] << 16
                                     | hexBytes[i*4+2] << 8
                                     | hexBytes[i*4+3];
                            }
                            return x;
                        }

                        public boolean checkPassword(String password) {
                            if (password.length() != 32) {
                                return false;
                            }
                            int[] x = passwordToIntArray(password);
                            return x[0] == 1096770097
                                && x[1] == 1952395366
                                && x[2] == 1600270708
                                && x[3] == 1601398833
                                && x[4] == 1716808014
                                && x[5] == 1734305335
                                && x[6] == 962749284
                                && x[7] == 828584245;
                        }
                        //: indicating comments\n""")
                print("So tell me, ready to give up on this yet?")
                answer = input("You can still try to give me the flag tho: ")
                if answer == "A_b1t_0f_b1t_sh1fTiNg_d79dd25ce3":
                    if "VaultDoor2" not in solved_challenges:
                        print("\nNo, not possible.. Seems like it's not as secure as I think it was")
                        print("You seem to be much more smarter than you look. :)")
                        print("You've gained 150 points and beaten my hardest reverse engineering problem!!\nNow you're officially the master of reverse engineering!!\n")
                        solved_challenges.append("VaultDoor2")
                        points += 150
                    else:
                        print("That is correct! However, you've already beaten this challenge.\n")
                else:
                    print("Told ya. This is impossible to break, well, nearly. Surrender cause you're not smart enough!!")
        except:
            print("\n[!] Invalid option!!\n\n")


def cryptography():
    option = 0
    global points
    while option!=4:
        print("\nAre you good at maths? Cause you're gonna need this for these challenges, I guess..")
        print("1. The numbers (50 points)")
        print("2. Caesar (100 points)")
        print("3. Easy Crypto (150 points)")
        try:
            option = int(input("Choose a challenge: "))
            if option > 4 or option < 1:
                print("Invalid option!!\n\n")
                continue
            elif option == 1:
                print("The numbers, what do they mean?")
                print("20 8 5 14 21 13 2 5 18 19 13 1 19 15 14\n")
                print("[*] Hint: The numbers seem smalll..\n")
                answer = input("Answer: ")
                if answer == "thenumbersmason" or answer == "THENUMBERSMASON":
                    if "The numbers" not in solved_challenges:
                        print("That is correct! You've gained 50 points!!\n")
                        solved_challenges.append("The numbers")
                        points += 50
                    else:
                        print("That is correct! However, you've already solved the problem\n")
                else:
                    print("Too bad.. Don't you realise what the hint is giving you?\n")
            elif option == 2:
                print("Try this one. The name is kinda the hint anyway: ")
                print("rgdhhxcviwtgjqxrdcdydkefyh\n")
                answer = input("Answer: ")
                if answer == "crossingtherubiconojovpqjs":
                    if "Caesar" not in solved_challenges:
                        print("That is correct! You've gained 100 points!!\n")
                        solved_challenges.append("Caesar")
                        points += 100
                    else:
                        print("That is correct! However, you've already solved the problem")
                else:
                    print("Wrong! Try to bruteforce all the possibilities and see which one makes sense\n")
            elif option == 3:
                print("This one is a hard one. Let's see if you're as smart as I think: ")
                print("-- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ---.. .---- ---.. ..--- ..--- ....- ..... --... .....\n")
                print("No hint :) Beat this if you can :O")
                answer = input("Answer: ")
                if answer == "M0RS3C0D31SFUN1818224575":
                    if "Easy Crypto" not in solved_challenges:
                        print("Very smart! You've beaten my hardest cryptography riddle!\n")
                        solved_challenges.append("Easy Crypto")
                        points += 150
                    else:
                        print("That is correct! However, you've already solved the problem")
                else:
                    print("Too bad you can't solve this. Seems like I've outsmarted you :O\n")
        except:
            print("Invalid option!!\n\n")

def menu_CTF():
    option = 0
    while (option!= 4):
        print("\n\nIt's a small project, so there are only 3 categories: \n")
        print("1. General skills")
        print("2. Reverse engineering")
        print("3. Cryptography")
        print("4. Return to main menu")
        try:
            option = int(input("Choose one category: "))
            if (option > 4 or option<1) :
                print("Please enter a valid option!\n\n")
                continue
            elif option == 1:
                general_skills()
            elif option == 2:
                reverse()
            elif option == 3:
                cryptography()
        except:
            print("Invalid option!!\n")





def menu():
  print("\n********************************************************************************************************")
  print("*  Welcome to my small project!                                                                        *")
  print("*  Play my CTF challenges to gain points and compete with your friends!                                *")
  print("********************************************************************************************************")
  print("1. Draw diamonds")
  print("2. Play CTF")
  print("3. Check my current scores and unsolved challenges")
  print("4. Quit")
  print("Enter your option: ")

def main():
    global points
    name = input("Please enter your name: ")
    option = 0
    while (option!=4):
        menu()
        try:
            option = int(input())
            if (option > 4 or option<1) :
                print("Please enter a valid option!\n\n")
                continue
            else:
                if option == 1:
                    sequence8()
                elif option == 2:
                    menu_CTF()
                elif option == 3:
                    unsolved = set(all_challenges).difference(set(solved_challenges))
                    print("\n[*] You are {} and you're currently having {} points".format(name, points))
                    print("Unsolved challenges: ")
                    for i in unsolved:
                        print("\t- {}".format(i))
                elif option == 4:
                    unsolved = set(all_challenges).difference(set(solved_challenges))
                    file = open("user.txt", "w")
                    file.write("Username: {}\n".format(name))
                    file.write("Points: {}\n".format(points))
                    file.write("Unsolved challenges: \n")
                    for i in unsolved:
                        file.write("\t- {}\n".format(i))
        except:
            print("Invalid option!!\n")
main()
