import numpy as np

#Computes an Adjacency Matrix A
#Computes the Characteristic Lag Which is the First Significant Lag
#Takes the Transfer Information Matrix and the Significance Thresholds

def AdjMatrices(T, SigThereshT,TvsIzero):

    nSignals, ~, nLags = np.shape(T)

    Abinary = np.zeros((nSignals,nSignals,nLags))
    Awtd = np.empty((nSignals, nSignals, nLags))
    Awtd.fill(np.NAN)

    AwtdCut = np.zeros((nSignals, nSignals, nLags))
    charLagFirstPeak = np.zeros((nSignals, nSignals))
    TcharLagFirstPeak = np.zeros((nSignals,nSignals))
    charLagMaxPeak = np.zeros((nSignals,nSignals))
    TcharLagMaxPeak = np.zeros((nSignals, nSignals))
    TvsIzerocharLagMaxPeak = np.zeros((nSignals, nSignals))
    nSigLags = np.zeros((nSignals, nSignals))
    FirstSigLag = np.empty((nSignals, nSignals))
    FirstSigLag.fill(np.NAN)

    LastSigLag = np.empty((nSignals, nSignals))
    LastSigLag.fill(np.NAN)

    for sX in range(nSignals):
        for sY in range(nSignals):
            FirstPeakFlag = 0
            FirstSigFlag = 0 

            Awtd = T

            #check the first Lag
            lag = 0
            if T[sX,sY,lag] > SigThereshT[sX,sY]:
                helper1(sX, sY, lag)
                helper2(sX, sY, lag)
                
                TvsIzerocharLagMaxPeak[sX, sY] = TvsIzero[sX, sY,lag]
                FirstSigFlag  = 1 

                if nLags > 1:
                    if T[sX, sY, lag] > T[xS, sY, lag+1]:
                        helper2(sX, sY, lag)
                        FirstPeakFlag = 1
                else:
                    helper2(sX, sY, lag)
                    FirstPeakFlag = 1

            #nlags: number of lags
            #re-check indexing becaus matlab uses indexing start with 1, python uses 0.
            #create function for 2 lag checkings (note the difference) for possible improvement 
            #check the other lag
            if nLags > 1:
                if nLags > 2:
                    for lag in range(1, nLags - 1):
                        if T[sX, sY, lag] > SingThreshT[sX, sY]:
                            helper1(sX, sY, lag)
                            if FirstSigFlag == 0:
                                    FirstSigLag[sX, sY] = lag
                                    FirstSigFlag = 1
                            if FirstPeakFlagst == 0 and T[sX, sY, lag] > T[sX, sY, lag - 1] and T[sX, sY, lag] > T[sX, sY, lag + 1]:
                                helper2(sX, sY, lag)
                                FirstPeakFlag =1
                            if T[sX, sY, lag] > TcharLagMaxPeak[sX, sY]:
                                helper2(sX, sY, lag)
                                TvsIzerocharLagMaxPeak[sX, sY] = TvsIzero[sX, sY, lag]
                #check the last lag
                lag = nLags - 1 
                if T[sX, sY, lag] > SingThreshT[sX, sY]:
                            helper1(sX, sY, lag)
                            if FirstSigFlag == 0:
                                    FirstSigLag[sX, sY] = lag
                                    FirstSigFlag = 1
                            if FirstPeakFlagst == 0 and T[sX, sY, lag] > T[sX, sY, lag - 1]
                                helper2(sX, sY, lag)
                                FirstPeakFlag =1
                            if T[sX, sY, lag] > TcharLagMaxPeak[sX, sY]:
                                helper2(sX, sY, lag)
                                TvsIzerocharLagMaxPeak[sX, sY] = TvsIzero[sX, sY, lag]

    return (Abinary, Awtd, AwtdCut, charLagFirstPeak, TcharLagFirstPeak, charLagMaxPeak, TcharLagMaxPeak, TvsIzerocharLagMaxPeak, nSigLags, FirstSigLag, LastSigLag)


def helper1(sX, sY, lag):
    Abinary[sX,sY,lag] = 1
    AwtdCut[sX,sY,lag] = T[sX,sY,lag]
    LastSigLag[sX,sY] = lag
    nSigLags[sX, sY] = nSigLags[sX, sY] + 1

def helper2(sX, sY, lag):
    charLagMaxPeak[sX, sY] = lag
    TcharLagMaxPeak[sX, sY] = T[sX, sY, lag]


