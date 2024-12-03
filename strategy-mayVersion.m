(* ::Package:: *)

(* see examples at the end of this file *)

getoptionComplete[mh0num_,vdnum_,mHdpmnum_,mHpmnum_,sinalphanum_,lam2num_,lam3num_,vtnum_]:=Block[{},
 mh02=mh0num^2;mHdpm2=mHdpmnum^2;mHpm2=mHpmnum^2;sA=sinalphanum;cA=Sqrt[1 - sA^2]; 
 lam2lam3rep={lam2->lam2num,lam3->lam3num};vt=vtnum;  vd=vdnum;   
 resmulam4$={mu -> Sqrt[2]*vt*((2*mHpm2)/(vd^2 + 2*vt^2) - (mHdpm2 + lam3*vt^2)/vd^2), 
 lam4 -> (4*mHpm2)/(vd^2 + 2*vt^2) - (4*(mHdpm2 + lam3*vt^2))/vd^2} //. lam2lam3rep;
 (* "condition starts here" *)
 test$ = -mh02 - mHdpm2 + (2 lam2 + lam3) vt^2 + (2 mHpm2 vd^2)/(vd^2 + 2 vt^2) //. lam2lam3rep;
 If[(* "test$ > 0 comes here"*)
        test$ > 0,
        (*Print[Style["The 125GeV state is the lighter CP-even", 
  FontColor -> Red]];*)
 reslam1$={lam1 -> (2 (mHdpm2 + lam3 vt^2))/vd^2 + (
    sA (mh02 + mHdpm2 - (2 lam2 + lam3) vt^2 - (2 mHpm2 vd^2)/(
    vd^2 + 2 vt^2)))/(cA vd vt)}  //.lam2lam3rep;
 reslam$={lam -> (2 mh02)/vd^2 + (2 sA^2 ((2 mHpm2)/(vd^2 + 2 vt^2) - (
    mh02 + mHdpm2 - (2 lam2 + lam3) vt^2)/vd^2))/cA^2 }//. lam2lam3rep;
        res$={resmulam4$, reslam1$, reslam$}//Flatten;
        result$= {{mHdpm -> Sqrt[(Sqrt[2] mu vd^2 - lam4 vd^2 vt - 2 lam3 vt^3)/vt]/
  Sqrt[2], mA-> Sqrt[(mu (vd^2 + 4 vt^2))/vt]/2^(1/4), 
 mHpm -> 1/2 Sqrt[((2 Sqrt[2] mu - lam4 vt) (vd^2 + 2 vt^2))/vt],
  mh0 -> (1/Sqrt[
  2])(\[Sqrt]((lam vd^2)/2 + (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
      2 vt) - \[Sqrt](4 vd^2 (-Sqrt[2] mu + (lam1 + lam4) vt)^2 + ((
           lam vd^2)/2 - (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
           2 vt))^2))), 
 mH0 -> (1/Sqrt[
  2])(\[Sqrt]((lam vd^2)/2 + (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
      2 vt) + \[Sqrt](4 vd^2 (-Sqrt[2] mu + (lam1 + lam4) vt)^2 + ((
           lam vd^2)/2 - (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
           2 vt))^2)))} //. res$ //. lam2lam3rep, res$, lam2lam3rep
           } //Flatten;
 unitarityBFBtest$=RKcombinedBFBunit[8,{lam,lam1,lam2,lam3,lam4}] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]];
 unitaritytest$=unitarity2corr[8, lam,lam1,lam2,lam3,lam4] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]]; 
BFBtest$=BFBnew[lam,lam1,lam2,lam3,lam4] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]]; 
           Clear[mh02,mHdpm2,mHpm2,sA,cA];
 unitarityBFBtest$=True;
           (****)
           If[unitarityBFBtest$,
        Append[result$, {sinalpha -> sinalphanum, "vt"-> vtnum, "vd" -> vdnum}] //Flatten
              ,If[unitaritytest$, {(*Print[Style["unbounded-from-below-potential!", FontColor-> Red]],*) result$ //Flatten},
              If[BFBtest$,{(*Print[Style["unitarity violated!", FontColor-> Red]],*) result$ //Flatten}, 
              {(*Print[Style["unitarity and BFB violated!", FontColor-> Red]], *)result$ //Flatten}]]],
     (* "test$ < 0 comes here"*)
     Print[Style["The 125GeV state is the heavier CP-even", 
  FontColor -> Red]];
  reslam1$={lam1 -> (2 (mHdpm2 + lam3 vt^2))/vd^2 - (
    cA (mh02 + mHdpm2 - (2 lam2 + lam3) vt^2 - (2 mHpm2 vd^2)/(
    vd^2 + 2 vt^2)))/(sA vd vt)}  //.lam2lam3rep;
  reslam$={lam -> (2 mh02)/vd^2 + (2 cA^2 ((2 mHpm2)/(vd^2 + 2 vt^2) - (
    mh02 + mHdpm2 - (2 lam2 + lam3) vt^2)/vd^2))/sA^2 }//. lam2lam3rep;
    res$={resmulam4$, reslam1$, reslam$}//Flatten;
        result$= {{mHdpm -> Sqrt[(Sqrt[2] mu vd^2 - lam4 vd^2 vt - 2 lam3 vt^3)/vt]/
  Sqrt[2], mA-> Sqrt[(mu (vd^2 + 4 vt^2))/vt]/2^(1/4), 
 mHpm -> 1/2 Sqrt[((2 Sqrt[2] mu - lam4 vt) (vd^2 + 2 vt^2))/vt],
  mh0 -> (1/Sqrt[
  2])(\[Sqrt]((lam vd^2)/2 + (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
      2 vt) - \[Sqrt](4 vd^2 (-Sqrt[2] mu + (lam1 + lam4) vt)^2 + ((
           lam vd^2)/2 - (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
           2 vt))^2))), 
 mH0 -> (1/Sqrt[
  2])(\[Sqrt]((lam vd^2)/2 + (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
      2 vt) + \[Sqrt](4 vd^2 (-Sqrt[2] mu + (lam1 + lam4) vt)^2 + ((
           lam vd^2)/2 - (Sqrt[2] mu vd^2 + 4 (lam2 + lam3) vt^3)/(
           2 vt))^2)))} //. res$ //. lam2lam3rep, res$, lam2lam3rep
           } //Flatten;
 unitarityBFBtest$=RKcombinedBFBunit[8,{lam,lam1,lam2,lam3,lam4}] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]];
 unitaritytest$=unitarity2corr[8, lam,lam1,lam2,lam3,lam4] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]]; 
BFBtest$=BFBnew[lam,lam1,lam2,lam3,lam4] //. reslam$ //. reslam1$ //. lam2lam3rep //. resmulam4$[[-1]]; 
           Clear[mh02,mHdpm2,mHpm2,sA,cA,vt,vd];
           (****)
           If[unitarityBFBtest$,
        Append[result$, {sinalpha -> sinalphanum, "vt"-> vtnum, "vd" -> vdnum}] //Flatten
              ,If[unitaritytest$, Print[Style["unbounded-from-below-potential!", FontColor-> Red]],If[BFBtest$,Print[Style["unitarity violated!", FontColor-> Red]], Print[Style["unitarity and BFB violated!", FontColor-> Red]]]]]
 ]
        ];
        
      (* "END" of "alternativeCOMPLETE" *)  
        
    
    (* unitarity and BFB constraints *)
    
    
    
    RKcombinedBFBunit[kappa_, lambdas_] := (
  lam = lambdas[[1]]; lam1 = lambdas[[2]]; lam2 = lambdas[[3]]; 
  lam3 = lambdas[[4]]; lam4 = lambdas[[5]]; 
  tmpbool = 
   And[unitarity2corr[kappa, lam, lam1, lam2, lam3, lam4], 
    BFBnew[lam, lam1, lam2, lam3, lam4]]; Clear[lam, lam1, lam2, lam3, lam4]; tmpbool)
  
  unitarity2corr[kappa_, lam_, lam1_, lam2_, lam3_, lam4_] := ( 
  tmpbool = 
   lam1 <= kappa*Pi && lam1 >= -(kappa*Pi) && lam1 + lam4 <= kappa*Pi &&    
    lam1 + lam4 >= -(kappa*Pi) && lam1 + (3*lam4)/2 <= kappa*Pi &&     
    lam1 + (3*lam4)/2 >= -(kappa*Pi) && 10/2 <= kappa*Pi && 
    lam/2 >= -(kappa*Pi) &&     2*lam2 <= kappa*Pi && 
    2*lam2 >= -(kappa*Pi) && 2*(lam2 + lam3) <= kappa*Pi &&    
    2*(lam2 + lam3) >= -(kappa*Pi) &&    (lam + 4*lam2 + 8*lam3 + 
        Sqrt[(lam - 4*lam2 - 8*lam3)^2 + 16*lam4^2])/4 <= 
     kappa*Pi &&    (lam + 4*lam2 + 8*lam3 + 
        Sqrt[(lam - 4*lam2 - 8*lam3)^2 + 16*lam4^2])/
      4 >=     -(kappa*Pi) && (lam + 4*lam2 + 8*lam3 -        
        Sqrt[(lam - 4*lam2 - 8*lam3)^2 + 16*lam4^2])/4 <= 
     kappa*Pi &&    (lam + 4*lam2 + 8*lam3 - 
        Sqrt[(lam - 4*lam2 - 8*lam3)^2 + 16*lam4^2])/
      4 >=     -(kappa*Pi) && (3*lam + 16*lam2 + 12*lam3 +        
        Sqrt[(-3*lam + 16*lam2 + 12*lam3)^2 + 24*(2*lam1 + lam4)^2])/4 <= 
     kappa*Pi &&    (3*lam + 16*lam2 + 12*lam3 + 
        Sqrt[(-3*lam + 16*lam2 + 12*lam3)^2 +          24*(2*lam1 + lam4)^2])/
      4 >= -(kappa*Pi) &&    (3*lam + 16*lam2 + 12*lam3 - 
        Sqrt[(-3*lam + 16*lam2 + 12*lam3)^2 +          24*(2*lam1 + lam4)^2])/
      4 <= kappa*
      Pi &&    (3*lam + 16*lam2 + 12*lam3 - 
        Sqrt[(-3*lam + 16*lam2 + 12*lam3)^2 +          24*(2*lam1 + lam4)^2])/
      4 >= -(kappa*Pi) && lam1 - lam4/2 <= kappa*Pi &&    
    lam1 - lam4/2 >= -(kappa*Pi) &&  lam2 - lam3 <= kappa*Pi && 
    2 lam2 - lam3 >= -kappa*Pi;
  tmpbool);
  
  BFBnew[lam_, lam1_, lam2_, lam3_, lam4_] := 
  And[lam >= 0, lam2 + lam3 >= 0, lam2 + lam3/2 >= 0, 
   Or[ And[lam1 + Sqrt[lam*(lam2 + lam3)] >= 0, 
     Sqrt[lam]*lam3 <= Sqrt[(lam2 + lam3)*lam4^2], 
     lam1 + lam4 + Sqrt[lam*(lam2 + lam3)] >= 0], 
    And[Sqrt[lam]*lam3 >= 
      Sqrt[(lam2 + lam3)*lam4^2], -Sqrt[lam*(lam2 + lam3/2) (1 - lam4^2/2/lam/lam3)] <= 
      lam1 + lam4/2]]];
      
      (* three examples
      
  1/    getoption1AlternativeCOMPLETE[125, 246, 300, 320, 
 8.10001 10^-4, .1, .1, .1]
 
 gives message
 
 "The 125GeV state is the lighter CP-even"
 
 and the output
 
 {mHdpm -> 300., mA -> 338.821, mHpm -> 320., mh0 -> 125., 
 mH0 -> 338.821, mu -> 0.268279, lam4 -> 0.819616, lam1 -> -0.291101, 
 lam -> 0.516395, lam2 -> 0.1, lam3 -> 0.1, sinalpha -> 0.000810001, 
 "vt" -> 0.1, "vd" -> 246}
 
 
 
 2/   getoption1AlternativeCOMPLETE[125.`, 246.`, 105.18`, 92.6729`,
0.99999993`, -0.1216`, 0.6539792024505005`, 0.1`]

gives the message

"The 125GeV state is the heavier CP-even"

and the output

{mHdpm -> 105.18, mA -> 78.1901, mHpm -> 92.6729, mh0 -> 78.1901, 
 mH0 -> 125., mu -> 0.0142872, lam4 -> -0.163565, lam1 -> 0.22095, 
 lam -> 0.516392, lam2 -> -0.1216, lam3 -> 0.653979, sinalpha -> 1., 
 "vt" -> 0.1, "vd" -> 246.}  
 
 
 3/ getoption1AlternativeCOMPLETE[125.`, 246.`, 105.18`, 92.6729`,
 0.99999, -0.1216`, 0.6539792024505005`, 0.1`]
 
 gives the messages
 
" The 125GeV state is the heavier CP-even"
 
 "unbounded-from-below-potential!"
 
 Note the high fine-tuning of sinalpha, between case 2/ and 3/ leading to different
 situations.
 
 *)





 
 
 
  
