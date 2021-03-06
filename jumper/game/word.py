import random


class Word:
    """Select a ramdom word in the lists as the secret word"""

    def __init__(self):
        self._list = ["aspiring", "moon", "attempt", "physical", "staking", "pointless", "adventurous", "wail",
                      "chivalrous", "risk", "gruesome", "button", "tacky", "alike", "deafening", "right", "brown",
                      "island", "lamp", "delightful", "oven", "oval", "tree", "ill-informed", "useless", "stone",
                      "describe", "post", "solid", "questionable", "cut", "possible", "nervous", "roof", "tub", "bikes",
                      "listen", "advise", "wiry", "statement", "therapeutic", "twig", "bustling", "alcoholic", "key",
                      "middle", "pedal", "educate", "bushes", "thunder", "admire", "skin", "motion", "abaft",
                      "abundant", "jam", "month", "concerned", "advice", "bleach", "form", "minister", "wind",
                      "complex", "playground", "industry", "chilly", "record", "mom", "last", "literate", "jar", "vase",
                      "daughter", "torpid", "produce", "mess up", "ultra", "thrill", "unaccountable", "mend",
                      "property", "tearful", "insurance", "writing", "interesting", "amount", "ashamed", "telephone",
                      "language", "dependent", "neat", "harbor", "messy", "repulsive", "pocket", "clumsy", "phobic",
                      "nine", "worm", "pizzas", "real", "mundane", "tiny", "release", "stew", "circle", "kiss",
                      "loving", "crack", "exuberant", "wait", "misty", "reward", "reaction", "detailed", "print", "mug",
                      "railway", "oranges", "trap", "finger", "coil", "befitting", "sedate", "smell", "snobbish",
                      "front", "precious", "pies", "glass", "addition", "shocking", "drop", "station", "view", "white",
                      "haircut", "bird", "pinch", "unfasten", "succeed", "stingy", "valuable", "dispensable", "queue",
                      "angle", "historical", "design", "crabby", "word", "man", "education", "wood", "war", "scarf",
                      "wealth", "didactic", "able", "icicle", "jelly", "plantation", "stuff", "sign", "march", "stop",
                      "picture", "regular", "day", "tax", "acrid", "bait", "squirrel", "disapprove", "count",
                      "peaceful", "winter", "macho", "lackadaisical", "tease", "spooky", "stem", "oafish", "brush",
                      "tank", "worry", "enormous", "vigorous", "itchy", "jagged", "dance", "shade", "committee", "whip",
                      "rampant", "existence", "smiling", "frame", "piquant", "doctor", "profit", "letter", "church",
                      "ants", "greasy", "tall", "cub", "voyage", "comfortable", "degree", "little", "private", "zip",
                      "disgusted", "enchanting", "cap", "deceive", "apologise", "rabbit", "mix", "lowly", "acceptable",
                      "legs", "curve", "flavor", "cloth", "craven", "windy", "tawdry", "handle", "multiply", "bare",
                      "sponge", "upset", "blind", "analyze", "imported", "sand", "joke", "earth", "flag", "magnificent",
                      "beneficial", "tender", "rest", "person", "groovy", "theory", "floor",
                      "vivacious", "paint", "moldy", "toes", "rich", "broken", "argument", "sparkle", "rings", "spiky",
                      "follow", "carpenter", "pump", "grouchy", "abiding", "recognise", "gaudy", "own", "naive",
                      "stormy", "luxuriant", "introduce", "great", "jobless", "rob", "allow", "eyes", "yam", "inform",
                      "quaint", "embarrass", "reproduce", "smooth", "tooth", "violet", "noiseless", "cluttered",
                      "scare", "quizzical", "happen", "puzzling", "pig", "art", "harm", "blade", "receptive", "smelly",
                      "quack", "toothsome", "deep", "entertaining", "tart", "skate", "nail", "cheese", "pleasant",
                      "efficient", "arm", "absurd", "mammoth", "kindly", "tent", "tumble", "slap", "memorize", "shoe",
                      "applaud", "painful", "open", "dare", "fearless", "zebra", "geese", "sable", "blushing", "lean",
                      "spoon", "harass", "ambitious", "carry", "ducks", "suggest", "receipt", "cumbersome",
                      "destruction", "business", "equal", "wet", "normal", "slim", "press", "squeak", "copper", "sock",
                      "fanatical", "sugar", "check", "nimble", "glamorous", "kick", "truck", "preach", "toothpaste",
                      "shock", "protest", "skinny", "pine", "nosy", "pickle", "settle", "canvas", "veil", "grumpy",
                      "waste", "cheap", "harmony", "second", "brake", "encourage", "fool", "odd", "next", "north",
                      "launch", "irritating", "spectacular", "overjoyed", "hill", "shallow", "ethereal", "vein",
                      "party", "stay", "shape", "sudden", "deserted", "fantastic", "ring", "damage", "terrific",
                      "afraid", "grotesque", "envious", "test", "yell", "young", "part", "whisper", "growth", "visit",
                      "locket", "chess", "creator", "blot", "roomy", "malicious", "tangible", "grandfather", "rotten",
                      "loaf", "peel", "robust", "way", "frail", "descriptive", "melted", "green", "childlike",
                      "uninterested", "achiever", "structure", "limit", "wholesale", "glove", "brass", "remove",
                      "attach", "exciting", "rainy", "skillful", "trust", "wooden", "change", "fuel", "third", "annoy",
                      "racial", "stupid", "disastrous", "electric", "simple", "closed", "noise", "sprout", "thing",
                      "fabulous", "material", "leather", "destroy", "late", "nondescript", "condition", "irritate",
                      "absorbed", "recondite", "touch", "interfere", "moor", "nest", "ball", "clam", "train",
                      "secretary", "bawdy", "tiger", "hateful", "same", "calm", "obese", "elegant", "hall", "peck",
                      "perpetual", "grandiose", "plate", "gamy", "whimsical", "report", "imperfect", "disappear",
                      "sour", "invincible", "haunt", "aquatic", "jeans", "clover", "tickle", "air", "fail", "supreme",
                      "mellow", "resolute", "diligent", "fumbling", "power", "paper", "prose", "ban", "unit", "action",
                      "teeny"]
        self._puzzle = self._list[random.randint(0, len(self._list) - 1)]

    def get_puzzle(self):
        """Return the secret word"""
        return self._puzzle
