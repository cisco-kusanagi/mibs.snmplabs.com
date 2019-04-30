#
# PySNMP MIB module CTRON-SSR-HARDWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SSR-HARDWARE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:15:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, ObjectIdentity, Bits, Counter32, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, TimeTicks, ModuleIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "TimeTicks", "ModuleIdentity", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hardwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200))
hardwareMIB.setRevisions(('2000-07-17 00:00', '2000-07-15 00:00', '2000-05-31 00:00', '2000-03-20 00:00', '1999-12-30 00:00', '1999-01-20 00:00', '1998-08-04 00:00',))
if mibBuilder.loadTexts: hardwareMIB.setLastUpdated('200007170000Z')
if mibBuilder.loadTexts: hardwareMIB.setOrganization('Cabletron Systems, Inc.')
class SSRInterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class SSRModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 503, 504, 505, 506, 507))
    namedValues = NamedValues(("controlModule", 1), ("ether100TX", 2), ("ether100FX", 3), ("gigabitSX", 4), ("gigabitLX", 5), ("serial4port", 6), ("hssi", 7), ("unknown", 8), ("gigabitLLX", 9), ("none", 10), ("controlModule2", 11), ("gigabitLLX2P", 12), ("serial2port", 13), ("cmts1x4port", 15), ("fddi2port", 16), ("controlModule3", 17), ("serial4portCE", 20), ("ether100TX16port", 21), ("gigabitTX", 22), ("atm155", 24), ("sonet4PortOc3", 25), ("sonet2PortOc12", 26), ("gigabitFX4P", 27), ("gigabitFX4PGBIC", 28), ("gigabitFX2PGBIC", 29), ("gigabit6K2PBP", 30), ("rbGigabit8PGBIC", 503), ("rbGigabit4PGBIC", 504), ("rbEther100TX24P", 505), ("rbEther100TC32P", 506), ("rbControlModule", 507))

class SSRModuleStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class SSRPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("etherFast", 1), ("gigEther", 2), ("hssi", 3), ("serial", 4), ("unknown", 5), ("sonet", 6), ("ds1", 7), ("ds3", 8), ("cmt", 9), ("e1", 10), ("e3", 11), ("fddi", 12))

class SSRPortConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("empty", 0), ("db9m", 1), ("db9f", 2), ("db15m", 3), ("db15f", 4), ("db25m", 5), ("db25f", 6), ("rj11", 7), ("rj45", 8), ("aui", 9), ("ftypef", 10), ("fiberScMM", 11), ("v35", 12), ("eia530", 13), ("rs44x", 14), ("x21", 15), ("hssi", 16), ("unknown", 17), ("fiberScSM", 18), ("fiberMTRjMM", 19), ("fiberMTRjSM", 20), ("bncf", 21), ("bncm", 22), ("rj21", 23), ("fiberScSMLH", 24))

class SSRserviceType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

class SSRmemorySize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class SSRSwitchingFabricInfo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class SSRCmLedState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class SSRBackupCMState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inactive", 2), ("standby", 3), ("notInstalled", 4), ("active", 5))

sysHwGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1))
sysHwNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwNumSlots.setStatus('current')
sysHwModuleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2), )
if mibBuilder.loadTexts: sysHwModuleTable.setStatus('current')
sysHwModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1), ).setIndexNames((0, "CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: sysHwModuleEntry.setStatus('current')
sysHwModuleSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleSlotNumber.setStatus('current')
sysHwModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 2), SSRModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleType.setStatus('current')
sysHwModuleDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleDesc.setStatus('current')
sysHwModuleNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleNumPorts.setStatus('current')
sysHwModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleVersion.setStatus('current')
sysHwModuleMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 6), SSRmemorySize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleMemory.setStatus('current')
sysHwModuleService = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 8), SSRserviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleService.setStatus('current')
sysHwModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 9), SSRModuleStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleStatus.setStatus('current')
sysHwPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3), )
if mibBuilder.loadTexts: sysHwPortTable.setStatus('current')
sysHwPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1), ).setIndexNames((0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), (0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"))
if mibBuilder.loadTexts: sysHwPortEntry.setStatus('current')
sysHwPortSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortSlotNumber.setStatus('current')
sysHwPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortNumber.setStatus('current')
sysHwPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 3), SSRPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortType.setStatus('current')
sysHwPortConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 4), SSRPortConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortConnectorType.setStatus('current')
sysHwPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 5), SSRInterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortIfIndex.setStatus('current')
class PowerSupplyBits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

sysHwPowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 4), PowerSupplyBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPowerSupply.setStatus('current')
sysHwFan = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("notWorking", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwFan.setStatus('current')
sysHwTemperature = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("outOfRange", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTemperature.setStatus('current')
sysHwChassisId = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwChassisId.setStatus('current')
sysHwSwitchingFabric = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 19), SSRSwitchingFabricInfo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwSwitchingFabric.setStatus('current')
sysHwControlModuleLED = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 20), SSRCmLedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwControlModuleLED.setStatus('current')
sysHwControlModuleBackupState = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 21), SSRBackupCMState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwControlModuleBackupState.setStatus('current')
sysHwLastHotSwapEvent = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 22), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwLastHotSwapEvent.setStatus('current')
sysHwTotalInOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalInOctets.setStatus('deprecated')
sysHwTotalOutOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalOutOctets.setStatus('deprecated')
sysHwTotalInFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalInFrames.setStatus('deprecated')
sysHwTotalOutFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalOutFrames.setStatus('deprecated')
sysHwTotalL2SwitchedFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalL2SwitchedFrames.setStatus('deprecated')
sysHwTotalL3SwitchedFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalL3SwitchedFrames.setStatus('deprecated')
hwConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2))
hwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 1))
hwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2))
hwComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV10 = hwComplianceV10.setStatus('deprecated')
hwComplianceV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV11 = hwComplianceV11.setStatus('deprecated')
hwComplianceV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV12 = hwComplianceV12.setStatus('deprecated')
hwComplianceV30 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV30"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV30 = hwComplianceV30.setStatus('current')
hwConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInOctets"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutOctets"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL2SwitchedFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL3SwitchedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV10 = hwConfGroupV10.setStatus('deprecated')
hwConfGroupV11 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV11 = hwConfGroupV11.setStatus('deprecated')
hwConfGroupV12 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV12 = hwConfGroupV12.setStatus('deprecated')
hwConfGroupV30 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleBackupState"), ("CTRON-SSR-HARDWARE-MIB", "sysHwLastHotSwapEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV30 = hwConfGroupV30.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-HARDWARE-MIB", hardwareMIB=hardwareMIB, sysHwModuleEntry=sysHwModuleEntry, sysHwModuleStatus=sysHwModuleStatus, sysHwPortIfIndex=sysHwPortIfIndex, SSRserviceType=SSRserviceType, sysHwTotalL2SwitchedFrames=sysHwTotalL2SwitchedFrames, sysHwGroup=sysHwGroup, sysHwPortNumber=sysHwPortNumber, sysHwChassisId=sysHwChassisId, sysHwModuleVersion=sysHwModuleVersion, hwConfGroupV11=hwConfGroupV11, sysHwNumSlots=sysHwNumSlots, hwGroups=hwGroups, hwConfGroupV12=hwConfGroupV12, sysHwPortTable=sysHwPortTable, SSRModuleStatus=SSRModuleStatus, SSRCmLedState=SSRCmLedState, sysHwPortType=sysHwPortType, sysHwPortSlotNumber=sysHwPortSlotNumber, sysHwModuleService=sysHwModuleService, sysHwFan=sysHwFan, SSRInterfaceIndex=SSRInterfaceIndex, sysHwModuleDesc=sysHwModuleDesc, sysHwLastHotSwapEvent=sysHwLastHotSwapEvent, PYSNMP_MODULE_ID=hardwareMIB, sysHwModuleMemory=sysHwModuleMemory, sysHwTotalOutFrames=sysHwTotalOutFrames, sysHwControlModuleLED=sysHwControlModuleLED, hwComplianceV12=hwComplianceV12, SSRModuleType=SSRModuleType, hwComplianceV10=hwComplianceV10, SSRPortType=SSRPortType, hwConformance=hwConformance, hwConfGroupV30=hwConfGroupV30, hwComplianceV30=hwComplianceV30, sysHwModuleSlotNumber=sysHwModuleSlotNumber, sysHwTotalInOctets=sysHwTotalInOctets, sysHwSwitchingFabric=sysHwSwitchingFabric, hwConfGroupV10=hwConfGroupV10, hwComplianceV11=hwComplianceV11, SSRPortConnectorType=SSRPortConnectorType, sysHwPortConnectorType=sysHwPortConnectorType, sysHwTemperature=sysHwTemperature, sysHwTotalOutOctets=sysHwTotalOutOctets, sysHwPortEntry=sysHwPortEntry, sysHwControlModuleBackupState=sysHwControlModuleBackupState, sysHwModuleType=sysHwModuleType, sysHwTotalInFrames=sysHwTotalInFrames, sysHwModuleNumPorts=sysHwModuleNumPorts, SSRSwitchingFabricInfo=SSRSwitchingFabricInfo, sysHwModuleTable=sysHwModuleTable, hwCompliances=hwCompliances, SSRmemorySize=SSRmemorySize, PowerSupplyBits=PowerSupplyBits, sysHwTotalL3SwitchedFrames=sysHwTotalL3SwitchedFrames, SSRBackupCMState=SSRBackupCMState, sysHwPowerSupply=sysHwPowerSupply)
