#
# PySNMP MIB module RIVERSTONE-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-INVENTORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, iso, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "iso", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsInventoryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 40))
rsInventoryMIB.setRevisions(('2001-08-22 00:00', '2001-06-19 00:00', '2001-06-11 00:00', '2001-06-01 00:00', '2001-05-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInventoryMIB.setRevisionsDescriptions(('Change the CLEI object to read-write. Delete fabric and submodule groups.', 'Comments from review meeting with NMS team. Delete all objects pertaining to the state of the system. This MIB will focus on the inventory of the system. The state of the system would be in another MIB. Get rid of all extra objects. Delete the following tables: rsInventoryPortTable. Delete the following objects: rsInventoryChassisType, rsInventoryChassisMaxSlots, rsInventoryChassisNumModules, rsInventoryModuleType, rsInventoryModuleNumPorts, rsInventoryModuleState. Change name from rstone-hardware-mib.txt to rstone-inventory-mib.txt. Delete textual conventions RSChassisType, RSModuleType, RSModuleState, RSPortType, RSPortConnectorType. Change the length of RSModuleServiceString', "Comments from Mike MacFaden. Use INTEGER only for enumerations, otherwise use Integer32. Use OBJECT-IDENTITY instead of OBJECT-IDENTIFIER? Don't use -1 for enumerations? Add more comments in REVISION DESCRIPTION. Comments from Thippana Hongal. Change range of RSMemorySize to start from 0. Rename the enumerations in RSChassisType. Give an example of RSModuleServiceString? Rename enumerations for RSModuleState. Make the ordering of rsChassisMaxSlots and rsInventoryChassisNumModules consistent with their order in SEQUENCE RsInventoryChassisEntry. Give an example of rsInventoryChassisId. Add an object describing the position of the modules in the chassis?", 'Comments from Kenshin Sakura. Add IA product line. Stop using internal names. Make RSModuleType enumerations consistent like this: <type><# of ports><bandwidth>. Capitalize the connector name in a more consistent matter. For example fiberSCsmLH from fiberScSMLH. Modify the description for rsInventoryModuleMemorySize so power supply and fan would not be mentioned.', 'First Version of the Riverstone Inventory MIB.',))
if mibBuilder.loadTexts: rsInventoryMIB.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: rsInventoryMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsInventoryMIB.setContactInfo('Riverstone Networks Customer Service Postal: Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA 95054 USA PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsInventoryMIB.setDescription('This module defines a schema to do an inventory of an RS system.')
rsInventoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1))
rsInventoryOther = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 1))
rsInventoryUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 2))
rsInventoryChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3))
rsInventoryBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 4))
rsInventoryPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6))
rsInventoryFan = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7))
rsInventorySensor = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 8))
rsInventoryModule = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9))
rsInventoryPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 10))
rsInventoryStack = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 11))
class RSMemorySize(TextualConvention, Integer32):
    description = 'An integer that represents the size of memory in Megabytes. 0 represents not-available or not-applicable value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RSModuleServiceString(TextualConvention, OctetString):
    description = 'A string that is unique to a module in production. This string is used by Service and Manufacturing to identify shipped inventory.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

rsInventoryChassisTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1), )
if mibBuilder.loadTexts: rsInventoryChassisTable.setStatus('current')
if mibBuilder.loadTexts: rsInventoryChassisTable.setDescription('')
rsInventoryChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: rsInventoryChassisEntry.setStatus('current')
if mibBuilder.loadTexts: rsInventoryChassisEntry.setDescription('')
rsInventoryChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInventoryChassisId.setStatus('current')
if mibBuilder.loadTexts: rsInventoryChassisId.setDescription('Operator defined serial number for this particular chassis.')
rsInventoryChassisAssetCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsInventoryChassisAssetCLEI.setReference('Bellcore Technical reference GR-485-CORE, COMMON LANGUAGE Equipment Processes and Guidelines, Issue 2, October, 1995.')
if mibBuilder.loadTexts: rsInventoryChassisAssetCLEI.setStatus('current')
if mibBuilder.loadTexts: rsInventoryChassisAssetCLEI.setDescription('The CLEI (Common Language Equipment Identifier) code for the chassis. If the string has length 0, then the physical entity does not have a CLEI code assisgned to it. This object can be changed if the physical entity has incorrect or no CLEI code.')
rsInventoryPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1), )
if mibBuilder.loadTexts: rsInventoryPowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: rsInventoryPowerSupplyTable.setDescription('This table contains one row per power supply for each chassis.')
rsInventoryPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: rsInventoryPowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: rsInventoryPowerSupplyEntry.setDescription('Each entry contains information for one power supply.')
rsInventoryPowerSupplyAssetCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsInventoryPowerSupplyAssetCLEI.setReference('Bellcore Technical reference GR-485-CORE, COMMON LANGUAGE Equipment Processes and Guidelines, Issue 2, October, 1995.')
if mibBuilder.loadTexts: rsInventoryPowerSupplyAssetCLEI.setStatus('current')
if mibBuilder.loadTexts: rsInventoryPowerSupplyAssetCLEI.setDescription('The CLEI (Common Language Equipment Identifier) code for this equipment. If the string has length 0, then the physical entity does not have a CLEI code assisgned to it. This object can be changed if the physical entity has incorrect or no CLEI code.')
rsInventoryFanTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1), )
if mibBuilder.loadTexts: rsInventoryFanTable.setStatus('current')
if mibBuilder.loadTexts: rsInventoryFanTable.setDescription('This table contains one row per fan for each chassis.')
rsInventoryFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: rsInventoryFanEntry.setStatus('current')
if mibBuilder.loadTexts: rsInventoryFanEntry.setDescription('Each entry contains information for a fan.')
rsInventoryFanAssetCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsInventoryFanAssetCLEI.setReference('Bellcore Technical reference GR-485-CORE, COMMON LANGUAGE Equipment Processes and Guidelines, Issue 2, October, 1995.')
if mibBuilder.loadTexts: rsInventoryFanAssetCLEI.setStatus('current')
if mibBuilder.loadTexts: rsInventoryFanAssetCLEI.setDescription('The CLEI (Common Language Equipment Identifier) code for this equipment. If the string has length 0, then the physical entity does not have a CLEI code assisgned to it. This object can be changed if the physical entity has incorrect or no CLEI code.')
rsInventoryModuleTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1), )
if mibBuilder.loadTexts: rsInventoryModuleTable.setStatus('current')
if mibBuilder.loadTexts: rsInventoryModuleTable.setDescription('')
rsInventoryModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: rsInventoryModuleEntry.setStatus('current')
if mibBuilder.loadTexts: rsInventoryModuleEntry.setDescription('')
rsInventoryModuleMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 1), RSMemorySize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInventoryModuleMemorySize.setStatus('current')
if mibBuilder.loadTexts: rsInventoryModuleMemorySize.setDescription('System Memory size available on the Module. Reports -1 if no memory exists on this module.')
rsInventoryModuleServiceString = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 2), RSModuleServiceString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInventoryModuleServiceString.setStatus('current')
if mibBuilder.loadTexts: rsInventoryModuleServiceString.setDescription('The service identifier string for this Card/Module.The board serial number is appended to the string too.')
rsInventoryModuleAssetCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsInventoryModuleAssetCLEI.setReference('Bellcore Technical reference GR-485-CORE, COMMON LANGUAGE Equipment Processes and Guidelines, Issue 2, October, 1995.')
if mibBuilder.loadTexts: rsInventoryModuleAssetCLEI.setStatus('current')
if mibBuilder.loadTexts: rsInventoryModuleAssetCLEI.setDescription('The CLEI (Common Language Equipment Identifier) code for the chassis. If the string has length 0, then the physical entity does not have a CLEI code assisgned to it. This object can be changed if the physical entity has incorrect or no CLEI code.')
rsInventoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3))
rsInventoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 1))
rsInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2))
rsInventoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 1, 1)).setObjects(("RIVERSTONE-INVENTORY-MIB", "rsChassisGroup"), ("RIVERSTONE-INVENTORY-MIB", "rsModuleGroup"), ("RIVERSTONE-INVENTORY-MIB", "rsEnvGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsInventoryCompliance = rsInventoryCompliance.setStatus('current')
if mibBuilder.loadTexts: rsInventoryCompliance.setDescription('')
rsChassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 1)).setObjects(("RIVERSTONE-INVENTORY-MIB", "rsInventoryChassisId"), ("RIVERSTONE-INVENTORY-MIB", "rsInventoryChassisAssetCLEI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsChassisGroup = rsChassisGroup.setStatus('current')
if mibBuilder.loadTexts: rsChassisGroup.setDescription('')
rsModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 2)).setObjects(("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleMemorySize"), ("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleServiceString"), ("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleAssetCLEI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsModuleGroup = rsModuleGroup.setStatus('current')
if mibBuilder.loadTexts: rsModuleGroup.setDescription('')
rsEnvGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 3)).setObjects(("RIVERSTONE-INVENTORY-MIB", "rsInventoryPowerSupplyAssetCLEI"), ("RIVERSTONE-INVENTORY-MIB", "rsInventoryFanAssetCLEI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsEnvGroup = rsEnvGroup.setStatus('current')
if mibBuilder.loadTexts: rsEnvGroup.setDescription('')
mibBuilder.exportSymbols("RIVERSTONE-INVENTORY-MIB", rsInventoryModule=rsInventoryModule, rsInventoryModuleEntry=rsInventoryModuleEntry, rsInventoryPowerSupply=rsInventoryPowerSupply, rsInventoryPort=rsInventoryPort, rsModuleGroup=rsModuleGroup, RSModuleServiceString=RSModuleServiceString, rsInventoryBackplane=rsInventoryBackplane, rsInventoryFanAssetCLEI=rsInventoryFanAssetCLEI, rsInventoryMIBObjects=rsInventoryMIBObjects, rsInventoryCompliance=rsInventoryCompliance, rsInventorySensor=rsInventorySensor, rsInventoryChassis=rsInventoryChassis, rsInventoryPowerSupplyEntry=rsInventoryPowerSupplyEntry, rsInventoryModuleAssetCLEI=rsInventoryModuleAssetCLEI, rsChassisGroup=rsChassisGroup, rsInventoryUnknown=rsInventoryUnknown, rsInventoryChassisAssetCLEI=rsInventoryChassisAssetCLEI, RSMemorySize=RSMemorySize, rsInventoryMIB=rsInventoryMIB, rsInventoryStack=rsInventoryStack, rsInventoryGroups=rsInventoryGroups, rsInventoryPowerSupplyAssetCLEI=rsInventoryPowerSupplyAssetCLEI, rsInventoryFanTable=rsInventoryFanTable, rsInventoryChassisTable=rsInventoryChassisTable, rsInventoryChassisId=rsInventoryChassisId, rsInventoryModuleMemorySize=rsInventoryModuleMemorySize, PYSNMP_MODULE_ID=rsInventoryMIB, rsInventoryOther=rsInventoryOther, rsInventoryPowerSupplyTable=rsInventoryPowerSupplyTable, rsInventoryFan=rsInventoryFan, rsEnvGroup=rsEnvGroup, rsInventoryModuleServiceString=rsInventoryModuleServiceString, rsInventoryFanEntry=rsInventoryFanEntry, rsInventoryConformance=rsInventoryConformance, rsInventoryCompliances=rsInventoryCompliances, rsInventoryModuleTable=rsInventoryModuleTable, rsInventoryChassisEntry=rsInventoryChassisEntry)
