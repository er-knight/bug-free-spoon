import argparse

def calculate_sloc(file_path: str) -> dict:
    stats = {
        "physical" : 0,
        "source"   : 0,
        "comment"  : {
            "single-line" : 0,
            "multi-line"  : 0,
            "total"       : 0
        },
        "empty"    : 0
    }
    with open(file_path, "r") as f:

        comment_begin  = False
        comment_end    = False
        comment_symbol = None  # """ or '''

        for line in f.readlines():
            stats["physical"] += 1

            line = line.strip()

            if not line:
                stats["empty"] += 1
            elif comment_begin and not comment_end:
                stats["comment"]["multi-line"] += 1
                stats["comment"]["total"] += 1
            elif line.startswith("#"):
                stats["comment"]["single-line"] += 1
                stats["comment"]["total"] += 1
            elif line.startswith("\"\"\""):
                if comment_begin and comment_symbol == "\"\"\"":
                    comment_end    = True
                    comment_symbol = None 
                else:
                    comment_begin  = True
                    comment_symbol = "\"\"\""
                stats["comment"]["multi-line"] += 1
                stats["comment"]["total"] += 1
            elif line.startswith("'''"):
                if comment_begin and comment_symbol == "'''":
                    comment_end    = True
                    comment_symbol = None
                else:
                    comment_begin  = True
                    comment_symbol = "'''"
                stats["comment"]["multi-line"] += 1
                stats["comment"]["total"] += 1
            else:
                stats["source"] += 1

    return stats

def write_to_json(stats: dict) -> None:...

def write_to_csv(stats: dict) -> None:...

def write_to_cli(stats: dict) -> None:
    print(f"           physical : {stats['physical']}")
    print(f"             source : {stats['source']}")
    print(f"            comment : {stats['comment']['total']}")
    print(f"single-line comment : {stats['comment']['single-line']}")
    print(f" multi-line comment : {stats['comment']['multi-line']}")
    print(f"              empty : {stats['empty']}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--file-path", "-p", type=str)
    parser.add_argument("--format", "-f", type=str, choices=["csv", "json"])

    args = parser.parse_args()

    stats = calculate_sloc(args.file_path)

    if args.format == None:
        write_to_cli(stats)
    if args.format == "csv":
        write_to_csv(stats)
    if args.format == "json":
        write_to_json(stats)

# bug: multiline comment counting not working

# https://en.wikipedia.org/wiki/Source_lines_of_code
# https://github.com/flosse/sloc