from random import choice

def batter():
    return choice([1, 2, 3, 4, "howzthat", 6])

def umpires_decision():
    return choice(["bowled", "stumped", "caught", "not out", "no ball", "lbw"])

def is_out(decision):
    return decision in ["bowled", "caught", "stumped", "lbw"]

def inning(team, total_overs=5):
    ...


if __name__ == "__main__":
    india = [
        {   
            "name"        : "India",
            "runs scored" : 0,
            "over played" : 0.0,
            "run rate"    : 0.0
        },
        {
            "name"        : "R. Sharma",
            "runs scored" : 0,
            "status"      : "didn't bat",
            "balls faced" : 0,
            "strike rate" : 0.0
        },
        {
            "name"        : "V. Sehwag",
            "runs_scored" : 0,
            "status"      : "didn't bat",
            "balls faced" : 0,
            "strike rate" : 0.0
        },
        {
            "name"        : "S. Tendulkar",
            "runs_scored" : 0,
            "status"      : "didn't bat",
            "balls faced" : 0,
            "strike rate" : 0.0
        },
        {
            "name"        : "R. Dravid",
            "runs_scored" : 0,
            "status"      : "didn't bat",
            "balls faced" : 0,
            "strike rate" : 0.0
        },
        {
            "name"        : "MS Dhoni",
            "runs_scored" : 0,
            "status"      : "didn't bat",
            "balls faced" : 0,
            "strike rate" : 0.0
        }
    ]

    inning(india)