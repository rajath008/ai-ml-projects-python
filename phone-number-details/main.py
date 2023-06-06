import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your phone number with country code : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(f"{phone}\n")
print(f"Carrier: {car}\n")
print(f"Time zone: {time}\n")
print(f"Region: {reg}\n")
