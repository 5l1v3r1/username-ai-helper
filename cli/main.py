import framework
import atexit


def show_tutorial():
    print("You will be presented with a list of 4 usernames. Choose the one you like most."
          "\nKeep choosing the usernames and watch them become more personalized with the power of ai.\n"
          "To end the program press ctrl+c at any point")
    while True:
        if input("Press enter to continue ") == "":
            return
        else:
            continue


def generate_new_usernames(generated_usernames):
    filtered_usernames = framework.split_usernames(user_choose_usernames(generated_usernames))
    new_generated_usernames = framework.generate_usernames(filtered_usernames, 20)
    generate_new_usernames(new_generated_usernames)


def user_choose_usernames(raw_usernames):
    filtered_usernames = []
    filter_counter = 0
    if not len(raw_usernames) % 4 == 0:
        print("Error: amount of usernames can not be divided by 4. (amount: " + str(len(raw_usernames)) + ")")
        exit()
    else:
        for counter in range(0, len(raw_usernames), 4):
            selected_username = input(
                "(" + str(filter_counter + 1) + "/" + str(int(len(raw_usernames) / 4)) + ") Select best username: " +
                raw_usernames[counter] + "(1); " + raw_usernames[counter + 1] + "(2); " + raw_usernames[
                    counter + 2] + "(3); " + raw_usernames[counter + 3] + "(4)\n")
            filtered_usernames.append(raw_usernames[counter + int(selected_username) - 1])
            filter_counter += 1
        return filtered_usernames


def main_loop():
    while True:
        user_input = input("Welcome to username-ai-helper. Press enter to start or t to view the tutorial ")
        if user_input == "":
            # First run
            print("Generating usernames")
            cut_usernames = framework.split_usernames(user_choose_usernames(framework.get_random_names(2)))
            generate_new_usernames(framework.generate_usernames(cut_usernames, 20))
        elif user_input == "T" or "t":
            show_tutorial()
            continue
        else:
            continue


try:
    main_loop()
except KeyboardInterrupt:
    print("\n\n")
    print("Thank you for using username-ai-helper.")
