#
# PySNMP MIB module CXLapBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXLapBD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Alias, SapIndex, cxLapBD = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "SapIndex", "cxLapBD")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Counter64, ModuleIdentity, IpAddress, MibIdentifier, Integer32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Counter64", "ModuleIdentity", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Sapi(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 16, 63))
    namedValues = NamedValues(("q930-q931", 0), ("x25", 16), ("mngmt", 63))

class Tei(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 127)

lapbdLowerPoolThreshold = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdLowerPoolThreshold.setStatus('mandatory')
lapbdUpperPoolThreshold = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdUpperPoolThreshold.setStatus('mandatory')
lapbdTraceSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdTraceSize.setStatus('mandatory')
lapbdTraceFlags = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdTraceFlags.setStatus('mandatory')
lapbdTraps = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdTraps.setStatus('mandatory')
lapbdStatusEvent = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noEvent", 1), ("enteringCongestion", 2), ("exitingCongestion", 3), ("linkUp", 4), ("linkDown", 5), ("protocolError", 6), ("invTeiRemovalAttempt", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdStatusEvent.setStatus('mandatory')
lapbdSoftwareVersions = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdSoftwareVersions.setStatus('mandatory')
lapbdMacSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20), )
if mibBuilder.loadTexts: lapbdMacSapTable.setStatus('mandatory')
lapbdMacSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1), ).setIndexNames((0, "CXLapBD-MIB", "lapbdMacSapNumber"))
if mibBuilder.loadTexts: lapbdMacSapEntry.setStatus('mandatory')
lapbdMacSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapNumber.setStatus('mandatory')
lapbdMacSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapRowStatus.setStatus('mandatory')
lapbdMacSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapAlias.setStatus('mandatory')
lapbdMacSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapCompanionAlias.setStatus('mandatory')
lapbdMacSapLapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lapb", 1), ("lapd", 2))).clone('lapb')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapLapType.setStatus('mandatory')
lapbdMacSapLogicalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2))).clone('dte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapLogicalInterfaceType.setStatus('mandatory')
lapbdMacSapArbitrationLogic = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passive", 1), ("active", 2))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapArbitrationLogic.setStatus('mandatory')
lapbdMacSapLapDProtocolFlavor = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ccitt", 1), ("vn3", 2), ("etsi", 3))).clone('ccitt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapLapDProtocolFlavor.setStatus('mandatory')
lapbdMacSapLapBProtocolFlavor = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("v8022", 2))).clone('standard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapLapBProtocolFlavor.setStatus('mandatory')
lapbdMacSapWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapWindow.setStatus('mandatory')
lapbdMacSapTxQUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapTxQUpperThreshold.setStatus('mandatory')
lapbdMacSapTxQLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapTxQLowerThreshold.setStatus('mandatory')
lapbdMacSapConnectionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapConnectionTimer.setStatus('mandatory')
lapbdMacSapT202Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapT202Timer.setStatus('mandatory')
lapbdMacSapN202Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapN202Counter.setStatus('mandatory')
lapbdMacSapTeiCheckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2047))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapTeiCheckTimer.setStatus('mandatory')
lapbdMacSapT201Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapT201Timer.setStatus('mandatory')
lapbdMacSapLowTei = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapLowTei.setStatus('mandatory')
lapbdMacSapKeepL1Up = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdMacSapKeepL1Up.setStatus('mandatory')
lapbdMacSapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("clearStats", 1), ("enableTrace", 2), ("disableTrace", 3), ("enableMacSap", 4), ("disableMacSap", 5)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: lapbdMacSapControl.setStatus('mandatory')
lapbdMacSapHighLevelState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unbound", 1), ("configured", 2), ("bound", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapHighLevelState.setStatus('mandatory')
lapbdMacSapFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("flowNormal", 1), ("flowStopped", 2), ("noFlow", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapFlowControlState.setStatus('mandatory')
lapbdMacSapOutstandingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapOutstandingFrames.setStatus('mandatory')
lapbdMacSapTotalFramesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTotalFramesDropped.setStatus('mandatory')
lapbdMacSapActiveSaps = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapActiveSaps.setStatus('mandatory')
lapbdMacSapTxIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxIFrames.setStatus('mandatory')
lapbdMacSapRxIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxIFrames.setStatus('mandatory')
lapbdMacSapTxRrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxRrFrames.setStatus('mandatory')
lapbdMacSapRxRrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxRrFrames.setStatus('mandatory')
lapbdMacSapTxRnrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxRnrFrames.setStatus('mandatory')
lapbdMacSapRxRnrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxRnrFrames.setStatus('mandatory')
lapbdMacSapTxRejFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxRejFrames.setStatus('mandatory')
lapbdMacSapRxRejFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxRejFrames.setStatus('mandatory')
lapbdMacSapTxSabmFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxSabmFrames.setStatus('mandatory')
lapbdMacSapRxSabmFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxSabmFrames.setStatus('mandatory')
lapbdMacSapTxDiscFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxDiscFrames.setStatus('mandatory')
lapbdMacSapRxDiscFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxDiscFrames.setStatus('mandatory')
lapbdMacSapTxUaFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxUaFrames.setStatus('mandatory')
lapbdMacSapRxUaFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxUaFrames.setStatus('mandatory')
lapbdMacSapTxDmFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxDmFrames.setStatus('mandatory')
lapbdMacSapRxDmFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxDmFrames.setStatus('mandatory')
lapbdMacSapTxFrmrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxFrmrFrames.setStatus('mandatory')
lapbdMacSapRxFrmrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxFrmrFrames.setStatus('mandatory')
lapbdMacSapTxUiFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxUiFrames.setStatus('mandatory')
lapbdMacSapRxUiFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxUiFrames.setStatus('mandatory')
lapbdMacSapTxXidFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapTxXidFrames.setStatus('mandatory')
lapbdMacSapRxXidFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxXidFrames.setStatus('mandatory')
lapbdMacSapRxInvalidFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxInvalidFrames.setStatus('mandatory')
lapbdMacSapRxInvalidDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapRxInvalidDiscards.setStatus('mandatory')
lapbdMacSapSabmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 74), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapSabmErrors.setStatus('mandatory')
lapbdMacSapFrmrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 75), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdMacSapFrmrErrors.setStatus('mandatory')
lapbdDlSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21), )
if mibBuilder.loadTexts: lapbdDlSapTable.setStatus('mandatory')
lapbdDlSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1), ).setIndexNames((0, "CXLapBD-MIB", "lapbdDlSapMacSapNumber"), (0, "CXLapBD-MIB", "lapbdDlSapNumber"))
if mibBuilder.loadTexts: lapbdDlSapEntry.setStatus('mandatory')
lapbdDlSapMacSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlSapMacSapNumber.setStatus('mandatory')
lapbdDlSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 2), Sapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlSapNumber.setStatus('mandatory')
lapbdDlSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapAlias.setStatus('mandatory')
lapbdDlSapMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1380)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapMaxFrameSize.setStatus('mandatory')
lapbdDlSapWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapWindowSize.setStatus('mandatory')
lapbdDlSapMaxRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapMaxRetransmissions.setStatus('mandatory')
lapbdDlSapCongestionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2047)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapCongestionTimer.setStatus('mandatory')
lapbdDlSapT1T200Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapT1T200Timer.setStatus('mandatory')
lapbdDlSapT2Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapT2Timer.setStatus('mandatory')
lapbdDlSapT3T203Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapT3T203Timer.setStatus('mandatory')
lapbdDlSapModulo = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2))).clone('modulo8')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapModulo.setStatus('mandatory')
lapbdDlSapMaxDlcs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapMaxDlcs.setStatus('mandatory')
lapbdDlSapTeiAssignmentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonAutomatic", 1), ("automatic", 2))).clone('automatic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdDlSapTeiAssignmentMode.setStatus('mandatory')
lapbdDlSapHighLevelState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unbound", 1), ("configured", 2), ("bound", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlSapHighLevelState.setStatus('mandatory')
lapbdDlSapActiveDlcs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlSapActiveDlcs.setStatus('mandatory')
lapbdTeiTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22), )
if mibBuilder.loadTexts: lapbdTeiTable.setStatus('mandatory')
lapbdTeiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1), ).setIndexNames((0, "CXLapBD-MIB", "lapbdTeiMacSapNumber"), (0, "CXLapBD-MIB", "lapbdTeiSapi"), (0, "CXLapBD-MIB", "lapbdTeiNumber"))
if mibBuilder.loadTexts: lapbdTeiEntry.setStatus('mandatory')
lapbdTeiMacSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdTeiMacSapNumber.setStatus('mandatory')
lapbdTeiSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 2), Sapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdTeiSapi.setStatus('mandatory')
lapbdTeiNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 3), Tei()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdTeiNumber.setStatus('mandatory')
lapbdTeiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbdTeiRowStatus.setStatus('mandatory')
lapbdDlcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23), )
if mibBuilder.loadTexts: lapbdDlcStatusTable.setStatus('mandatory')
lapbdDlcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1), ).setIndexNames((0, "CXLapBD-MIB", "lapbdDlcMacSapNumber"), (0, "CXLapBD-MIB", "lapbdDlcSapi"), (0, "CXLapBD-MIB", "lapbdDlcTei"))
if mibBuilder.loadTexts: lapbdDlcStatusEntry.setStatus('mandatory')
lapbdDlcMacSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcMacSapNumber.setStatus('mandatory')
lapbdDlcSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 2), Sapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcSapi.setStatus('mandatory')
lapbdDlcTei = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 3), Tei()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcTei.setStatus('mandatory')
lapbdDlcLinkLevelState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("disconnectedDisabled", 1), ("connectingLinkLevel", 2), ("dataTransfer", 3), ("disconnectingLinkLevel", 4), ("connectingAwaitingTei", 5), ("resettingLinkLevelEnabled", 6), ("resettingLinkLevelDisabled", 7), ("frameRejection", 8), ("disconnectedEnabled", 9), ("assignAwaitingTei", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcLinkLevelState.setStatus('mandatory')
lapbdDlcNextTxNs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcNextTxNs.setStatus('mandatory')
lapbdDlcNextRxNs = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcNextRxNs.setStatus('mandatory')
lapbdDlcRetransmissionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcRetransmissionCount.setStatus('mandatory')
lapbdDlcLocalFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localFlowNormal", 1), ("localFlowStopped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcLocalFlowControlState.setStatus('mandatory')
lapbdDlcRemoteFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remoteFlowNormal", 1), ("remoteFlowStopped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcRemoteFlowControlState.setStatus('mandatory')
lapbdDlcMacTxFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flowNormal", 1), ("flowStopped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcMacTxFlowControlState.setStatus('mandatory')
lapbdDlcTxQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbdDlcTxQSize.setStatus('mandatory')
lapbdStatusIndication = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27) + (0,1)).setObjects(("CXLapBD-MIB", "lapbdTeiMacSapNumber"), ("CXLapBD-MIB", "lapbdTeiSapi"), ("CXLapBD-MIB", "lapbdTeiNumber"), ("CXLapBD-MIB", "lapbdStatusEvent"))
mibBuilder.exportSymbols("CXLapBD-MIB", lapbdMacSapActiveSaps=lapbdMacSapActiveSaps, lapbdMacSapRxXidFrames=lapbdMacSapRxXidFrames, Tei=Tei, lapbdUpperPoolThreshold=lapbdUpperPoolThreshold, lapbdMacSapOutstandingFrames=lapbdMacSapOutstandingFrames, lapbdMacSapRxSabmFrames=lapbdMacSapRxSabmFrames, lapbdMacSapN202Counter=lapbdMacSapN202Counter, lapbdDlSapNumber=lapbdDlSapNumber, lapbdMacSapSabmErrors=lapbdMacSapSabmErrors, lapbdDlSapHighLevelState=lapbdDlSapHighLevelState, lapbdMacSapTxSabmFrames=lapbdMacSapTxSabmFrames, lapbdDlSapMaxDlcs=lapbdDlSapMaxDlcs, lapbdDlcStatusTable=lapbdDlcStatusTable, lapbdMacSapAlias=lapbdMacSapAlias, lapbdMacSapWindow=lapbdMacSapWindow, lapbdDlcNextRxNs=lapbdDlcNextRxNs, lapbdDlcRetransmissionCount=lapbdDlcRetransmissionCount, lapbdStatusEvent=lapbdStatusEvent, lapbdDlcMacSapNumber=lapbdDlcMacSapNumber, lapbdTeiRowStatus=lapbdTeiRowStatus, lapbdDlcTxQSize=lapbdDlcTxQSize, lapbdDlSapEntry=lapbdDlSapEntry, lapbdMacSapTxXidFrames=lapbdMacSapTxXidFrames, lapbdStatusIndication=lapbdStatusIndication, lapbdMacSapFlowControlState=lapbdMacSapFlowControlState, lapbdDlSapWindowSize=lapbdDlSapWindowSize, lapbdMacSapHighLevelState=lapbdMacSapHighLevelState, lapbdMacSapTeiCheckTimer=lapbdMacSapTeiCheckTimer, lapbdDlcLinkLevelState=lapbdDlcLinkLevelState, lapbdDlSapMacSapNumber=lapbdDlSapMacSapNumber, lapbdMacSapEntry=lapbdMacSapEntry, lapbdTeiMacSapNumber=lapbdTeiMacSapNumber, lapbdMacSapTxRrFrames=lapbdMacSapTxRrFrames, lapbdDlcStatusEntry=lapbdDlcStatusEntry, lapbdMacSapConnectionTimer=lapbdMacSapConnectionTimer, lapbdDlSapMaxFrameSize=lapbdDlSapMaxFrameSize, lapbdDlSapModulo=lapbdDlSapModulo, lapbdMacSapLowTei=lapbdMacSapLowTei, lapbdTraceFlags=lapbdTraceFlags, lapbdMacSapT201Timer=lapbdMacSapT201Timer, lapbdMacSapLapType=lapbdMacSapLapType, lapbdDlcNextTxNs=lapbdDlcNextTxNs, lapbdMacSapTxQLowerThreshold=lapbdMacSapTxQLowerThreshold, lapbdMacSapControl=lapbdMacSapControl, lapbdMacSapRowStatus=lapbdMacSapRowStatus, lapbdDlcTei=lapbdDlcTei, Sapi=Sapi, lapbdMacSapRxRejFrames=lapbdMacSapRxRejFrames, lapbdMacSapRxUiFrames=lapbdMacSapRxUiFrames, lapbdMacSapFrmrErrors=lapbdMacSapFrmrErrors, lapbdDlSapMaxRetransmissions=lapbdDlSapMaxRetransmissions, lapbdMacSapRxRrFrames=lapbdMacSapRxRrFrames, lapbdDlSapT1T200Timer=lapbdDlSapT1T200Timer, lapbdMacSapTxDiscFrames=lapbdMacSapTxDiscFrames, lapbdMacSapTxRnrFrames=lapbdMacSapTxRnrFrames, lapbdTeiNumber=lapbdTeiNumber, lapbdMacSapLapDProtocolFlavor=lapbdMacSapLapDProtocolFlavor, lapbdMacSapTable=lapbdMacSapTable, lapbdMacSapRxDiscFrames=lapbdMacSapRxDiscFrames, lapbdTeiTable=lapbdTeiTable, lapbdMacSapRxUaFrames=lapbdMacSapRxUaFrames, lapbdDlSapCongestionTimer=lapbdDlSapCongestionTimer, lapbdMacSapT202Timer=lapbdMacSapT202Timer, lapbdTraceSize=lapbdTraceSize, lapbdMacSapRxInvalidDiscards=lapbdMacSapRxInvalidDiscards, lapbdDlSapT2Timer=lapbdDlSapT2Timer, lapbdMacSapTxFrmrFrames=lapbdMacSapTxFrmrFrames, lapbdDlSapT3T203Timer=lapbdDlSapT3T203Timer, lapbdMacSapRxInvalidFrames=lapbdMacSapRxInvalidFrames, lapbdSoftwareVersions=lapbdSoftwareVersions, lapbdTraps=lapbdTraps, lapbdDlcRemoteFlowControlState=lapbdDlcRemoteFlowControlState, lapbdMacSapRxRnrFrames=lapbdMacSapRxRnrFrames, lapbdDlcLocalFlowControlState=lapbdDlcLocalFlowControlState, lapbdMacSapTxDmFrames=lapbdMacSapTxDmFrames, lapbdDlSapTeiAssignmentMode=lapbdDlSapTeiAssignmentMode, lapbdDlcSapi=lapbdDlcSapi, lapbdMacSapLapBProtocolFlavor=lapbdMacSapLapBProtocolFlavor, lapbdMacSapTxUiFrames=lapbdMacSapTxUiFrames, lapbdLowerPoolThreshold=lapbdLowerPoolThreshold, lapbdTeiSapi=lapbdTeiSapi, lapbdMacSapRxIFrames=lapbdMacSapRxIFrames, lapbdMacSapLogicalInterfaceType=lapbdMacSapLogicalInterfaceType, lapbdDlSapAlias=lapbdDlSapAlias, lapbdMacSapArbitrationLogic=lapbdMacSapArbitrationLogic, lapbdDlcMacTxFlowControlState=lapbdDlcMacTxFlowControlState, lapbdMacSapNumber=lapbdMacSapNumber, lapbdMacSapTxQUpperThreshold=lapbdMacSapTxQUpperThreshold, lapbdMacSapTxIFrames=lapbdMacSapTxIFrames, lapbdMacSapRxDmFrames=lapbdMacSapRxDmFrames, lapbdMacSapTotalFramesDropped=lapbdMacSapTotalFramesDropped, lapbdDlSapActiveDlcs=lapbdDlSapActiveDlcs, lapbdMacSapRxFrmrFrames=lapbdMacSapRxFrmrFrames, lapbdMacSapKeepL1Up=lapbdMacSapKeepL1Up, lapbdMacSapTxUaFrames=lapbdMacSapTxUaFrames, lapbdMacSapCompanionAlias=lapbdMacSapCompanionAlias, lapbdMacSapTxRejFrames=lapbdMacSapTxRejFrames, lapbdTeiEntry=lapbdTeiEntry, lapbdDlSapTable=lapbdDlSapTable)