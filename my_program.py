import argparse
import wrapper
import database

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    subparsers = ap.add_subparsers(help="Commands `new` and `list`", dest="command")

    newParser = subparsers.add_parser("new")
    listParser = subparsers.add_parser("list")

    newParser.add_argument("-t", "--type", help="Type of an activity")
    newParser.add_argument("-p", "--participants", help="Number of participants")
    newParser.add_argument("-pm", "--minprice", help="Minimal price")
    newParser.add_argument("-px", "--maxprice", help="Maximal price")
    newParser.add_argument("-am", "--minaccessibility", help="Minimal accessibility")
    newParser.add_argument("-ax", "--maxaccessibility", help="Maximal accessibility")

    args = ap.parse_args().__dict__
    command = args['command']
    del args['command']
    saver = database.ActivitySaver()
    if command == "new":
        api = wrapper.APIWrapper()
        result = api.request(args)
        if len(result) != 1:
            saver.saveActivity(result)
        else:
            print("There is an error.")
    elif command == "list":
        saver.getLatestActivities()
