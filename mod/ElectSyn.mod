UNITS {
    (nA) = (nanoamp)
    (mV) = (millivolt)
    (uS) = (microsiemens)
}

    
NEURON {
    POINT_PROCESS ElectSyn
    NONSPECIFIC_CURRENT i
    RANGE g, i
    RANGE weight
    
    RANGE vpeer     : Using a RANGE variable as opposed to POINTER for parallel mode
        

}

PARAMETER {
    v (millivolt)
    vpeer (millivolt)
    g = 0.000049999999999999996 (microsiemens)
    weight = 1

}


ASSIGNED {
    i (nanoamp)
}

BREAKPOINT {
    i = weight * g * (v - vpeer)
} 