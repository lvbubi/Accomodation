# library
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plotHistogram(diagramModel):
    sns.set_theme(style="whitegrid")

    g = sns.catplot(
        data=diagramModel, kind="bar",
        x="county", y=0,
        ci="sd", palette="dark", alpha=.6, height=16
    )
    g.despine(left=True)
    g.set_axis_labels("", "Külföldiek vendéglátó egységekben")

    g.savefig("output.png")

def plotLollipop(diagramModel):

    # stem function: first way
    plt.stem(diagramModel.county, diagramModel[0])
    #plt.ylim(0, 1.2)
    plt.show()

    # stem function: If no X provided, a sequence of numbers is created by python:
    #plt.stem(values)
    # plt.show()

    # stem function: second way
    #(markerline, stemlines, baseline) = plt.stem(x, values)
    #plt.setp(baseline, visible=False)
    # plt.show()
