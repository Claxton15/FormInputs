from flask import Flask, request, render_template
app = Flask(__name__)
#STUFF FOR MY WEBSITE
#Add categories for different types of video game videos
#Grab videos from Youtube that relate to the category and the game
#Show the thumbnail for the videos
#Show picture for game on button that leads to game's video categories

#STUFF FOR FORMINPUTS
#Take someone's name and replace it with more complicated name
#Choose a class
#Choose homeland
#Choose weapon proficiancy
#Choose familiar
#Choose adventure
#print all inputs in a text

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    if name is "":
         return render_template("main_page.html", input_data=dropdown,
                           output="It seem's you've forgotten to give me your name.")
    return render_template("main_page.html",
                           output="along time ago %s, a " % name )
