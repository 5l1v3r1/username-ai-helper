# This is the main file which will be utilized by all platforms
import urllib.request
from urllib.error import HTTPError, URLError
from ast import literal_eval
from random import randint


def check_username(platforms_as_dict, username):
    if len(username) >= 21:
        return "Invalid username: too long"
    else:
        results_dict = {}
        for service in platforms_as_dict:
            print("Testing: " + service)
            if platforms_as_dict[service] == 1:
                match service:
                    case "youtube":
                        results_dict[service] = "unsupported"  # unsupported for now
                    case "reddit":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "twitch":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "steam":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "github":
                        results_dict[service] = check_with_status_code("https://github.com/", username)
                    case "twitter":
                        results_dict[service] = check_with_status_code("https://nitter.net/", username)
                    case "minecraft":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "fortnite":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "pinterest":
                        results_dict[service] = check_with_nordpass(service, username)
                    case "vimeo":
                        results_dict[service] = check_with_nordpass(service, username)
                    case _:
                        print("Unsupported service: " + service)
                        results_dict[service] = "unsupported"
            else:
                continue
        return results_dict


def check_with_nordpass(service, username):
    availability_request = urllib.request.Request(
        url="https://username-checker.nordpass.com/checker?username=" + username + "&website=" + service, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    response_dict_as_string = urllib.request.urlopen(availability_request).read()
    return literal_eval(response_dict_as_string.decode())["status"]


def check_with_status_code(url_begin, username):
    availability_request = urllib.request.Request(
        url=url_begin + username, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    try:
        urllib.request.urlopen(availability_request)
        return "taken"
    except HTTPError as error:
        if error.code == 404:
            return "available"
        else:
            return "error"


def get_random_names(request_amount):
    combined_dictionary = []
    for main_counter in range(request_amount):
        random_names_request = urllib.request.Request(
            url="https://boredhumans.com/api_superhero.php",
            headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
        request_dictionary = urllib.request.urlopen(random_names_request).read().decode().split("\r\n<br />")
        request_dictionary.pop()
        request_dictionary[0] = request_dictionary[0].replace("\n", "")
        for counter in range(len(request_dictionary)):
            request_dictionary[counter] = request_dictionary[counter].split(" ")[0]
            request_dictionary[counter] = request_dictionary[counter].split("-")[0]
            request_dictionary[counter] = request_dictionary[counter].split("/")[0]
            request_dictionary[counter] = request_dictionary[counter].split("'")[0]
        for username in request_dictionary:
            combined_dictionary.append(username)
    return combined_dictionary


def testing_simulate_user_choice(raw_usernames, automated_for_testing=False):
    filtered_usernames = []
    filter_counter = 0
    if not len(raw_usernames) % 4 == 0:
        print("amount of usernames cant be devided by 4(amount: " + str(len(raw_usernames)) + ")")
        exit()
    else:
        for counter in range(0, len(raw_usernames), 4):
            if not automated_for_testing:
                selected_username = input(
                    "Select best username: " + raw_usernames[counter] + "(1); " + raw_usernames[counter + 1] + "(2); " +
                    raw_usernames[counter + 2] + "(3); " + raw_usernames[counter + 3] + "(4)\n")
                filtered_usernames.append(raw_usernames[counter + int(selected_username) - 1])
                filter_counter += 1
            else:
                selected_username = randint(0, 3)
                filtered_usernames.append(raw_usernames[counter + int(selected_username) - 1])
                filter_counter += 1
        return filtered_usernames


def split_usernames(filtered_username):
    # create cut up pieces
    username_pieces = []
    for counter in filtered_username:
        match len(counter):
            case (1 | 2 | 3 | 4 | 5):
                username_pieces.append(counter)
            case (6 | 8):
                username_pieces.append(counter[int(len(counter) / 2):])
                username_pieces.append(counter[0:int(len(counter) / 2)])
            case 7:
                split_point = randint(3, 4)
                username_pieces.append(counter[0:split_point])
                username_pieces.append(counter[split_point:])
            case (9 | 10):
                username_pieces.append(counter[0:3])
                username_pieces.append(counter[3:6])
                username_pieces.append(counter[6:])
            case 11:
                split_point1 = randint(3, 4)
                if split_point1 == 3:
                    split_point2 = 4
                    split_point3 = 4
                else:
                    split_point2 = randint(3, 4)
                    if split_point2 == 3:
                        split_point3 = 4
                    else:
                        split_point3 = 3
                username_pieces.append(counter[0:split_point1])
                username_pieces.append(counter[split_point1:split_point2])
                username_pieces.append(counter[split_point2:split_point3])
                username_pieces.append(counter[split_point3:])
            case 12:
                if randint(3, 4) == 3:
                    username_pieces.append(counter[0:3])
                    username_pieces.append(counter[3:6])
                    username_pieces.append(counter[6:9])
                    username_pieces.append(counter[9:])
                else:
                    username_pieces.append(counter[0:4])
                    username_pieces.append(counter[4:8])
                    username_pieces.append(counter[8:])
            case 13:
                split_point1 = randint(3, 4)
                if split_point1 == 3:
                    split_point2 = 4
                    split_point3 = 4
                    split_point4 = 4
                else:
                    split_point2 = randint(3, 4)
                    if split_point2 == 3:
                        split_point3 = 4
                        split_point4 = 4
                    else:
                        split_point3 = randint(3, 4)
                        if split_point3 == 3:
                            split_point4 = 4
                        else:
                            split_point4 = 3
                username_pieces.append(counter[0:split_point1])
                username_pieces.append(counter[split_point1:split_point2])
                username_pieces.append(counter[split_point2:split_point3])
                username_pieces.append(counter[split_point3:split_point4])
                username_pieces.append(counter[split_point4:])
            case (14 | 15):
                username_pieces.append(counter[0:5])
                username_pieces.append(counter[5:10])
                username_pieces.append(counter[10:])
            case _:
                print('Username "' + counter + '" is too long(' + str(len(counter)) + ")")
    # removing empty strings:
    filtered_dictionary = [x for x in username_pieces if x]
    return filtered_dictionary


def generate_usernames(username_pieces, amount, fix_capitalization=True):
    new_usernames = []
    amount_of_generated = 0
    pieces_amount = len(username_pieces) - 1
    while True:
        if not amount_of_generated == amount:
            generated_username = username_pieces[randint(0, pieces_amount)] + username_pieces[
                randint(0, pieces_amount)] + username_pieces[randint(0, pieces_amount)]
            if len(generated_username) >= 16:
                continue
            else:
                if fix_capitalization:
                    new_usernames.append(generated_username.lower().title())
                else:
                    new_usernames.append(generated_username)
                amount_of_generated += 1
        else:
            break
    return new_usernames


# testing only
'''
def for_testing_only(old_names):
    user_filtered_usernames = testing_simulate_user_choice(old_names, True)
    print("Filtered by user:")
    print(user_filtered_usernames)
    filtered_names = split_usernames(user_filtered_usernames)
    print("Split_names: ")
    print(filtered_names)
    new_names = generate_usernames(filtered_names, 20)
    print("Result: ")
    print(new_names)
    global run_count
    run_count += 1
    print("Run_id: " + str(run_count) + "\n \n")
    for_testing_only(new_names)


# for testing only, remove for release
test_dict = {
    "youtube": 0,  # currently unsupported
    "reddit": 1,
    "twitch": 1,
    "steam": 1,
    "github": 1,
    "twitter": 1,
    "minecraft": 1,
    "fortnite": 1,
    "pinterest": 1,
    "vimeo": 1
}
# print(check_username(test_dict, "test5432"))
# results = []
filtered_names = testing_simulate_user_choice(get_random_names(2), True)
print("filtered_names_first_run: ")
print(filtered_names)
cut_names = split_usernames(filtered_names)
print("pieces_of_filtered_names_first_run: ")
print(cut_names)
results = generate_usernames(cut_names, 20)
print("first_run_results: ")
print(results)
print("First run\n")
run_count = 0

for_testing_only(results)
'''
