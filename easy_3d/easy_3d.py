import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def easy_plot3d(xr=[-1,1], yr=[-1,1], xsam=20, ysam=20, func=(lambda x,y:np.exp(-2*x**2-2*y**2)), how="wireframe", show=True, **kwargs):
    x = np.linspace(xr[0], xr[1], xsam)
    y = np.linspace(yr[0], yr[1], ysam)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    if how == "contourproj":
        ax = plt.axes()
        ax.contour(X, Y, func(X, Y), **kwargs)
    elif how == "contourfproj":
        ax = plt.axes()
        ax.contourf(X, Y, func(X, Y), **kwargs)
    else:
        ax = Axes3D(fig)
        if how == "surface":
            ax.plot_surface(X, Y, func(X, Y), **kwargs)
        elif how == "wireframe":
            ax.plot_wireframe(X, Y, func(X, Y), **kwargs)
        elif how == "contour":
            ax.contour(X, Y, func(X, Y), **kwargs)
        elif how == "contourf":
            ax.contourf(X, Y, func(X, Y), **kwargs)
    if show:
        plt.show()
    return fig, ax

if __name__ == "__main__":
    easy_plot3d()
