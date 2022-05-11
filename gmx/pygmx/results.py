# encoding: utf-8
"""
@author: Xin Zhang
@contact: zhangxin@szbl.ac.cn
@file: mmpbsa_data.py
@time: 5/21/21 5:29 PM
@desc:
"""

affinity = {
    '7KFY': 55.7,
    '7KFX': 14.1,
    '7KFV': 4.2,
    '7KFW': 76.3,
    '7JVA': 7.5,
    '7KGJ': 38,
    '7KGK': 40.6,
    '7C8D': 6.4,
    '6LZG': 18.5,
    '7L5B': 0.0275,
    '7JW0': 4.58,
    # Rp
    '6YZ5': 39,
    '6ZBP': 12,
    '7B27': 8.23,
    '7BWJ': 5.14,
    '7CH4': 0.18,
    '7CH5': 0.78,
    '7E23': 0.698,
    '7JMO': 39.6,
    '7JMP': 20.9,
    '7K8M': 27,
    # 3TH
    '7DEU': 0.001,
    '7CM4': 0.027,
    '6W41': 115,
    '6YM0': 19,
    '6ZER': 2,
    '7B3O': 8.1,
    '7C01': 4.14,
    '7DEO': 2.33,
    '7MZF': 5.69,
    '7DPM': 5.48
}

restrain = {
    '7KFY': -5.486,
    '7KFX': 3.653,
    '7KFV': -3.771,
    '7KFW': -9.842,
    '7JVA': -16.462,
    # '7KGJ': -21.779,
    '7KGK': -16.955,
    '7C8D': -13.162,
    # '7L5B': -20.577,
    # '7JW0': -26.291,
    # Rp
    '6YZ5': -0.620,
    '6ZBP': -12.784,
    '7B27': -24.292,
    '7BWJ': -26.060,
    '7CH4': -21.641,
    '7CH5': -12.316,
    '7E23': -23.549,
    '7JMO': -0.121,
    # '7JMP': -23.757,
    '7K8M': -3.090,
    # '7DEU': -22.617,
    # '7CM4': -21.970,
    '6W41': -19.909,
    '6YM0': -14.759,
    '6ZER': 0.947,
    # '7B3O': 3.764,
    '7C01': 2.289,
    '7DEO': -21.426,
    '7DPM': -19.459
}

# most_restr = {
#     '7KFY': -8.653,
#     '7KFX': -6.044,
#     '7KFV': 2.241,
#     '7KFW': -15.628,
#     '7JVA': -12.382,
#     # '7KGJ': -,
#     '7KGK': -18.850,
#     '7C8D': -11.476,
#     '7L5B': -22.593,
#     '7JW0': -29.404,
#     # Rp
#     '6YZ5': -4.281,
#     '6ZBP': -16.830,
#     '7B27': -16.896,
#     '7BWJ': -26.239,
#     '7CH4': -16.852,
#     '7CH5': -17.718,
#     '7E23': -20.526,
#     '7JMO': -5.468,
#     # '7JMP': -23.757,
#     '7K8M': -4.144,
#     '7DEU': -18.056,
#     '7CM4': -21.196,
#     '6W41': -16.464,
#     '6YM0': -15.375,
#     '6ZER': -3.615,
#     # '7B3O':
#     '7C01': 2.244,
#     '7DEO': -19.836
# }
#
# most_restr_2 = {  # USE 10NS ENTROPY
#     '7KFY': -5.878,
#     '7KFX': 3.376,
#     '7KFV': -2.702,
#     '7KFW': -10.953,
#     '7JVA': -12.382,
#     # '7KGJ': -,
#     '7KGK': -16.080,
#     '7C8D': -10.909,
#     '7L5B': -20.117,
#     '7JW0': -26.728,
#     # Rp
#     '6YZ5': -4.281,
#     '6ZBP': -14.305,
#     '7B27': -15.575,
#     '7BWJ': -26.877,
#     '7CH4': -22.278,
#     '7CH5': -15.042,
#     '7E23': -23.351,
#     '7JMO': -2.516,
#     # '7JMP': -23.757,
#     '7K8M': -3.510,
#     '7DEU': -23.395,
#     '7CM4': -20.080,
#     '6W41': -17.506,
#     '6YM0': -16.124,
#     '6ZER': -2.955,
#     # '7B3O':
#     '7C01': 2.484,
#     '7DEO': -19.693
# }


relax10_200 = {
    '7KFY': -3.231,
    '7KFX': -0.207,
    '7KFV': -6.179,
    '7KFW': 0.571,
    '7JVA': -4.797,
    '7KGK': -2.690,
    # '6LZG': -14.006,
    # '7L5B': -19.445,
    # '7JW0': 28.586,
    '6YZ5': -8.440,
    '6ZBP': -13.476,
    '7B27': -8.235,
    '7BWJ': -13.726,
    # '7CH4': -10.411,
    # '7CH5': -1.853,
    '7E23': -19.594,
    '7JMO': 3.812,
    # '7JMP': -31.643,
    '7K8M': -3.218,
    # '7DEU': -17.934,
    # '7CM4': -1.063,
    '6W41': -8.762,
    '6YM0': -10.630,
    '6ZER': -9.253,
    # '7B3O': -2.842,
    # '7C01': -11.285,
    '7DEO': -20.911,
    # '7DPM': -11.198
}

# relax10_1000 = {
#     '7KFY': -3.217,
#     '7KFX': -3.647,
#     '7KFV': -9.875,
#     '7KFW': 0.387,
#     '7JVA': -6.273,
#     # '7KGJ': -15.383,
#     '7KGK': -3.223,
#     '7C8D': -10.546,
#     '7L5B': -9.871,
#     # '7JW0': 28.586,
#     # Rp
#     '6YZ5': -2.874,
#     '6ZBP': -23.671,
#     '7B27': -5.256,
#     '7BWJ': -17.503,
#     '7CH4': -22.238,
#     '7CH5': -6.655,
#     '7E23': -33.263,
#     '7JMO': -0.962,
#     # '7JMP': -31.643,
#     '7K8M': -17.288,
#     '7DEU': -14.413,
#     '7CM4': -14.350,
#     '6W41': -14.711,
#     '6YM0': -21.000,
#     '6ZER': -9.233,
#     # '7B3O': -2.842,
#     '7C01': -14.301,
#     '7DEO': -25.871
# }


# relax_most = {
#     '7KFY': 5.508,
#     '7KFX': 1.422,
#     '7KFV': 0.213,
#     '7KFW': 3.334,
#     '7JVA': -5.354,
#     # '7KGJ': -13.424,
#     '7KGK': 13.084,
#     # '7C8D': -9.332,
#     '6LZG': -5.534,
#     # '7L5B': -20.016,
#     # '7JW0': -5.622,
#     '6YZ5': -5.784,
#     '6ZBP': -17.258,
#     '7B27': -11.117,
#     '7BWJ': -23.299,
#     # '7CH4': -11.055,
#     # '7CH5': -12.025,
#     '7E23': -16.402,
#     '7JMO': 3.338,
#     # '7JMP':
#     '7K8M': -12.491,
#     # '7DEU': -17.897,
#     # '7CM4': -16.715,
#     '6W41': 5.038,
#     '6YM0': -7.709,
#     '6ZER': -14.475,
#     # '7B3O':
#     '7C01': -5.565,
#     '7DEO': -10.112,
#     '7DPM': -15.314
# }

# relax_use_10ie = {
#     '7KFY': -2.828,
#     '7KFX': -0.539,
#     '7KFV': -7.474,
#     '7KFW': 0.075,
#     '7JVA': -7.211,
#     # '7KGJ': -13.424,
#     '7KGK': -2.116,
#     '7C8D': -11.74,
#     '7L5B': -20.75,
#     # '7JW0': -5.622,
#     '6YZ5': -9.441,
#     '6ZBP': -13.615,
#     '7B27': -8.496,
#     '7BWJ': -15.696,
#     '7CH4': -9.307,
#     '7CH5': -3.160,
#     '7E23': -20.883,
#     '7JMO': 3.085,
#     # '7JMP':
#     '7K8M': -4.144,
#     '7DEU': -17.963,
#     '7CM4': -5.356,
#     '6W41': 7.446,
#     '6YM0': -9.431,
#     '6ZER': -8.279,
#     # '7B3O':
#     '7C01': -9.003,
#     '7DEO': -19.71
# }


# relax_most_20 = {
#     '7KFY': -0.158,
#     '7KFX': -5.067,
#     '7KFV': -8.911,
#     '7KFW': -0.0179,
#     '7JVA': -6.406,
#     # '7KGJ': -13.424,
#     '7KGK': -2.94,
#     '7C8D': -13.721,
#     '7L5B': -15.578,
#     '7JW0': -5.622,
#     '6YZ5': -4.319,
#     '6ZBP': -27.999,
#     '7B27': -12.003,
#     '7BWJ': -23.186,
#     '7CH4': -20.326,
#     '7CH5': -9.126,
#     '7E23': -28.700,
#     '7JMO': -3.097,
#     # '7JMP':
#     '7K8M': -14.663,
#     '7DEU': -22.633,
#     '7CM4': -17.988,
#     '6W41': -3.105,
#     '6YM0': -16.596,
#     '6ZER': -13.291,
#     # '7B3O':
#     '7C01': -11.489,
#     '7DEO': -23.254
# }

# most = {
#     '7KFY': -0.158,
#     '7KFX': -5.067,
#     '7KFV': -8.911,
#     '7KFW': -0.0179,
#     '7JVA': -6.406,
#     '7KGJ': -13.424,
#     '7KGK': -2.94,
#     '7C8D': -13.721,
#     '7L5B': -15.578,
#     '7JW0': -5.622
# }
#
# ave = {
#     '7KFY': -2.435,
#     '7KFX': -6.857,
#     '7KFV': -8.415,
#     '7KFW': 1.021,
#     '7JVA': -7.738,
#     '7KGJ': -13.668,
#     '7KGK': 0.692,
#     '7C8D': -15.142,
#     '7L5B': -10.109,
#     '7JW0': -6.478
# }
#
# IE = {
#     # '7KFY': -3.217,
#     # '7KFX': -3.647,
#     # '7KFV': -9.875,
#     # Rp
#     '6YZ5': -2.874,
#     '6ZBP': -23.671,
#     '7B27': -5.256,
#     '7BWJ': -17.503,
#     '7CH4': -22.238,
#     '7CH5': -6.655,
#     '7JMO': -0.962,
#     # '7JMP': -31.643,
#     '7K8M': -14.952
# }
#
# Sch = {
#     # '7KFY': 55.7,
#     # '7KFX': 14.1,
#     # '7KFV': 4.2,
#     # Rp
#     '6YZ5': -14.93,
#     '6ZBP': -32.448,
#     '7B27': -35.307,
#     '7BWJ': -26.926,
#     '7CH4': -35.062,
#     '7CH5': -22.437,
#     '7JMO': -12.665,
#     # '7JMP': 20.9,
#     '7K8M': -23.799
# }
#
# mmpbsa = {
#     # '7KFY': 55.7,
#     # '7KFX': 14.1,
#     # '7KFV': 4.2,
#     # Rp
#     '6YZ5': -16.460,
#     '6ZBP': -33.958,
#     '7B27': -36.922,
#     '7BWJ': -29.890,
#     '7CH4': -37.940,
#     '7CH5': -25.244,
#     '7JMO': -15.533,
#     # '7JMP': 20.9,
#     '7K8M': -26.617
# }
#
#
# hyHOH_restr = {
#     '7KFY': -0.342,
#     '7KFX': -4.145,
#     # '7JVA': -6.231,
#     '7KGK': -35.974,
#     # Rp
#     '6YZ5': 3.373,
#     '6ZBP': -13.875,
#     '7B27': -9.373,
#     '7BWJ': -28.019,
#     '7CH4': -15.258,
#     # '7JMO': -7.105,
#     # '7JMP': -29.114,
#     '7K8M': -5.959
# }
#
# mm_pro = {
#     '7KFY': -16.387,
#     '7KFX': -9.996,
#     '7JVA': -26.702,
#     '7KGK': -46.551,
#     # Rp
#     '6YZ5': -8.99,
#     '6ZBP': -24.378,
#     '7B27': -52.937,
#     '7BWJ': -35.504,
#     '7CH4': -46.148,
#     '7JMO': -21.897,
#     # '7JMP': -32.097,
#     '7K8M': -15.132
# }
#
# mm_com = {
#     '7KFY': -225.743,
#     '7KFX': -277.936,
#     '7JVA': -227.773,
#     '7KGK': -225.240,
#     # Rp
#     '6YZ5': -166.171,
#     '6ZBP': -125.567,
#     '7B27': -265.442,
#     '7BWJ': -146.94,
#     '7CH4': -234.644,
#     '7JMO': -273.666,
#     '7JMP': -163.202,
#     '7K8M': -212.151
# }

relax10_hyhoh_10IE = {
    '7KFY': 2.637,
    '7KFX': -2.327,
    '7KFV': -14.108,
    '7KFW': 2.618,
    '7JVA': -7.226,
    '7KGK': -8.460,
    # '6LZG': -10.743,
    '6YZ5': -8.529,
    '6ZBP': -13.629,
    '7B27': -6.831,
    '7BWJ': -11.436,
    '7E23': -16.954,
    '7JMO': -4.260,
    '7K8M': -5.169,
    '6W41': -0.930,
    '6YM0': -16.459,
    '6ZER': -16.929,
    # '7C01': -12.165,
    '7DEO': -13.762,
    # '7DPM': -16.863,
}

# relax10_hyhoh = {
#     '7KFY': 0.460,
#     '7KFX': 2.451,
#     '7KFV': -9.013,
#     '7KFW': 1.991,
#     '7JVA': -7.304,
#     # '7KGJ': -15.383,
#     '7KGK': 2.590,
#     '7C8D': -11.618,
#     # '7L5B': -19.445,
#     # '7JW0': 28.586,
#     # Rp
#     '6YZ5': -2.274,
#     '6ZBP': -13.109,
#     '7B27': -17.348,
#     '7BWJ': -8.214,
#     # '7CH4': -10.411,
#     # '7CH5': -1.853,
#     '7E23': -23.882,
#     '7JMO': 0.293,
#     # '7JMP': -31.643,
#     '7K8M': -13.883,
#     # '7DEU': -15.686,
#     # '7CM4': -7.646,
#     '6W41': -0.371,
#     '6YM0': -17.647,
#     '6ZER': -5.766,
#     # '7B3O': -2.842,
#     '7C01': -11.650,
#     '7DEO': -11.172,
#     '7DPM': -22.761
# }


# relax10_hyhoh_most = {
#     '7KFY': 14.095,
#     '7KFX': 7.994,
#     '7KFV': 1.281,
#     '7KFW': -1.533,
#     '7JVA': 8.468,
#     # '7KGJ': -15.383,
#     '7KGK': 14.080,
#     '7C8D': -8.333,
#     # '7L5B': -19.445,
#     # '7JW0': 28.586,
#     # Rp
#     '6YZ5': -8.509,
#     '6ZBP': -17.428,
#     '7B27': 13.574,
#     '7BWJ': -13.451,
#     # '7CH4': -10.411,
#     # '7CH5': -1.853,
#     '7E23': -30.673,
#     '7JMO': 2.408,
#     # '7JMP': -20.,
#     '7K8M': -20.509,
#     # '7DEU': -12.743,
#     # '7CM4': -22.344,
#     '6W41': -0.764,
#     '6YM0': -7.557,
#     '6ZER': -3.660,
#     # '7B3O': -2.842,
#     '7C01': -5.957,
#     '7DEO': -3.590,
#     '7DPM': -20.071
# }
#
#
# relax10_hyhoh_most_10ie = {
#     '7KFY': 9.087,
#     '7KFX': 0.945,
#     '7KFV': -6.497,
#     '7KFW': 4.868,
#     '7JVA': -1.761,
#     # '7KGJ': -15.383,
#     '7KGK': 10.019,
#     '7C8D': -11.307,
#     # '7L5B': -19.445,
#     # '7JW0': 28.586,
#     # Rp
#     '6YZ5': -5.529,
#     '6ZBP': -17.058,
#     '7B27': -12.181,
#     '7BWJ': -19.759,
#     # '7CH4': -10.411,
#     # '7CH5': -1.853,
#     '7E23': -14.348,
#     '7JMO': -0.334,
#     # '7JMP': -20.,
#     '7K8M': -13.716,
#     # '7DEU': -16.437,
#     # '7CM4': -15.324,
#     '6W41': 6.389,
#     '6YM0': -14.838,
#     '6ZER': -22.438,
#     # '7B3O': -2.842,
#     '7C01': -7.397,
#     '7DEO': -4.950,
#     '7DPM': -20.411
# }


for1_10_20 = {
    '7KFY': 8.923,
    '7KFX': 14.769,
    '7KFV': 0.846,
    '7KFW': 8.001,
    '7JVA': 4.92,
    '7KGK': 8.252,
    '6YZ5': -5.176,
    '6ZBP': -14.351,
    '7B27': 3.77,
    '7BWJ': -4.486,
    '7E23': -21.452,
    '7JMO': 14.614,
    '7K8M': -3.42,
    '6W41': 18.1,
    '6YM0': 19.948,
    '6ZER': -6.599,
    '7DEO': -7.466
}

for1_10_20_hy = {
    '7KFY': 14.165,
    '7KFX': 13.453,
    '7KFV': -6.094,
    '7KFW': 9.958,
    '7JVA': 4.441,
    '7KGK': 0.236,
    '6YZ5': -4.756,
    '6ZBP': -14.757,
    '7B27': 7.489,
    '7BWJ': -5.77,
    '7E23': -19.469,
    '7JMO': 10.644,
    '7K8M': -5,
    '6W41': 18.724,
    '6YM0': 14.853,
    '6ZER': -12.843,
    '7DEO': -0.616
}

for5_10_20 = {
    '7KFY': 1.643,
    '7KFX': 16.577,
    '7KFV': 0.334,
    '7KFW': -10.964,
    '7JVA': 1.731,
    '7KGK': -1.757,
    '6YZ5': -7.133,
    '6ZBP': -15.002,
    '7B27': -5.248,
    '7BWJ': -4.399,
    '7E23': -32.613,
    '7JMO': 12.638,
    '7K8M': -5.731,
    '6W41': 8.294,
    '6YM0': 12.119,
    '6ZER': -11.402,
    '7DEO': -7.681
}

for5_10_20hy = {
    '7KFY': 9.035,
    '7KFX': 16.31,
    '7KFV': -0.941,
    '7KFW': -8.410,
    '7JVA': 0.860,
    '7KGK': -3.471,
    '6YZ5': -6.320,
    '6ZBP': -13.080,
    '7B27': -4.185,
    '7BWJ': -2.761,
    '7E23': -30.693,
    '7JMO': 12.986,
    '7K8M': -5.661,
    '6W41': 8.294,
    '6YM0': 8.426,
    '6ZER': -9.912,
    '7DEO': -0.101
}

for1_5_20 = {
    '7KFY': 3.697,
    '7KFX': 7.513,
    '7KFV': -0.003,
    '7KFW': 9.329,
    '7JVA': 7.409,
    '7KGK': 10.957,
    '6YZ5': -2.718,
    '6ZBP': -14.581,
    '7B27': 10.215,
    '7BWJ': -11.246,
    '7E23': -22.746,
    '7JMO': 11.491,
    '7K8M': -8.212,
    '6W41': 9.480,
    '6YM0': 3.846,
    '6ZER': -4.688,
    '7DEO': -7.282
}

for1_5_20hy = {
    '7KFY': 6.963,
    '7KFX': 7.531,
    '7KFV': -6.544,
    '7KFW': 6.328,
    '7JVA': 8.21,
    '7KGK': -1.497,
    '6YZ5': -2.984,
    '6ZBP': -17.829,
    '7B27': 14.559,
    '7BWJ': -8.496,
    '7E23': -18.99,
    '7JMO': 4.461,
    '7K8M': -10.177,
    '6W41': 8.32,
    '6YM0': -1.647,
    '6ZER': -8.07,
    '7DEO': -1.419
}

distant_water_1_5_20 = {
    '7KFY': 40.986,
    '7KFX': 28.215,
    '7KFV': 35.713,
    '7KFW': 23.022,
    '7JVA': 13.544,
    '7KGK': 21.427,
    # '6LZG': 17.311,
    '6YZ5': 12.405,
    '6ZBP': 2.390,
    '7B27': 31.640,
    '7BWJ': 7.170
}


distant_water_1_5_20_Pb = {
    '7KFY': -111.788,
    '7KFX': -134.982,
    '7KFV': -127.277,
    '7KFW': -166.334,
    '7JVA': -69.494,
    '7KGK': -96.843,
    # '6LZG': 17.311,
    '6YZ5': -93.722,
    '6ZBP': -78.481,
    '7B27': -162.836,
    '7BWJ': -81.620
}