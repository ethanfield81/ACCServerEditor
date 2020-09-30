import json

#designing python objects to convert to json for the server files
class configurationJSON():
    """Object to store server information"""
    def __init__(self):
        self.x = {
            "udpPort": 9231,
            "tcpPort": 9232,
            "maxConnections": 85,
            "lanDiscovery": 1,
            "registerToLobby": 1,
            "configVersion": 1
            }

    def print(self):
        print(json.dumps(self.x))

    def save(self,location):
        filename = "configuration.json"
        try:
            file = open(filename, "w")
            file.write(json.dumps(self.x))
            file.close()
        except:
            print("error opening file")

    def getudpPort(self):
        print(self.x["udpPort"])

    def setudpPort(self, newPort):
        self.x["udpPort"] = newPort

    def gettcpPort(self):
        print(self.x["tcpPort"])

    def settcpPort(self, newPort):
        self.x["tcpPort"] = newPort

    def getmaxConnections(self):
        print(self.x["maxConnections"])

    def setmaxConnections(self, maxConnect):
        if maxConnect > 1:
            if maxConnect < 85:
                self.x["maxConnections"] = maxConnect
        else:
            print("maxConnect not within range")

    def getlanDiscovery(self):
        print(self.x["lanDiscovery"])

    def setlanDiscovery(self, canDiscover):
        self.x["lanDiscovery"] = canDiscover

    def getregisterToLobby(self):
        print(self.x["registerToLobby"])

    def setregisterToLobby(self, canRegister):
        self.x["registerToLobby"] = canRegister

    def getconfigVersion(self):
        print(self.x["configVersion"])

    def setconfigVersion(self, versionNum):
        self.x["configVersion"] = versionNum

class settingsJSON():

    def __init__(self):
        self.x = {
                    "serverName": "Kunos Test Server #03",
                    "adminPassword": " adminPw123",
                    "carGroup": "GT4",
                    "trackMedalsRequirement": 0,
                    "safetyRatingRequirement": 0,
                    "racecraftRatingRequirement": -1,
                    "password": "",
                    "spectatorPassword": "spectPw432",
                    "maxCarSlots": 16,
                    "dumpLeaderboards": 1,
                    "isRaceLocked": 0,
                    "randomizeTrackWhenEmpty": 0,
                    "centralEntryListPath": "",
                    "allowAutoDQ": 1,
                    "shortFormationLap": 0,
                    "dumpEntryList": 0,
                    "formationLapType": 3
                    }
    def print(self):
        print(json.dumps(self.x))

    def save(self,location):
        filename = "settings.json"
        try:
            file = open(filename, "w")
            file.write(json.dumps(self.x))
            file.close()
        except:
            print("error opening file") 

    def getServerName(self):
        print(self.x["serverName"])

    def setServerName(self, newServerName):
        self.x["serverName"] = newServerName

    def getAdminPassword(self):
        print(self.x["adminPassword"])

    def setadminPassword(self, adminPassword):
        self.x["adminPassword"] = adminPassword

    def getcarGroup(self):
        print(self.x["carGroup"])

    def setcarGroup(self, carGroup):
        self.x["carGroup"] = carGroup

    def gettrackMedalsRequirement(self):
        print(self.x["trackMedalsRequirement"])

    def settrackMedalsRequirement(self, trackMedalsRequirement):
        self.x["trackMedalsRequirement"] = trackMedalsRequirement

    def getsafetyRatingRequirement(self):
        print(self.x["safetyRatingRequirement"])

    def setsafetyRatingRequirement(self, safetyRatingRequirement):
        self.x["safetyRatingRequirement"] = safetyRatingRequirement

    def getracecraftRatingRequirement(self):
        print(self.x["racecraftRatingRequirement"])

    def setracecraftRatingRequirement(self, racecraftRatingRequirement):
        self.x["racecraftRatingRequirement"] = racecraftRatingRequirement

    def getpassword(self):
        print(self.x["password"])

    def setpassword(self, password):
        self.x["password"] = password

    def getspectatorPassword(self):
        print(self.x["spectatorPassword"])

    def setspectatorPassword(self, spectatorPassword):
        self.x["spectatorPassword"] = spectatorPassword

    def getmaxCarSlots(self):
        print(self.x["maxCarSlots"])

    def setmaxCarSlots(self, maxCarSlots):
        self.x["maxCarSlots"] = maxCarSlots

    def getdumpLeaderboards(self):
        print(self.x["dumpLeaderboards"])

    def getisRaceLocked(self):
        print(self.x["isRaceLocked"])

    def setisRaceLocked(self, isRaceLocked):
        self.x["isRaceLocked"] = isRaceLocked

    def getrandomizeTrackWhenEmpty(self):
        print(self.x["randomizeTrackWhenEmpty"])

    def setrandomizeTrackWhenEmpty(self, randomizeTrackWhenEmpty):
        self.x["randomizeTrackWhenEmpty"] = randomizeTrackWhenEmpty

    def getcentralEntryListPath(self):
        print(self.x["centralEntryListPath"])

    def setcentralEntryListPath(self, centralEntryListPath):
        self.x["centralEntryListPath"] = centralEntryListPath

    def getallowAutoDQ(self):
        print(self.x["allowAutoDQ"])

    def setallowAutoDQ(self, allowAutoDQ):
        self.x["allowAutoDQ"] = allowAutoDQ

    def getshortFormationLap(self):
        print(self.x["shortFormationLap"])

    def setshortFormationLap(self, shortFormationLap):
        self.x["shortFormationLap"] = shortFormationLap

    def getdumpEntryList(self):
        print(self.x["dumpEntryList"])

    def setdumpEntryList(self, dumpEntryList):
        self.x["dumpEntryList"] = dumpEntryList

    def getformationLapType(self):
        print(self.x["formationLapType"])

    def setformationLapType(self, formationLapType):
        self.x["formationLapType"] = formationLapType

class eventJSON():

    def __init__(self):
        self.x = {
            "track": "spa",
            "preRaceWaitingTimeSeconds": 60,
            "sessionOverTimeSeconds": 120,
            "ambientTemp": 26,
            "cloudLevel": 0.3,
            "rain": 0.0,
            "weatherRandomness": 1,
            "configVersion": 1,
            "sessions": [{
                "hourOfDay": 10,
                "dayOfWeekend": 1,
                "timeMultiplier": 1,
                "sessionType": "P",
                "sessionDurationMinutes": 20
                },{
                "hourOfDay": 17,
                "dayOfWeekend": 2,
                "timeMultiplier": 8,
                "sessionType": "Q",
                "sessionDurationMinutes": 10
                },{
                "hourOfDay": 16,
                "dayOfWeekend": 3,
                "timeMultiplier": 3,
                "sessionType": "Q",
                "sessionDurationMinutes": 20
                }]}

    def gettrack(self):
        print(self.x["track"])

    def settrack(self,track):
        self.x["track"] = track

    def getpreRaceWaitingTimeSeconds(self):
        print(self.x["preRaceWaitingTimeSeconds"])

    def setpreRaceWaitingTimeSeconds(self, preRaceWaitingTimeSeconds):
        self.x["preRaceWaitingTimeSeconds"] = preRaceWaitingTimeSeconds

    def getsessionOverTimeSeconds(self):
        print(self.x["sessionOverTimeSeconds"])

    def setsessionOverTimeSeconds(self, sessionOverTimeSeconds):
        self.x["sessionOverTimeSeconds"] = sessionOverTimeSeconds

    def getambientTemp(self):
        print(self.x["ambientTemp"])

    def setambientTemp(self, ambientTemp):
        self.x[ambientTemp] = ambientTemp

    def getcloudLevel(self):
        print(self.x["cloudLevel"])

    def setcloudLevel(self, cloudLevel):
        self.x["cloudLevel"] = cloudLevel

    def getrain(self):
        print(self.x["rain"])

    def setrain(self, rain):
        self.x["rain"] = rain

    def getweatherRandomness(self):
        print(self.x["weatherRandomness"])

    def setweatherRandomness(self, weatherRandomness):
        self.x["weatherRandomness"] = weatherRandomness

    def getconfigVersion(self):
        print(self.x["configVersion"])

    def setconfigVersion(self, versionNum):
        self.x["configVersion"] = versionNum