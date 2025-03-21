def generate_template(template, attendees):
    if not template:
        print("Erreur : Modèle d'invitation vide ou invalide.")
        return

    if not attendees:
        print("Erreur : Liste des invités vide.")
        return

    for i, attendee in enumerate(attendees, 1):
        content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        with open(f"invitation_{i}.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Invitation générée : invitation_{i}.txt")

try:
    with open("template.txt", "r", encoding="utf-8") as file:
        template = file.read().strip()
except FileNotFoundError:
    print("Erreur : Le fichier template.txt est introuvable.")
    template = ""

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_template(template, attendees)
