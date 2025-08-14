import fitz
import pyttsx3


############################### LOAD THE PDF ###############################
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


############################### CONVERT TEXT TO SPEECH ###############################
def text_to_audio(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


############################### MAIN ###############################
pdf_path = "text.pdf"  # Add file path here
text = extract_text_from_pdf(pdf_path)


# text_to_audio(text)  # Uncomment to play audio directly

def save_audio(text, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()


save_audio(text, "output.mp3")
