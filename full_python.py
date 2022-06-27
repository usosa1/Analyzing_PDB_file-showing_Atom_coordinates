# showing atom x coordinates
visited = {}
print("X_coordinates:")
for MYline in open('1a3d.pdb'):
    list = MYline.split()
    id = list[0]
    if id == 'ATOM':
        x_pos_cordinate = list[6:7]
        print(x_pos_cordinate)
        
# showing atom y coordinates
print("Y_coordinates:")
for MYline in open('1a3d.pdb'):
    list = MYline.split()
    id = list[0]
    if id == 'ATOM':
        y_pos_cordinate = list[7:8]
        print(y_pos_cordinate)
        
# showing atom z coordinates
print("Z_coordinates:")
for MYline in open('1a3d.pdb'):
    list = MYline.split()
    id = list[0]
    if id == 'ATOM':
        z_pos_cordinate = list[8:9]
        print(z_pos_cordinate)
