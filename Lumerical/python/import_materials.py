
import sys
sys.path.append(r"C:\Program Files\Lumerical\v252\api\python")

from pathlib import Path
import pandas as pd
import numpy as np
import lumapi

# connect to Lumerical FDTD
fdtd = lumapi.FDTD(hide=False)
mat_name = "LN - Oh"


new_mat = fdtd.addmaterial("Sellmeier")

fdtd.setmaterial(new_mat,"name", mat_name)

fdtd.setmaterial(mat_name, "Anisotropy", 1)

fdtd.eval(f'''
setmaterial("{mat_name}", "A0", [1.0, 1.0, 1.0]);
setmaterial("{mat_name}", "B1", [2.6734, 2.6734, 2.9804]);
setmaterial("{mat_name}", "C1", [0.01764, 0.01764, 0.02047]);
setmaterial("{mat_name}", "B2", [1.229, 1.229, 0.5981]);
setmaterial("{mat_name}", "C2", [0.05914, 0.05914, 0.0666]);
setmaterial("{mat_name}", "B3", [12.614, 12.614, 8.9543]);
setmaterial("{mat_name}", "C3", [474.6, 474.6, 416.08]);
''')
