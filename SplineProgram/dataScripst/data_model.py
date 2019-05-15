#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:14:38 2018

@author: semion
"""
import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt


def func(x):
    """
    модельная функция
    """
    y = ((0.79*(np.sin(2*np.pi/24*x) +
          np.exp(-(x - 70)**2/100) +
          np.exp(-(x - 130)**2/130) +
          0.5*np.sin(np.heaviside(x-96, 76)*2*np.pi/27.4*x) +
          np.exp(-(np.heaviside(x-57, 1)*x - 200)**2/200)*np.sin(0.01*x) +
          0.01*np.heaviside(157-x, 1)*np.sin(2*np.pi*x/365)) + 20))
#   y = 2*np.sin(2*np.pi*x/12) + 0.5*np.cos(2*np.pi*x/10)+23 - np.abs(x-100)/20
    return y


def func_rand(func, x):
    """
    модель измерения с шумом
    """
    y = func(x) + np.random.randn(np.size(x))*0.60
    return y

x = np.load("data_x_2.npy")  # загрузим из файла х
y = np.load("data_y_2.npy")  # загрузим из файла у построенный по модели

x_f = np.append(x[:500], x[600:1000])
y_f = np.append(y[:500], y[600:1000])

x_f = np.append(x_f, x[1100:])
y_f = np.append(y_f, y[1100:])

# x = np.linspace(0, 200, 1600)
# y = func_rand(func, x)  # func(x)
y_pure = func(x)  #
noise_f = y_f - func(x_f)  #
noise = y - func(x)  #

q = 5  #
rho = np.array([5.68138,
                34.81482,
                42.65844,
                52.74310,
                59.46620,
                66.18930,
                93.08171,
                124.45618,
                180.48203,
                280.20804,
                325.58898])  # значения сглаживающего фактора

rho_f = np.array([44.91039,
                  54.24864,
                  63.06809,
                  88.22947])

# rho = np.array([80.95694,
#                202.67597,
#                416.18312,
#                547.87912,
#                597.76397,
#                637.67185,
#                707.51064,
#                845.19282,
#                925.00858,
#                950.9487])

# восстаовленные зависимости
s = [UnivariateSpline(x, y, k=5, s=rho[i]) for i in range(np.size(rho))]
s_f = [UnivariateSpline(x_f, y_f, k=5, s=rho_f[i])
       for i in range(np.size(rho_f))]
# восстановленные зависимости в моменты времени измерений
y_dependences = np.array([s_i(x) for s_i in s])

y_1 = s[1](x)
y_2 = s[2](x)
y_err_pl = s[3](x)
y_4 = s[4](x)
y_spl_pl = s[5](x)
y_6 = s[6](x)
y_7 = s[7](x)
err_y1 = y - y_1
err_y2 = y - y_2
err_y_pl = y - y_err_pl
err_y4 = y - y_4
err_y5 = y - y_spl_pl
err_y6 = y - y_6
err_y7 = y - y_7

y_1_f = s_f[0](x)
y_2_f = s_f[1](x)
y_3_f = s_f[2](x)
y_4_f = s_f[3](x)

err_y1_f = y_f - s_f[0](x_f)
err_y2_f = y_f - s_f[1](x_f)
err_y3_f = y_f - s_f[2](x_f)
err_y4_f = y_f - s_f[3](x_f)
norm_noise = np.linalg.norm(noise)
norm_rem = np.linalg.norm(
                       [y-spline(x)-noise for spline in s], axis=1)/norm_noise
norm_func = np.linalg.norm(y_pure)
norm = np.linalg.norm([y_pure-spline(x) for spline in s], axis=1)/norm_func

norm_noise_f = np.linalg.norm(noise_f)
norm_rem_f = np.linalg.norm(
             [y_f-spline(x_f)-noise_f for spline in s_f], axis=1)/norm_noise_f

norm_f = np.linalg.norm([y_pure-spline(x) for spline in s_f], axis=1)/norm_func

if __name__ == "__main__":
    """
    plt.figure(1, figsize=(16, 9))
    plt.title("Signal")
    plt.plot(x_f[:500], y_f[:500], "k-",
             x_f[500:900], y_f[500:900], "k-",
             x_f[900:], y_f[900:], "k-")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['signal'])
    plt.savefig('data_signal_f.pdf', dpi=300)

    plt.figure(2, figsize=(16, 9))
    plt.title("Model Function")
    plt.plot(x, y_pure, "k-")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['model function'])
    plt.savefig('data_model_function_f.pdf', dpi=300)

    plt.figure(3, figsize=(16, 9))
    plt.title("Noise")
    plt.plot(x_f[:500], noise_f[:500], "k-",
             x_f[500:900], noise_f[500:900], "k-",
             x_f[900:], noise_f[900:], "k-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['real noise'])
    plt.savefig('data_real_noise_f.pdf', dpi=300)


#########
# Splines
#########

    plt.figure(16, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho_f[0])
    plt.plot(x, y_1_f, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho_f[0]])
    plt.savefig('spline_1_f.pdf', dpi=300)

    plt.figure(17, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho_f[1])
    plt.plot(x, y_2_f, "-b")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho_f[1]])
    plt.savefig('spline_2_f.pdf', dpi=300)

    plt.figure(5, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho_f[2])
    plt.plot(x, y_3_f, "-g")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho_f[2]])
    plt.savefig('spline_3_f.pdf', dpi=300)

    plt.figure(6, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho_f[3])
    plt.plot(x, y_4_f, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho_f[3]])
    plt.savefig('spline_4_f.pdf', dpi=300)

#######
# Noise
#######

    plt.figure(10, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho_f[0])
    plt.plot(x_f[:500], err_y1_f[:500], "g-",
             x_f[500:900], err_y1_f[500:900], "g-",
             x_f[900:], err_y1_f[900:], "g-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho_f[0]])
    plt.savefig('remnands_1_f.pdf', dpi=300)

    plt.figure(11, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho_f[1])
    plt.plot(x_f[:500], err_y2_f[:500], "b-",
             x_f[500:900], err_y2_f[500:900], "b-",
             x_f[900:], err_y2_f[900:], "b-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho_f[1]])
    plt.savefig('remnands_2_f.pdf', dpi=300)

    plt.figure(12, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho_f[2])
    plt.plot(x_f[:500], err_y3_f[:500], "k-",
             x_f[500:900], err_y3_f[500:900], "k-",
             x_f[900:], err_y3_f[900:], "k-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho_f[2]])
    plt.savefig('remnands_3_f.pdf', dpi=300)

    plt.figure(13, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho_f[3])
    plt.plot(x_f[:500], err_y4_f[:500], "k-",
             x_f[500:900], err_y4_f[500:900], "k-",
             x_f[900:], err_y4_f[900:], "k-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho_f[3]])
    plt.savefig('remnands_4_f.pdf', dpi=300)
    """

    """
    plt.figure(1, figsize=(16, 9))
    plt.title("Signal")
    plt.plot(x, y, "k-")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['signal'])
    plt.savefig('data_signal.pdf', dpi=300)

    plt.figure(2, figsize=(16, 9))
    plt.title("Model Function")
    plt.plot(x, y_pure, "k-")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['model function'])
    plt.savefig('data_model_function.pdf', dpi=300)

    plt.figure(3, figsize=(16, 9))
    plt.title("Noise")
    plt.plot(x, noise, "k-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['real noise'])
    plt.savefig('data_real_noise.pdf', dpi=300)

#########
# Splines
#########

    plt.figure(16, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[1])
    plt.plot(x, y_1, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[1]])
    plt.savefig('spline_1.pdf', dpi=300)

    plt.figure(17, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[2])
    plt.plot(x, y_2, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[2]])
    plt.savefig('spline_2.pdf', dpi=300)

    plt.figure(5, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[3])
    plt.plot(x, y_err_pl, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[3]])
    plt.savefig('spline_3.pdf', dpi=300)

    plt.figure(6, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[4])
    plt.plot(x, y_4, "-b")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[4]])
    plt.savefig('spline_4.pdf', dpi=300)

    plt.figure(7, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[5])
    plt.plot(x, y_spl_pl, "-g")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[5]])
    plt.savefig('spline_5.pdf', dpi=300)

    plt.figure(8, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[6])
    plt.plot(x, y_6, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[6]])
    plt.savefig('spline_6.pdf', dpi=300)

    plt.figure(9, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[7])
    plt.plot(x, y_7, "-k")
    plt.ylim(18, 23)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[7]])
    plt.savefig('spline_7.pdf', dpi=300)

#######
# Noise
#######

    plt.figure(10, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[1])
    plt.plot(x, err_y1, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[1]])
    plt.savefig('remnands_1.pdf', dpi=300)

    plt.figure(11, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[2])
    plt.plot(x, err_y2, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[2]])
    plt.savefig('remnands_2.pdf', dpi=300)

    plt.figure(12, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[3])
    plt.plot(x, err_y_pl, "-g")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[3]])
    plt.savefig('remnands_3.pdf', dpi=300)

    plt.figure(13, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[4])
    plt.plot(x, err_y4, "-b")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[4]])
    plt.savefig('remnands_4.pdf', dpi=300)

    plt.figure(14, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[5])
    plt.plot(x, err_y5, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[5]])
    plt.savefig('remnands_5.pdf', dpi=300)

    plt.figure(15, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[6])
    plt.plot(x, err_y6, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[6]])
    plt.savefig('remnands_6.pdf', dpi=300)

    plt.figure(19, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[7])
    plt.plot(x, err_y7, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[7]])
    plt.savefig('remnands_7.pdf', dpi=300)
    """

    """
    plt.figure(1, figsize=(16, 9))
    plt.title("Signal")
    plt.plot(x, y, "k-")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['signal'])
    plt.savefig('data_signal_2.pdf', dpi=300)

    plt.figure(2, figsize=(16, 9))
    plt.title("Model Function")
    plt.plot(x, y_pure, "k-")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['model function'])
    plt.savefig('data_model_function_2.pdf', dpi=300)

    plt.figure(3, figsize=(16, 9))
    plt.title("Noise")
    plt.plot(x, noise, "k-")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['real noise'])
    plt.savefig('data_real_noise_2.pdf', dpi=300)


#########
# Splines
#########

    plt.figure(16, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[1])
    plt.plot(x, y_1, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[1]])
    plt.savefig('spline_1_2.pdf', dpi=300)

    plt.figure(17, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[2])
    plt.plot(x, y_2, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[2]])
    plt.savefig('spline_2_2.pdf', dpi=300)

    plt.figure(5, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[3])
    plt.plot(x, y_err_pl, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[3]])
    plt.savefig('spline_3_2.pdf', dpi=300)

    plt.figure(6, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[4])
    plt.plot(x, y_4, "-b")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[4]])
    plt.savefig('spline_4_2.pdf', dpi=300)

    plt.figure(7, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[5])
    plt.plot(x, y_spl_pl, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[5]])
    plt.savefig('spline_5_2.pdf', dpi=300)

    plt.figure(8, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[6])
    plt.plot(x, y_6, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[6]])
    plt.savefig('spline_6_2.pdf', dpi=300)

    plt.figure(9, figsize=(16, 9))
    plt.title("Spline(%.2f)" %rho[7])
    plt.plot(x, y_7, "-k")
    plt.ylim(15, 27)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['spline(%.2f)' %rho[7]])
    plt.savefig('spline_7_2.pdf', dpi=300)

#######
# Noise
#######

    plt.figure(10, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[1])
    plt.plot(x, err_y1, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[1]])
    plt.savefig('remnands_1_2.pdf', dpi=300)

    plt.figure(11, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[2])
    plt.plot(x, err_y2, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[2]])
    plt.savefig('remnands_2_2.pdf', dpi=300)

    plt.figure(12, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[3])
    plt.plot(x, err_y_pl, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[3]])
    plt.savefig('remnands_3_2.pdf', dpi=300)

    plt.figure(13, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[4])
    plt.plot(x, err_y4, "-b")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[4]])
    plt.savefig('remnands_4_2.pdf', dpi=300)

    plt.figure(14, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[5])
    plt.plot(x, err_y5, "-g")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[5]])
    plt.savefig('remnands_5_2.pdf', dpi=300)

    plt.figure(15, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[6])
    plt.plot(x, err_y6, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[6]])
    plt.savefig('remnands_6_2.pdf', dpi=300)

    plt.figure(19, figsize=(16, 9))
    plt.title("Remains(%.2f)" %rho[7])
    plt.plot(x, err_y7, "-k")
    plt.ylim(-2, 3)
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.98, top=0.96)
    plt.legend(['remains(%.2f)' %rho[7]])
    plt.savefig('remnands_7_2.pdf', dpi=300)
    """
