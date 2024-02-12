'''
This file gathers the source code that plots
skills matrices.


Author: R. Thomas
Year: 2023-24
Place: U. of Sheffield
Licence: GPLv3
Pylint: 10
'''

##third party imports
import numpy
import matplotlib.pyplot as plt


def plot_aestethics(ax, title, axis='off', ticks_on = True, nticks=10,
                    circles_on = True, circles_rad = [5,10,15,20]):
    '''
    This is a generic function to make the aesthetics of the plots
    '''

    if axis == 'off':
        ax.axis('off')

    if title:
        ax.title.set_text(title)
        #ax.text(0.45, 0.5, title, transform=plt.gcf().transFigure, fontsize=10)

    ####show some ticks
    if ticks_on:
        for i in range(nticks): ###number of ticks to show
            ax.plot(numpy.linspace(-numpy.pi/40, numpy.pi/40, 100),
                    5+numpy.ones(100)*i, color='r', linestyle='-', lw=1)
            ax.plot(numpy.linspace(numpy.pi/2-numpy.pi/40, numpy.pi/2+numpy.pi/40, 100),
                    5+numpy.ones(100)*i, color='r', linestyle='-', lw=1)
            ax.plot(numpy.linspace(-numpy.pi/2-numpy.pi/40, -numpy.pi/2+numpy.pi/40, 100),
                    5+numpy.ones(100)*i, color='r', linestyle='-', lw=1)
            ax.plot(numpy.linspace(numpy.pi-numpy.pi/40, numpy.pi+numpy.pi/40, 100),
                    5+numpy.ones(100)*i, color='r', linestyle='-', lw=1)

    ##add some concentric circles on left plot
    if circles_on:
        for radius in circles_rad:
            ax.plot(numpy.linspace(0, 2*numpy.pi, 100), numpy.ones(100)*radius, color='k',
                    linestyle='--', lw=1)


def make_training(needs, fig=None, ax=None):
    '''
    This function prepares data to that will then be plotted
    in the skills matrix template
    '''

    if fig == None and ax == None:
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111, polar=True)


    ##prepare values
    angles = numpy.linspace(0, 2 * numpy.pi, len(needs), endpoint=False).tolist()
    values = numpy.array(list(needs.values())) + 5
 
    ##background
    ax.bar(x=0, height=5+len(values), width=2*numpy.pi, bottom=0, color='0.9')
    ax.bar(x=0, height=2.5, width=2*numpy.pi, bottom=0, color='k')

    ####some aesthetics
    plot_aestethics(ax, title='RSE Training needs Matrix', nticks=len(values)+1,
                    circles_rad=[5, 5+len(values)])

    ###fill the plot
    ax.fill(angles, values, color='red', alpha=0.25)

    ###place the skills
    for a,s in zip(angles, list(needs.keys())):
        ###label
        angle_label = numpy.rad2deg(a)
        if a >=numpy.pi/2 and a<3*numpy.pi/2:
            angle_label += 180
            align = 'right'
        else:
            align = 'left'

        ax.text(x=a, y=5+len(values)/2, s=s.split('(')[0][0:20]+'...', color='k',
                rotation=angle_label, rotation_mode="anchor",
                ha=align, va='center')
        ax.plot(numpy.ones(25)*a, numpy.linspace(0,len(needs),25),
                linestyle='--', lw=0.4, color='0.4')

    ##and display
    plt.show()

def make_matrix_barplot(name, matrix, fig=None, ax=None, title='RSE matrix'):
    '''
    This function makes a polar barplot to represent the matrix

    Parameter
    ---------
    name        :   str
                    Name of the matrix
    matrix      :   dict
                    skill vs number
    Return
    ------
    None        
    '''
    if fig == None and ax == None:
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111, polar=True)

    ###get the max value
    max_value = int(max(list(matrix.values())))

    ##background
    ax.bar(x=0, height=5+max_value, width=2*numpy.pi, bottom=0, color='0.9')
    ax.bar(x=0, height=2.5, width=2*numpy.pi, bottom=0, color='k')

    ####some aesthetics
    plot_aestethics(ax, title=title, nticks=max_value+1,
                    circles_rad=[5, 5+max_value])

    ###plot the data
    N = len(matrix)
    size_chunk = 2*numpy.pi/N
    start_angle = numpy.pi/6
    bars = []
    for s in list(matrix.keys())[::-1]:
        ax.bar(x=start_angle, height=matrix[s], width=size_chunk,
                bottom=5, edgecolor='k', color='royalblue')

        ###label
        angle_label = numpy.rad2deg(start_angle)
        if start_angle >=numpy.pi/2 and start_angle<3*numpy.pi/2:
            angle_label += 180
            align = 'right'
        else:
            align = 'left'

        ax.text(x=start_angle, y=5+max_value/2, s=s.split('(')[0][0:20]+'...', color='k',
                rotation=angle_label, rotation_mode="anchor",
                ha=align, va='center')

        start_angle += size_chunk

    plt.show()


def make_matrix_spiderplot(name, matrix, fig=None, ax=None, title='RSE matrix'):
    '''
    This function makes a polar barplot to represent the matrix

    Parameter
    ---------
    name        :   str
                    Name of the matrix
    matrix      :   dict
                    skill vs number
    Return
    ------
    None        
    '''
    if fig == None and ax == None:
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111, polar=True)

    ##prepare values
    angles = numpy.linspace(0, 2 * numpy.pi, len(matrix), endpoint=False).tolist()
    values = numpy.array(list(matrix.values())) + 5
 
    ###get the max value
    max_value = int(max(values))

    ##background
    ax.bar(x=0, height=max_value, width=2*numpy.pi, bottom=0, color='0.9')
    ax.bar(x=0, height=2.5, width=2*numpy.pi, bottom=0, color='k')

    ####some aesthetics
    plot_aestethics(ax, title=title, nticks=max_value+1-5,
                    circles_rad=[5, max_value])

    ###fill the plot
    ax.fill(angles, values, color='red', alpha=0.25)

    ###place the skills
    for a,s in zip(angles, list(matrix.keys())):
        ###label
        angle_label = numpy.rad2deg(a)
        if a >=numpy.pi/2 and a<3*numpy.pi/2:
            angle_label += 180
            align = 'right'
        else:
            align = 'left'

        ax.text(x=a, y=5+len(values)/2, s=s.split('(')[0][0:20]+'...', color='k',
                rotation=angle_label, rotation_mode="anchor",
                ha=align, va='center')
        ax.plot(numpy.ones(25)*a, numpy.linspace(0,len(matrix),25),
                linestyle='--', lw=0.4, color='0.4')



    plt.show()



def make_rse_indiv(rse_skills, rse_name, fig=None, ax=None, title='RSE matrix'):
    '''
    This is the method that creates the plot for an individual
    rse
    '''
    ###create fig and plot
    if fig == None and ax == None:
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111, polar=True)


    ##prepare values
    angles = numpy.linspace(0, 2 * numpy.pi, len(rse_skills), endpoint=False).tolist()
    values = numpy.array(list(rse_skills.values())) + 5
 
    ###get the max value
    max_value = int(max(values))

    ##background
    ax.bar(x=0, height=3+5, width=2*numpy.pi, bottom=0, color='0.9')
    ax.bar(x=0, height=2.5, width=2*numpy.pi, bottom=0, color='k')

    ####some aesthetics
    plot_aestethics(ax, title=title, nticks=4,
                    circles_rad=[5, max_value])
    
    ###fill the plot
    ax.fill(angles, values, color='red', alpha=0.25)

    ###place the skills
    for a,s in zip(angles, list(rse_skills.keys())):
        ###label
        angle_label = numpy.rad2deg(a)
        if a >=numpy.pi/2 and a<3*numpy.pi/2:
            angle_label += 180
            align = 'right'
        else:
            align = 'left'

        ax.text(x=a, y=max_value, s=s.split('(')[0][0:20]+'...', color='k',
                rotation=angle_label, rotation_mode="anchor",
                ha=align, va='center')
        ax.plot(numpy.ones(4)*a, numpy.linspace(0,8,4),
                linestyle='--', lw=0.4, color='0.4')

    ###display
    plt.show()
