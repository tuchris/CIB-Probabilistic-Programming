import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


def print_beta():
    a = 10
    b = 10
    x = np.linspace(beta.ppf(0, a, b),
                    beta.ppf(1, a, b), 1000)

    plt.plot(x, beta.pdf(x, a, b),
             lw=5, alpha=0.6, label='beta pdf')
    plt.vlines(0.5, 0, 3.5, linestyles='--', colors='red', label='mean')
    plt.title("Beta 10, 10")
    # fig.set_title("Beta 10,10")
    plt.xlabel("pi")
    plt.ylabel("p(pi)")
    plt.savefig("./beta_10_10.png")
    plt.show()


def main():
    #plt.rcParams["text.usetex"] = True
    print_beta()


if __name__ == '__main__':
    main()
