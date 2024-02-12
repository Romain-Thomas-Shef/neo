################################################
####This file plots the RSEworldcloud.
###it requires matplotlib, catscii and wordcloud
####Author: R. Thomas, 2023
################################################

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from catscii import catscii

def color_func(word, font_size, position, orientation, font_path, random_state):
    if word in ['Research', 'Software', 'Engineering']:
        return 'black'
    elif word == 'France':
        return 'limegreen'
    else:
        r, g, b, alpha = plt.get_cmap('prism')(font_size / 120)
        return (int(r * 255), int(g * 255), int(b * 255))

###load the data
cat = catscii.load_cat('wordcloud_data.txt', True)
skills = cat.get_column('wordcloud', str)
skills = [' '.join(i.split('-')) for i in skills]
weight = cat.get_column('weight', int)

###reorganize in dictionary
dict_weight = {skills[i]:weight[i] for i in range(len(skills))}


###create the image
wordcloud  = WordCloud(font_path = 'SourceCodePro-VariableFont_wght.ttf', width=1000, height=1000, relative_scaling=1.0, background_color='white').generate_from_frequencies(dict_weight)

###make the plot
fig = plt.figure(figsize=(10,10))
ax = plt.subplot(111)
ax.axis('off')

##change colors
wordcloud.recolor(color_func=test_color_func)

##add it to the plot
ax.imshow(wordcloud, interpolation='bilinear')

#display
plt.show()





