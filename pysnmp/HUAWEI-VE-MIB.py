#
# PySNMP MIB module HUAWEI-VE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Gauge32, Integer32, IpAddress, TimeTicks, Bits, iso, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "Integer32", "IpAddress", "TimeTicks", "Bits", "iso", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hwVe = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146))
if mibBuilder.loadTexts: hwVe.setLastUpdated('200611221414Z')
if mibBuilder.loadTexts: hwVe.setOrganization('Huawei Technologies Co.,Ltd.')
hwVirtualEthernetMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1))
hwVirtualEthernetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1), )
if mibBuilder.loadTexts: hwVirtualEthernetTable.setStatus('current')
hwVirtualEthernetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VE-MIB", "hwVirtualEthernetGroupId"))
if mibBuilder.loadTexts: hwVirtualEthernetEntry.setStatus('current')
hwVirtualEthernetGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwVirtualEthernetGroupId.setStatus('current')
hwL2VirtualEthernetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 11), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwL2VirtualEthernetName.setStatus('current')
hwL3VirtualEthernetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 12), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwL3VirtualEthernetName.setStatus('current')
hwVirtualEthernetGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVirtualEthernetGroupRowStatus.setStatus('current')
hwVirtualEthernetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2))
hwVirtualEthernetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 2))
hwVirtualEthernetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 2, 1)).setObjects(("HUAWEI-VE-MIB", "hwVirtualEthernetObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVirtualEthernetCompliance = hwVirtualEthernetCompliance.setStatus('current')
hwVirtualEthernetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 1))
hwVirtualEthernetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 1, 1)).setObjects(("HUAWEI-VE-MIB", "hwL2VirtualEthernetName"), ("HUAWEI-VE-MIB", "hwL3VirtualEthernetName"), ("HUAWEI-VE-MIB", "hwVirtualEthernetGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVirtualEthernetObjectGroup = hwVirtualEthernetObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-VE-MIB", hwVirtualEthernetCompliance=hwVirtualEthernetCompliance, PYSNMP_MODULE_ID=hwVe, hwVirtualEthernetGroupId=hwVirtualEthernetGroupId, hwL2VirtualEthernetName=hwL2VirtualEthernetName, hwL3VirtualEthernetName=hwL3VirtualEthernetName, hwVirtualEthernetConformance=hwVirtualEthernetConformance, hwVirtualEthernetGroupRowStatus=hwVirtualEthernetGroupRowStatus, hwVirtualEthernetMibObjects=hwVirtualEthernetMibObjects, hwVirtualEthernetEntry=hwVirtualEthernetEntry, hwVirtualEthernetGroups=hwVirtualEthernetGroups, hwVirtualEthernetCompliances=hwVirtualEthernetCompliances, hwVe=hwVe, hwVirtualEthernetObjectGroup=hwVirtualEthernetObjectGroup, hwVirtualEthernetTable=hwVirtualEthernetTable)
