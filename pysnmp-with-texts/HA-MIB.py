#
# PySNMP MIB module HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fibrechannel, = mibBuilder.importSymbols("Brocade-REG-MIB", "fibrechannel")
entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalName")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, NotificationType, IpAddress, Gauge32, TimeTicks, iso, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "NotificationType", "IpAddress", "Gauge32", "TimeTicks", "iso", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swSsn, swID = mibBuilder.importSymbols("SW-MIB", "swSsn", "swID")
haMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2))
haMIB.setRevisions(('2002-08-16 00:00', '2004-02-25 15:30', '2009-02-09 00:00', '2009-04-06 00:00', '2009-06-25 12:00', '2010-07-22 10:00', '2012-09-25 10:00', '2013-05-07 17:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: haMIB.setRevisionsDescriptions(('The initial revision for the High Availability MIB.', 'Added mib objects fruSupplierId, fruSupplierPartNum, fruSupplierSerialNum and fruSupplierRevCode to fruTable.', 'Added new value coreblade and ap blade for fru table.', 'Added textual convention for FruClass.', "Removed the version information from Brocade's proprietary MIB file name.", 'Added frutype and frunum to the existing frustatuschange trap.', 'Added two enums powerdown & initialized for frustatus trap.', 'Added bpTable',))
if mibBuilder.loadTexts: haMIB.setLastUpdated('201305071757Z')
if mibBuilder.loadTexts: haMIB.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: haMIB.setContactInfo('Customer Support Group Brocade Communications Systems, 1745 Technology Drive, San Jose, CA 95110 U.S.A Tel: +1-408-392-6061 Fax: +1-408-392-6656 Email: support@Brocade.COM WEB: www.brocade.com')
if mibBuilder.loadTexts: haMIB.setDescription('The MIB module High Availability MIB. Copyright (c) 2002-2003 Brocade Communications Systems, Inc. All rights reserved.')
highAvailability = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1))
haStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("redundant", 0), ("nonredundant", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haStatus.setStatus('current')
if mibBuilder.loadTexts: haStatus.setDescription('Whether the system is redundant or not.')
class FruClass(TextualConvention, Integer32):
    description = 'The type of the FRU object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("cp", 4), ("other-CP", 5), ("switchblade", 6), ("wwn", 7), ("powerSupply", 8), ("fan", 9), ("coreblade", 10), ("applicationblade", 11))

fruTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5), )
if mibBuilder.loadTexts: fruTable.setStatus('current')
if mibBuilder.loadTexts: fruTable.setDescription("This table inventories the field replaceable units (FRUs) slots available. There is entry in this table for each entry in the entPhysicalTable that has entPhysicalClass set to 'Container (5)' and has a child entry having entPhysicalIsFRU field to be true")
fRUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: fRUEntry.setStatus('current')
if mibBuilder.loadTexts: fRUEntry.setDescription('An entry for FRU slot in the fruTable')
fruClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 1), FruClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruClass.setStatus('current')
if mibBuilder.loadTexts: fruClass.setDescription('The type of the FRU object that these slot can hold')
fruStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("on", 3), ("off", 4), ("faulty", 5), ("poweredon", 6), ("initialized", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruStatus.setStatus('current')
if mibBuilder.loadTexts: fruStatus.setDescription('The current status of the FRU object in the slot')
fruObjectNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruObjectNum.setStatus('current')
if mibBuilder.loadTexts: fruObjectNum.setDescription('Gives the slot number of the blade and unit number for everything else')
fruSupplierId = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSupplierId.setStatus('current')
if mibBuilder.loadTexts: fruSupplierId.setDescription('The supplier id.')
fruSupplierPartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSupplierPartNum.setStatus('current')
if mibBuilder.loadTexts: fruSupplierPartNum.setDescription('The supplier part number.')
fruSupplierSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSupplierSerialNum.setStatus('current')
if mibBuilder.loadTexts: fruSupplierSerialNum.setDescription('The supplier serial number.')
fruSupplierRevCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSupplierRevCode.setStatus('current')
if mibBuilder.loadTexts: fruSupplierRevCode.setDescription('The supplier revision code.')
fruPowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 5, 1, 8), DisplayString()).setUnits('watt').setMaxAccess("readonly")
if mibBuilder.loadTexts: fruPowerConsumption.setStatus('current')
if mibBuilder.loadTexts: fruPowerConsumption.setDescription('This represents power consumption of blades. This will have values only for core/switch blades and for other FRUs, it will be 0')
fruHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6), )
if mibBuilder.loadTexts: fruHistoryTable.setStatus('current')
if mibBuilder.loadTexts: fruHistoryTable.setDescription('This table gives the contents of the entire history log of the FRU events')
fruHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1), ).setIndexNames((0, "HA-MIB", "fruHistoryIndex"))
if mibBuilder.loadTexts: fruHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: fruHistoryEntry.setDescription('An entry in this table represents a particular FRU event')
fruHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: fruHistoryIndex.setDescription('Index of the FRU event in the history table')
fruHistoryClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 2), FruClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryClass.setStatus('current')
if mibBuilder.loadTexts: fruHistoryClass.setDescription('The type of the FRU object related to the event')
fruHistoryObjectNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryObjectNum.setStatus('current')
if mibBuilder.loadTexts: fruHistoryObjectNum.setDescription('Gives the slot number of the blade and unit number for everything else')
fruHistoryEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("added", 1), ("removed", 2), ("invalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryEvent.setStatus('current')
if mibBuilder.loadTexts: fruHistoryEvent.setDescription('The type of the FRU event')
fruHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryTime.setStatus('current')
if mibBuilder.loadTexts: fruHistoryTime.setDescription('Gives the time at which this event happened')
fruHistoryFactoryPartNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryFactoryPartNum.setStatus('current')
if mibBuilder.loadTexts: fruHistoryFactoryPartNum.setDescription('Gives the factory part num of the FRU object')
fruHistoryFactorySerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruHistoryFactorySerialNum.setStatus('current')
if mibBuilder.loadTexts: fruHistoryFactorySerialNum.setDescription('Gives the factory serial num of the FRU object')
cpTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7), )
if mibBuilder.loadTexts: cpTable.setStatus('current')
if mibBuilder.loadTexts: cpTable.setDescription('This table lists all the CPs in the system')
cpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cpEntry.setStatus('current')
if mibBuilder.loadTexts: cpEntry.setDescription('An entry represents a single CP in the system')
cpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("active", 3), ("standby", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpStatus.setStatus('current')
if mibBuilder.loadTexts: cpStatus.setDescription('Gives the current status of the CP')
cpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpIpAddress.setStatus('current')
if mibBuilder.loadTexts: cpIpAddress.setDescription('The IP Address of the Ethernet interface of this CP.')
cpIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpIpMask.setStatus('current')
if mibBuilder.loadTexts: cpIpMask.setDescription('The IP Mask of the Ethernet interface of this CP.')
cpIpGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpIpGateway.setStatus('current')
if mibBuilder.loadTexts: cpIpGateway.setDescription('The IP Address of the IP Gateway for this CP.')
cpLastEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("haSync", 3), ("haOutSync", 4), ("cpFaulty", 5), ("cpHealthy", 6), ("cpActive", 7), ("configChange", 8), ("failOverStart", 9), ("failOverDone", 10), ("firmwareCommit", 11), ("firmwareUpgrade", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpLastEvent.setStatus('current')
if mibBuilder.loadTexts: cpLastEvent.setDescription('The last event related to this CP')
bpTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8), )
if mibBuilder.loadTexts: bpTable.setStatus('current')
if mibBuilder.loadTexts: bpTable.setDescription('The table of blade processor entries.')
bpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: bpEntry.setStatus('current')
if mibBuilder.loadTexts: bpEntry.setDescription('An entry of the blade processor information.')
bpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3), ("unknow", 4), ("others", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpStatus.setStatus('current')
if mibBuilder.loadTexts: bpStatus.setDescription('This object identifies the Blade Processor Status.')
bpeth0IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpeth0IpAddress.setStatus('current')
if mibBuilder.loadTexts: bpeth0IpAddress.setDescription('The IP Address of the Ethernet interface Eth0 of Scimitar blade.')
bpeth1IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpeth1IpAddress.setStatus('current')
if mibBuilder.loadTexts: bpeth1IpAddress.setDescription('The IP Address of the Ethernet interface Eth1 of Scimitar blade.')
bpsubNetMaskIpaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpsubNetMaskIpaddress.setStatus('current')
if mibBuilder.loadTexts: bpsubNetMaskIpaddress.setDescription('The IP Mask of the Ethernet interface of this CP.')
bpIpGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpIpGateway.setStatus('current')
if mibBuilder.loadTexts: bpIpGateway.setDescription('The IP Address of the IP Gateway for this CP.')
bpSasPriVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpSasPriVersion.setStatus('current')
if mibBuilder.loadTexts: bpSasPriVersion.setDescription('The current primary version of the SAS.')
bpSasSecVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 1, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bpSasSecVersion.setStatus('current')
if mibBuilder.loadTexts: bpSasSecVersion.setDescription('The current Secondary version of the SAS.')
haMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2))
haMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0))
fruStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("HA-MIB", "fruStatus"), ("HA-MIB", "fruClass"), ("HA-MIB", "fruObjectNum"))
if mibBuilder.loadTexts: fruStatusChanged.setStatus('current')
if mibBuilder.loadTexts: fruStatusChanged.setDescription('This trap is sent when status of any FRU object is changed')
cpStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 2)).setObjects(("HA-MIB", "cpStatus"), ("HA-MIB", "cpLastEvent"), ("SW-MIB", "swID"), ("SW-MIB", "swSsn"))
if mibBuilder.loadTexts: cpStatusChanged.setStatus('current')
if mibBuilder.loadTexts: cpStatusChanged.setDescription('This trap is sent when status of any CP object is changed')
fruHistoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 2, 2, 0, 3)).setObjects(("HA-MIB", "fruHistoryClass"), ("HA-MIB", "fruHistoryObjectNum"), ("HA-MIB", "fruHistoryEvent"), ("HA-MIB", "fruHistoryTime"), ("HA-MIB", "fruHistoryFactoryPartNum"), ("HA-MIB", "fruHistoryFactorySerialNum"))
if mibBuilder.loadTexts: fruHistoryTrap.setStatus('current')
if mibBuilder.loadTexts: fruHistoryTrap.setDescription('This trap is sent when a FRU is added or removed')
mibBuilder.exportSymbols("HA-MIB", bpStatus=bpStatus, fruClass=fruClass, haStatus=haStatus, bpeth1IpAddress=bpeth1IpAddress, bpSasPriVersion=bpSasPriVersion, fruHistoryClass=fruHistoryClass, bpeth0IpAddress=bpeth0IpAddress, fruSupplierId=fruSupplierId, bpsubNetMaskIpaddress=bpsubNetMaskIpaddress, fRUEntry=fRUEntry, cpStatus=cpStatus, bpEntry=bpEntry, fruPowerConsumption=fruPowerConsumption, cpIpGateway=cpIpGateway, fruSupplierSerialNum=fruSupplierSerialNum, bpSasSecVersion=bpSasSecVersion, fruHistoryObjectNum=fruHistoryObjectNum, bpTable=bpTable, cpLastEvent=cpLastEvent, haMIBTrapPrefix=haMIBTrapPrefix, cpIpAddress=cpIpAddress, fruHistoryFactorySerialNum=fruHistoryFactorySerialNum, cpEntry=cpEntry, fruHistoryTime=fruHistoryTime, cpStatusChanged=cpStatusChanged, fruStatusChanged=fruStatusChanged, fruTable=fruTable, PYSNMP_MODULE_ID=haMIB, FruClass=FruClass, cpTable=cpTable, fruStatus=fruStatus, fruSupplierRevCode=fruSupplierRevCode, highAvailability=highAvailability, fruHistoryTrap=fruHistoryTrap, fruObjectNum=fruObjectNum, cpIpMask=cpIpMask, bpIpGateway=bpIpGateway, haMIB=haMIB, fruHistoryTable=fruHistoryTable, fruHistoryFactoryPartNum=fruHistoryFactoryPartNum, haMIBTraps=haMIBTraps, fruHistoryIndex=fruHistoryIndex, fruHistoryEvent=fruHistoryEvent, fruHistoryEntry=fruHistoryEntry, fruSupplierPartNum=fruSupplierPartNum)
