paintings = ['The Two Fridas', 'My Dress Hangs Here','Tree of Hope','Self Portrait With Monkeys']
dates = [1939,1933,1946,1940]

paintings = list(zip(paintings,dates))
paintings_to_add = ('The Broken Column', 1944),('The Wounded Deer', 1946),('Me and My Doll',1937)

for painting in paintings_to_add:
    paintings.append(painting)

num_paintings = len(paintings)
audio_tour_number = range(1,num_paintings)
print(audio_tour_number)

master_list = list(zip(audio_tour_number,paintings))
print(master_list)
