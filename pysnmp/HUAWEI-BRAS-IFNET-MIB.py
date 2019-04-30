#
# PySNMP MIB module HUAWEI-BRAS-IFNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-IFNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, NotificationType, ModuleIdentity, ObjectIdentity, IpAddress, iso, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "NotificationType", "ModuleIdentity", "ObjectIdentity", "IpAddress", "iso", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Bits", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwSUBINT = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11))
if mibBuilder.loadTexts: hwSUBINT.setLastUpdated('200508101200Z')
if mibBuilder.loadTexts: hwSUBINT.setOrganization('HAUWEI MIB Standard community ')
hwhwSUBINTMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1))
hwSubIntTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1), )
if mibBuilder.loadTexts: hwSubIntTable.setStatus('current')
hwSubIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HUAWEI-BRAS-IFNET-MIB", "hwSubInterfaceNo"))
if mibBuilder.loadTexts: hwSubIntEntry.setStatus('current')
hwSubInterfaceNo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSubInterfaceNo.setStatus('current')
hwSubIntRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSubIntRowStatus.setStatus('current')
hwSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSubIfIndex.setStatus('current')
hwSubIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSubIfDescr.setStatus('current')
hwSubIntConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2))
hwSubIntCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 1))
hwSubIntCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 1, 1)).setObjects(("HUAWEI-BRAS-IFNET-MIB", "hwSubIntTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSubIntCompliance = hwSubIntCompliance.setStatus('current')
hwSubIntTableGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 2))
hwSubIntTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 2, 1)).setObjects(("HUAWEI-BRAS-IFNET-MIB", "hwSubInterfaceNo"), ("HUAWEI-BRAS-IFNET-MIB", "hwSubIntRowStatus"), ("HUAWEI-BRAS-IFNET-MIB", "hwSubIfIndex"), ("HUAWEI-BRAS-IFNET-MIB", "hwSubIfDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSubIntTableGroup = hwSubIntTableGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-IFNET-MIB", PYSNMP_MODULE_ID=hwSUBINT, hwSubIntEntry=hwSubIntEntry, hwSubIntCompliance=hwSubIntCompliance, hwSubIfDescr=hwSubIfDescr, hwSubIntTable=hwSubIntTable, hwSubIntRowStatus=hwSubIntRowStatus, hwSubIntConformance=hwSubIntConformance, hwSUBINT=hwSUBINT, hwSubIntTableGroups=hwSubIntTableGroups, hwSubInterfaceNo=hwSubInterfaceNo, hwSubIntCompliances=hwSubIntCompliances, hwhwSUBINTMibObjects=hwhwSUBINTMibObjects, hwSubIfIndex=hwSubIfIndex, hwSubIntTableGroup=hwSubIntTableGroup)
