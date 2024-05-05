GUI Captcha Generator
Dieses Programm ist ein Captcha Generator (Completely Automated Turing test to tell
Computers and Humans Apart) basiert auf Benutzer Graphische Oberfläche Tkinter von Python

Funktionalitäten

1. Captcha generieren
   der Benutzer kann den text spezifizieren, zu dem er den Captcha generieren möchte, wenn der Benutzer auf den Button "Generate klicke", wird der Captcha erzeugt und angezeigt

2. Captcha speichern
    nachdem der Captcha generiert wurde, kann der User auf dem Button "Save Captcha" klicken und den Captcha auf dem Computer speichern

Verwendung

1. gibt der Text den Captcha ein.
    in den Input Feld "Gibt den captcha Text ein" gibt ein, der Sie verwenden möchten, um ein Captcha zu generieren

2. Captcha generieren
    klicken Sie auf dem Button "Generate Captcha" um den Captcha zu generieren, das Bild wird unten angezeigt

3. Captcha speichern,
    sobald den Captcha generiert wurde, klicken Sie auf dem Button "Save Captcha", um den Captcha auf dem Computer zu speichern.
    Ein Popup wird angezeigt, damit Sie den SpeicherOrt wählen und ein Name eingibt.

Dependencies

Dieses Programm verwendet folgende Modules:

    tkinter: für die Erstellung des grafischen Benutzer Oberfläche
    captcha: für die Erstellung des Captcha Bild
    PIL (Python Imaging Library): für die Manipulierung von Bilder
    tkinter.filedialog: für den Dialog zur Speicherung von Datei

Anweisung zum Ausführen

Stellen Sie sicher, dass Python auf Ihr System installiert wurde
installieren Sie die nötigen Dependencies mit dem Befehl: "pip install tkinter captcha Pillow".
führen Sie den Script in ihren Terminal mit dem folgenden Befehl: python captchaGen.py oder python3 captchaGen.py
verwenden Sie den GUI, um Captcha zu generieren und zu speichern