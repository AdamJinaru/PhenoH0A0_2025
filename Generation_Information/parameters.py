# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 10.0 for Linux x86 (64-bit) (December 4, 2014)
# Date: Fri 27 Nov 2015 14:39:16



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
s12 = Parameter(name = 's12',
                nature = 'external',
                type = 'real',
                value = 0.221,
                texname = '\\text{S$\\theta $}_{12}',
                lhablock = 'CKMBLOCK',
                lhacode = [ 1 ])

s23 = Parameter(name = 's23',
                nature = 'external',
                type = 'real',
                value = 0.04,
                texname = '\\text{S$\\theta $}_{23}',
                lhablock = 'CKMBLOCK',
                lhacode = [ 2 ])

s13 = Parameter(name = 's13',
                nature = 'external',
                type = 'real',
                value = 0.0035,
                texname = '\\text{S$\\theta $}_{13}',
                lhablock = 'CKMBLOCK',
                lhacode = [ 3 ])

vt = Parameter(name = 'vt',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{vt}',
               lhablock = 'NEW',
               lhacode = [ 1 ])

ealpha = Parameter(name = 'ealpha',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{ealpha}',
                   lhablock = 'NEW',
                   lhacode = [ 2 ])

ebeta = Parameter(name = 'ebeta',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{ebeta}',
                  lhablock = 'NEW',
                  lhacode = [ 3 ])

ebetap = Parameter(name = 'ebetap',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{ebetap}',
                   lhablock = 'NEW',
                   lhacode = [ 4 ])

sinalpha = Parameter(name = 'sinalpha',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{sinalpha}',
                     lhablock = 'NEW',
                     lhacode = [ 5 ])

lam = Parameter(name = 'lam',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{lam}',
                lhablock = 'NEW',
                lhacode = [ 6 ])

lam1 = Parameter(name = 'lam1',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam1}',
                 lhablock = 'NEW',
                 lhacode = [ 7 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam2}',
                 lhablock = 'NEW',
                 lhacode = [ 8 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam3}',
                 lhablock = 'NEW',
                 lhacode = [ 9 ])

lam4 = Parameter(name = 'lam4',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{lam4}',
                 lhablock = 'NEW',
                 lhacode = [ 10 ])

mu = Parameter(name = 'mu',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\mu',
               lhablock = 'NEW',
               lhacode = [ 11 ])

sn12 = Parameter(name = 'sn12',
                 nature = 'external',
                 type = 'real',
                 value = 0.549508978070806,
                 texname = '\\text{S$\\theta $}_{\\text{n12}}',
                 lhablock = 'PMNSBLOCK',
                 lhacode = [ 1 ])

sn23 = Parameter(name = 'sn23',
                 nature = 'external',
                 type = 'real',
                 value = 0.7071067811865475,
                 texname = '\\text{S$\\theta $}_{\\text{n23}}',
                 lhablock = 'PMNSBLOCK',
                 lhacode = [ 2 ])

sn13 = Parameter(name = 'sn13',
                 nature = 'external',
                 type = 'real',
                 value = 0.15643446504023087,
                 texname = '\\text{S$\\theta $}_{\\text{n13}}',
                 lhablock = 'PMNSBLOCK',
                 lhacode = [ 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0025499999999999997,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 173.34,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

dmsol2 = Parameter(name = 'dmsol2',
                   nature = 'external',
                   type = 'real',
                   value = 0.0086,
                   texname = '\\text{dmsol2}',
                   lhablock = 'FRBlock',
                   lhacode = [ 1 ])

dmatm2 = Parameter(name = 'dmatm2',
                   nature = 'external',
                   type = 'real',
                   value = 0.048,
                   texname = '\\text{dmatm2}',
                   lhablock = 'FRBlock',
                   lhacode = [ 2 ])

NIH = Parameter(name = 'NIH',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{NIH}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

mnl = Parameter(name = 'mnl',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{mnl}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0025499999999999997,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.34,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

mh = Parameter(name = 'mh',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{mh}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

mH = Parameter(name = 'mH',
               nature = 'external',
               type = 'real',
               value = 300,
               texname = '\\text{mH}',
               lhablock = 'MASS',
               lhacode = [ 9000035 ])

mha = Parameter(name = 'mha',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{mha}',
                lhablock = 'MASS',
                lhacode = [ 9000036 ])

mHp = Parameter(name = 'mHp',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{mHp}',
                lhablock = 'MASS',
                lhacode = [ 9000037 ])

mHpp = Parameter(name = 'mHpp',
                 nature = 'external',
                 type = 'real',
                 value = 300,
                 texname = '\\text{mHpp}',
                 lhablock = 'MASS',
                 lhacode = [ 9000055 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.338,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

wh = Parameter(name = 'wh',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{wh}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 9000035 ])

Wha = Parameter(name = 'Wha',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wha}',
                lhablock = 'DECAY',
                lhacode = [ 9000036 ])

WHp = Parameter(name = 'WHp',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WHp}',
                lhablock = 'DECAY',
                lhacode = [ 9000037 ])

WHpp = Parameter(name = 'WHpp',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WHpp}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000055 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

c12 = Parameter(name = 'c12',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s12**2)',
                texname = '\\text{C$\\theta $}_{12}')

c23 = Parameter(name = 'c23',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s23**2)',
                texname = '\\text{C$\\theta $}_{23}')

c13 = Parameter(name = 'c13',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s13**2)',
                texname = '\\text{C$\\theta $}_{13}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 's13',
                   texname = '\\text{CKM1x3}')

mn1 = Parameter(name = 'mn1',
                nature = 'internal',
                type = 'real',
                value = '(mnl*NIH + (1 - NIH)*cmath.sqrt(dmatm2 - dmsol2 + mnl**2))/1.e9',
                texname = '\\text{mn1}')

mn2 = Parameter(name = 'mn2',
                nature = 'internal',
                type = 'real',
                value = '((1 - NIH)*cmath.sqrt(dmatm2 + mnl**2) + NIH*cmath.sqrt(dmsol2 + mnl**2))/1.e9',
                texname = '\\text{mn2}')

mn3 = Parameter(name = 'mn3',
                nature = 'internal',
                type = 'real',
                value = '(mnl*(1 - NIH) + NIH*cmath.sqrt(dmatm2 + mnl**2))/1.e9',
                texname = '\\text{mn3}')

cn12 = Parameter(name = 'cn12',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - sn12**2)',
                 texname = '\\text{C$\\theta $}_{\\text{n12}}')

cn23 = Parameter(name = 'cn23',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - sn23**2)',
                 texname = '\\text{C$\\theta $}_{\\text{n23}}')

cn13 = Parameter(name = 'cn13',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - sn13**2)',
                 texname = '\\text{C$\\theta $}_{\\text{n13}}')

PMNS1x3 = Parameter(name = 'PMNS1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'sn13',
                    texname = '\\text{PMNS1x3}')

cosalpha = Parameter(name = 'cosalpha',
                     nature = 'internal',
                     type = 'real',
                     value = 'ealpha*cmath.sqrt(1 - sinalpha**2)',
                     texname = '\\text{cosalpha}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'c12*c13',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'c13*s12',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(c23*s12) - c12*s13*s23',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'c12*c23 - s12*s13*s23',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'c13*s23',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(c12*c23*s13) + s12*s23',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(c23*s12*s13) - c12*s23',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'c13*c23',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

PMNS1x1 = Parameter(name = 'PMNS1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cn12*cn13',
                    texname = '\\text{PMNS1x1}')

PMNS1x2 = Parameter(name = 'PMNS1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cn13*sn12',
                    texname = '\\text{PMNS1x2}')

PMNS2x1 = Parameter(name = 'PMNS2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(cn23*sn12) - cn12*sn13*sn23',
                    texname = '\\text{PMNS2x1}')

PMNS2x2 = Parameter(name = 'PMNS2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cn12*cn23 - sn12*sn13*sn23',
                    texname = '\\text{PMNS2x2}')

PMNS2x3 = Parameter(name = 'PMNS2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cn13*sn23',
                    texname = '\\text{PMNS2x3}')

PMNS3x1 = Parameter(name = 'PMNS3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(cn12*cn23*sn13) + sn12*sn23',
                    texname = '\\text{PMNS3x1}')

PMNS3x2 = Parameter(name = 'PMNS3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = '-(cn23*sn12*sn13) - cn12*sn23',
                    texname = '\\text{PMNS3x2}')

PMNS3x3 = Parameter(name = 'PMNS3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cn13*cn23',
                    texname = '\\text{PMNS3x3}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

yn1x1 = Parameter(name = 'yn1x1',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13**2*(cn12**2*mn1 + mn2*sn12**2) + mn3*sn13**2)/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn1x1}')

yn1x2 = Parameter(name = 'yn1x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13*mn3*sn13*sn23 + cn12*cn13*mn1*(-(cn23*sn12) - cn12*sn13*sn23) + cn13*mn2*sn12*(cn12*cn23 - sn12*sn13*sn23))/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn1x2}')

yn1x3 = Parameter(name = 'yn1x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13*cn23*mn3*sn13 + cn13*mn2*sn12*(-(cn23*sn12*sn13) - cn12*sn23) + cn12*cn13*mn1*(-(cn12*cn23*sn13) + sn12*sn23))/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn1x3}')

yn2x2 = Parameter(name = 'yn2x2',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13**2*mn3*sn23**2 + mn1*(-(cn23*sn12) - cn12*sn13*sn23)**2 + mn2*(cn12*cn23 - sn12*sn13*sn23)**2)/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn2x2}')

yn2x3 = Parameter(name = 'yn2x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13**2*cn23*mn3*sn23 + mn1*(-(cn12*cn23*sn13) + sn12*sn23)*(-(cn23*sn12) - cn12*sn13*sn23) + mn2*(-(cn23*sn12*sn13) - cn12*sn23)*(cn12*cn23 - sn12*sn13*sn23))/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn2x3}')

yn3x3 = Parameter(name = 'yn3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '(cn13**2*cn23**2*mn3 + mn2*(-(cn23*sn12*sn13) - cn12*sn23)**2 + mn1*(-(cn12*cn23*sn13) + sn12*sn23)**2)/(vt*cmath.sqrt(2))',
                  texname = '\\text{yn3x3}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

yn2x1 = Parameter(name = 'yn2x1',
                  nature = 'internal',
                  type = 'real',
                  value = 'yn1x2',
                  texname = '\\text{yn2x1}')

yn3x1 = Parameter(name = 'yn3x1',
                  nature = 'internal',
                  type = 'real',
                  value = 'yn1x3',
                  texname = '\\text{yn3x1}')

yn3x2 = Parameter(name = 'yn3x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'yn2x3',
                  texname = '\\text{yn3x2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = '\\text{cw}')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = '\\text{sw}')

g = Parameter(name = 'g',
              nature = 'internal',
              type = 'real',
              value = 'ee/sw',
              texname = 'g')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = '\\text{g1}')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = 'cmath.sqrt((4*MW**2*sw**2)/ee**2 - vt**2)',
              texname = 'v')

cosbeta = Parameter(name = 'cosbeta',
                    nature = 'internal',
                    type = 'real',
                    value = '(ebeta*v)/cmath.sqrt(v**2 + 4*vt**2)',
                    texname = '\\text{cosbeta}')

cosbetap = Parameter(name = 'cosbetap',
                     nature = 'internal',
                     type = 'real',
                     value = '(ebetap*v)/cmath.sqrt(v**2 + 2*vt**2)',
                     texname = '\\text{cosbetap}')

sinbeta = Parameter(name = 'sinbeta',
                    nature = 'internal',
                    type = 'real',
                    value = '(2*ebeta*vt)/cmath.sqrt(v**2 + 4*vt**2)',
                    texname = '\\text{sinbeta}')

sinbetap = Parameter(name = 'sinbetap',
                     nature = 'internal',
                     type = 'real',
                     value = '(ebetap*vt*cmath.sqrt(2))/cmath.sqrt(v**2 + 2*vt**2)',
                     texname = '\\text{sinbetap}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/v',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/v',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/v',
                texname = '\\text{yup}')

muD2 = Parameter(name = 'muD2',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*mu*v**2 - (lam1 + lam4)*v**2*vt*cmath.sqrt(2) - 2*(lam2 + lam3)*vt**3*cmath.sqrt(2))/(2.*vt*cmath.sqrt(2))',
                 texname = '\\text{muD2}')

muH2 = Parameter(name = 'muH2',
                 nature = 'internal',
                 type = 'real',
                 value = '(lam*v**2)/4. + ((lam1 + lam4)*vt**2)/2. - mu*vt*cmath.sqrt(2)',
                 texname = '\\text{muH2}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x1 + PMNS2x1*yn2x1 + PMNS3x1*yn3x1',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x2 + PMNS2x1*yn2x2 + PMNS3x1*yn3x2',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x3 + PMNS2x1*yn2x3 + PMNS3x1*yn3x3',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x1 + PMNS2x2*yn2x1 + PMNS3x2*yn3x1',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x2 + PMNS2x2*yn2x2 + PMNS3x2*yn3x2',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x3 + PMNS2x2*yn2x3 + PMNS3x2*yn3x3',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x1 + PMNS2x3*yn2x1 + PMNS3x3*yn3x1',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x2 + PMNS2x3*yn2x2 + PMNS3x3*yn3x2',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x3 + PMNS2x3*yn2x3 + PMNS3x3*yn3x3',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x1 + PMNS2x1*yn2x1 + PMNS3x1*yn3x1',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x1 + PMNS2x2*yn2x1 + PMNS3x2*yn3x1',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x1 + PMNS2x3*yn2x1 + PMNS3x3*yn3x1',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x2 + PMNS2x1*yn2x2 + PMNS3x1*yn3x2',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x2 + PMNS2x2*yn2x2 + PMNS3x2*yn3x2',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x2 + PMNS2x3*yn2x2 + PMNS3x3*yn3x2',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*yn1x3 + PMNS2x1*yn2x3 + PMNS3x1*yn3x3',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*yn1x3 + PMNS2x2*yn2x3 + PMNS3x2*yn3x3',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3*yn1x3 + PMNS2x3*yn2x3 + PMNS3x3*yn3x3',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1**2*yn1x1 + PMNS1x1*PMNS2x1*yn1x2 + PMNS1x1*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x1*yn2x1 + PMNS2x1**2*yn2x2 + PMNS2x1*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x1*yn3x1 + PMNS2x1*PMNS3x1*yn3x2 + PMNS3x1**2*yn3x3',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2*yn1x1 + PMNS1x1*PMNS2x2*yn1x2 + PMNS1x1*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x1*yn2x1 + PMNS2x1*PMNS2x2*yn2x2 + PMNS2x1*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x1*yn3x1 + PMNS2x2*PMNS3x1*yn3x2 + PMNS3x1*PMNS3x2*yn3x3',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3*yn1x1 + PMNS1x1*PMNS2x3*yn1x2 + PMNS1x1*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x1*yn2x1 + PMNS2x1*PMNS2x3*yn2x2 + PMNS2x1*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x1*yn3x1 + PMNS2x3*PMNS3x1*yn3x2 + PMNS3x1*PMNS3x3*yn3x3',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2*yn1x1 + PMNS1x2*PMNS2x1*yn1x2 + PMNS1x2*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x2*yn2x1 + PMNS2x1*PMNS2x2*yn2x2 + PMNS2x2*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x2*yn3x1 + PMNS2x1*PMNS3x2*yn3x2 + PMNS3x1*PMNS3x2*yn3x3',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2**2*yn1x1 + PMNS1x2*PMNS2x2*yn1x2 + PMNS1x2*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x2*yn2x1 + PMNS2x2**2*yn2x2 + PMNS2x2*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x2*yn3x1 + PMNS2x2*PMNS3x2*yn3x2 + PMNS3x2**2*yn3x3',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3*yn1x1 + PMNS1x2*PMNS2x3*yn1x2 + PMNS1x2*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x2*yn2x1 + PMNS2x2*PMNS2x3*yn2x2 + PMNS2x2*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x2*yn3x1 + PMNS2x3*PMNS3x2*yn3x2 + PMNS3x2*PMNS3x3*yn3x3',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3*yn1x1 + PMNS1x3*PMNS2x1*yn1x2 + PMNS1x3*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x3*yn2x1 + PMNS2x1*PMNS2x3*yn2x2 + PMNS2x3*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x3*yn3x1 + PMNS2x1*PMNS3x3*yn3x2 + PMNS3x1*PMNS3x3*yn3x3',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3*yn1x1 + PMNS1x3*PMNS2x2*yn1x2 + PMNS1x3*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x3*yn2x1 + PMNS2x2*PMNS2x3*yn2x2 + PMNS2x3*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x3*yn3x1 + PMNS2x2*PMNS3x3*yn3x2 + PMNS3x2*PMNS3x3*yn3x3',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3**2*yn1x1 + PMNS1x3*PMNS2x3*yn1x2 + PMNS1x3*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x3*yn2x1 + PMNS2x3**2*yn2x2 + PMNS2x3*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x3*yn3x1 + PMNS2x3*PMNS3x3*yn3x2 + PMNS3x3**2*yn3x3',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1**2*yn1x1 + PMNS1x1*PMNS2x1*yn1x2 + PMNS1x1*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x1*yn2x1 + PMNS2x1**2*yn2x2 + PMNS2x1*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x1*yn3x1 + PMNS2x1*PMNS3x1*yn3x2 + PMNS3x1**2*yn3x3',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2*yn1x1 + PMNS1x2*PMNS2x1*yn1x2 + PMNS1x2*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x2*yn2x1 + PMNS2x1*PMNS2x2*yn2x2 + PMNS2x2*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x2*yn3x1 + PMNS2x1*PMNS3x2*yn3x2 + PMNS3x1*PMNS3x2*yn3x3',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3*yn1x1 + PMNS1x3*PMNS2x1*yn1x2 + PMNS1x3*PMNS3x1*yn1x3 + PMNS1x1*PMNS2x3*yn2x1 + PMNS2x1*PMNS2x3*yn2x2 + PMNS2x3*PMNS3x1*yn2x3 + PMNS1x1*PMNS3x3*yn3x1 + PMNS2x1*PMNS3x3*yn3x2 + PMNS3x1*PMNS3x3*yn3x3',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2*yn1x1 + PMNS1x1*PMNS2x2*yn1x2 + PMNS1x1*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x1*yn2x1 + PMNS2x1*PMNS2x2*yn2x2 + PMNS2x1*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x1*yn3x1 + PMNS2x2*PMNS3x1*yn3x2 + PMNS3x1*PMNS3x2*yn3x3',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2**2*yn1x1 + PMNS1x2*PMNS2x2*yn1x2 + PMNS1x2*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x2*yn2x1 + PMNS2x2**2*yn2x2 + PMNS2x2*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x2*yn3x1 + PMNS2x2*PMNS3x2*yn3x2 + PMNS3x2**2*yn3x3',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3*yn1x1 + PMNS1x3*PMNS2x2*yn1x2 + PMNS1x3*PMNS3x2*yn1x3 + PMNS1x2*PMNS2x3*yn2x1 + PMNS2x2*PMNS2x3*yn2x2 + PMNS2x3*PMNS3x2*yn2x3 + PMNS1x2*PMNS3x3*yn3x1 + PMNS2x2*PMNS3x3*yn3x2 + PMNS3x2*PMNS3x3*yn3x3',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3*yn1x1 + PMNS1x1*PMNS2x3*yn1x2 + PMNS1x1*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x1*yn2x1 + PMNS2x1*PMNS2x3*yn2x2 + PMNS2x1*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x1*yn3x1 + PMNS2x3*PMNS3x1*yn3x2 + PMNS3x1*PMNS3x3*yn3x3',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3*yn1x1 + PMNS1x2*PMNS2x3*yn1x2 + PMNS1x2*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x2*yn2x1 + PMNS2x2*PMNS2x3*yn2x2 + PMNS2x2*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x2*yn3x1 + PMNS2x3*PMNS3x2*yn3x2 + PMNS3x2*PMNS3x3*yn3x3',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3**2*yn1x1 + PMNS1x3*PMNS2x3*yn1x2 + PMNS1x3*PMNS3x3*yn1x3 + PMNS1x3*PMNS2x3*yn2x1 + PMNS2x3**2*yn2x2 + PMNS2x3*PMNS3x3*yn2x3 + PMNS1x3*PMNS3x3*yn3x1 + PMNS2x3*PMNS3x3*yn3x2 + PMNS3x3**2*yn3x3',
                  texname = '\\text{I4a33}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1**2 + PMNS2x1**2 + PMNS3x1**2',
                  texname = '\\text{I5a11}')

I5a12 = Parameter(name = 'I5a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2 + PMNS2x1*PMNS2x2 + PMNS3x1*PMNS3x2',
                  texname = '\\text{I5a12}')

I5a13 = Parameter(name = 'I5a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3 + PMNS2x1*PMNS2x3 + PMNS3x1*PMNS3x3',
                  texname = '\\text{I5a13}')

I5a21 = Parameter(name = 'I5a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x2 + PMNS2x1*PMNS2x2 + PMNS3x1*PMNS3x2',
                  texname = '\\text{I5a21}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2**2 + PMNS2x2**2 + PMNS3x2**2',
                  texname = '\\text{I5a22}')

I5a23 = Parameter(name = 'I5a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3 + PMNS2x2*PMNS2x3 + PMNS3x2*PMNS3x3',
                  texname = '\\text{I5a23}')

I5a31 = Parameter(name = 'I5a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1*PMNS1x3 + PMNS2x1*PMNS2x3 + PMNS3x1*PMNS3x3',
                  texname = '\\text{I5a31}')

I5a32 = Parameter(name = 'I5a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2*PMNS1x3 + PMNS2x2*PMNS2x3 + PMNS3x2*PMNS3x3',
                  texname = '\\text{I5a32}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3**2 + PMNS2x3**2 + PMNS3x3**2',
                  texname = '\\text{I5a33}')

