## display a window that first prompts to input a folder, something like "\Steam\steamapps\common\Assetto Corsa Competizione\server"

## then shows a screen with 5 tabs, configuration, settings, event, event rules, and assist rules
## these allow a user to adjust these .json found in .\server
## these can be saved within a preset in the editor and are saved over any current files in UTF16-LE .json upon completion


## once file is selected, search within it for the .json files

    ## if found move on

    ## if not, error out and prompt for a different folder

## configuration.json stuff, low priority
   
    ## only really talks about server stuff, most don't need to change anything

## settings.json

    ## Text input: serverName
    ## Text input: adminPassword
    ## Categorical Input: carGroup
    ## Slider Input: trackMedalsRequirement
    ## Slider Input: safetyRatingRequiremnt
    ## Slider Input + disable checkbox: racecraftRatingRequirement
    ## Text input: password
    ## Text input: spectatorPassword
    ## Slider input: maxCarSlots
    ## Check box: dumpLeaderboards (should default on)
    ## Check box: isRaceLocked
    ## Check box: randomizeTrackWhenEmpty
    ## File Location Prompt: CentralEntryListPath (consider moving to within Entry List menu)
    ## Check box: allowAutoDQ
    ## Check box: shortFormationLap (consider lumping under formationLapType)
    ## Check box: dumpEntryList
    ## Categorical Input: formationLapType

## event.json
    
    ## General Settings:
    ## Categorical Input: track
    ## Slider Input: preRaceWaitingTimeSeconds
    ## Slider Input: sessionOverTimeSeconds
    ## Slider Input: ambientTemp
    ## Slider Input: cloudLevel
    ## Slider Input: rain
    ## Slider Input: weatherRandomness
    ## Slider Input: postQualySeconds
    ## Slider Input: postRaceSeconds
    
    ## Add button: sessions

        ## Slider Input: hourOfDay
        ## Slider Input: dayOfWeekend
        ## Slider Input: timeMultiplier
        ## Categorical Input: sessionType
        ## Slider Input: sessionDurationMinutes

## eventRules.json (public servers ignore this file) low priority

## assistRules.json (public servers ignore this file) low priority

## entrylist.json medium-low priority
    ## need add team or add single person button
    ## add single person essentially within add team

    ## Single Person:
    ## playerID
    ## firstName
    ## lastName
    ## shortName
    ## driverCategory

    ## Per Team:
    ## raceNumber
    ## forcedCarModel
    ## overrideDriverInfo
    ## isServerAdmin
    ## customCar
    ## overrideCarModelForCustomcar
    ## defaultGridPosition
    ## ballastKG
    ## restrictor

## result files, medium priority