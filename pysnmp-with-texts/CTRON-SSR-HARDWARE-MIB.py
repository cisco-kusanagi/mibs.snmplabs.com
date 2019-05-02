#
# PySNMP MIB module CTRON-SSR-HARDWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SSR-HARDWARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:31:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, Bits, Unsigned32, Integer32, NotificationType, IpAddress, ObjectIdentity, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "Integer32", "NotificationType", "IpAddress", "ObjectIdentity", "MibIdentifier", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hardwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200))
hardwareMIB.setRevisions(('2000-07-17 00:00', '2000-07-15 00:00', '2000-05-31 00:00', '2000-03-20 00:00', '1999-12-30 00:00', '1999-01-20 00:00', '1998-08-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hardwareMIB.setRevisionsDescriptions(('Add support for the Smart Switch 6000 2 Port Gigabit Backplane module to the SSRModuleType for the Enterasys SSR product line', 'Update contact information. This mib is found on Riverstone Networks RS product line as well as Enterasys SSR product line', 'Modify SSRPortConnectorType for GBIC connector in 4.0 and update sysHwModuleService by appending the board serial number for 4.0 for RS-32000.', 'Add Firmware 4.0 support. 3200 series modules, gigabit modules with GBIC support.', 'Add Firmware 3.1 support. 16 port 10/100 TX, Gigabit over Copper, ATM OC-3, POS OC3/12.', 'Add Firmware 3.0 support. Add Backup control module status and last Hotswap event.', 'First Revision of SSR Hardware mib. ',))
if mibBuilder.loadTexts: hardwareMIB.setLastUpdated('200007170000Z')
if mibBuilder.loadTexts: hardwareMIB.setOrganization('Cabletron Systems, Inc.')
if mibBuilder.loadTexts: hardwareMIB.setContactInfo('Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 (603) 332-9400 support@enterasys.com http://www.enterasys.com')
if mibBuilder.loadTexts: hardwareMIB.setDescription('This module defines a schema to access SSR hardware configuration.')
class SSRInterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class SSRModuleType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each module type supported by the SSR series of products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 503, 504, 505, 506, 507))
    namedValues = NamedValues(("controlModule", 1), ("ether100TX", 2), ("ether100FX", 3), ("gigabitSX", 4), ("gigabitLX", 5), ("serial4port", 6), ("hssi", 7), ("unknown", 8), ("gigabitLLX", 9), ("none", 10), ("controlModule2", 11), ("gigabitLLX2P", 12), ("serial2port", 13), ("cmts1x4port", 15), ("fddi2port", 16), ("controlModule3", 17), ("serial4portCE", 20), ("ether100TX16port", 21), ("gigabitTX", 22), ("atm155", 24), ("sonet4PortOc3", 25), ("sonet2PortOc12", 26), ("gigabitFX4P", 27), ("gigabitFX4PGBIC", 28), ("gigabitFX2PGBIC", 29), ("gigabit6K2PBP", 30), ("rbGigabit8PGBIC", 503), ("rbGigabit4PGBIC", 504), ("rbEther100TX24P", 505), ("rbEther100TC32P", 506), ("rbControlModule", 507))

class SSRModuleStatus(TextualConvention, Integer32):
    description = 'Current state of module. online indicates the normal state. Offline indicates a powered off or failed module. Modules may be powered off prior to hot swap.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class SSRPortType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each physical port type supported by the SSR series of products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("etherFast", 1), ("gigEther", 2), ("hssi", 3), ("serial", 4), ("unknown", 5), ("sonet", 6), ("ds1", 7), ("ds3", 8), ("cmt", 9), ("e1", 10), ("e3", 11), ("fddi", 12))

class SSRPortConnectorType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each physical port type supported by the SSR series of products'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("empty", 0), ("db9m", 1), ("db9f", 2), ("db15m", 3), ("db15f", 4), ("db25m", 5), ("db25f", 6), ("rj11", 7), ("rj45", 8), ("aui", 9), ("ftypef", 10), ("fiberScMM", 11), ("v35", 12), ("eia530", 13), ("rs44x", 14), ("x21", 15), ("hssi", 16), ("unknown", 17), ("fiberScSM", 18), ("fiberMTRjMM", 19), ("fiberMTRjSM", 20), ("bncf", 21), ("bncm", 22), ("rj21", 23), ("fiberScSMLH", 24))

class SSRserviceType(TextualConvention, OctetString):
    description = 'A string that is unique to a module in production. This string is used by Cabletron Service and Manufacturing as to identify shipped inventory.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

class SSRmemorySize(TextualConvention, Integer32):
    description = 'An integer that represents the size of memory in Megabytes. -1 represents not-available or not-applicable value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class SSRSwitchingFabricInfo(TextualConvention, Integer32):
    description = 'A bit string that represents the status of Switching Fabric in the shelf/chassis. Switching Fabric #1 is first 2 bits 0-1, #2 is 2-3. For example, given a 16 slot SSR 8600 which has one Switching Fabric in Switching Fabric Slot #1 (lowest full length midplane slot) the integer value 0x00000007 translates into (bits): 0 0 0 0 0 1 1 1 | | | | | | | +--- switching fabric #1 is present | | +----- switching fabric is primary | + ------ switching fabric #2 is present +--------- switching fabric is standby'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class SSRCmLedState(TextualConvention, Integer32):
    description = 'A bit string that represents the status of the active Control Module. Each LED occupies a bit. The value 1 indicates LED is on, 0 is off. The integer value 0x00000015 translates into (bits): 0 0 0 0 1 1 1 1 | | | | | | | +- System OK -- SYS OK | | +--- Heartbeat -- HB | +----- Error -- ERR + ------ Diagnostic -- Diag'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class SSRBackupCMState(TextualConvention, Integer32):
    description = "A enumeration that represents the state of the backup control module. A backup control module prom will boot the system firmware to an intermediate state and begins sending hello messages to the main cpu and assume the monitor(3) state. If the prom does not boot the backup control module, the active control module will report the status as inactive(2). inactive(2) indicates a failed state as it means the backup control module can not take over for the active control module. If the main cpu fails to respond to the backup control module's periodic status checks and the backup control module is in the standby(3) state, the backup control module will reset the active control module, then reset all line cards and then finish a normal boot sequence so that it becomes the master. At this point, the value of this object is active(5). Flows in the hardware must be reprogrammed and all control protocols will have to reestablish. An enterprise trap may also be sent. Normally, slot: CM will be the primary control module. CM/1 is the slot for the backup control module. If some other line card exists in slot CM/1 or no card exists, the state of this object is notInstalled(4)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inactive", 2), ("standby", 3), ("notInstalled", 4), ("active", 5))

sysHwGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1))
sysHwNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwNumSlots.setStatus('current')
if mibBuilder.loadTexts: sysHwNumSlots.setDescription('The number of slots present in the Shelf/Chassis.')
sysHwModuleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2), )
if mibBuilder.loadTexts: sysHwModuleTable.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleTable.setDescription('A list of module entries.')
sysHwModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1), ).setIndexNames((0, "CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"))
if mibBuilder.loadTexts: sysHwModuleEntry.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleEntry.setDescription('An entry containing management information applicable to a particular module.')
sysHwModuleSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleSlotNumber.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleSlotNumber.setDescription('The physical slot number of the module in the Shelf/Chassis.')
sysHwModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 2), SSRModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleType.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleType.setDescription('The physical module type.')
sysHwModuleDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleDesc.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleDesc.setDescription("The description of the module with it's version number etc. For the Control Module it should have the software version, the amount of dynamic RAM, flash RAM.")
sysHwModuleNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleNumPorts.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleNumPorts.setDescription('The number of physical ports on this Card/Module.')
sysHwModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleVersion.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleVersion.setDescription('The alpha-numeric version string for this Card/Module.')
sysHwModuleMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 6), SSRmemorySize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleMemory.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleMemory.setDescription('System Memory size available on the Module. Reports -1 if no memory exists on this module, such as power supplies.')
sysHwModuleService = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 8), SSRserviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleService.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleService.setDescription('The Cabletron service identifier string for this Card/Module.The board serial number is appended to the string too.')
sysHwModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 9), SSRModuleStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwModuleStatus.setStatus('current')
if mibBuilder.loadTexts: sysHwModuleStatus.setDescription('The current status of this module, online or offline.')
sysHwPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3), )
if mibBuilder.loadTexts: sysHwPortTable.setStatus('current')
if mibBuilder.loadTexts: sysHwPortTable.setDescription('A list of module entries.')
sysHwPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1), ).setIndexNames((0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), (0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"))
if mibBuilder.loadTexts: sysHwPortEntry.setStatus('current')
if mibBuilder.loadTexts: sysHwPortEntry.setDescription('An entry containing management information applicable to a particular module.')
sysHwPortSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortSlotNumber.setStatus('current')
if mibBuilder.loadTexts: sysHwPortSlotNumber.setDescription('The physical slot number of the module in the Chassis.')
sysHwPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortNumber.setStatus('current')
if mibBuilder.loadTexts: sysHwPortNumber.setDescription('The port number of the physical port in the Card/Module.')
sysHwPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 3), SSRPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortType.setStatus('current')
if mibBuilder.loadTexts: sysHwPortType.setDescription('The physical port type.')
sysHwPortConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 4), SSRPortConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortConnectorType.setStatus('current')
if mibBuilder.loadTexts: sysHwPortConnectorType.setDescription('The physical port connector type.')
sysHwPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 5), SSRInterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: sysHwPortIfIndex.setDescription('The value of ifIndex used to access this port in the Interface MIB.')
class PowerSupplyBits(TextualConvention, Integer32):
    description = "The encoding of the bits are as follows : Each power supply in the system is represented by two bits. The lower bit reflecting the presence of the power supply and the higher bit representing it's state. A 1 reflects a properly working power supply a 0 one which is down. This encoding allows for a maximum of 16 power supplies. For example : The integer value 0x00000007 translates into 0 0 0 0 0 1 1 1 in bits | | | | | | | +- power supply 1 is present | | +--- power supply 1 is working normally | +----- power supply 2 is present +------- power supply 2 is down"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

sysHwPowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 4), PowerSupplyBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwPowerSupply.setStatus('current')
if mibBuilder.loadTexts: sysHwPowerSupply.setDescription('The number and status of power supplies powering the Shelf/Chassis.')
sysHwFan = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("notWorking", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwFan.setStatus('current')
if mibBuilder.loadTexts: sysHwFan.setDescription('The current state of the fans located inside the Shelf/Chassis.')
sysHwTemperature = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("outOfRange", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTemperature.setStatus('current')
if mibBuilder.loadTexts: sysHwTemperature.setDescription('The current temperature status of the Shelf/Chassis.')
sysHwChassisId = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwChassisId.setStatus('current')
if mibBuilder.loadTexts: sysHwChassisId.setDescription('Operator defined serial number for this particular chassis/shelf.')
sysHwSwitchingFabric = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 19), SSRSwitchingFabricInfo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwSwitchingFabric.setStatus('current')
if mibBuilder.loadTexts: sysHwSwitchingFabric.setDescription('Status of Switching Fabric in shelf/chassis.')
sysHwControlModuleLED = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 20), SSRCmLedState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwControlModuleLED.setStatus('current')
if mibBuilder.loadTexts: sysHwControlModuleLED.setDescription("Status of the shelf/chassis Active Control Module's four LED displays.")
sysHwControlModuleBackupState = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 21), SSRBackupCMState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwControlModuleBackupState.setStatus('current')
if mibBuilder.loadTexts: sysHwControlModuleBackupState.setDescription('Status of the the backup Control Module as interpreted from the active control module. CLI: system show hardware will present the following data: Redundant CPU slot : Not present')
sysHwLastHotSwapEvent = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 22), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwLastHotSwapEvent.setStatus('current')
if mibBuilder.loadTexts: sysHwLastHotSwapEvent.setDescription('The value of sysUpTime when the last hotswap of a physical module event occured.')
sysHwTotalInOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalInOctets.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalInOctets.setDescription('The total number of octets into the switch.')
sysHwTotalOutOctets = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalOutOctets.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalOutOctets.setDescription('The total number of octets out of the switch.')
sysHwTotalInFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalInFrames.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalInFrames.setDescription('The total number of frames into the switch.')
sysHwTotalOutFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalOutFrames.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalOutFrames.setDescription('The total number of frames out of the switch.')
sysHwTotalL2SwitchedFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalL2SwitchedFrames.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalL2SwitchedFrames.setDescription('The current number of frames switched at Layer 2 (transport).')
sysHwTotalL3SwitchedFrames = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHwTotalL3SwitchedFrames.setStatus('deprecated')
if mibBuilder.loadTexts: sysHwTotalL3SwitchedFrames.setDescription('The current number of frames switched at IETF Layers 3 (transport) and 4 (application).')
hwConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2))
hwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 1))
hwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2))
hwComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV10 = hwComplianceV10.setStatus('deprecated')
if mibBuilder.loadTexts: hwComplianceV10.setDescription('The compliance statement for the SSR-HARDWARE-MIB.')
hwComplianceV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV11 = hwComplianceV11.setStatus('deprecated')
if mibBuilder.loadTexts: hwComplianceV11.setDescription('The compliance statement for the SSR-HARDWARE-MIB.')
hwComplianceV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV12 = hwComplianceV12.setStatus('deprecated')
if mibBuilder.loadTexts: hwComplianceV12.setDescription('The compliance statement for the SSR-HARDWARE-MIB.')
hwComplianceV30 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "hwConfGroupV30"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwComplianceV30 = hwComplianceV30.setStatus('current')
if mibBuilder.loadTexts: hwComplianceV30.setDescription('The compliance statement for the SSR-HARDWARE-MIB.')
hwConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInOctets"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutOctets"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL2SwitchedFrames"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL3SwitchedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV10 = hwConfGroupV10.setStatus('deprecated')
if mibBuilder.loadTexts: hwConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the SSR Hardware mib.')
hwConfGroupV11 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV11 = hwConfGroupV11.setStatus('deprecated')
if mibBuilder.loadTexts: hwConfGroupV11.setDescription('A set of managed objects that make up version 1.1 of the SSR Hardware mib.')
hwConfGroupV12 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 3)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV12 = hwConfGroupV12.setStatus('deprecated')
if mibBuilder.loadTexts: hwConfGroupV12.setDescription('A set of managed objects that make up version 1.2 of the SSR Hardware mib.')
hwConfGroupV30 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 4)).setObjects(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"), ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"), ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"), ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"), ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"), ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"), ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"), ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleBackupState"), ("CTRON-SSR-HARDWARE-MIB", "sysHwLastHotSwapEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwConfGroupV30 = hwConfGroupV30.setStatus('current')
if mibBuilder.loadTexts: hwConfGroupV30.setDescription('A set of managed objects that make up version 3.0 of the SSR Hardware mib.')
mibBuilder.exportSymbols("CTRON-SSR-HARDWARE-MIB", sysHwPortSlotNumber=sysHwPortSlotNumber, sysHwPortEntry=sysHwPortEntry, SSRModuleStatus=SSRModuleStatus, hwGroups=hwGroups, PYSNMP_MODULE_ID=hardwareMIB, sysHwTotalOutFrames=sysHwTotalOutFrames, sysHwModuleType=sysHwModuleType, sysHwModuleMemory=sysHwModuleMemory, sysHwModuleTable=sysHwModuleTable, sysHwTotalInOctets=sysHwTotalInOctets, sysHwModuleSlotNumber=sysHwModuleSlotNumber, sysHwModuleStatus=sysHwModuleStatus, PowerSupplyBits=PowerSupplyBits, hardwareMIB=hardwareMIB, hwComplianceV12=hwComplianceV12, hwConfGroupV12=hwConfGroupV12, sysHwChassisId=sysHwChassisId, sysHwTotalOutOctets=sysHwTotalOutOctets, sysHwPortConnectorType=sysHwPortConnectorType, sysHwGroup=sysHwGroup, SSRInterfaceIndex=SSRInterfaceIndex, hwConfGroupV11=hwConfGroupV11, sysHwPortType=sysHwPortType, SSRCmLedState=SSRCmLedState, hwComplianceV11=hwComplianceV11, sysHwPowerSupply=sysHwPowerSupply, sysHwPortNumber=sysHwPortNumber, sysHwTotalL3SwitchedFrames=sysHwTotalL3SwitchedFrames, SSRSwitchingFabricInfo=SSRSwitchingFabricInfo, sysHwModuleVersion=sysHwModuleVersion, sysHwModuleService=sysHwModuleService, sysHwPortTable=sysHwPortTable, sysHwTotalL2SwitchedFrames=sysHwTotalL2SwitchedFrames, hwComplianceV10=hwComplianceV10, sysHwTemperature=sysHwTemperature, sysHwControlModuleLED=sysHwControlModuleLED, sysHwNumSlots=sysHwNumSlots, sysHwTotalInFrames=sysHwTotalInFrames, sysHwModuleEntry=sysHwModuleEntry, hwConformance=hwConformance, sysHwControlModuleBackupState=sysHwControlModuleBackupState, sysHwSwitchingFabric=sysHwSwitchingFabric, sysHwModuleDesc=sysHwModuleDesc, hwConfGroupV10=hwConfGroupV10, SSRBackupCMState=SSRBackupCMState, hwComplianceV30=hwComplianceV30, SSRModuleType=SSRModuleType, SSRPortType=SSRPortType, hwConfGroupV30=hwConfGroupV30, SSRmemorySize=SSRmemorySize, SSRPortConnectorType=SSRPortConnectorType, SSRserviceType=SSRserviceType, sysHwFan=sysHwFan, hwCompliances=hwCompliances, sysHwModuleNumPorts=sysHwModuleNumPorts, sysHwPortIfIndex=sysHwPortIfIndex, sysHwLastHotSwapEvent=sysHwLastHotSwapEvent)
