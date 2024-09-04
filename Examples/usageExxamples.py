# Usage of the appl.functions

# Create a Vaihtotarjous object
vaihtotarjous = Vaihtotarjous(1, 42, 3, "Sample title")
print(vaihtotarjous.otsikko)  # Output: "Sample title"

kayttaja1 = Kayttaja(1, "john_doe")
print(kayttaja1.getTunnus())  # Output: "john_doe"
print(kayttaja1.getKayttajaID())  # Output: 1

kayttaja2 = Kayttaja("alice")
print(kayttaja2.getTunnus())  # Output: "alice"
print(kayttaja2.getKayttajaID())  # Output: -1

keskustelualue1 = Keskustelualue(1, "General Discussion")
print(keskustelualue1.getNimi())  # Output: "General Discussion"
print(keskustelualue1.getId())  # Output: 1

keskustelualue2 = Keskustelualue("Feedback")
print(keskustelualue2.getNimi())  # Output: "Feedback"
print(keskustelualue2.getId())  # Output: None

kalue = Keskustelualue(1, "General Discussion")
item = KeskustelualueListausItem(1, kalue, 10, datetime.now())
print(item.getNimi())  # Output: "General Discussion"
print(item.getMaara())  # Output: 10
print(item.getKeskusteluAlueId())  # Output: 1
print(item.getViimeisin())  # Output: current timestamp

kalue = Keskustelualue(1, "General Discussion")
item1 = KeskustelualueListausItem(1, kalue, 10, datetime.now())
item2 = KeskustelualueListausItem(2, kalue, 5, datetime.now())

print(item1.getNimi())  # Output: "General Discussion"
print(item1.getMaara())  # Output: 10
print(item1.getKeskusteluAlueId())  # Output: 1
print(item1.getViimeisin())  # Output: current timestamp

# Comparing items
print(item1 < item2)  # Output: True
print(item1 == item2)  # Output: False
print(item1 > item2)  # Output: False

print(current_timestamp)  # Output: 2024-07-16 17:02:42.123456 (actual timestamp will vary)

# You can also create a Timestamp from a specific date and time
specific_date = datetime(2024, 7, 16, 10, 30, 0)  # July 16, 2024, 10:30 AM
print(specific_date)  # Output: 2024-07-16 10:30:00

viesti1 = Viesti(42, "John", 1, "Hello, world!")
print(viesti1.getKirjoittaja())  # Output: "John"
print(viesti1.getLahetysaika())  # Output: current timestamp

viesti2 = Viesti(1, "Alice", 2, "Another message")
print(viesti2.getKirjoittaja())  # Output: "Alice"
print(viesti2.getLahetysaika())  # Output: current timestamp

