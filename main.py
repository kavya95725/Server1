from flask import Flask, jsonify ,request

import requests
from smsbomber import  mixfr ,  mixl , bgl#Bomber
import os
import multiprocessing

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/sms/<string:number>')
def user(number):

    user_ip  = request.environ['HTTP_X_FORWARDED_FOR'].split(', ')
    
    print(user_ip)
    user_ip = user_ip[0]
    print(user_ip)
    print(request.environ['REMOTE_ADDR'])

    try:
        number = int(number)
    except:
        return jsonify(
            Response="Please Input A Number",
            number=number,
            Admin="Dikshajha"
        )

    # Add a condition to check if the number is not equal to 1234567 or 97876263

    if len(str(number)) == 10:

        # Send a notification to a Telegram bot



        url = "https://api.telegram.org/bot5558804724:AAFQ_6-FU6aQF8bsX5jcUXaO2eJXFBkz668/sendMessage?chat_id=-1001506553207&text=Paidbomb%20No%20:%20" + str(number)
        r = requests.get(url)
        print(r.text)
        # os.system(f"sed 's/€hiru/{number}/g' hiru.sh > hiruop.sh")
        attack2 = multiprocessing.Process(target=mixfr , args=[number])
        attack2.start()
        # bombobj = Bomber(number)
        # bombobj.startBombing()

        return jsonify(
            Response="SMS bombing started successfully!",
            Number=number,
            Author="Dikshajha"
        )

    return jsonify(
        Response="Something is wrong with the phone number",
        Number=number
    )

@app.route('/mail/<string:mail>')
def usersssss(mail):
        
    number =  mail
        

    # try:
    #     number = int(number)
    # except:
    #     return jsonify(
    #         Response="Please Input A Number",
    #         number=number,
    #         Admin="Dikshajha"
    #     )

    # # Add a condition to check if the number is not equal to 1234567 or 97876263

    # if len(str(number)) == 10:

        # Send a notification to a Telegram bot



    url = "https://api.telegram.org/bot5558804724:AAFQ_6-FU6aQF8bsX5jcUXaO2eJXFBkz668/sendMessage?chat_id=-1001506553207&text=Paidbomb%20No%20:%20" + str(number)
    r = requests.get(url)
    print(r.text)
    # os.system(f"sed 's/€hiru/{number}/g' hiru.sh > hiruop.sh")
    attack2 = multiprocessing.Process(target=mixl , args=[number])
    attack2.start()
    # bombobj = Bomber(number)
    # bombobj.startBombing()

    return jsonify(
        Response="SMS bombing started successfully!",
        Number=number,
        Author="Dikshajha"
    )

    # return jsonify(
    #     Response="Something is wrong with the phone number",
    #     Number=number
    # )




@app.route('/bangla/<string:number>')
def userss(number):
        
    # number =  mail
        

    try:
        number = int(number)
    except:
        return jsonify(
            Response="Please Input A Number",
            number=number,
            Admin="Dikshajha"
        )

    # # Add a condition to check if the number is not equal to 1234567 or 97876263

    # if len(str(number)) == 10:

        # Send a notification to a Telegram bot



    url = "https://api.telegram.org/bot5558804724:AAFQ_6-FU6aQF8bsX5jcUXaO2eJXFBkz668/sendMessage?chat_id=-1001506553207&text=Paidbomb%20No%20:%20" + str(number)
    r = requests.get(url)
    print(r.text)
    # os.system(f"sed 's/€hiru/{number}/g' hiru.sh > hiruop.sh")
    attack2 = multiprocessing.Process(target=bgl , args=[number])
    attack2.start()
    # bombobj = Bomber(number)
    # bombobj.startBombing()

    return jsonify(
        Response="SMS bombing started successfully!",
        Number=number,
        Author="Dikshajha"
    )

    # return jsonify(
    #     Response="Something is wrong with the phone number",
    #     Number=number
    # )



if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
