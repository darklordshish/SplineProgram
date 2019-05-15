#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:05:54 2019

@author: semion
"""
import numpy as np
import dill
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import os


def func1(x):
    """
    модельная функция 1
    """
    y = ((0.79*(np.sin(2*np.pi/24*x) +
          np.exp(-(x - 70)**2/100) +
          np.exp(-(x - 130)**2/130) +
          0.5*np.sin(np.heaviside(x-96, 76)*2*np.pi/27.4*x) +
          np.exp(-(np.heaviside(x-57, 1)*x - 200)**2/200)*np.sin(0.01*x) +
          0.01*np.heaviside(157-x, 1)*np.sin(2*np.pi*x/365)) + 20))
    return y


def func2(x):
    """
    модельная функция 2
    """
    y = (2*np.sin(2*np.pi*x/12) +
         0.5*np.cos(2*np.pi*x/10)+23 -
         np.abs(x-100)/20)
    return y


def func_rand(func, x):
    """
    модель измерения с шумом
    """
    y = func(x) + np.random.randn(np.size(x))*0.60
    return y


x1 = np.loadtxt("x_1.csv")
y1 = np.loadtxt("y_1.csv")
n1 = np.loadtxt("n_1.csv")
f1 = np.loadtxt("y0_1.csv")

x2 = np.loadtxt("x_2.csv")
y2 = np.loadtxt("y_2.csv")
n2 = np.loadtxt("n_2.csv")
f2 = np.loadtxt("y0_2.csv")

y1ch = f1 + n2
y2ch = f2 + n1

x = x1
# y = y1ch
y = y2ch


"""
with open('data_model_1_ch.pickle') as f1:
    dictMmodelChange_1 = dill.load(f1)
with open('data_model_2_ch.pickle') as f2:
    dictMmodelChange_2 = dill.load(f2)

rho1 = dictMmodelChange_1["Detailed"]["x_1"]
s1 = [UnivariateSpline(x1, y1ch, k=5, s=rho1[i]) for i in range(len(rho1))]

rho2 = dictMmodelChange_2["Detailed"]["x_1"]
s2 = [UnivariateSpline(x2, y2ch, k=5, s=rho2[i]) for i in range(len(rho2))]

y1_1 = s1[1](x1)
y1_2 = s1[2](x1)
y1_3 = s1[3](x1)
y1_4 = s1[4](x1)
y1_5 = s1[5](x1)
y1_6 = s1[6](x1)
y1_7 = s1[7](x1)

err1_1 = y1ch - y1_1
err1_2 = y1ch - y1_2
err1_3 = y1ch - y1_3
err1_4 = y1ch - y1_4
err1_5 = y1ch - y1_5
err1_6 = y1ch - y1_6
err1_7 = y1ch - y1_7
"""


def plot_all(n):
    if n == 1:
        os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/")
        with open('data_model_1_ch.pickle') as f1:
            dictMmodelChange_1 = dill.load(f1)

        rho1 = dictMmodelChange_1["Detailed"]["x_1"]
        s1 = [UnivariateSpline(x1, y1ch, k=5, s=rho1[i])
              for i in range(len(rho1))]
        y1_1 = s1[1](x1)
        y1_2 = s1[2](x1)
        y1_3 = s1[3](x1)
        y1_4 = s1[4](x1)
        y1_5 = s1[5](x1)
        y1_6 = s1[6](x1)
        y1_7 = s1[7](x1)

        err1_1 = y1ch - y1_1
        err1_2 = y1ch - y1_2
        err1_3 = y1ch - y1_3
        err1_4 = y1ch - y1_4
        err1_5 = y1ch - y1_5
        err1_6 = y1ch - y1_6
        err1_7 = y1ch - y1_7
        os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/model_ch1_fig/")
        norm_noise1 = np.linalg.norm(n2)
        norm_rem1 = np.linalg.norm(
                       [y1ch-spline(x1)-n2 for spline in s1],
                        axis=1)/norm_noise1
        norm_func1 = np.linalg.norm(func1(x1))
        norm1 = np.linalg.norm([func1(x1)-spline(x1) for spline in s1],
                                axis=1)/norm_func1
        plt.figure(1, figsize=(16, 9))
        plt.title("Signal")
        plt.plot(x1, y1ch, "k-")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['signal'])
        plt.savefig('data_signal.pdf', dpi=300)
        plt.clf()

        plt.figure(2, figsize=(16, 9))
        plt.title("Model Function")
        plt.plot(x1, func1(x1), "k-")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['model function'])
        plt.savefig('data_model_function.pdf', dpi=300)
        plt.clf()

        plt.figure(3, figsize=(16, 9))
        plt.title("Noise")
        plt.plot(x1, n2, "k-")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['real noise'])
        plt.savefig('data_real_noise.pdf', dpi=300)
        plt.clf()

        #########
        # Splines
        #########

        plt.figure(4, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[1])
        plt.plot(x1, y1_1, "-k")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[1]])
        plt.savefig('spline_1.pdf', dpi=300)
        plt.clf()

        plt.figure(5, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[2])
        plt.plot(x1, y1_2, "-k")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[2]])
        plt.savefig('spline_2.pdf', dpi=300)
        plt.clf()

        plt.figure(6, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[3])
        plt.plot(x1, y1_3, "-g")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[3]])
        plt.savefig('spline_3.pdf', dpi=300)
        plt.clf()

        plt.figure(7, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[4])
        plt.plot(x1, y1_4, "-b")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[4]])
        plt.savefig('spline_4.pdf', dpi=300)
        plt.clf()

        plt.figure(8, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[5])
        plt.plot(x1, y1_5, "-k")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[5]])
        plt.savefig('spline_5.pdf', dpi=300)
        plt.clf()

        plt.figure(9, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[6])
        plt.plot(x1, y1_6, "-k")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[6]])
        plt.savefig('spline_6.pdf', dpi=300)
        plt.clf()

        plt.figure(10, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[7])
        plt.plot(x1, y1_7, "-k")
        plt.ylim(16, 25)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[7]])
        plt.savefig('spline_7.pdf', dpi=300)
        plt.clf()

        #######
        # Noise
        #######

        plt.figure(11, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[1])
        plt.plot(x1, err1_1, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[1]])
        plt.savefig('remnains_1.pdf', dpi=300)
        plt.clf()

        plt.figure(12, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[2])
        plt.plot(x1, err1_2, "-b")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[2]])
        plt.savefig('remnains_2.pdf', dpi=300)
        plt.clf()

        plt.figure(13, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[3])
        plt.plot(x1, err1_3, "-g")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[3]])
        plt.savefig('remnains_3.pdf', dpi=300)
        plt.clf()

        plt.figure(14, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[4])
        plt.plot(x1, err1_4, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[4]])
        plt.savefig('remnains_4.pdf', dpi=300)
        plt.clf()

        plt.figure(15, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[5])
        plt.plot(x1, err1_5, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[5]])
        plt.savefig('remnains_5.pdf', dpi=300)
        plt.clf()

        plt.figure(16, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[6])
        plt.plot(x1, err1_6, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[6]])
        plt.savefig('remnains_6.pdf', dpi=300)
        plt.clf()

        plt.figure(17, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[7])
        plt.plot(x1, err1_7, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[7]])
        plt.savefig('remnains_7.pdf', dpi=300)
        plt.clf()
        return [norm1[1:8], dictMmodelChange_1["Detailed"]["x_1"][1:8],
                dictMmodelChange_1["Detailed"]["t_1"][1:8],
                dictMmodelChange_1["Detailed"]["t_2"][1:8]]


    elif n == 2:
        os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/")
        with open('data_model_2_ch.pickle') as f1:
            dictMmodelChange_1 = dill.load(f1)

        rho1 = dictMmodelChange_1["Detailed"]["x_1"][1:]
        s1 = [UnivariateSpline(x1, y2ch, k=5, s=rho1[i])
              for i in range(len(rho1))]
        y1_1 = s1[1](x1)
        y1_2 = s1[2](x1)
        y1_3 = s1[3](x1)
        y1_4 = s1[4](x1)
        y1_5 = s1[5](x1)
        y1_6 = s1[6](x1)
        y1_7 = s1[7](x1)

        err1_1 = y2ch - y1_1
        err1_2 = y2ch - y1_2
        err1_3 = y2ch - y1_3
        err1_4 = y2ch - y1_4
        err1_5 = y2ch - y1_5
        err1_6 = y2ch - y1_6
        err1_7 = y2ch - y1_7
        os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/model_ch2_fig/")
        norm_noise2 = np.linalg.norm(n1)
        norm_rem2 = np.linalg.norm(
                       [y2ch-spline(x1)-n1 for spline in s1],
                        axis=1)/norm_noise2
        norm_func2 = np.linalg.norm(func2(x1))
        norm2 = np.linalg.norm([func2(x1)-spline(x1) for spline in s1],
                                axis=1)/norm_func2
        plt.figure(1, figsize=(16, 9))
        plt.title("Signal")
        plt.plot(x1, y2ch, "k-")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['signal'])
        plt.savefig('data_signal.pdf', dpi=300)
        plt.clf()

        plt.figure(2, figsize=(16, 9))
        plt.title("Model Function")
        plt.plot(x1, func2(x1), "k-")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['model function'])
        plt.savefig('data_model_function.pdf', dpi=300)
        plt.clf()

        plt.figure(3, figsize=(16, 9))
        plt.title("Noise")
        plt.plot(x1, n1, "k-")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['real noise'])
        plt.savefig('data_real_noise.pdf', dpi=300)
        plt.clf()

        #########
        # Splines
        #########

        plt.figure(4, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[1])
        plt.plot(x1, y1_1, "-k")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[1]])
        plt.savefig('spline_1.pdf', dpi=300)
        plt.clf()

        plt.figure(5, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[2])
        plt.plot(x1, y1_2, "-k")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[2]])
        plt.savefig('spline_2.pdf', dpi=300)
        plt.clf()

        plt.figure(6, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[3])
        plt.plot(x1, y1_3, "-k")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[3]])
        plt.savefig('spline_3.pdf', dpi=300)
        plt.clf()

        plt.figure(7, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[4])
        plt.plot(x1, y1_4, "-g")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[4]])
        plt.savefig('spline_4.pdf', dpi=300)
        plt.clf()

        plt.figure(8, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[5])
        plt.plot(x1, y1_5, "-b")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[5]])
        plt.savefig('spline_5.pdf', dpi=300)
        plt.clf()

        plt.figure(9, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[6])
        plt.plot(x1, y1_6, "-b")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[6]])
        plt.savefig('spline_6.pdf', dpi=300)
        plt.clf()

        plt.figure(10, figsize=(16, 9))
        plt.title("Spline(%.2f)" % rho1[7])
        plt.plot(x1, y1_7, "-k")
        plt.ylim(15.5, 26.5)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['spline(%.2f)' % rho1[7]])
        plt.savefig('spline_7.pdf', dpi=300)
        plt.clf()

        #######
        # Noise
        #######

        plt.figure(11, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[1])
        plt.plot(x1, err1_1, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[1]])
        plt.savefig('remnains_1.pdf', dpi=300)
        plt.clf()

        plt.figure(12, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[2])
        plt.plot(x1, err1_2, "-b")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[2]])
        plt.savefig('remnains_2.pdf', dpi=300)
        plt.clf()

        plt.figure(13, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[3])
        plt.plot(x1, err1_3, "-b")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[3]])
        plt.savefig('remnains_3.pdf', dpi=300)
        plt.clf()

        plt.figure(14, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[4])
        plt.plot(x1, err1_4, "-g")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[4]])
        plt.savefig('remnains_4.pdf', dpi=300)
        plt.clf()

        plt.figure(15, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[5])
        plt.plot(x1, err1_5, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[5]])
        plt.savefig('remnains_5.pdf', dpi=300)
        plt.clf()

        plt.figure(16, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[6])
        plt.plot(x1, err1_6, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[6]])
        plt.savefig('remnains_6.pdf', dpi=300)
        plt.clf()

        plt.figure(17, figsize=(16, 9))
        plt.title("Remains(%.2f)" % rho1[7])
        plt.plot(x1, err1_7, "-k")
        plt.ylim(-2, 3)
        plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
        plt.legend(['remains(%.2f)' % rho1[7]])
        plt.savefig('remnains_7.pdf', dpi=300)
        plt.clf()
        return [norm2[1:8], dictMmodelChange_1["Detailed"]["x_1"][2:9],
                dictMmodelChange_1["Detailed"]["t_1"][2:9],
                dictMmodelChange_1["Detailed"]["t_2"][2:9]]

"""
if __name__ == "__main__":
    os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/")
    norm_1 = plot_all(1)
    norm_2 = plot_all(2)
    os.chdir("/home/semion/Documents/Docs/SciWork/PlBel/SplineProgram/")
"""