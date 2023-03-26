from flask import Flask, request
import pyttsx3

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <html>
<head>
    <title>ROBOT SPEAKER</title>
</head>
<style>
    * {
        margin: 0;
        padding: 0;
        font-family: 'Oswald', sans-serif;
    }

    .header {
        min-height: 100%;
        width: 100%;
        background-image: linear-gradient(rgba(4, 9, 30, 0.7), rgba(4, 9, 30, 0.7)), url(img/robot.jpg);
        background-position: center;
        background-size: cover;
        position: relative;

    }

    .text {
        font-family: 'Roboto Slab', serif;
        width: 100%;
        position: absolute;
        top: 30%;
        transform: translateY(-50%);
        text-align: center;
        color: white;
    }

    .text h1 {


        font-size: 90px;
        text-align: center;
        padding-top: 10%;
        color: white;
    }

    .text p {
        font-family: 'Roboto Slab', serif;
        font-size: 20px;
        margin: auto;
        align-content: center;
        padding: 50px 50px;
        color: white;
    }

    .header #form {
        font-family: 'Roboto Slab', serif;
        margin-top: 50px;
        width: 90%;
        position: absolute;
        top: 60%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white
    }

    #text {
        font-family: 'Roboto Slab', serif;
        padding: 10px;
        border-radius: 10px;

        border-color: white;
    }

    .button {
        color: white;
        margin-top: 80px;
        margin-left: 40px;
        width: 100px;
        padding: 15px;
        text-align: center;
        margin: 20px, 10px;
        border-radius: 20px;
        font-weight: bold;
        border: 2px solid #009688;
        background: transparent;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    span {
        background: #ff0000;
        height: 100%;
        width: 0;
        border-radius: 20px;
        position: absolute;
        left: 0;
        bottom: 0;
        z-index: -1;
        transition: 0.5s;

    }

    button:hover span {
        width: 100%;

    }

    button:hover {
        border: none;
    }

    .header{
        animation: typewritter 4s steps(40) 1s 1 normal both,
        blinkTextCursor 500ms steps(40) infinite normal;
    }

    @keyframes typwritter {
        from {
            width: 0;
        }

        to {
            width: 16em;
        }
    }

</style>

<body>
    <section class="header">
        <div class="text">
            <h1>ROBOT SPEAKER</h1>
            <p>Robot Speaker Bot is a highly advanced and sophisticated robotic device designed to deliver high-quality
                audio output in various settings. It is equipped with cutting-edge technology, such as AI-driven natural
                language processing and speech recognition, which allows it to understand and respond to verbal
                commands.
                <span id="texts"> </span>
            </p>
        </div>
        <div class="form" id="form">
            <form action="/speak" method="POST">
                <label for="text">ENTER TEXT TO SPEAK:</label>
                <input type="text" id="text" name="text">
                <br>
                <button id="btn" class="button" type="submit"><span></span> Speak</button>
        </div>
        </form>
    </section>
</body>
</html>
    '''

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form["text"]
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    engine.say(text)
    engine.runAndWait()
    return '''
   <html>
<head>
    <title>ROBOT SPEAKER</title>
</head>
<style>
    * {
        margin: 0;
        padding: 0;
        font-family: 'Oswald', sans-serif;
    }

    .header {
        min-height: 100%;
        width: 100%;
        background-image: linear-gradient(rgba(4, 9, 30, 0.7), rgba(4, 9, 30, 0.7)), url(img/robot.jpg);
        background-position: center;
        background-size: cover;
        position: relative;

    }

    .text {
        font-family: 'Roboto Slab', serif;
        width: 100%;
        position: absolute;
        top: 30%;
        transform: translateY(-50%);
        text-align: center;
        color: white;
    }

    .text h1 {


        font-size: 90px;
        text-align: center;
        padding-top: 10%;
        color: white;
    }

    .text p {
        font-family: 'Roboto Slab', serif;
        font-size: 20px;
        margin: auto;
        align-content: center;
        padding: 50px 50px;
        color: white;
    }

    .header #form {
        font-family: 'Roboto Slab', serif;
        margin-top: 50px;
        width: 90%;
        position: absolute;
        top: 60%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white
    }

    #text {
        font-family: 'Roboto Slab', serif;
        padding: 10px;
        border-radius: 10px;

        border-color: white;
    }

    .button {
        color: white;
        margin-top: 80px;
        margin-left: 40px;
        width: 100px;
        padding: 15px;
        text-align: center;
        margin: 20px, 10px;
        border-radius: 20px;
        font-weight: bold;
        border: 2px solid #009688;
        background: transparent;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    span {
        background: #ff0000;
        height: 100%;
        width: 0;
        border-radius: 20px;
        position: absolute;
        left: 0;
        bottom: 0;
        z-index: -1;
        transition: 0.5s;

    }

    button:hover span {
        width: 100%;

    }

    button:hover {
        border: none;
    }

    .header{
        animation: typewritter 4s steps(40) 1s 1 normal both,
        blinkTextCursor 500ms steps(40) infinite normal;
    }

    @keyframes typwritter {
        from {
            width: 0;
        }

        to {
            width: 16em;
        }
    }

</style>

 <body>
        <h1>Robot Speaker</h1>
        <p>The robot has spoken:</p>
        <p>{}</p>
        <a href="/">Back</a>
      </body>
</html>
'''.format(text)
if __name__ == "__main__":
    app.run()
    