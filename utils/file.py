import os
from django.conf import settings


def getFilePathForUpload(nameUser, type, nameFile = ""):
    nameFileClean = nameFile.lower().replace(" ", "_")
    if type =="recipe":
        return nameUser + "/recipe/" + nameFileClean
    if type == "profil":
        return nameUser + "/profil/" + nameFileClean
    if type == "ingredient":
        return "/ingredient/" + nameFileClean
    if type == "utensil":
        return "/utensil/" + nameFileClean

    
def getAwsPathMedia(nameUser, nameFile, type):
    if type == "recipe":
        return settings.MEDIA_URL + settings.PUBLIC_MEDIA_LOCATION + "/" + nameUser + "/recipe/" + nameFile
    if type == "profil":
        return settings.MEDIA_URL + settings.PUBLIC_MEDIA_LOCATION + "/" + nameUser + "/profil/" + nameFile
