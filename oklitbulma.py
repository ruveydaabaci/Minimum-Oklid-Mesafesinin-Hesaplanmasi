import math

# Noktaların tanımlanması ve kullanıcıdan alınması
points = []
num_points = int(input("Kaç tane nokta gireceksiniz? "))
for i in range(num_points):
    x = float(input("{}. noktanın x koordinatını girin: ".format(i+1)))
    y = float(input("{}. noktanın y koordinatını girin: ".format(i+1)))
    points.append((x, y))

# Öklid Mesafesi İçin Fonksiyon Tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafelerin Hesaplanması ve distances listesine eklenmesi
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
