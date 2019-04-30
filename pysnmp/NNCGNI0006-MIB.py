#
# PySNMP MIB module NNCGNI0006-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI0006-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nncLegacyModules, nncExtCodeSpace, nncExtSystem, nncExtEnvironmental, nncExtNVM, nncExtRestart, nncExtProbe, nncExtDiag = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncLegacyModules", "nncExtCodeSpace", "nncExtSystem", "nncExtEnvironmental", "nncExtNVM", "nncExtRestart", "nncExtProbe", "nncExtDiag")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Bits, Counter64, TimeTicks, iso, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Bits", "Counter64", "TimeTicks", "iso", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
nncExtBasics = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 4, 1))
if mibBuilder.loadTexts: nncExtBasics.setLastUpdated('9904301330Z')
if mibBuilder.loadTexts: nncExtBasics.setOrganization('Newbridge Networks Corporation')
class RestartCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72))
    namedValues = NamedValues(("trblnoProblem", 0), ("trblUnknown", 1), ("trblBusError", 2), ("trblAddressError", 3), ("trblIllegalInst", 4), ("trblZeroDivide", 5), ("trblChkFailure", 6), ("trblTrapVInst", 7), ("trblPrivilege", 8), ("trblTraceTrap", 9), ("trblLine1010", 10), ("trblLine1111", 11), ("trblUninitialized", 15), ("trblSpurious", 24), ("trblIntLevel1", 25), ("trblIntLevel2", 26), ("trblIntLevel3", 27), ("trblIntLevel4", 28), ("trblIntLevel5", 29), ("trblIntLevel6", 30), ("trblIntLevel7", 31), ("trblTrap00", 32), ("trblTrap01", 33), ("trblTrap02", 34), ("trblTrap03", 35), ("trblTrap04", 36), ("trblTrap05", 37), ("trblTrap06", 38), ("trblTrap07", 39), ("trblTrap08", 40), ("trblTrap09", 41), ("trblTrap10", 42), ("trblTrap11", 43), ("trblTrap12", 44), ("trblTrap13", 45), ("trblTrap14", 46), ("trblTrap15", 47), ("trblWatchDog", 48), ("trblNCIReset", 49), ("trblNCIRunMinusOne", 50), ("trblPanic", 51), ("trblRunBootProm", 52), ("trblCopyRamToFlash", 53), ("trblDnldAborted", 54), ("trblBadFlashConfig", 55), ("trblNVMReset", 56), ("trblDspReset", 57), ("trblDspDnldFailed", 58), ("trblDspPollFailed", 59), ("trblDspDiedOnTx", 60), ("trblDspDead", 61), ("trblDCMPDeath", 62), ("trblRunningLowComms", 63), ("trblRunningLowFrame", 64), ("trblRunningLowSys", 65), ("trblRunningLowSonic", 66), ("trblRunningLowMgmt", 67), ("trblRunningLowPoolUnknown", 68), ("trblNCIReload", 69), ("trblPushButton", 70), ("trblCPUReset", 71), ("trblRDSReset", 72))

class Nci2DeviceIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 93, 97, 101, 102, 112))
    namedValues = NamedValues(("unknown", 0), ("nc3600", 1), ("dcp3600", 2), ("dtu2601", 4), ("dtu2602", 5), ("dtu2603", 6), ("dclcRs232", 7), ("dclcX21", 8), ("dclcV35", 9), ("ldm1124", 10), ("ldm1121", 11), ("ldm1135", 12), ("nmu4601", 13), ("nmu4602", 14), ("nc3624", 15), ("nc3612", 16), ("nc3630", 17), ("dtu2601Anm", 18), ("dtu2602Anm", 19), ("dtu2603Anm", 20), ("dtu2608", 21), ("dsp3600", 22), ("dpm3600", 23), ("detT1", 24), ("detE1", 25), ("nmu4601A", 26), ("nmu4605", 27), ("nmu5602", 28), ("nmu5610", 29), ("nc3645SE", 30), ("nc3645PE", 31), ("dtu2610Pad", 32), ("dtu2606", 33), ("nmu5610ci", 34), ("ncDS3", 35), ("ta1601S", 36), ("ta1601U", 37), ("ta1602S", 38), ("ta1602U", 39), ("ta1603S", 40), ("ta1603U", 41), ("elb8230", 42), ("nvpSysMgr", 43), ("nvpVoiceSrvr", 44), ("nvpEdsp", 45), ("nc1615C", 46), ("nc3606Voice", 47), ("nc3606Data", 48), ("nvp1000", 49), ("dtu2701", 50), ("dtu2702", 51), ("dtu2703", 52), ("bert2601", 53), ("bert2602", 54), ("bert2603", 55), ("dtu2701Anm", 56), ("dtu2702Anm", 57), ("dtu2703Anm", 58), ("tap", 59), ("nmu8001", 60), ("bertMgr", 61), ("dclcRs422", 62), ("eapApi", 63), ("ncdE3", 64), ("er8231", 65), ("tr8251", 66), ("pte", 67), ("nc3664", 68), ("nc36150", 69), ("esn3700", 70), ("esnEsc", 71), ("esnOne", 72), ("dtu2704", 73), ("nmu4602Dn", 74), ("nmu4602Cn", 75), ("nmu4602Rn", 76), ("nc3620", 77), ("ncWgs", 78), ("nc36170", 79), ("bri3600St", 80), ("ncFRATM", 81), ("ncRouteServer", 82), ("ncSystemManager", 83), ("ncATMNIC", 84), ("ncYellowRidge", 85), ("ncELSU", 93), ("ncBlueRidge", 97), ("ncOrangeRidge", 101), ("ncRedRidge", 102), ("ncCampusSwitch", 112))

class CurrentGenericType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class ProductPartNumberType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class CardIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 5, 6, 7, 51, 57, 58, 59, 60, 61, 62))
    namedValues = NamedValues(("unknown", 0), ("yellowRidgeMainCard", 4), ("yellowRidgeLEDBoard", 5), ("yellowRidgeOc3MmfPdmModule", 6), ("yellowRidgeBufferModule", 7), ("yellowRidgeOc3SmfPdmModule", 51), ("cpElsuMainCard", 57), ("coElsuAtmCard", 58), ("coElsuMainCard", 59), ("elsuDisplayModule", 60), ("elsuAuiBackplane", 61), ("coElsu10BaseTBackplane", 62))

class CardSerialNumberType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-2d,1d,8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class NncSwStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 1), ("ok", 2), ("error", 3), ("empty", 4))

class NncSwBank(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 257))
    namedValues = NamedValues(("notapplicable", 0), ("bootbank", 1), ("bank1", 2), ("bank2", 3), ("bank3", 4), ("bank4", 5), ("bank5", 6), ("bank6", 7), ("bank7", 8), ("bank8", 9), ("bank9", 10), ("bank10", 11), ("bank11", 12), ("bank12", 13), ("bank13", 14), ("bank14", 15), ("bank15", 16), ("bank16", 17), ("bank17", 18), ("bank18", 19), ("bank19", 20), ("bank20", 21), ("bank21", 22), ("bank22", 23), ("bank23", 24), ("bank24", 25), ("bank25", 26), ("bank26", 27), ("bank27", 28), ("bank28", 29), ("bank29", 30), ("bank30", 31), ("bank31", 32), ("bank32", 33), ("unknown", 257))

nncExtSysProductName = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysProductName.setStatus('current')
nncExtSysCurrentGeneric = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 2), CurrentGenericType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCurrentGeneric.setStatus('current')
nncExtSysProductPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 3), ProductPartNumberType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysProductPartNumber.setStatus('current')
nncExtSysNci2DeviceID = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 4), Nci2DeviceIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysNci2DeviceID.setStatus('current')
nncExtSysCurrentDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 5), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtSysCurrentDateAndTime.setStatus('current')
nncExtSysCardTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 1, 6), )
if mibBuilder.loadTexts: nncExtSysCardTable.setStatus('current')
nncExtSysCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtSysCardIndex"))
if mibBuilder.loadTexts: nncExtSysCardEntry.setStatus('current')
nncExtSysCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardIndex.setStatus('current')
nncExtSysCardIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 2), CardIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardIDType.setStatus('current')
nncExtSysCardName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardName.setStatus('current')
nncExtSysCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 4), CardSerialNumberType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardSerialNumber.setStatus('current')
nncExtEnvFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fanOk", 1), ("fanFailed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanStatus.setStatus('current')
nncExtEnvTemperatureSensor = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("tooHot", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvTemperatureSensor.setStatus('current')
nncExtEnvPlus12Status = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("outOfSpec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPlus12Status.setStatus('current')
nncExtEnvMinus12Status = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("outOfSpec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvMinus12Status.setStatus('current')
class FanStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("bad", 1))

nncExtEnvFanTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 2, 5), )
if mibBuilder.loadTexts: nncExtEnvFanTable.setStatus('current')
nncExtEnvFanTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtEnvFanIndex"))
if mibBuilder.loadTexts: nncExtEnvFanTableEntry.setStatus('current')
nncExtEnvFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanIndex.setStatus('current')
nncExtEnvFanStatusByFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 2), FanStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanStatusByFanIndex.setStatus('current')
class PwrSupplyStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("noAc", 1), ("noDc", 2), ("notPresent", 3))

nncExtEnvPwrSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 2, 6), )
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTable.setStatus('current')
nncExtEnvPwrSupplyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtEnvPwrSupplySlotIndex"))
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTableEntry.setStatus('current')
nncExtEnvPwrSupplySlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPwrSupplySlotIndex.setStatus('current')
nncExtEnvPwrSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 2), PwrSupplyStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPwrSupplyStatus.setStatus('current')
nncExtRestarts = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestarts.setStatus('current')
nncExtFaultInducedRestarts = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtFaultInducedRestarts.setStatus('current')
nncExtLastFault = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 3), RestartCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtLastFault.setStatus('current')
nncExtFaultRepetitions = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtFaultRepetitions.setStatus('current')
nncExtRestartTracebackTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 3, 5), )
if mibBuilder.loadTexts: nncExtRestartTracebackTable.setStatus('current')
nncExtRestartTracebackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtRestartTracebackIndex"))
if mibBuilder.loadTexts: nncExtRestartTracebackEntry.setStatus('current')
nncExtRestartTracebackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartTracebackIndex.setStatus('current')
nncExtRestartTracebackPCValue = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartTracebackPCValue.setStatus('current')
nncExtRestartRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 3, 6), )
if mibBuilder.loadTexts: nncExtRestartRegisterTable.setStatus('current')
nncExtRestartRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtRestartRegisterIndex"))
if mibBuilder.loadTexts: nncExtRestartRegisterEntry.setStatus('current')
nncExtRestartRegisterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartRegisterIndex.setStatus('current')
nncExtRestartRegisterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartRegisterValue.setStatus('current')
nncExtRestartForceToBoot = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtRestartForceToBoot.setStatus('current')
nncExtRestartCause = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 8), RestartCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartCause.setStatus('current')
nncExtRestartSystem = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36000))).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtRestartSystem.setStatus('current')
class CodeSpaceIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

nncExtCodeSpaceCurrentlyActive = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 1), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCurrentlyActive.setStatus('current')
nncExtCodeSpaceNextActive = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 2), CodeSpaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtCodeSpaceNextActive.setStatus('current')
nncExtCodeSpaceNumber = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 3), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceNumber.setStatus('current')
nncExtCodeSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 4, 4), )
if mibBuilder.loadTexts: nncExtCodeSpaceTable.setStatus('current')
nncExtCodeSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtCodeSpaceIndex"))
if mibBuilder.loadTexts: nncExtCodeSpaceEntry.setStatus('current')
nncExtCodeSpaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 1), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceIndex.setStatus('current')
nncExtCodeSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceSize.setStatus('current')
nncExtCodeSpaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceStatus.setStatus('current')
nncExtCodeSpaceGeneric = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 4), CurrentGenericType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceGeneric.setStatus('current')
nncExtCodeSpaceDownloadDate = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadDate.setStatus('current')
nncExtCodeSpaceDownloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadTime.setStatus('current')
nncExtCodeSpaceDownloadServer = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadServer.setStatus('current')
nncExtCodeSpaceDownloadRequestor = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadRequestor.setStatus('current')
nncExtCodeSpaceCompressionType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("c1", 2), ("c2", 3), ("c3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCompressionType.setStatus('current')
nncExtCodeSpaceLoadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceLoadSize.setStatus('current')
nncExtCodeSpaceCompressLoadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCompressLoadSize.setStatus('current')
class NVMPoolIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

nncExtNVMUsageTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 5, 1), )
if mibBuilder.loadTexts: nncExtNVMUsageTable.setStatus('current')
nncExtNVMUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtNVMPoolIndex"))
if mibBuilder.loadTexts: nncExtNVMUsageEntry.setStatus('current')
nncExtNVMPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 1), NVMPoolIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolIndex.setStatus('current')
nncExtNVMPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolSize.setStatus('current')
nncExtNVMPoolBytesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolBytesUsed.setStatus('current')
nncExtNVMLastRepair = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(31, 31)).setFixedLength(31)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMLastRepair.setStatus('current')
nncExtProbeMPLTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 12, 1), )
if mibBuilder.loadTexts: nncExtProbeMPLTable.setStatus('current')
nncExtProbeMPLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtProbeMPL"))
if mibBuilder.loadTexts: nncExtProbeMPLEntry.setStatus('current')
nncExtProbeMPL = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtProbeMPL.setStatus('current')
class SvcEpdOptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class SvcPpdOptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

nncDiagUndoAll = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("undo", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncDiagUndoAll.setStatus('current')
nncExtStartupDiagnosticResults = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("unspecifiedFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtStartupDiagnosticResults.setStatus('current')
mibBuilder.exportSymbols("NNCGNI0006-MIB", nncExtFaultRepetitions=nncExtFaultRepetitions, nncExtEnvPwrSupplyStatus=nncExtEnvPwrSupplyStatus, nncExtRestartRegisterEntry=nncExtRestartRegisterEntry, nncExtProbeMPLTable=nncExtProbeMPLTable, nncExtCodeSpaceDownloadRequestor=nncExtCodeSpaceDownloadRequestor, nncExtEnvPwrSupplyTable=nncExtEnvPwrSupplyTable, nncExtSysProductPartNumber=nncExtSysProductPartNumber, nncExtEnvTemperatureSensor=nncExtEnvTemperatureSensor, nncExtRestartRegisterTable=nncExtRestartRegisterTable, nncExtCodeSpaceCurrentlyActive=nncExtCodeSpaceCurrentlyActive, FanStatusType=FanStatusType, SvcEpdOptionType=SvcEpdOptionType, nncExtRestartTracebackEntry=nncExtRestartTracebackEntry, nncExtSysCardIndex=nncExtSysCardIndex, nncExtCodeSpaceNextActive=nncExtCodeSpaceNextActive, nncExtRestartForceToBoot=nncExtRestartForceToBoot, nncExtSysCardTable=nncExtSysCardTable, nncExtRestartCause=nncExtRestartCause, CurrentGenericType=CurrentGenericType, NncSwStatus=NncSwStatus, nncExtCodeSpaceNumber=nncExtCodeSpaceNumber, nncExtSysNci2DeviceID=nncExtSysNci2DeviceID, SvcPpdOptionType=SvcPpdOptionType, nncExtEnvFanStatus=nncExtEnvFanStatus, nncExtSysCardSerialNumber=nncExtSysCardSerialNumber, nncExtCodeSpaceTable=nncExtCodeSpaceTable, nncExtStartupDiagnosticResults=nncExtStartupDiagnosticResults, nncExtRestarts=nncExtRestarts, ProductPartNumberType=ProductPartNumberType, nncExtEnvFanTableEntry=nncExtEnvFanTableEntry, CardSerialNumberType=CardSerialNumberType, nncExtRestartTracebackTable=nncExtRestartTracebackTable, nncExtCodeSpaceGeneric=nncExtCodeSpaceGeneric, nncExtCodeSpaceSize=nncExtCodeSpaceSize, nncExtCodeSpaceStatus=nncExtCodeSpaceStatus, nncExtEnvFanTable=nncExtEnvFanTable, nncExtSysProductName=nncExtSysProductName, PYSNMP_MODULE_ID=nncExtBasics, nncExtProbeMPL=nncExtProbeMPL, nncExtSysCurrentGeneric=nncExtSysCurrentGeneric, nncExtSysCardIDType=nncExtSysCardIDType, nncExtProbeMPLEntry=nncExtProbeMPLEntry, nncExtCodeSpaceDownloadDate=nncExtCodeSpaceDownloadDate, CardIDType=CardIDType, nncExtCodeSpaceEntry=nncExtCodeSpaceEntry, nncDiagUndoAll=nncDiagUndoAll, nncExtFaultInducedRestarts=nncExtFaultInducedRestarts, nncExtEnvPlus12Status=nncExtEnvPlus12Status, nncExtSysCardEntry=nncExtSysCardEntry, NncSwBank=NncSwBank, nncExtBasics=nncExtBasics, nncExtNVMPoolIndex=nncExtNVMPoolIndex, nncExtCodeSpaceDownloadTime=nncExtCodeSpaceDownloadTime, nncExtRestartTracebackIndex=nncExtRestartTracebackIndex, nncExtEnvFanIndex=nncExtEnvFanIndex, Nci2DeviceIDType=Nci2DeviceIDType, nncExtSysCardName=nncExtSysCardName, nncExtCodeSpaceDownloadServer=nncExtCodeSpaceDownloadServer, nncExtNVMPoolBytesUsed=nncExtNVMPoolBytesUsed, nncExtRestartRegisterIndex=nncExtRestartRegisterIndex, CodeSpaceIndex=CodeSpaceIndex, nncExtLastFault=nncExtLastFault, nncExtRestartRegisterValue=nncExtRestartRegisterValue, RestartCause=RestartCause, nncExtCodeSpaceCompressionType=nncExtCodeSpaceCompressionType, nncExtNVMLastRepair=nncExtNVMLastRepair, nncExtNVMUsageTable=nncExtNVMUsageTable, NVMPoolIndex=NVMPoolIndex, nncExtEnvPwrSupplySlotIndex=nncExtEnvPwrSupplySlotIndex, nncExtCodeSpaceCompressLoadSize=nncExtCodeSpaceCompressLoadSize, nncExtNVMUsageEntry=nncExtNVMUsageEntry, nncExtRestartTracebackPCValue=nncExtRestartTracebackPCValue, nncExtSysCurrentDateAndTime=nncExtSysCurrentDateAndTime, nncExtCodeSpaceLoadSize=nncExtCodeSpaceLoadSize, nncExtRestartSystem=nncExtRestartSystem, nncExtNVMPoolSize=nncExtNVMPoolSize, PwrSupplyStatusType=PwrSupplyStatusType, nncExtEnvPwrSupplyTableEntry=nncExtEnvPwrSupplyTableEntry, nncExtCodeSpaceIndex=nncExtCodeSpaceIndex, nncExtEnvMinus12Status=nncExtEnvMinus12Status, nncExtEnvFanStatusByFanIndex=nncExtEnvFanStatusByFanIndex)
