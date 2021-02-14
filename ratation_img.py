# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:39:39 2021.

@author: timot
"""


import PIL


def echange_pix(image: list, x0: int, y0: int, x1: int, y1: int) -> None:
    px = image[y0][x0]
    image[y0][x0] = image[y1][x1]
    image[y1][x1] = px


def list_image(imge: PIL.Image) -> list:
    largeur, hauteur = imge.size
    return [[imge.getpixel((x, y))
             for y in range(hauteur)]
            for x in range(largeur)]


def fusion(lst1: list, lst2: list) -> None:
    new = []
    ln_list1 = len(lst1)
    for i in range(ln_list1):
        new.append(lst1[i] + lst2[i])
    return new


def rotate(image: list) -> None:
    largeur = len(image)
    mi_len = largeur // 2
    if largeur <= 2:
        echange_pix(image, 0, 0, 1, 0)
        echange_pix(image, 0, 0, 1, 1)
        echange_pix(image, 0, 0, 0, 1)
        return_val = image
    else:
        ne = []
        no = []
        se = []
        so = []
        for i in range(largeur // 2):
            ne.append(image[i][:mi_len])
            no.append(image[i][mi_len:])
            se.append(image[i + mi_len][:mi_len])
            so.append(image[i + mi_len][mi_len:])
        return_val = fusion(rotate(so), rotate(no)) + fusion(rotate(se),
                                                             rotate(ne))
    return return_val


img_path = "marmote.jpg"


img = PIL.Image.open(img_path)


largeur, hauteur = img.size


print("new_image ...", end=" ")
new_img = [[img.getpixel((x, y)) for y in range(hauteur)]
           for x in range(largeur)]
print("done")


print('rotate ...', end=" ")
new_img2 = rotate(new_img)
print("done")
print("create a new image ...", end=" ")
img2 = PIL.Image.new("RGB", (largeur, hauteur))
for x in range(largeur):
    for y in range(hauteur):
        img2.putpixel((x, y), new_img2[x][y])

print("done")
