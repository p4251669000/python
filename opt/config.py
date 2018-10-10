# opt/settings/config.py

DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'company',
    'user': 'user',
    'password': 'password',
    'port': 3306
}

# -------------------------------游戏配置start-------------------------------------------

#  PT
GAME_PT_CONFIG = {
    "Switch": "1",
    "SourceUrl": "https://kioskpublicapi.redhorse88.com/customreport/getdata/reportname/",
    "Password": "0oZsdDSy",
    "CertificatePath": "play.p12",
    "SourceEntityKey": "5fbf03d2d4fda646012205381bd50893e28186eec878bdd9db56084dc3effcfd7dcdf250e328d15ab22ee4d72197d54dedde0108a698fed32f8f346d6e5990a1",
    "SourceParam": "PlayerGames/startdate/{0}/enddate/{1}/frozen/all"
}

# PT2

GAME_PT2_CONFIG = {
    "Switch": "1",
    "SourceUrl": "https://kioskpublicapi.luckyspin88.com/customreport/getdata/reportname/",
    "Password": "changeit",
    "CertificatePath": "New GTLCCNYTLE.p12",
    "SourceEntityKey": "7ad9b7809ccd3a2757cd7d72d673aeb3298d8bd8b90f1fea9f0b3dd5d852016619fe21bf94e5c2d1321e70943fda6d040b6d9ef7f806b22eafd4da02e51e4981",
    "SourceParam": "PlayerGames/startdate/{0}/enddate/{1}/frozen/all"
}


# ----------------------------------游戏配置end----------------------------------------------------
