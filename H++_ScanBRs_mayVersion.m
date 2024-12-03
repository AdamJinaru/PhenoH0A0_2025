(* ::Package:: *)

ScanBRTEST[mhthis_, vdthis_, vtthis_,mHppthis_,{mHpminthis_,mHpmaxthis_} , 
{salphaminthis_,salphamaxthis_} ,tmpminl_, tmpmaxl_, Npoints_] := 
 Block[{}, tmpprecis = 12; 
  lscandata =  (  
       Table[  
         {
        mh=mhthis;
        mHpp=mHppthis;
        vdnew=vdthis;
        vtnew=vtthis;
        lam2random = RandomReal[{tmpminl, tmpmaxl}, 
            WorkingPrecision -> tmpprecis];
        lam3random = RandomReal[{tmpminl, tmpmaxl}, 
            WorkingPrecision -> tmpprecis];
         mHprandom = RandomReal[{mHpminthis, mHpmaxthis}, 
            WorkingPrecision -> tmpprecis];
         sinalpharandom = RandomReal[{salphaminthis, salphamaxthis}, 
            WorkingPrecision -> tmpprecis];
        (*mA=0;mH=0; munew=0; lam4new=0;lam1new=0;lamnew=0;*);
        MZ=91.; MW=80.; sw=Sqrt[.23] ; cw=Sqrt[1- sw^2];
        MT=173.34;  yt=Sqrt[2]MT/vdnew; ee=Sqrt[4 Pi/137.]; mb=4.7 ;yb=Sqrt[2]mb/vdnew; mc=1.27; yc=Sqrt[2]mc/vdnew; mtau=1.777; ytau=Sqrt[2]mtau/vdnew;
        CKM3x3 = 1.014;
        importdata=getoptionComplete[mh,vdnew,mHpp,mHprandom,sinalpharandom,lam2random,lam3random,vtnew]; 
          If[unitarityBFBtest$,{
        sinbeta=2 vt/Sqrt[vd^2 + 4 vt^2]//.importdata; cosbeta=Sqrt[1 - sinbeta^2]//.importdata;
        cosalpha = Sqrt[1 - sinalpha^2]//.importdata;cosbetap=vd/Sqrt[vd^2 + 2vt^2]//.importdata; sinbetap=Sqrt[1 - cosbetap^2];
     
decayHplusplusHplusWqq=If[mHpp <mHpm+MW, 0 ,(((-2*cosbetap^2*ee^2*mHpm^2)/sw^2 - (2*cosbetap^2*ee^2*mHpm^2)/sw^2 + (cosbetap^2*ee^2*mHpm^4)/(MW^2*sw^2) 
- (2*cosbetap^2*ee^2*mHpm^2*mHpp^2)/(MW^2*sw^2) + (cosbetap^2*ee^2*mHpp^4)/(MW^2*sw^2) + 
(cosbetap^2*ee^2*MW^2)/sw^2)* Sqrt[mHpm^4 - 2*mHpm^2*mHpp^2 + mHpp^4 - 2*mHpm^2*MW^2 - 2*mHpp^2*MW^2 + MW^4])/(16.*\[Pi]*Abs[mHpp]^3)] //.importdata,

decayHplusplusHplusWlnu=If[mHpp <mHpm+MW, 0,(((-2*cosbetap^2*ee^2*mHpm^2)/sw^2 - (2*cosbetap^2*ee^2*mHpm^2)/sw^2 + (cosbetap^2*ee^2*mHpm^4)/(MW^2*sw^2) 
- (2*cosbetap^2*ee^2*mHpm^2*mHpp^2)/(MW^2*sw^2) + (cosbetap^2*ee^2*mHpp^4)/(MW^2*sw^2) + 
(cosbetap^2*ee^2*MW^2)/sw^2)* Sqrt[mHpm^4 - 2*mHpm^2*mHpp^2 + mHpp^4 - 2*mHpm^2*MW^2 - 2*mHpp^2*MW^2 + MW^4])/(16.*\[Pi]*Abs[mHpp]^3)] //.importdata,
                
decayHplusplusHplusWW=If[mHpp <2*MW, 0,((6*ee^4*vt^2)/sw^4 + (ee^4*mHpp^4*vt^2)/(2.*MW^4*sw^4) - 
(2*ee^4*mHpp^2*vt^2)/(MW^2*sw^4))*Sqrt[mHpp^4 - 4*mHpp^2*MW^2]/(32.*\[Pi]*Abs[mHpp]^3)] //.importdata 
} , importdatanull = importdata /. Null -> Sequence[] //Flatten];} ;

 If[unitarityBFBtest$, list[ mHpm //.importdata, (* BrH++-> *) 
 decayHplusplusHplusWqq/ (decayHplusplusHplusWqq +decayHplusplusHplusWW + decayHplusplusHplusWlnu) //.importdata, 
  decayHplusplusHplusWlnu/ (decayHplusplusHplusWqq +decayHplusplusHplusWW + decayHplusplusHplusWlnu) //.importdata, 
 decayHplusplusHplusWW/ (decayHplusplusHplusWqq +decayHplusplusHplusWW + decayHplusplusHplusWlnu) //.importdata, 
 importdata[[{1,3,4,5,2,6,9,8,10,11,7}]]
   ], list[ mHpm //.importdata, (* BrH++-> *)
 decayHplusplusHplusWqq/ (decayHplusplusHplusWqq +decayHplusplusplusWW + decayHplusplusHplusWlnu) //.importdata, 
  decayHplusplusHplusWlnu/ (decayHplusplusHplusWqq +decayHplusplusplusWW + decayHplusplusHplusWlnu) //.importdata, ,
 decayHplusplusWW/ (ddecayHplusplusHplusW +decayHplusplusplusWW ) //.importdata,importdata[[{1,3,4,5,2,6,9,8,10,11,7}]]
   ]] 
  ,{i, 1, Npoints}] // Flatten /. Null -> Sequence[]
       ) //. list -> List; 
(*Clear[lam,lam1,lam2,lam3,mHdpm,mHpm,lam4,mu,mA0,mH0,vt,vd,decayEtalon, decayH0ZZ,decayH0WW,decayH0hh,decayH0HplusWminus,decayH0HminusWplus,decayH0tt]*);lscandata];
       
       (* e.g. *)
       
      (* ScanBRTEST[125, 246, .1, 200,{180,220}, {0,250},{1/1000,1/10000}, -1, 1, 400,"ZZ"];*)
       
       (*followed by *)
       
       (*ListLogPlot[lscandata] *)
    
   
       

