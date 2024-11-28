   
The procedure 
> do not fix l2 and l3 by hand to 0.2, 0.3 respectively

> do instead, e.g. for mHpp = 220 GeV and mHp=215 GeV:  
data = ScanBRTEST[125, 246, 0.1,  220, {215, 215}, {8/10000, 8/10000}, -1, 1, 3];
or  
data = ScanBRTEST[125, 246, 0.1,  220, {214, 216}, {8/10000, 8/10000}, -1, 1, 3];

> print the data set: 
data

>

{{215., 0., 0., 
  1., {mHdpm -> 220., mHpm -> 215., mh0 -> 125., mH0 -> 209.881, 
   mA -> 209.881, mu -> 0.102941, lam -> 0.516393, lam1 -> 0.675187, 
   lam2 -> -0.0171637791391, lam3 -> 0.583920897543, 
   lam4 -> -0.143765}}, {215., 0., 0., 
  1., {mHdpm -> 220., mHpm -> 215., mh0 -> 125., mH0 -> 209.881, 
   mA -> 209.881, mu -> 0.102941, lam -> 0.516393, lam1 -> 0.675188, 
   lam2 -> -0.875080944148, lam3 -> 0.937541165382, 
   lam4 -> -0.143765}}, {215., 0., 0., 
  1., {mHdpm -> 220., mHpm -> 215., mh0 -> 125., mH0 -> 209.881, 
   mA -> 209.881, mu -> 0.102941, lam -> 0.516393, lam1 -> 0.675187, 
   lam2 -> 0.105810637704, lam3 -> -0.160770363376, 
   lam4 -> -0.143765}}}

>then chose a point with random l2 and l3 values and the fixed/near desired Hp mass 

> check on the BR plots this is a good point 


