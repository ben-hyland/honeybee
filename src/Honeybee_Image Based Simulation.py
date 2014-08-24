# By Mostapha Sadeghipour Roudsari
# Sadeghipour@gmail.com
# Honeybee started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

"""
Analysis Recipie for Image-Based Analysis
-
Provided by Honeybee 0.0.53
    
    Args:
        _skyFile: Path to a radiance sky file
        _rhinoViewsName_: viewName to be rendered
        sectionPlane_: Optional view fore clipping plane. The Plane should be perpendicular to the view
        _cameraType_: [0] Perspective, [1] FishEye, [2] Parallel
        _simulationType_: [0] illuminance(lux), [1] radiation (wh), [2] luminance (Candela). Default is 2 > luminance.
        _imageWidth_: Optional input for image width in pixels
        _imageHeight_: Optional input for image height in pixels
        _radParameters_: Radiance parameters
        backupImages_: [0] No backup, [1] Backup in the same folder, [2] Backup in separate folders. Default is 0.
        
    Returns:
        analysisRecipe: Recipe for image-based simulation
"""

ghenv.Component.Name = "Honeybee_Image Based Simulation"
ghenv.Component.NickName = 'imageBasedSimulation'
ghenv.Component.Message = 'VER 0.0.53\nAUG_23_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "03 | Daylight | Recipes"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass


import scriptcontext as sc
import Rhino as rc
import Grasshopper.Kernel as gh

def main():
    # check for Honeybee
    if not sc.sticky.has_key('honeybee_release'):
        msg = "You should first let Honeybee to fly..."
        w = gh.GH_RuntimeMessageLevel.Warning
        ghenv.Component.AddRuntimeMessage(w, msg)
        return
        
    DLAnalysisRecipe = sc.sticky["honeybee_DLAnalysisRecipe"]
    
    # As much as I dislike using global variables I feel lazy to change this now
    recipe = DLAnalysisRecipe(0, _skyFile, _rhinoViewsName_, _radParameters_,
                              _cameraType_, _simulationType_, _imageWidth_,
                              _imageHeight_, sectionPlane_, backupImages_)
    
    return recipe

if _skyFile:
    
    try: int(_simulationType_)
    except: _simulationType_ = 2 #luminance
    
    recipe = main()
    
    if recipe!=None and recipe.skyFile != None:
        analysisRecipe = recipe



