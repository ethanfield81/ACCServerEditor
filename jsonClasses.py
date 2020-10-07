import json
#help functions
def boolToText(bool):
    if bool == 1:
        return ("Yes")
    else:
        return("No")
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
    def importJSON(self,dir):
        dir = dir+"/configuration.json"
        with open(dir) as f:
            readdata = f.read()
            print(readdata)
            data = json.loads(readdata)
        print(json.dumps(data))

    def print(self):
        return(json.dumps(self.x))

    def save(self,location):
        filename = "configuration.json"
        try:
            file = open(filename, "w")
            file.write(json.dumps(self.x))
            file.close()
        except:
            return("error opening file")

    def getudpPort(self):
        return(self.x["udpPort"])

    def setudpPort(self, newPort):
        self.x["udpPort"] = newPort

    def gettcpPort(self):
        return(self.x["tcpPort"])

    def settcpPort(self, newPort):
        self.x["tcpPort"] = newPort

    def getmaxConnections(self):
        return(self.x["maxConnections"])

    def setmaxConnections(self, maxConnect):
        if maxConnect > 1:
            if maxConnect < 85:
                self.x["maxConnections"] = maxConnect
        else:
            return("maxConnect not within range")

    def getlanDiscovery(self):
        return(self.x["lanDiscovery"])

    def setlanDiscovery(self, canDiscover):
        self.x["lanDiscovery"] = canDiscover

    def getregisterToLobby(self):
        return(self.x["registerToLobby"])

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
    def importJSON(self,dir):
        dir = dir+"/settings.json"
        with open(dir) as f:
            data = json.load(f)
        print(json.dumps(data))
        
    def print(self):
        return(json.dumps(self.x))

    def save(self,location):
        filename = "settings.json"
        try:
            file = open(filename, "w")
            file.write(json.dumps(self.x))
            file.close()
        except:
            return("error opening file") 

    def getServerName(self):
        return(self.x["serverName"])

    def setServerName(self, newServerName):
        self.x["serverName"] = newServerName

    def getAdminPassword(self):
        return(self.x["adminPassword"])

    def setadminPassword(self, adminPassword):
        self.x["adminPassword"] = adminPassword

    def getcarGroup(self):
        return(self.x["carGroup"])

    def setcarGroup(self, carGroup):
        self.x["carGroup"] = carGroup

    def gettrackMedalsRequirement(self):
        return(self.x["trackMedalsRequirement"])

    def settrackMedalsRequirement(self, trackMedalsRequirement):
        self.x["trackMedalsRequirement"] = trackMedalsRequirement

    def getsafetyRatingRequirement(self):
        return(self.x["safetyRatingRequirement"])

    def setsafetyRatingRequirement(self, safetyRatingRequirement):
        self.x["safetyRatingRequirement"] = safetyRatingRequirement

    def getracecraftRatingRequirement(self):
        return(self.x["racecraftRatingRequirement"])

    def setracecraftRatingRequirement(self, racecraftRatingRequirement):
        self.x["racecraftRatingRequirement"] = racecraftRatingRequirement

    def getpassword(self):
        return(self.x["password"])

    def setpassword(self, password):
        self.x["password"] = password

    def getspectatorPassword(self):
        return(self.x["spectatorPassword"])

    def setspectatorPassword(self, spectatorPassword):
        self.x["spectatorPassword"] = spectatorPassword

    def getmaxCarSlots(self):
        return(self.x["maxCarSlots"])

    def setmaxCarSlots(self, maxCarSlots):
        self.x["maxCarSlots"] = maxCarSlots

    def getdumpLeaderboards(self):
        return(self.x["dumpLeaderboards"])

    def getisRaceLocked(self):
        return(self.x["isRaceLocked"])

    def setisRaceLocked(self, isRaceLocked):
        self.x["isRaceLocked"] = isRaceLocked

    def getrandomizeTrackWhenEmpty(self):
        return(self.x["randomizeTrackWhenEmpty"])

    def setrandomizeTrackWhenEmpty(self, randomizeTrackWhenEmpty):
        self.x["randomizeTrackWhenEmpty"] = randomizeTrackWhenEmpty

    def getcentralEntryListPath(self):
        return(self.x["centralEntryListPath"])

    def setcentralEntryListPath(self, centralEntryListPath):
        self.x["centralEntryListPath"] = centralEntryListPath

    def getallowAutoDQ(self):
        return(self.x["allowAutoDQ"])

    def setallowAutoDQ(self, allowAutoDQ):
        self.x["allowAutoDQ"] = allowAutoDQ

    def getshortFormationLap(self):
        return(self.x["shortFormationLap"])

    def setshortFormationLap(self, shortFormationLap):
        self.x["shortFormationLap"] = shortFormationLap

    def getdumpEntryList(self):
        return(self.x["dumpEntryList"])

    def setdumpEntryList(self, dumpEntryList):
        self.x["dumpEntryList"] = dumpEntryList

    def getformationLapType(self):
        return(self.x["formationLapType"])

    def setformationLapType(self, formationLapType):
        self.x["formationLapType"] = formationLapType

class eventJSON():

    def __init__(self):
        self.x = { #sessions is a list of Session objects
            "track": "spa",
            "preRaceWaitingTimeSeconds": 60,
            "sessionOverTimeSeconds": 120,
            "ambientTemp": 26,
            "cloudLevel": 0.3,
            "rain": 0.0,
            "weatherRandomness": 1,
            "configVersion": 1,
            "sessions": [session("P", "Default Practice"), session("Q", "Default Qualifying"), session("R", "Default Race")]
            }
    def importJSON(self,dir):
        dir = dir+"/event.json"
        with open(dir) as f:
            data = json.load(f)
        print(json.dumps(data))


    def print(self):
        printObj = self.x
        for i in range(0,len(self.x["sessions"])):
            printObj["sessions"][i] = self.x["sessions"][i].print()
        return(json.dumps(printObj))

    def save(self,location):
        filename = "event.json"
        try:
            file = open(filename, "w")
            file.write(json.dumps(print(self)))
            file.close()
        except:
            print("error opening file")

    def gettrack(self):
        return(self.x["track"])

    def settrack(self,track):
        self.x["track"] = track

    def getpreRaceWaitingTimeSeconds(self):
        return(self.x["preRaceWaitingTimeSeconds"])

    def setpreRaceWaitingTimeSeconds(self, preRaceWaitingTimeSeconds):
        self.x["preRaceWaitingTimeSeconds"] = preRaceWaitingTimeSeconds

    def getsessionOverTimeSeconds(self):
        return(self.x["sessionOverTimeSeconds"])

    def setsessionOverTimeSeconds(self, sessionOverTimeSeconds):
        self.x["sessionOverTimeSeconds"] = sessionOverTimeSeconds

    def getambientTemp(self):
        return(self.x["ambientTemp"])

    def setambientTemp(self, ambientTemp):
        self.x[ambientTemp] = ambientTemp

    def getcloudLevel(self):
        return(self.x["cloudLevel"])

    def setcloudLevel(self, cloudLevel):
        self.x["cloudLevel"] = cloudLevel

    def getrain(self):
        return(self.x["rain"])

    def setrain(self, rain):
        self.x["rain"] = rain

    def getweatherRandomness(self):
        return(self.x["weatherRandomness"])

    def setweatherRandomness(self, weatherRandomness):
        self.x["weatherRandomness"] = weatherRandomness

    def getconfigVersion(self):
        return(self.x["configVersion"])

    def setconfigVersion(self, versionNum):
        self.x["configVersion"] = versionNum

    def addSession(self, sessionType, hour, day, timeMulti, sessionLength):
        self.x["sessions"].append()
       

class session():
    def __init__(self, sessionType, nickname):
        self.name = nickname
        if sessionType == "P":
            self.x={
                "hourOfDay": 10,
                "dayOfWeekend": 2,
                "timeMultiplier": 1,
                "sessionType": "P",
                "sessionDurationMinutes": 10
                }
        elif sessionType == "Q":
            self. x ={
                "hourOfDay": 17,
                "dayOfWeekend": 2,
                "timeMultiplier": 1,
                "sessionType": "Q",
                "sessionDurationMinutes": 10
                }
        elif sessionType == "R":
            self.x = {
                "hourOfDay": 16,
                "dayOfWeekend": 3,
                "timeMultiplier": 1,
                "sessionType": "R",
                "sessionDurationMinutes": 20
                }
        else:
            return("SessionTypeError")

    def print(self):
        return(json.dumps(self.x))

    def gethourOfDay(self):
        return(self.x["hourOfDay"])

    def sethourOfDay(self, newTime):
        self.x["hourOfDay"] = newTime

    def getdayOfWeekend(self):
        return(self.x["dayOfWeekend"])

    def setdayOfWeekend(self, newTime):
        self.x["dayOfWeekend"] = newTime
     
    def gettimeMultiplier(self):
        return(self.x["timeMultiplier"])

    def settimeMultiplier(self, newTime):
        self.x["timeMultiplier"] = newTime

    def getsessionType(self):
        return(self.x["sessionType"])

    def setsessionType(self, newTime):
        self.x["sessionType"] = newTime
     
    def getsessionDurationMinutes(self):
        return(self.x["sessionDurationMinutes"])

    def setsessionDurationMinutes(self, newTime):
        self.x["sessionDurationMinutes"] = newTime


# still need to add assistRules.json