import requests

x_coord_range = [74789, 74795]
y_coord_range = [117660, 117662]
zoom = 18
# y_coord is static for this example

# Iterate x coord URLs
for ycoord in range(y_coord_range[0], y_coord_range[1]):
    for xcoord in range(x_coord_range[0], x_coord_range[1]):
        # Plug in xcoord for URL
        image_url = 'https://khms0.googleapis.com/kh?v=877&hl=en-US&x={}&y={}&z={}'.format(xcoord, ycoord, zoom)
        # Get page content
        img_data = requests.get(image_url).content
        # Filename according to coord
        file_name = 'image_x_coord_{}__y_coord_{}.jpg'.format(xcoord, ycoord)
        # Write image to current directory
        with open(file_name, 'wb') as handler:
            handler.write(img_data)