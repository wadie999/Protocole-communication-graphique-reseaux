from PIL import Image, ImageDraw
import math

def triangle(size):
    height = int(math.sqrt(3) * size)
    width = size * 2
    x1 = width / 2
    y1 = 0
    x2 = 0
    y2 = height
    x3 = width
    y3 = height
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)] , fill='black')
    return [(x1, y1), (x2, y2), (x3, y3)], image


def codage_dict(number_of_colors =  3):
    """ 
    we can augment the number of colors to increase the weight of hamming by incresing the distance
    between charcters whichs alowed since the number of available combination is greater then the number
    of charcters
     ex : 3 colors ====>  81 combination
         4 colors ====> 256 combination
          5 colors ===> 625 combination
    """
    colors = ['red','green','blue','yellow','white','black']
    dict_num_colors = {}
    for i in range(len(colors)):
        dict_num_colors[i]=colors[i]
    charcters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?:/.!*-+"
    dict_char_num ={}
    pt = 0
    while pt <len(charcters):
        for i in range(number_of_colors-1,-1,-1):
            for j in range(number_of_colors-1,-1,-1):
                for k in range(number_of_colors-1,-1,-1):
                    for l in range(number_of_colors-1,-1,-1):
                        if (i,j,k,l) not in dict_char_num.values():
                            dict_char_num[charcters[pt]]=(i,j,k,l)
        pt +=1
    dict_char_num["@"] = (5,5,5,4)
    return dict_num_colors,dict_char_num
dict_num_colors,dict_char_num = codage_dict()
print(dict_num_colors,dict_char_num)



def draw_and_get_sub_triangles(points, size, image,combination=(4,4,4,4)):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    height = int(math.sqrt(3) * size)
    width = size * 2

    draw = ImageDraw.Draw(image)

    # Draw the main triangle
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill='black')

    # Calculate the sub-triangles
    triangles =[0,0,0,0]
    triangles[0] = [(x1, y1), ((x1+x2)/2, (y1+y2)/2), ((x1+x3)/2, (y1+y3)/2)]
    triangles[1] = [((x1+x2)/2, (y1+y2)/2),(x2, y2), ((x2+x3)/2, (y2+y3)/2)]
    triangles[2] = [((x1+x3)/2, (y1+y3)/2), ((x2+x3)/2, (y2+y3)/2), (x3, y3)]
    triangles[3] = [((x2+x3)/2, (y2+y3)/2),((x1+x2)/2, (y1+y2)/2),((x1+x3)/2, (y1+y3)/2)]
    # Draw the sub-triangles
    dict_num_colors,dict_char_num = codage_dict()
    for  i in range(len(triangles)):
        draw.polygon(triangles[i], fill=dict_num_colors[combination[i]])
    return triangles



def draw_and_get_sub_triangles(points, size, image,combination=(4,4,4,4)):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    height = int(math.sqrt(3) * size)
    width = size * 2

    draw = ImageDraw.Draw(image)

    # Draw the main triangle
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill='black')

    # Calculate the sub-triangles
    triangles =[0,0,0,0]
    triangles[0] = [(x1, y1), ((x1+x2)/2, (y1+y2)/2), ((x1+x3)/2, (y1+y3)/2)]
    triangles[1] = [((x1+x2)/2, (y1+y2)/2),(x2, y2), ((x2+x3)/2, (y2+y3)/2)]
    triangles[2] = [((x1+x3)/2, (y1+y3)/2), ((x2+x3)/2, (y2+y3)/2), (x3, y3)]
    triangles[3] = [((x2+x3)/2, (y2+y3)/2),((x1+x2)/2, (y1+y2)/2),((x1+x3)/2, (y1+y3)/2)]
    # Draw the sub-triangles
    dict_num_colors,dict_char_num = codage_dict()
    for  i in range(len(triangles)):
        draw.polygon(triangles[i], fill=dict_num_colors[combination[i]])
    return triangles



def make_it(s,num):
    #this function makes a string have 16 chars by duplicationg it after adding @
    # '123' ===>'123@123@123@123@'
    s += "@"
    while len(s) < num:
        s += s
    return s[:num]
def draw_message_64(points, size, image,msg):
    dict_num_colors,dict_char_num = codage_dict()
    triangles_1 = draw_and_get_sub_triangles(points, size, image)
    pt = 0
    for i in range(4):
        tmp = draw_and_get_sub_triangles(triangles_1[i], size, image)
        for j in range(4):
            tmp1 =  draw_and_get_sub_triangles(tmp[j], size, image)
            for k in range(4):
                tmp2 =  draw_and_get_sub_triangles(tmp1[k], size, image,dict_char_num[msg[pt]])
                pt += 1
    image.show()
def draw_msg_under_64(points, size, image,msg,num):
    msg = make_it(msg,num)
    draw_message_64(points, size, image,msg)



    def decompose_to_3(msg):
    if len(msg)%3==0:
        tmp = len(msg)//3
    else:
        tmp = len(msg)//3+1
    return [msg[0:tmp],msg[tmp:2*tmp],msg[2*tmp:]]
def codage_taille(taille):
    dict_num_colors,dict_char_num = codage_dict()
    msg_size = str(taille)
    while len(msg_size)<4:
        msg_size = "0"+msg_size
    tmp = []
    for chiffre in msg_size:
        tmp.append(dict_char_num[chiffre])
    return tmp
def draw_number(points, size, image,number):
    tmp = codage_taille(number)
    tout = draw_and_get_sub_triangles(points, size, image,(5,5,5,5))
    i = 0
    for chiffre in tmp:
        draw_and_get_sub_triangles(tout[i], size, image,chiffre)
        i +=1
def count_words(string):
    # Split the string into a list of words
    words = string.split()
    # Return the length of the list
    return len(words)
def main(points, size, image,msg):
    dict_num_colors,dict_char_num = codage_dict()
    triangles_1 = draw_and_get_sub_triangles(points, size, image)
    # -------------protocole information-------------
    tmp = draw_and_get_sub_triangles(triangles_1[0], size, image)
    # orientation black head
    tmp1 = draw_and_get_sub_triangles(tmp[0], size, image,(5,5,5,5))
    # number of characters
    taille = len(msg)
    draw_number(tmp[1], size, image,taille)
    # number of words
    words = count_words(msg)
    draw_number(tmp[2], size, image,words)
    # triangle size
    tmp3 = draw_and_get_sub_triangles(tmp[3], size, image,(5,5,5,5))
    tmp4 =  draw_and_get_sub_triangles(tmp3[3], size, image,(4,4,4,4))
    tmp5 =  draw_and_get_sub_triangles(tmp4[0], size, image,(4,4,4,4))
    tmp5 =  draw_and_get_sub_triangles(tmp4[1], size, image,(4,4,4,4))
    tmp5 =  draw_and_get_sub_triangles(tmp4[2], size, image,(4,4,4,4))
    tmp5 =  draw_and_get_sub_triangles(tmp4[3], size, image,(5,5,5,5))
     # -------------message-------------
    list_msg = decompose_to_3(msg)
    for i in range(len(list_msg)):
        draw_msg_under_64(triangles_1[i+1], size, image,list_msg[i],64)



# ************************************ TEST ****************************************
size = 750
points,image=triangle(size)
msg="Le TP de reseau etait vraiment interessant ! On a realise un protocole de communication graphique en utilisant le pavage des triangles et seulement 4 couleurs. C'etait une experience fascinante qui nous a permis de mieux comprendre les concepts de base de la communication reseau."
main(points, size, image,msg)
image.show()