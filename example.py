from UrbanPy import urbandictionary

client = urbandictionary.UrbanDictionary()

#random definitions
randomWords = client.define()
for d in randomWords:
    print(f'{d.word}\n\t{d.definition} (ID: {d.definitionId})\n\t{d.example}\n ^ {d.thumbs_up} v {d.thumbs_down}\n Written by {d.author}')


