import os
import numpy as np
import matplotlib.pyplot as plt

def interactive_plots(b):
    if b:
        plt.ion()
        plt.show()
    else:
        plt.ioff()

def plot_results(t, x, v, l_track, l_runout, filename=None, title=None,
                 interactive=False):

    plt.clf()
    plt.cla()
    fig, ax1 = plt.subplots()

    # Plot the race
    ax1.plot(t, x, 'b-')

    L = l_track + l_runout
    ax1.set_ylim(0, L+.05*L)
    ax1.set_xlim(0, np.amax(t))
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Distance (m)', color='b')
    ax1.tick_params('y', colors='b')

    # Plot the velocity
    ax2 = ax1.twinx()
    ax2.plot(t, v, 'r-.')
    ax2.set_ylim(0, None)
    ax2.set_ylabel('Velocity (m/s)', color='r')
    ax2.tick_params('y', colors='r')

    # plot the time the track crossed the finish
    t_finish = np.interp(l_track, x, t)
    ax1.plot([t_finish, t_finish], [0, l_track], 'k--', lw=.5)
    ax1.plot([0, t_finish], [l_track, l_track], 'k--', lw=.5)
    ax1.plot([t_finish], [l_track], 'k.', ms=12)
    ax1.plot([0, t[-1]], [L, L], 'k--', lw=.5)
    textstr = r'$t_f={0:.5f}$ (s)'.format(t_finish)
    ax1.text(t_finish+.01*t_finish, l_track-.01*l_track,
             textstr, fontsize=10, verticalalignment='top')

    fig.tight_layout()
    if title is not None:
        plt.suptitle(title)
        plt.subplots_adjust(top=0.925)

    if interactive:
        plt.draw()
        plt.pause(.001)
    elif filename is None:
        plt.show()
    else:
        plt.savefig(filename, transparent=True)
