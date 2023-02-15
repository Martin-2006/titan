import datetime
import os

def process_keystrokes(file_path):
    new_text = []
    current_word = ""
    prev_timestamp = None

    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            timestamp_str, key = line.strip().split(" - press: ")
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            if prev_timestamp is None:
                prev_timestamp = timestamp
                current_word += key
                continue

            time_diff = (timestamp - prev_timestamp).total_seconds()
            if time_diff < 2.5:
                current_word += key
            else:
                new_text.append(current_word)
                current_word = " |-=- Eltelt: %s mp -=-|  "%time_diff + str(key)

            prev_timestamp = timestamp

        new_text.append(current_word)

    return (((" ".join(new_text)).replace("space"," ")).replace("shift","")).replace("back"," |> TÖRLÉS <| ")

file_path = os.path.join(os.path.dirname(__file__), 'billentyu.txt')
processed_text = process_keystrokes(file_path)
hely = os.path.join(os.path.dirname(__file__), 'bill-vissza.txt')
with open(hely, "a") as f:
    f.write(processed_text)