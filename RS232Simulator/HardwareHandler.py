import SwapBridgeSimulator
import IRs232HardWareInterface
def GetHardwareReturn(Simulator,data):
    if Simulator == 'SB':
        return SwapBridgeSimulator.SwapBridgeSimulator.GetHardwareReturn(data);
def InitialHardware(Simulator):
    if Simulator == 'SB':
        SwapBridgeSimulator.SwapBridgeSimulator.InitialHardware();
        return True
    else:
        return False
def SimulatorGUI(Simulator):
    if Simulator == 'SB':
        SwapBridgeSimulator.SwapBridgeSimulator.SimulatorGUI();
    