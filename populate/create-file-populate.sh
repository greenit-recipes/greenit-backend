read -p 'Name of file : ' nom

FILE_EXTENSION="-populate.json"

if [ -f ${nom}${FILE_EXTENSION} ]; then
    echo "${nom}${FILE_EXTENSION} exists use another name"
else 
    echo '[
    {
        "pk": 1,
        "model": "model",
        "fields": {
            "name": "Cire émulsifiante végétale",
        }
    },
]' > ${nom}${FILE_EXTENSION}
fi
