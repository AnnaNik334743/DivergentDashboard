from flask import Flask, render_template, request


app = Flask(__name__)

# будем использовать только имена главных персонажей
character_names = sorted(['Tris', 'Four', 'Caleb', 'Jeanine', 'Christina', 'Tori', 'Eric', 'Peter',
                          'Natalie', 'Andrew', 'Will', 'Uriah', 'Al', 'Marcus'])

# краткие текстовые описания персонажей
character_descriptions = {
    "Tris": """Tris (Beatrice) Prior is the main character of the story.
She is a fearless and self-sacrificing teenager who leaves Abnegation and chooses to join the Dauntless faction. 
Her choices and actions challenge the society's structure and force her to make tough decisions that might endanger her 
and her friends.""",

    "Four": """Four (Tobias Eaton) is a Dauntless leader with a mysterious past.
He is brave, caring, and protective. He acts as a mentor to Tris and helps her navigate the brutal initiation process.
""",

    "Caleb": """Caleb Prior is Tris's older brother. He is smart and logical. Caleb chose the Erudite faction over 
his family's Abnegation faction. He becomes essential to the Erudite's hostile takeover of the government, 
which leads to devastating consequences.""",

    "Jeanine": """Jeanine Matthews is a cold, calculating, and ambitious leader of the Erudite faction, 
who believes that knowledge is power. 
She is willing to do anything, even mass murder, to protect her position and impose her ideas on society.
""",

    "Eric": """Eric is a Dauntless leader. He is ambitious, cunning, and utterly ruthless. 
He uses fear and violence to maintain his power and does not hesitate to kill anyone who opposes him.
""",

    "Al": """Al is an initiate in the Dauntless faction, 
who struggles to fit in and ends up betraying Tris. 
He is a conflicted character who ultimately struggles to find his place in the world.
""",

    "Christina": """Christina is a friendly and outgoing fellow initiate who becomes Tris's friend. 
Thanks to her positive attitude, she brings lightness to the story and helps Tris learn to trust others.
""",
    "Will": """Will is a smart, friendly, and loyal fellow initiate who becomes Tris's close friend. 
He is willing to help her and others at any cost, even if it means sacrificing his own life.
""",

    "Peter": """Peter is a violent and sadistic Dauntless initiate who bullies his fellow initiates, 
including Tris. He is afraid of losing control and resorts to violence to assert his authority.""",

    "Marcus": """Marcus Eaton is Four's father, a leader in the Abnegation faction, 
who has a troubled relationship with his son. He serves as a morally ambiguous character whose motivations 
remain shrouded in mystery.""",

    "Natalie": """Natalie Prior is Tris's mother, 
a former member of the Dauntless faction, who left the faction and joined Abnegation to raise her family. 
Her influence and love shape Tris's values and guide her actions throughout the story.""",

    "Andrew": """Andrew Prior is Tris's father, who is also a leader in the Abnegation faction. 
He is a kind and selfless man whose values and principles align with Abnegation's central tenets of charity and service.
""",

    "Uriah": """Uriah is a fellow Dauntless initiate who becomes one of Tris's closest friends and allies. 
He has a laid-back and fun-loving personality and is unafraid to speak his mind, which earns him Tris's respect and admiration.
""",

    "Tori": """Tori Wu is a tattoo artist in the Dauntless faction who helps Tris understand her identity as a Divergent. 
Tori acts as a source of guidance and support for Tris as she navigates the dangerous and ever-changing landscape of the divided factions.
"""
}


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    name = request.form.get('characters', 'Tris')  # по умолчанию графики строятся для Трис
    image_path = f"static/wordclouds/{name}.png"  # нужные графики из кэша в зависимости от имени персонажа
    html_file1 = f"graphs_cached/frequencies/{name}.html"
    html_file2 = f"graphs_cached/graphs/{name}.html"
    return render_template('dashboard.html', name=name, description=character_descriptions[name],
                           characters=character_names, image_path=image_path, html_file1=html_file1,
                           html_file2=html_file2)


if __name__ == '__main__':
    app.run(debug=False)
