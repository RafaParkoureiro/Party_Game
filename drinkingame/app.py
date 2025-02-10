from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game state
players = {
    'male': [],
    'female': []
}
spiciness = 0  # Global variable to track game progression


question_list = {

        "easy": [
            "Who likes foreplay more, {} or {}? They can give out 2 penalties.",
            "Take 2 penalties if you've ever m*sterbated just before hooking up so that you'll last longer.",
            "{} and {}, you can have sex for five minutes with whomever and wherever you want, and then you will die. Who and where would it be? Everyone else, vote for the best one. Winner gives out 2 penalties.",
            "Take 5 penalties if you have watched porn in the last two weeks.",
            "If you have ever thought of someone other than your partner during sex, take 2 penalties.",
            "Who in the group has the biggest difference in age with a sexual partner? They have to drink that age difference.",
            "{} tell us the first name and age of each player. The person whose name or age you screw up can give out 2 penalties.",
            "{} choose a part of your body. The first player to touch it can give out 2 penalties.",
            "Go around the room and say how long it's been since you last had sex. The person with the longest dry spell takes 3 penalties.",
            "{} and {}, each tell us your weirdest sex dream. Everyone else, vote on the oddest one. The winner can give out 2 penalties.",
            "{} give a dare to {}. If they do it, they can give out 2 penalties.",
            "Take 3 penalties if you prefer foreplay to penetration.",
            "{} and {} take a penalty together.",
            "How many times a week would you ideally have sex? {} and {} give out one penalty for every time you said you'd like to have sex in a week.",
            "{} name the first three people you have slept with (if there are 3) and take a penalty for the ones you regret.",
            "List things to arouse your partner. {} you start. If you repeat or can't think of one, take 2 penalties.",
            "{} choose a player to take off an item of clothing. Both take 2 penalties if either of you refuses.",
            "Play Never Have I Ever (3 fingers). {} you start. First person out takes 3 penalties, the rest take one penalty for each finger out.",
            "{} choose an object in the room. The first person to touch it can give out 3 penalties.",
            "{} make a rule. Whoever breaks it drinks.",
            "{} if you have ever had sex in a hot tub, take two penalties. If not, then give them out.",
            "{} ask the kinkiest person in the group to take a shot.",
            "Everyone point to the person in this room you find the most attractive. That person takes a shot for each vote received.",
            "{} illustrate your favorite sex position using just hand gestures. Keep it clean, folks!",
            "{} reveal your favorite sexual position.",
            "{} reveal the sexiest feature in a person you’re attracted to.",

        ],
        "medium": [
            "{} choose a player to cup your ass for the next 5 rounds.",
            "{} take 2 penalties. Then tell us your favorite way to give or receive head.",
            "Take a penalty if you've ever had multiple f*ck buddies at the same time.",
            "{girl} give someone a lap dance for 10 seconds. Both take 2 penalties if either refuses",
            "Take 2 penalties if you've ever had multiple orgasms in one session.",
            "{} who do you think had sex for a long session the last time they did it, {} or {}? They can give out 4 penalties.",
            "{} give a dare to {}. If they do it, they can give out 2 penalties.",
            "{} if you've ever woken up someone in the middle of the night to have sex, take 2 penalties. If not, give out them.",
            "Heartbreakers who've dumped more than 2 people, give out 3 penalties.",
            "{} choose a player to lick your lips. Both take 3 penalties if either of you refuses.",
            "{} choose someone to play with. Take a penalty, then kiss. Repeat for the next three penalties.",
            "{} pass an ice cube from your mouth to {}'s mouth. Take 3 penalties.",
            "Take it in turns to touch the chest of the player to your left. {} you start. Anyone who refuses takes 3 penalties.",
            "{} who do you think gave/received head more recently, {} or {}? They can give out 4 penalties.",
            "{} choose a player and put your hand on their thigh for the next 5 rounds.",
            "Take it in turns to kiss another player on the mouth. {} you start. Anyone who refuses has to take 3 penalties.",
            "Guys, show your boxers. Girls, vote on the best. The winner can give out 3 penalties.",
            "Take it in turns to choose a player to touch your crotch. {} you start. Anyone who refuses has to take 3 penalties.",
            "{} who do you think believes they are better in bed, {} or {}? They have to take 2 penalties.",
            "{} and {} tell your craziest sex story. Everyone vote on the craziest. Winner gives out 3 penalties.",
            "Who do you think would like to sleep with {} more, {} or {}? Everyone vote, the winner takes 4 penalties."
            "{} take as many penalties as there are players.",
            "Take 2 penalties if your last 3 times were with f*ck buddies.",
            "If you love oral, take 2 penalties.",
            "{} who do you think is best with their fingers, {} or {}? The other player has to take 3 penalties.",
            "{} and {} switch shirts. Both take 3 penalties if either refuses.",
            "{} name the biggest flirt in the room. They drink full glass.",
            "{} do a body shot of a person of the other sex. Everyone needs to vote for the person to choose it.",
            "{} have a 30-second makeout session with an imaginary partner. Put your passion on display!",
            "{} whisper something dirty in the ear of the person next to you. Let’s see if you can make them blush!",
            "{} choose someone in the room to give you a neck massage. Will they be gentle or go for the deep tissue?",
            "{} let {} spank you with a kitchen utensil of their choice.",
            "{} take off an item of clothing and keep it off for the rest of the game.",
            "{} switch clothes with the person to your right for the next three rounds.",
            "{} share the most scandalous thing you’ve ever done in a public place.",
            "{} dial your 5th contact and proposition them for sex.",
            "{} open up about your biggest turn-on. What gets your motor running?",
            "{} share a secret fetish or fantasy you’ve never told anyone.",
            "{} kiss the first person you make eye contact with after reading this dare.",
            "{} ask the person to your left to spank you in the ass.",
            "{} let {} lick your ear. This is only for the brave ones.",
            "{} show everyone your last-watched porn. And be prepared for some judgment!",
            "{boy} kiss {girl}’s neck for 10 seconds.",
            "{boy} give a little kiss to {girl}, if either refuses take 3 penalties",
            "{girl} give a little kiss to {girl}, if either refuses take 3 penalties",
            "{boy} give a little kiss to {girl}, if either refuses take 3 penalties",


        ],
        "hard": [
            "{boy} challenge a player to unclip one of the girl's bras. If they can't do it in under 5 seconds, they have to take 3 penalties.",
            "{girl} choose a player to rub your nipples. Both take 3 penalties if either of you refuses.",
            "{} show us an intimate part of your body or take 3 penalties.",
            "{boy} and {girl}, you have to french kiss for 5 seconds, you can go outside if you want",
            "{girl} and {girl}, you have to french kiss for 5 seconds, you can go outside if you want",
            "{girl} and {boy}, you have to french kiss for 5 seconds, you can go outside if you want",
            "{} blindfold yourself. Two players then have to kiss you wherever they want. If you guess who either of them is, give out 2 penalties.",
            "{} choose a player and rub your face against an intimate part of their body. Both take 3 penalties if either of you refuses.",
            "{} choose a player and put your hand in their panties. Both take 2 penalties if either of you refuses.",
            "Girls, show the guys your bras. Guys, vote on the best. The winner can give out 3 penalties.",
            "{} and {} demonstrate a sex position that everyone needs to agree on. Take 3 penalties.",
            "{} pretend you're having an orgasm for 5 seconds, then take a maximum penalty.",
            "{girl} and {boy} act like you're doing it doggy for 5 seconds.",
            "{boy} and {girl} cuddle for the next 5 minutes."
            "{} seductively eat a piece of fruit. Remember, it’s all about the technique!",
            "{} imitate the sounds you make when you climax.",
            "{} do a striptease for 30 seconds, using only one piece of clothing.",
            "{} and {} kiss for 5 seconds. If either refuses, both take 3 penalties.",
            "{} have the group choose a person and lick their belly button. If either refuses, they take 3 penalties.",
            "{boy} give a hickey to {girl}. Watch out for those teeth!",
            "{boy} lick whipped cream/honey/nutella off of {girl} body part of your choice, blindfolded.",
            "{girl} lick whipped cream/honey/nutella off of {boy} body part of your choice, blindfolded.",
            "{} give the person on your right a sensual massage for five minutes.",
            "{} act out your best orgasm. Can you top Meg Ryan’s performance?",
            "{} run an ice cube over your lips, neck, and inner thighs.",
            "{boy} and {girl} take turns kissing each other on different body parts. Stop when one refuses. The refuser takes 3 penalties.",
            "{girl} and {girl} take turns kissing each other on different body parts. Stop when one refuses. The refuser takes 3 penalties.",
            "{boy} and {girl} take turns kissing each other on different body parts. Stop when one refuses. The refuser takes 3 penalties.",
            "{girl} kiss {boy}’s neck for 10 seconds.",
            "{boy} and {girl} kiss for 5 seconds. If either refuses, both take 3 penalties.",
            "{girl}, {girl} and {boy} do a three-way kiss. If anyone refuses, they take 3 penalties.",
            "{} choose a player to give you a passionate kiss. Both take 2 penalties if either refuses.",
            "{} blindfold yourself and kiss a random player chosen by the group.",
            "{girl} and {} hold a kiss for as long as possible. Whoever stops first takes 2 penalties.",
            "{} kiss {girl} like it's your last kiss before the world ends.",
            "{} and {} swap gum with a kiss. If either refuses, they take 3 penalties."
            "{girl}, {girl} and {boy} do a three-way kiss. If anyone refuses, they take 3 penalties.",
            "{girl}, {} and {boy} do a three-way kiss. If anyone refuses, they take 3 penalties.",
            "{girl}, {girl} and {} do a three-way kiss. If anyone refuses, they take 3 penalties.",
            "{}, {girl} and {boy} do a three-way kiss. If anyone refuses, they take 3 penalties."
        ],

}   

def select_random(who, exclude=[], gender=None):
    if who == 'random':
        if gender == 'boy':
            all_players = players['male']
        elif gender == 'girl':
            all_players = players['female']
        else:
            all_players = players['male'] + players['female']
    elif who == 'male':
        all_players = players['male']
    elif who == 'female':
        all_players = players['female']
    else:
        return "No players available"
    
    all_players = [p for p in all_players if p not in exclude]
    return random.choice(all_players) if all_players else "No valid selection"

@app.route('/')
def home():
    global spiciness
    spiciness = 0  # Reset spiciness when starting a new game
    players['male'].clear()
    players['female'].clear()
    return render_template('index.html')

@app.route('/add_player', methods=['POST'])
def add_player():
    data = request.json
    name = data.get('name')
    gender = data.get('gender')
    
    if name in players['male'] or name in players['female']:
        return jsonify({'success': False, 'message': 'Player already exists!'})
    
    players[gender].append(name)
    return jsonify({'success': True, 'message': f'{name} added!'})

@app.route('/get_question', methods=['GET'])
def get_question():
    global spiciness
    
    if spiciness < 10:
        difficulty_weights = [1.0, 0.0, 0.0]  # 100% easy
    else:
        medium_prob = min((spiciness - 10) * 0.05, 0.5)  # Increases by 5% per question, max 50%
        hard_prob = min((spiciness - 25) * 0.03, 0.5)  # Starts increasing after spiciness 25, max 50%
        if hard_prob < 0.0:
            hard_prob = 0.0
        if medium_prob < 0.0:
            medium_prob = 0.0
        easy_prob = 1.0 - (medium_prob + hard_prob)
        difficulty_weights = [easy_prob, medium_prob, hard_prob]
    
    difficulty = random.choices(["easy", "medium", "hard"], weights=difficulty_weights, k=1)[0]
    question = random.choice(question_list[difficulty])
    players_to_use = []
    print(difficulty_weights)

    while '{boy}' in question or '{girl}' in question:
        if '{boy}' in question:
            player = select_random('random', gender='boy', exclude=players_to_use)
            question = question.replace('{boy}', player, 1)
            players_to_use.append(player)
        if '{girl}' in question:
            player = select_random('random', gender='girl', exclude=players_to_use)
            question = question.replace('{girl}', player, 1)
            players_to_use.append(player)

    placeholder_count = question.count('{}')
    for _ in range(placeholder_count):
        player = select_random('random', exclude=players_to_use)
        question = question.replace('{}', player, 1)
        players_to_use.append(player)
    
    spiciness += 1  # Increase spiciness after each question

    return jsonify({'question': question, 'difficulty': difficulty})


@app.route('/reset_game', methods=['POST'])
def reset_game():
    global spiciness
    spiciness = 0  # Reset spiciness when the game resets
    players['male'].clear()
    players['female'].clear()
    return jsonify({'success': True, 'message': 'Game reset!'})

if __name__ == '__main__':
    app.run(debug=True)
