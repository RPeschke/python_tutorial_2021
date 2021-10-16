c_BKLM = 1
c_EKLM = 2

c_BKLM_BackwardSection = 0
c_BKLM_ForwardSection = 1
c_EKLM_BackwardSection = 1
c_EKLM_ForwardSection = 2

c_ZPlane = 0
c_PhiPlane = 1

i_sector_EKLM_ForwardSection  = 0
i_sector_BKLM_ForwardSection   = 1
i_sector_BKLM_BackwardSection  = 2
i_sector_EKLM_BackwardSection  = 3


def add_i_section(df):
    df["i_sector"] = i_sector_EKLM_ForwardSection * ((df["Subdetector"] == c_EKLM) & (df["section"] == c_EKLM_ForwardSection)) + \
                     i_sector_BKLM_ForwardSection * ((df["Subdetector"] == c_BKLM) & (df["section"] == c_BKLM_ForwardSection)) + \
                     i_sector_BKLM_BackwardSection* ((df["Subdetector"] == c_BKLM) & (df["section"] == c_BKLM_BackwardSection))+ \
                     i_sector_EKLM_BackwardSection* ((df["Subdetector"] == c_EKLM) & (df["section"] == c_EKLM_BackwardSection)) 
    return df


def isInRange(x , x_min, x_max):
    return (x_min < x_max) & (x_min < x) & (x < x_max) | \
            ((x_min >= x_max) &((x_min < x) | (x < x_max )))


def geometryConverter(section, sector, layer, phiStrip, zStrip):
    x =0
    y =0
    z =0
    layer = min(int(layer),14)
    c_LayerXCoord = [1628, 1700, 1773, 1846, 1919, 1992, 2064, 2137, 2210, 2283, 2356, 2428, 2501, 2574, 2647]
    c_LayerY0  = [ -2403, -2566, -2744, -2862, -2979, -3097, -3234, -3354, -3474, -3587, -3708, -3828, -3948, -4061, -4181]
    c_PhiWidth = [128, 128, 157, 164, 170, 177, 138, 143, 148, 153, 158, 163, 168, 173, 178]

    c_Z01     = 18
    c_Z02     = 25
    c_ZWidth1 = 32
    c_ZWidth2 = 36
    c_ZOffset = 376

    flipped = False
    dy = 0
    dz = 0
    z0 = 0
    zWidth = 0

    # define if module is flipped
    if (layer == 0 and section == 0 and sector == 0): # // layer 0, backward, sector 0
        flipped = True
    elif (layer == 0 and section == 0 and sector == 1):
        flipped = True
    elif (layer == 0 and section == 0 and sector == 2):
        flipped = False
    elif (layer == 0 and section == 0 and sector == 3):
        flipped = False
    elif (layer == 0 and section == 0 and sector == 4):
        flipped = False
    elif (layer == 0 and section == 0 and sector == 5):
        flipped = False
    elif (layer == 0 and section == 0 and sector == 6):
        flipped = True
    elif (layer == 0 and section == 0 and sector == 7):
        flipped = True
    elif (layer == 0 and section == 1 and sector == 0): # // layer 0, forward, sector 0
        flipped = True
    elif (layer == 0 and section == 1 and sector == 1):
        flipped = True
    elif (layer == 0 and section == 1 and sector == 2):
        flipped = True
    elif (layer == 0 and section == 1 and sector == 3):
        flipped = False
    elif (layer == 0 and section == 1 and sector == 4):
        flipped = False
    elif (layer == 0 and section == 1 and sector == 5):
        flipped = False
    elif (layer == 0 and section == 1 and sector == 6):
        flipped = False
    elif (layer == 0 and section == 1 and sector == 7):
        flipped = True
    elif (layer == 1 and section == 0 and sector == 0):# // layer 1, backward, sector 0
        flipped = False
    elif (layer == 1 and section == 0 and sector == 1):
        flipped = False
    elif (layer == 1 and section == 0 and sector == 2):
        flipped = False
    elif (layer == 1 and section == 0 and sector == 3):
        flipped = True
    elif (layer == 1 and section == 0 and sector == 4):
        flipped = True
    elif (layer == 1 and section == 0 and sector == 5):
        flipped = True
    elif (layer == 1 and section == 0 and sector == 6):
        flipped = True
    elif (layer == 1 and section == 0 and sector == 7):
        flipped = False
    elif (layer == 1 and section == 1 and sector == 0):# // layer 1, forward, sector 0
        flipped = False
    elif (layer == 1 and section == 1 and sector == 1):
        flipped = False
    elif (layer == 1 and section == 1 and sector == 2):
        flipped = True
    elif (layer == 1 and section == 1 and sector == 3):
        flipped = True
    elif (layer == 1 and section == 1 and sector == 4):
        flipped = True
    elif (layer == 1 and section == 1 and sector == 5):
        flipped = True
    elif (layer == 1 and section == 1 and sector == 6):
        flipped = False
    elif (layer == 1 and section == 1 and sector == 7):
        flipped = False
    elif (layer > 2 and section == 0):# // backward RPCs
        flipped = True
    else:
        flipped = False

  # convert channels to x, y, z
    if (layer < 2):
        z0     = c_Z01
        zWidth = c_ZWidth1
    else:
        z0     = c_Z02
        zWidth = c_ZWidth2
  

  #// corrections to y and z
    if (layer == 2 or layer == 4 or layer == 8 or
      layer == 10 or layer == 11 or layer == 13):
        if (phiStrip > 45):
            dy = -9
        elif (phiStrip > 40):
            dy = -8
        elif (phiStrip > 35):
            dy = -7
        elif (phiStrip > 29):
            dy = -6
        elif (phiStrip > 24):
            dy = -5
        elif (phiStrip > 18):
            dy = -4
        elif (phiStrip > 13):
            dy = -3
        elif (phiStrip > 8):
            dy = -2
        elif (phiStrip > 2):
            dy = -1
        else:
            dy = 0
    elif (layer == 3 or layer == 6 or
             layer == 7 or layer == 9):
        if (phiStrip > 47):
            dy = -18
        elif (phiStrip > 45):
            dy = -17
        elif (phiStrip > 42):
            dy = -16
        elif (phiStrip > 39):
            dy = -15
        elif (phiStrip > 36):
            dy = -14
        elif (phiStrip > 34):
            dy = -13
        elif (phiStrip > 31):
            dy = -12
        elif (phiStrip > 28):
            dy = -11
        elif (phiStrip > 25):
            dy = -10
        elif (phiStrip > 23):
            dy = -9
        elif (phiStrip > 20):
            dy = -8
        elif (phiStrip > 17):
            dy = -7
        elif (phiStrip > 15):
            dy = -6
        elif (phiStrip > 12):
            dy = -5
        elif (phiStrip > 9):
            dy = -4
        elif (phiStrip > 6):
            dy = -3
        elif (phiStrip > 4):
            dy = -2
        elif (phiStrip > 1):
            dy = -1
        else:
            dy = 0
    else:
        dy = 0

    if (layer == 4):
        dy = -dy;

    if (layer >= 2):
        if (zStrip > 45):
            dz = 8
        elif (zStrip > 38):
            dz = 7
        elif (zStrip > 32):
            dz = 6
        elif (zStrip > 26):
            dz = 5
        elif (zStrip > 20):
            dz = 4
        elif (zStrip > 13):
            dz = 3
        elif (zStrip > 7):
            dz = 2
        elif (zStrip > 1):
            dz = 1
        else:
            dz = 0
    else:
        dz = 0
    try:
        y  = c_LayerY0[layer] + dy + phiStrip * c_PhiWidth[layer]
    except:
        print(layer)
        y = 0
    if (flipped):
        y = -y

    z  = z0 + dz + zStrip * zWidth
    if (section == 1):
        z = z + c_ZOffset
    else:
        z = -z + c_ZOffset

    x      = c_LayerXCoord[layer]
    y      = y / 8 #// y values are defined in 1/32 cm here, round up to 1/8 cm
    return [float(x),float(y),float(z)]


def corelate_sectors_to_mc_muons(klm_digits,mc_particles,df_acceptance):
    KLMDigits_with_accaptance = klm_digits.merge(df_acceptance, on=["Subdetector","section","sector"])
    MC_Muon1 = mc_particles.merge(KLMDigits_with_accaptance,on="event_nr")
    MC_Muon2 =MC_Muon1[\
        (isInRange(MC_Muon1.theta,  MC_Muon1.theta_min,  MC_Muon1.theta_max))& \
        (isInRange(MC_Muon1.phi,    MC_Muon1.phi_min,    MC_Muon1.phi_max)) \
    ]
    MC_Muon2 = MC_Muon2.drop(["theta_min","theta_max","phi_min","phi_max" ],axis=1)
    return MC_Muon2
    
    