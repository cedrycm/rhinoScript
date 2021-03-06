import System
import Rhino
import scriptcontext as sc

# Demonstrates how to capture a view to a bitmap
# Loops through every view to capture


def SampleViewCaptureToFile():
    # view = sc.doc.Views.ActiveView;
    allviews = sc.doc.Views.GetViewList(True, True)
    for view in allviews:
        sc.doc.View.ActiveView = view
        if view:
            view_capture = Rhino.Display.ViewCapture()
            view_capture.Width = view.ActiveViewport.Size.Width
            view_capture.Height = view.ActiveViewport.Size.Height
            view_capture.ScaleScreenItems = False
            view_capture.DrawAxes = False
            view_capture.DrawGrid = False
            view_capture.DrawGridAxes = False
            view_capture.TransparentBackground = False
            bitmap = view_capture.CaptureToBitmap(view)
            if bitmap:
                folder = System.Environment.SpecialFolder.Desktop
                path = System.Environment.GetFolderPath(folder)
                captureName = view.ActiveViewport.Name + "_ViewCapture.png"
                filename = System.IO.Path.Combine(path, captureName)
                bitmap.Save(filename, System.Drawing.Imaging.ImageFormat.Png)


# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    SampleViewCaptureToFile()
