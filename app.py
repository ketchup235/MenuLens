from flask import Flask, render_template, request

app = Flask(__name__)

restriction_keywords = {
    "vegan": [
        "beef", "pork", "lamb", "mutton", "chicken", "turkey", "duck", "goose",
        "veal", "venison", "bacon", "sausage", "ham", "meatball", "meatloaf",
        "salmon", "tuna", "trout", "cod", "tilapia", "halibut", "catfish",
        "shrimp", "prawn", "crab", "lobster", "oyster", "mussel", "clam", "scallop",
        "egg", "scrambled egg", "fried egg", "poached egg", "omelette", "quiche",
        "frittata", "egg salad", "egg wash",
        "milk", "butter", "cream", "heavy cream", "half and half", "cheese",
        "cheddar", "mozzarella", "parmesan", "feta", "goat cheese", "brie",
        "gouda", "swiss", "cream cheese", "sour cream", "yogurt", "ice cream",
        "gelato", "custard", "whey", "casein", "ghee","honey", "beeswax", "royal jelly", "propolis",
        "gelatin", "anchovy", "fish sauce", "oyster sauce", "Worcestershire sauce"
    ],

    "vegetarian": [
        "beef", "pork", "lamb", "mutton", "chicken", "turkey", "duck", "goose",
        "veal", "venison", "bacon", "sausage", "ham", "meatball", "meatloaf",
        "salmon", "tuna", "trout", "cod", "halibut", "catfish",
        "shrimp", "prawn", "crab", "lobster", "oyster", "mussel", "clam", "scallop",
        "gelatin", "fish sauce", "oyster sauce", "worcestershire sauce", "anchovy", "fish","caviar", "roe",
    ],

    "gluten-free": [
        "wheat", "barley", "rye", "spelt", "farro", "kamut", "triticale",
        "bread", "bagel", "bun", "roll", "muffin", "tortilla", "pita",
        "wrap", "crouton", "cracker", "pasta", "lasagna", "ravioli", "gnocchi",
        "noodle", "dumpling", "wonton", "pizza", "flatbread", "pancake", "waffle",
        "batter", "tempura", "beer", "ale", "lager"
    ],

    "pescetarian": [
        "beef", "pork", "lamb", "mutton", "chicken", "turkey", "duck", "goose",
        "veal", "venison", "bacon", "sausage", "ham", "meatball", "meatloaf"
    ],

    "dairy-free": [
        "milk", "butter", "cream", "half and half", "cheese", "cheddar",
        "mozzarella", "parmesan", "feta", "gouda", "swiss", "brie", "goat cheese",
        "cream cheese", "sour cream", "yogurt", "ice cream", "gelato", "custard",
        "whey", "casein", "lactose", "ghee"
    ],

    "nut-free": [
        "almond", "cashew", "walnut", "pecan", "hazelnut", "pistachio",
        "macadamia", "brazil nut", "pine nut", "chestnut",
        "almond butter", "cashew butter", "nut brittle", "marzipan",
        "nougat", "nut oil"
    ],

    "kosher": [
        "pork", "bacon", "ham", "prosciutto", "lard",
        "shrimp", "prawn", "crab", "lobster", "oyster", "mussel", "clam", "scallop",
        "cheeseburger", "meat and cheese", "milk gravy"
    ],

    "halal": [
        "pork", "bacon", "ham", "prosciutto", "lard",
        "wine", "beer", "spirits", "liqueur", "rum", "vodka", "whiskey",
        "beef", "chicken", "lamb", "goose", "duck", "turkey", "rabbit", "venison",
    ],

    "keto": [
        "bread", "bagel", "bun", "roll", "tortilla", "crouton", "cracker",
        "pasta", "rice", "couscous", "oats", "porridge", "cereal",
        "potato", "sweet potato", "yam", "cassava", "corn", "beet", "parsnip",
        "sugar", "honey", "maple syrup", "corn syrup", "fruit juice", "soda",
        "cake", "cookie", "pie", "donut", "muffin", "pancake", "waffle",
        "tortilla chips", "pretzel", "granola", "energy bar", "candy", "chocolate",
        "soft drink", "fruit smoothie", "milkshake", "ice cream", "gelato",
    ],

    "shellfish-free": [
        "shrimp", "prawn", "crab", "lobster", "oyster", "mussel", "clam", "scallop","langoustine","crawfish", "cockle"
    ],

    "peanut free": [
        "peanut", "peanut butter", "peanut oil", "kung pao", "satay", "goobers", "groundnut"
    ],

    "wheat-free": [        
        "wheat", "whole wheat", "durum", "semolina", "farina", "bulgur", "spelt",
        "bread", "bagel", "bun", "roll", "pasta", "noodle", "cracker", "tortilla",
        "crumbs", "batter", "tempura","pizza", "flatbread", "pancake", "waffle"
    ],
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    menu= request.files['pdf']
    restrictions = request.form.get('restrictions')
    restrictions = [r.strip().lower() for r in restrictions.split(',') if r]
        
    if menu:
        print("INSERT CODE TO SCRAPE PDF FPR KEYWORDS")
    return render_template('upload.html')