import seaborn as sns

def plotAccomodation(diagramModel):
    sns.set_theme(style="whitegrid")

    g = sns.catplot(
        data=diagramModel, kind="bar",
        x="county", y=0,
        ci="sd", palette="dark", alpha=.6, height=16
    )
    g.despine(left=True)
    g.set_axis_labels("", "Külföldiek vendéglátó egységekben")

    g.savefig("output.png")
