def set_size(width_pt=418.25555, fraction=1, subplots=(1, 1)):
    """
    set figuredimensions for nice fit in LaTex
        Params
        ------
        width_pt : float, (optional set for BA_SS)
                Document width in pt \showthe\textwidth
        fraction : float, optional
                Fraction of the width the figure should ocupy
        subplots : array-like, optional
                The number of rows and columns of subplots
        Returns
        -------
        fig_dim : tuple
                Dimenstions of the figure in inches
    """
    fig_width_pt = width_pt * fraction
    inches_per_pt = 1/72.27
    golden_ratio = (5**.5 -1) / 2
    fig_width_in = fig_width_pt * inches_per_pt
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)
