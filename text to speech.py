from gtts import gTTS

text_to_say = "This is a sample piece of text read by GTTS."

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")

french_text = "Bonjour. Je m'appelle Alexandra. Je suis programmeuse."

french_language = "fr"

french_gtts_object = gTTS(text = french_text,
                          lang = french_language,
                          slow = True)

french_gtts_object.save("/content/french.wav")

Audio("/content/french.wav")
