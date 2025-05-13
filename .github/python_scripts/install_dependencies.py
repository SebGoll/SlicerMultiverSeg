import slicer.util

from MultiverSeg.SegmentEditorMultiverSegLib import InstallLogic, DependenciesLogic

if __name__ == '__main__':

    ckpt_installer = InstallLogic()
    dep_installer = DependenciesLogic()

    dep_installer.installPyTorchExtension()

    slicer.util.restart()

    dep_installer.installTorchIfNeeded()
    dep_installer.installMultiverSegIfNeeded()

    ckpt_installer.downloadCheckpointsIfNeeded()
