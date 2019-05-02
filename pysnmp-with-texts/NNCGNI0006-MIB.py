#
# PySNMP MIB module NNCGNI0006-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI0006-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:22:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
nncExtEnvironmental, nncExtNVM, nncLegacyModules, nncExtCodeSpace, nncExtProbe, nncExtRestart, nncExtDiag, nncExtSystem = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtEnvironmental", "nncExtNVM", "nncLegacyModules", "nncExtCodeSpace", "nncExtProbe", "nncExtRestart", "nncExtDiag", "nncExtSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, NotificationType, Counter32, Bits, iso, Gauge32, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter32", "Bits", "iso", "Gauge32", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
nncExtBasics = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 4, 1))
if mibBuilder.loadTexts: nncExtBasics.setLastUpdated('9904301330Z')
if mibBuilder.loadTexts: nncExtBasics.setOrganization('Newbridge Networks Corporation')
if mibBuilder.loadTexts: nncExtBasics.setContactInfo(' Newbridge Networks Corporation Postal: 600 March Road Kanata, Ontario Canada K2K 2E6 Phone: +1 613 591 3600 Fax: +1 613 591 3680')
if mibBuilder.loadTexts: nncExtBasics.setDescription('The MIB module containing management information for basic network element functions: restart info, environmental info, box identity, etc.')
class RestartCause(TextualConvention, Integer32):
    description = 'Why the box restarted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72))
    namedValues = NamedValues(("trblnoProblem", 0), ("trblUnknown", 1), ("trblBusError", 2), ("trblAddressError", 3), ("trblIllegalInst", 4), ("trblZeroDivide", 5), ("trblChkFailure", 6), ("trblTrapVInst", 7), ("trblPrivilege", 8), ("trblTraceTrap", 9), ("trblLine1010", 10), ("trblLine1111", 11), ("trblUninitialized", 15), ("trblSpurious", 24), ("trblIntLevel1", 25), ("trblIntLevel2", 26), ("trblIntLevel3", 27), ("trblIntLevel4", 28), ("trblIntLevel5", 29), ("trblIntLevel6", 30), ("trblIntLevel7", 31), ("trblTrap00", 32), ("trblTrap01", 33), ("trblTrap02", 34), ("trblTrap03", 35), ("trblTrap04", 36), ("trblTrap05", 37), ("trblTrap06", 38), ("trblTrap07", 39), ("trblTrap08", 40), ("trblTrap09", 41), ("trblTrap10", 42), ("trblTrap11", 43), ("trblTrap12", 44), ("trblTrap13", 45), ("trblTrap14", 46), ("trblTrap15", 47), ("trblWatchDog", 48), ("trblNCIReset", 49), ("trblNCIRunMinusOne", 50), ("trblPanic", 51), ("trblRunBootProm", 52), ("trblCopyRamToFlash", 53), ("trblDnldAborted", 54), ("trblBadFlashConfig", 55), ("trblNVMReset", 56), ("trblDspReset", 57), ("trblDspDnldFailed", 58), ("trblDspPollFailed", 59), ("trblDspDiedOnTx", 60), ("trblDspDead", 61), ("trblDCMPDeath", 62), ("trblRunningLowComms", 63), ("trblRunningLowFrame", 64), ("trblRunningLowSys", 65), ("trblRunningLowSonic", 66), ("trblRunningLowMgmt", 67), ("trblRunningLowPoolUnknown", 68), ("trblNCIReload", 69), ("trblPushButton", 70), ("trblCPUReset", 71), ("trblRDSReset", 72))

class Nci2DeviceIDType(TextualConvention, Integer32):
    description = 'An entities device identifier. These numbers are assigned by the device ID administrator. He/she must be contacted if new device IDs need to be added.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 93, 97, 101, 102, 112))
    namedValues = NamedValues(("unknown", 0), ("nc3600", 1), ("dcp3600", 2), ("dtu2601", 4), ("dtu2602", 5), ("dtu2603", 6), ("dclcRs232", 7), ("dclcX21", 8), ("dclcV35", 9), ("ldm1124", 10), ("ldm1121", 11), ("ldm1135", 12), ("nmu4601", 13), ("nmu4602", 14), ("nc3624", 15), ("nc3612", 16), ("nc3630", 17), ("dtu2601Anm", 18), ("dtu2602Anm", 19), ("dtu2603Anm", 20), ("dtu2608", 21), ("dsp3600", 22), ("dpm3600", 23), ("detT1", 24), ("detE1", 25), ("nmu4601A", 26), ("nmu4605", 27), ("nmu5602", 28), ("nmu5610", 29), ("nc3645SE", 30), ("nc3645PE", 31), ("dtu2610Pad", 32), ("dtu2606", 33), ("nmu5610ci", 34), ("ncDS3", 35), ("ta1601S", 36), ("ta1601U", 37), ("ta1602S", 38), ("ta1602U", 39), ("ta1603S", 40), ("ta1603U", 41), ("elb8230", 42), ("nvpSysMgr", 43), ("nvpVoiceSrvr", 44), ("nvpEdsp", 45), ("nc1615C", 46), ("nc3606Voice", 47), ("nc3606Data", 48), ("nvp1000", 49), ("dtu2701", 50), ("dtu2702", 51), ("dtu2703", 52), ("bert2601", 53), ("bert2602", 54), ("bert2603", 55), ("dtu2701Anm", 56), ("dtu2702Anm", 57), ("dtu2703Anm", 58), ("tap", 59), ("nmu8001", 60), ("bertMgr", 61), ("dclcRs422", 62), ("eapApi", 63), ("ncdE3", 64), ("er8231", 65), ("tr8251", 66), ("pte", 67), ("nc3664", 68), ("nc36150", 69), ("esn3700", 70), ("esnEsc", 71), ("esnOne", 72), ("dtu2704", 73), ("nmu4602Dn", 74), ("nmu4602Cn", 75), ("nmu4602Rn", 76), ("nc3620", 77), ("ncWgs", 78), ("nc36170", 79), ("bri3600St", 80), ("ncFRATM", 81), ("ncRouteServer", 82), ("ncSystemManager", 83), ("ncATMNIC", 84), ("ncYellowRidge", 85), ("ncELSU", 93), ("ncBlueRidge", 97), ("ncOrangeRidge", 101), ("ncRedRidge", 102), ("ncCampusSwitch", 112))

class CurrentGenericType(DisplayString):
    description = 'The revision of the current executing firmware in the standard Newbridge fashion. The identifier is a string of up to 12 ASCII characters of the form ZAABCD-TM-LL where: ZAABC identifies the product, D identifies the major release T identifies the load type M identifies the minor release and LL identifies the load number'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class ProductPartNumberType(DisplayString):
    description = 'This type defines the standard Newbridge assembly part number. The assembly number identifier is a string of 17 ASCII characters of the form 90-xxxx-VV-CC-MMM where: 90 - Marketing part number xxxx - sequence number VV - Variant CC - Customer Code MMM - Manufacturing Code'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class CardIDType(TextualConvention, Integer32):
    description = 'An module identifier (from GNI0001 found in Tech Lib).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 5, 6, 7, 51, 57, 58, 59, 60, 61, 62))
    namedValues = NamedValues(("unknown", 0), ("yellowRidgeMainCard", 4), ("yellowRidgeLEDBoard", 5), ("yellowRidgeOc3MmfPdmModule", 6), ("yellowRidgeBufferModule", 7), ("yellowRidgeOc3SmfPdmModule", 51), ("cpElsuMainCard", 57), ("coElsuAtmCard", 58), ("coElsuMainCard", 59), ("elsuDisplayModule", 60), ("elsuAuiBackplane", 61), ("coElsu10BaseTBackplane", 62))

class CardSerialNumberType(TextualConvention, OctetString):
    description = 'An module serial number specification. 2d-2d,1d,8d field bytes contents range ----- ----- -------- ----- 1 1-2 week 1..52 2 3-4 year 0..99 3 5 assembly line 0..9 4 6-10 assembly number 0..99999'
    status = 'current'
    displayHint = '2d-2d,1d,8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class NncSwStatus(TextualConvention, Integer32):
    description = 'The NncSwStatus represents the status of any software bank.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 1), ("ok", 2), ("error", 3), ("empty", 4))

class NncSwBank(TextualConvention, Integer32):
    description = 'The NncSwBank represents a software bank.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 257))
    namedValues = NamedValues(("notapplicable", 0), ("bootbank", 1), ("bank1", 2), ("bank2", 3), ("bank3", 4), ("bank4", 5), ("bank5", 6), ("bank6", 7), ("bank7", 8), ("bank8", 9), ("bank9", 10), ("bank10", 11), ("bank11", 12), ("bank12", 13), ("bank13", 14), ("bank14", 15), ("bank15", 16), ("bank16", 17), ("bank17", 18), ("bank18", 19), ("bank19", 20), ("bank20", 21), ("bank21", 22), ("bank22", 23), ("bank23", 24), ("bank24", 25), ("bank25", 26), ("bank26", 27), ("bank27", 28), ("bank28", 29), ("bank29", 30), ("bank30", 31), ("bank31", 32), ("bank32", 33), ("unknown", 257))

nncExtSysProductName = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysProductName.setStatus('current')
if mibBuilder.loadTexts: nncExtSysProductName.setDescription('The marketing name for the product, e.g. 8231 MainStreet')
nncExtSysCurrentGeneric = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 2), CurrentGenericType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCurrentGeneric.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCurrentGeneric.setDescription('The revision of the current executing firmware in the controlling component of the system.')
nncExtSysProductPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 3), ProductPartNumberType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysProductPartNumber.setStatus('current')
if mibBuilder.loadTexts: nncExtSysProductPartNumber.setDescription('The Newbridge assembly part number for the given system.')
nncExtSysNci2DeviceID = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 4), Nci2DeviceIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysNci2DeviceID.setStatus('current')
if mibBuilder.loadTexts: nncExtSysNci2DeviceID.setDescription('The NCI2 device ID assigned to the device.')
nncExtSysCurrentDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 1, 5), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtSysCurrentDateAndTime.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCurrentDateAndTime.setDescription('If set on the device, this returns the date and time. Otherwise, returns all 0s.')
nncExtSysCardTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 1, 6), )
if mibBuilder.loadTexts: nncExtSysCardTable.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardTable.setDescription('Table containing information about the card in this system.')
nncExtSysCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtSysCardIndex"))
if mibBuilder.loadTexts: nncExtSysCardEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardEntry.setDescription('An entry in the system card table.')
nncExtSysCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardIndex.setDescription('Card number.')
nncExtSysCardIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 2), CardIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardIDType.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardIDType.setDescription('Type of module/card.')
nncExtSysCardName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardName.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardName.setDescription('The name of the card as saved on the SEEP.')
nncExtSysCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 4), CardSerialNumberType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSysCardSerialNumber.setStatus('current')
if mibBuilder.loadTexts: nncExtSysCardSerialNumber.setDescription('Serial number of the current card.')
nncExtEnvFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fanOk", 1), ("fanFailed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanStatus.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvFanStatus.setDescription('The current status of the fan. This is product dependent.')
nncExtEnvTemperatureSensor = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("tooHot", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvTemperatureSensor.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvTemperatureSensor.setDescription('The suitability of the current temperature. This is product dependent.')
nncExtEnvPlus12Status = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("outOfSpec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPlus12Status.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvPlus12Status.setDescription('Whether or not the +12V rail is in spec. This is product dependent.')
nncExtEnvMinus12Status = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("outOfSpec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvMinus12Status.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvMinus12Status.setDescription('Whether or not the -12V rail is in spec. This is product dependent.')
class FanStatusType(TextualConvention, Integer32):
    description = 'A value of this type identifies if the fan status is ok or bad'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("bad", 1))

nncExtEnvFanTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 2, 5), )
if mibBuilder.loadTexts: nncExtEnvFanTable.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvFanTable.setDescription('This table holds the fan status information')
nncExtEnvFanTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtEnvFanIndex"))
if mibBuilder.loadTexts: nncExtEnvFanTableEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvFanTableEntry.setDescription(' A conceptual row for nncExtEnvFanTable. ')
nncExtEnvFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvFanIndex.setDescription('The index into the fan table')
nncExtEnvFanStatusByFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 2), FanStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvFanStatusByFanIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvFanStatusByFanIndex.setDescription('The state of the fan - ok or bad')
class PwrSupplyStatusType(TextualConvention, Integer32):
    description = 'A value of this type identifies the power supply status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("noAc", 1), ("noDc", 2), ("notPresent", 3))

nncExtEnvPwrSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 2, 6), )
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTable.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTable.setDescription('This table holds the fan status information')
nncExtEnvPwrSupplyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtEnvPwrSupplySlotIndex"))
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTableEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvPwrSupplyTableEntry.setDescription(' A conceptual row for nncExtEnvPwrSupplyTable. ')
nncExtEnvPwrSupplySlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPwrSupplySlotIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvPwrSupplySlotIndex.setDescription('Power Supply Slot Number - Ranges from 1 to 255')
nncExtEnvPwrSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 2), PwrSupplyStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtEnvPwrSupplyStatus.setStatus('current')
if mibBuilder.loadTexts: nncExtEnvPwrSupplyStatus.setDescription('The state of the power supply - ok , off, bad or not present')
nncExtRestarts = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestarts.setStatus('current')
if mibBuilder.loadTexts: nncExtRestarts.setDescription('The number of times the active code bank has restarted.')
nncExtFaultInducedRestarts = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtFaultInducedRestarts.setStatus('current')
if mibBuilder.loadTexts: nncExtFaultInducedRestarts.setDescription('The number of restarts of the active code bank that have been caused by a fault, e.g. processor trap.')
nncExtLastFault = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 3), RestartCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtLastFault.setStatus('current')
if mibBuilder.loadTexts: nncExtLastFault.setDescription('The cause of the last restart of the active code bank that was caused by a fault, e.g. processor trap.')
nncExtFaultRepetitions = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtFaultRepetitions.setStatus('current')
if mibBuilder.loadTexts: nncExtFaultRepetitions.setDescription('The number of consecutive times the fault reported in nncExtLastFault has been repeated.')
nncExtRestartTracebackTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 3, 5), )
if mibBuilder.loadTexts: nncExtRestartTracebackTable.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartTracebackTable.setDescription('The sequence of program counter values that lead to the last recorded fault.')
nncExtRestartTracebackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtRestartTracebackIndex"))
if mibBuilder.loadTexts: nncExtRestartTracebackEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartTracebackEntry.setDescription('An entry in the sequence of program counter values.')
nncExtRestartTracebackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartTracebackIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartTracebackIndex.setDescription('The index into the traceback table')
nncExtRestartTracebackPCValue = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartTracebackPCValue.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartTracebackPCValue.setDescription('The program counter value for this entry in the traceback table.')
nncExtRestartRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 3, 6), )
if mibBuilder.loadTexts: nncExtRestartRegisterTable.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartRegisterTable.setDescription('The sequence of register values at the last recorded fault.')
nncExtRestartRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtRestartRegisterIndex"))
if mibBuilder.loadTexts: nncExtRestartRegisterEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartRegisterEntry.setDescription('An entry in the set of register values.')
nncExtRestartRegisterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartRegisterIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartRegisterIndex.setDescription('The index into the Register table. The Index to register mapping for a Motorola processor is as follows: 1 - D0 2 - D1 : 8 - D8 9 - A0 : 15 - A6 16 - Status Reg 17 - Program Counter')
nncExtRestartRegisterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartRegisterValue.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartRegisterValue.setDescription('The register value for this entry in the Register table.')
nncExtRestartForceToBoot = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtRestartForceToBoot.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartForceToBoot.setDescription('A set will cause the box to start executing from the boot PROM after the delay specified by the value written. A second set before the delay has expired will be rejected with badValue. A read will return zero.')
nncExtRestartCause = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 8), RestartCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtRestartCause.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartCause.setDescription('The cause of the last restart of the system.')
nncExtRestartSystem = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36000))).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtRestartSystem.setStatus('current')
if mibBuilder.loadTexts: nncExtRestartSystem.setDescription('A set will cause the Node to restart after a specified delay and then execute the System code that resides in the Next Active Code Bank. The delay is specified by the value written. A second set before the delay has expired will be rejected with badValue. A read will return zero. ')
class CodeSpaceIndex(TextualConvention, Integer32):
    description = 'The index into the codespace.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

nncExtCodeSpaceCurrentlyActive = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 1), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCurrentlyActive.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceCurrentlyActive.setDescription('The index into the code space table of the code space from which the box is currently executing')
nncExtCodeSpaceNextActive = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 2), CodeSpaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtCodeSpaceNextActive.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceNextActive.setDescription('The index into the code space table of the code space from which the box will execute after the next restart.')
nncExtCodeSpaceNumber = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 4, 3), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceNumber.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceNumber.setDescription('The number of code spaces supported by this box.')
nncExtCodeSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 4, 4), )
if mibBuilder.loadTexts: nncExtCodeSpaceTable.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceTable.setDescription('Information about all of the code spaces present in this box.')
nncExtCodeSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtCodeSpaceIndex"))
if mibBuilder.loadTexts: nncExtCodeSpaceEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceEntry.setDescription('Information about one of the code spaces present in this box.')
nncExtCodeSpaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 1), CodeSpaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceIndex.setDescription('The code space of interest')
nncExtCodeSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceSize.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceSize.setDescription('The size (in bytes) of the maximum code space available in flash memory.')
nncExtCodeSpaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceStatus.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceStatus.setDescription('Whether or not the specified code space is considered to be sane e.g.,checksum is valid.')
nncExtCodeSpaceGeneric = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 4), CurrentGenericType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceGeneric.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceGeneric.setDescription('Which generic is contained in the code space.')
nncExtCodeSpaceDownloadDate = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadDate.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadDate.setDescription('The date on which this generic was downloaded. This OBJECT is known by the target.')
nncExtCodeSpaceDownloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadTime.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadTime.setDescription('The time at which this generic was downloaded. This OBJECT is known by the target.')
nncExtCodeSpaceDownloadServer = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadServer.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadServer.setDescription('The address of the source of the generic that is present in the code space.')
nncExtCodeSpaceDownloadRequestor = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadRequestor.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceDownloadRequestor.setDescription('The address of the entity that caused this code space to be downloaded with the current generic.')
nncExtCodeSpaceCompressionType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("c1", 2), ("c2", 3), ("c3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCompressionType.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceCompressionType.setDescription('The kind of compression used on the load before it was placed into flash.')
nncExtCodeSpaceLoadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceLoadSize.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceLoadSize.setDescription('The size (in bytes) of the load stored in this code space when decompressed.')
nncExtCodeSpaceCompressLoadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtCodeSpaceCompressLoadSize.setStatus('current')
if mibBuilder.loadTexts: nncExtCodeSpaceCompressLoadSize.setDescription('The size (in bytes) of the load stored in this code space when compressed.')
class NVMPoolIndex(TextualConvention, Integer32):
    description = 'Index into the NVM pool.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

nncExtNVMUsageTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 5, 1), )
if mibBuilder.loadTexts: nncExtNVMUsageTable.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMUsageTable.setDescription('How much NVM is used in the box in bytes.')
nncExtNVMUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtNVMPoolIndex"))
if mibBuilder.loadTexts: nncExtNVMUsageEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMUsageEntry.setDescription('How much NVM is used in a pool of it')
nncExtNVMPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 1), NVMPoolIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolIndex.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMPoolIndex.setDescription('Which NVM pool')
nncExtNVMPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolSize.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMPoolSize.setDescription('The total number of bytes in the pool')
nncExtNVMPoolBytesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMPoolBytesUsed.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMPoolBytesUsed.setDescription('The number of bytes used in the pool')
nncExtNVMLastRepair = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(31, 31)).setFixedLength(31)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNVMLastRepair.setStatus('current')
if mibBuilder.loadTexts: nncExtNVMLastRepair.setDescription('Details of the last repair made to the database returned in a string format -- a readable form of the following: Offset Length Meaning 0 1 Number Of Bytes in the String (=31) 1 1 Length of repaired item (in bytes) 2 4 Address of Block containing repaired item 6 2 block number of the repaired block 8 2 item number of repaired entry 10 2 first parameter of repaired item 12 2 second parameter of repaired item 14 1 length of date string 15 9 date of repair (DD-MMM-YY) 24 1 length of time string (=6) 25 6 time of repair (HH:MMX)')
nncExtProbeMPLTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 12, 1), )
if mibBuilder.loadTexts: nncExtProbeMPLTable.setStatus('current')
if mibBuilder.loadTexts: nncExtProbeMPLTable.setDescription('A window into the Master Parameter List.')
nncExtProbeMPLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1), ).setIndexNames((0, "NNCGNI0006-MIB", "nncExtProbeMPL"))
if mibBuilder.loadTexts: nncExtProbeMPLEntry.setStatus('current')
if mibBuilder.loadTexts: nncExtProbeMPLEntry.setDescription('An entry in the master parameter list. The instance identifer is of the form: nncExtProbeMPL.<c>.<i>.<m1>.<m2>.<m3>.<m4>')
nncExtProbeMPL = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtProbeMPL.setStatus('current')
if mibBuilder.loadTexts: nncExtProbeMPL.setDescription('A window into in the Master Parameter List. The instance identifer is of the form: <c>.<i>.<m1>.<m2>.<m3>.<m4>')
class SvcEpdOptionType(TextualConvention, Integer32):
    description = 'A value of this type identifies the early packet discard option - off or on'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class SvcPpdOptionType(TextualConvention, Integer32):
    description = 'A value of this type identifies the partial packet discard option - off or on'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

nncDiagUndoAll = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("undo", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncDiagUndoAll.setStatus('current')
if mibBuilder.loadTexts: nncDiagUndoAll.setDescription("A write of 'undo' to this parameter will cause all maintenance operations to be removed, e.g. loopbacks busy-outs, etc")
nncExtStartupDiagnosticResults = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("unspecifiedFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtStartupDiagnosticResults.setStatus('current')
if mibBuilder.loadTexts: nncExtStartupDiagnosticResults.setDescription('If ALL of the systems startup diagnostic tests passed successfully, then this object is set to passed otherwise it is set to failed ')
mibBuilder.exportSymbols("NNCGNI0006-MIB", nncExtRestartSystem=nncExtRestartSystem, nncExtCodeSpaceCurrentlyActive=nncExtCodeSpaceCurrentlyActive, RestartCause=RestartCause, nncExtProbeMPL=nncExtProbeMPL, nncExtSysProductPartNumber=nncExtSysProductPartNumber, PYSNMP_MODULE_ID=nncExtBasics, nncExtNVMUsageTable=nncExtNVMUsageTable, nncExtRestartTracebackEntry=nncExtRestartTracebackEntry, nncExtEnvFanStatusByFanIndex=nncExtEnvFanStatusByFanIndex, nncExtCodeSpaceGeneric=nncExtCodeSpaceGeneric, nncExtFaultInducedRestarts=nncExtFaultInducedRestarts, nncExtRestartTracebackPCValue=nncExtRestartTracebackPCValue, nncExtSysCardSerialNumber=nncExtSysCardSerialNumber, nncExtSysNci2DeviceID=nncExtSysNci2DeviceID, nncExtSysCardEntry=nncExtSysCardEntry, nncExtEnvFanTableEntry=nncExtEnvFanTableEntry, NncSwBank=NncSwBank, nncExtEnvPwrSupplyTable=nncExtEnvPwrSupplyTable, nncExtEnvFanIndex=nncExtEnvFanIndex, nncExtFaultRepetitions=nncExtFaultRepetitions, nncExtCodeSpaceCompressionType=nncExtCodeSpaceCompressionType, CardIDType=CardIDType, nncExtSysCardTable=nncExtSysCardTable, nncExtEnvFanStatus=nncExtEnvFanStatus, NVMPoolIndex=NVMPoolIndex, nncExtSysCardIDType=nncExtSysCardIDType, nncExtRestartRegisterTable=nncExtRestartRegisterTable, nncExtRestartRegisterIndex=nncExtRestartRegisterIndex, nncExtCodeSpaceDownloadDate=nncExtCodeSpaceDownloadDate, nncExtProbeMPLEntry=nncExtProbeMPLEntry, nncExtCodeSpaceIndex=nncExtCodeSpaceIndex, nncExtCodeSpaceTable=nncExtCodeSpaceTable, nncDiagUndoAll=nncDiagUndoAll, nncExtCodeSpaceDownloadTime=nncExtCodeSpaceDownloadTime, nncExtCodeSpaceDownloadServer=nncExtCodeSpaceDownloadServer, nncExtCodeSpaceStatus=nncExtCodeSpaceStatus, nncExtEnvMinus12Status=nncExtEnvMinus12Status, nncExtRestartRegisterEntry=nncExtRestartRegisterEntry, nncExtCodeSpaceNumber=nncExtCodeSpaceNumber, nncExtRestartTracebackTable=nncExtRestartTracebackTable, SvcPpdOptionType=SvcPpdOptionType, nncExtNVMUsageEntry=nncExtNVMUsageEntry, nncExtNVMLastRepair=nncExtNVMLastRepair, nncExtEnvFanTable=nncExtEnvFanTable, nncExtLastFault=nncExtLastFault, nncExtNVMPoolSize=nncExtNVMPoolSize, NncSwStatus=NncSwStatus, nncExtEnvPwrSupplySlotIndex=nncExtEnvPwrSupplySlotIndex, SvcEpdOptionType=SvcEpdOptionType, CodeSpaceIndex=CodeSpaceIndex, nncExtCodeSpaceSize=nncExtCodeSpaceSize, ProductPartNumberType=ProductPartNumberType, nncExtCodeSpaceEntry=nncExtCodeSpaceEntry, nncExtCodeSpaceCompressLoadSize=nncExtCodeSpaceCompressLoadSize, PwrSupplyStatusType=PwrSupplyStatusType, nncExtEnvPlus12Status=nncExtEnvPlus12Status, CardSerialNumberType=CardSerialNumberType, nncExtCodeSpaceDownloadRequestor=nncExtCodeSpaceDownloadRequestor, nncExtSysCurrentGeneric=nncExtSysCurrentGeneric, CurrentGenericType=CurrentGenericType, nncExtProbeMPLTable=nncExtProbeMPLTable, nncExtRestarts=nncExtRestarts, nncExtCodeSpaceNextActive=nncExtCodeSpaceNextActive, nncExtEnvPwrSupplyStatus=nncExtEnvPwrSupplyStatus, nncExtRestartCause=nncExtRestartCause, nncExtEnvPwrSupplyTableEntry=nncExtEnvPwrSupplyTableEntry, nncExtSysCardName=nncExtSysCardName, nncExtBasics=nncExtBasics, nncExtRestartTracebackIndex=nncExtRestartTracebackIndex, nncExtStartupDiagnosticResults=nncExtStartupDiagnosticResults, nncExtCodeSpaceLoadSize=nncExtCodeSpaceLoadSize, nncExtSysProductName=nncExtSysProductName, nncExtSysCurrentDateAndTime=nncExtSysCurrentDateAndTime, nncExtNVMPoolIndex=nncExtNVMPoolIndex, Nci2DeviceIDType=Nci2DeviceIDType, nncExtNVMPoolBytesUsed=nncExtNVMPoolBytesUsed, nncExtEnvTemperatureSensor=nncExtEnvTemperatureSensor, nncExtRestartForceToBoot=nncExtRestartForceToBoot, nncExtSysCardIndex=nncExtSysCardIndex, nncExtRestartRegisterValue=nncExtRestartRegisterValue, FanStatusType=FanStatusType)
