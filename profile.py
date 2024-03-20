import cgi
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My profile</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Orelega+One&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }

        div#container {
            position: relative;
            top: 105px;
            box-shadow: 9px -7px 17px;
            border-radius: 27px;
            display: flex;
            flex-direction: column;
            width: 56vw;
            justify-content: space-evenly;
            margin: 20px auto;
            height: 333px;
        }

        div#image_name {
            padding-bottom: 12px;
            border-bottom: 2px solid gray;
            width: 432px;
            display: flex;
            align-items: flex-end;
        }

        img#dp {
            width: 84px;
            height: 84px;
            border: 3px solid grey;
            border-radius: 59%;
        }

        h2 {
            font-family: 'Orelega One', cursive;
            margin-left: 12px;
        }

        .margin {
            margin-left: 30px;
        }

        p#change_dp {
            width: 152px;
            color: gray;
            cursor: pointer;
        }

        .heading {
            font-size: 20px;
            font-family: 'Orelega One', cursive;
        }

        span {
            color: gray;
            margin-left: 12px;
        }

        div#box {
            display: none;
            bottom: 323px;
            left: 46%;
            border: 2px solid;
            position: absolute;
            border-radius: 12px;
            padding: 25px 10px;
            width: 285px;
        }

        #button1 {
            color: white;
            background-color: #24a0ed;
            font-weight: bold;
            padding: 7px 10px;
            text-align: center;
            outline: none;
            border: none;
            border-radius: 9px;
            cursor: pointer;
        }

        #box span {
            color: black;
            position: relative;
            top: -21px;
            font-weight: bold;
            right: 19px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <div id="container">
        <div class="margin" id="image_name"><img id="dp" src="profile.png">
            <h2>Saif Ali</h2>
        </div>
        <p class="margin " id="change_dp">Change profile picture</p>
        <p class="margin heading">Phone Number:-<span id="number">8013051576</span></p>
        <p class="margin heading">Email ID:-<span id="email">saifalifias@gmail.com</span></p>
        <p class="margin heading">Account Number:-<span id="account_no">123456789123</span></p>
    </div>
    <div id="box">
        <span id="cross">x</span>
        <div id="image-catalog">
            <img src="profile.png" onclick="pathchanger('profile.png')">
            <img src="profile1.png" onclick="pathchanger('profile1.png')">
            <img src="profile2.png" onclick="pathchanger('profile2.png')">
            <img src="profile3.png" onclick="pathchanger('profile3.png')">
            <img src="profile4.png" onclick="pathchanger('profile4.png')">
            <img src="profile5.png" onclick="pathchanger('profile5.png')">
        </div>
        <form action="">
            <input type="hidden" id="myfile" name="myfile"><br><br>
            <input type="submit" value="Save" id="button1">
        </form>
    </div>
</body>
<script src="jquery-3.5.1.min.js"></script>
<script>
    function pathchanger(image)
    {
        console.log("hellp")
        $("#dp").attr("src",image)
    }
    $("#change_dp").click(function () {
        $("#box").css("display", "block")
    })
    $("#cross").click(function () {
        $("#box").css("display", "none")
    })

</script>
</html>""")