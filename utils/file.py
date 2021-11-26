import os
from django.conf import settings


def getFilePathForUpload(nameUser, type, nameFile = ""):
    if type =="recipe":
        return nameUser + "/recipe/" + nameFile
    if type == "profil":
        return nameUser + "/profil/" + nameFile
    if type == "ingredient":
        return "ingredient/" + nameFile

    
def getAwsPathMedia(nameUser, nameFile, type):
    if type == "recipe":
        return settings.MEDIA_URL + settings.PUBLIC_MEDIA_LOCATION + "/" + nameUser + "/recipe/" + nameFile
    if type == "profil":
        return settings.MEDIA_URL + settings.PUBLIC_MEDIA_LOCATION + "/" + nameUser + "/profil/" + nameFile
