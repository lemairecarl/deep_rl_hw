import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('results_file', type=str)
parser.add_argument('-t', '--title', type=str, default='Reward')
args = parser.parse_args()

with open(args.results_file, 'r') as f:
    steps = list(f.readlines())

to_tuple = lambda s: (int(s[0:7]), float(s[8:16]), float(s[17:25]))

tsteps = [to_tuple(s) for s in steps]

t, mean_r, best_r = [x[0] for x in tsteps], [x[1] for x in tsteps], [x[2] for x in tsteps]


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
