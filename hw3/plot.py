import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('results_file', type=str)
parser.add_argument('-t', '--title', type=str, default='Reward')
args = parser.parse_args()

with open(args.results_file, 'r') as f:
    steps = list(f.readlines())

# There are 3 columns: Timesteps (7 char), [space], Mean reward (8 char), [space], Best mean reward (8 char).
to_tuple = lambda s: (int(s[0:7]), float(s[8:16]), float(s[17:25]))

tsteps = [to_tuple(s) for s in steps]

# The 3rd column, "Best mean reward", is the best mean reward over 100 episodes. If there are not yet 100 episodes seen,
# the value given is -infinity. Let's remove those rows.
tsteps = [x for x in tsteps if x[2] != float('-inf')]

t, mean_r, best_r = zip(*tsteps)  # zip(*x) can be seen as unzip(x), going from list(tuples) to tuple(lists).
# In fact, zip() returns a list, but you can assign it to a tuple, like I did.


def plot_dict(x, d):
    plt.figure()
    for k, v in d.items():
        plt.plot(x, v, label=k)
    plt.legend()
    plt.title(args.title)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.show()
    plt.close()

plot_dict(t, {'mean': mean_r, 'best': best_r})
