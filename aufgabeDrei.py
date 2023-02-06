lieferwagen_km = 85
lastwagen_km = 120
lieferwagen_kosten = lieferwagen_km * 1.6
lastwagen_kosten = lastwagen_km * 2.8
gesamt_kosten = lieferwagen_kosten + lastwagen_kosten
print(gesamt_kosten)

def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

# Beispiel für die Verwendung des Programms:
print(time_to_seconds(3, 30, 45)) # Output: 12645
