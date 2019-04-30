#
# PySNMP MIB module HUAWEI-BRAS-VT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-VT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter32, Bits, NotificationType, ModuleIdentity, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter32", "Bits", "NotificationType", "ModuleIdentity", "IpAddress", "Unsigned32", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwIFVT = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10))
if mibBuilder.loadTexts: hwIFVT.setLastUpdated('200508101200Z')
if mibBuilder.loadTexts: hwIFVT.setOrganization('HAUWEI MIB Standard community ')
hwhwIFVTMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1))
hwIFVTTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1), )
if mibBuilder.loadTexts: hwIFVTTable.setStatus('current')
hwIFVTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1), ).setIndexNames((0, "HUAWEI-BRAS-VT-MIB", "hwifVTNo"))
if mibBuilder.loadTexts: hwIFVTEntry.setStatus('current')
hwifVTNo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifVTNo.setStatus('current')
hwifVTDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifVTDescr.setStatus('current')
hwifVTMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 1500)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifVTMtu.setStatus('current')
hwifVTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifVTRowStatus.setStatus('current')
hwIfVtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2))
hwIfVtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 1))
hwIfVtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 1, 1)).setObjects(("HUAWEI-BRAS-VT-MIB", "hwIfVtTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIfVtCompliance = hwIfVtCompliance.setStatus('current')
hwIfVtObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 2))
hwIfVtTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 2, 1)).setObjects(("HUAWEI-BRAS-VT-MIB", "hwifVTNo"), ("HUAWEI-BRAS-VT-MIB", "hwifVTDescr"), ("HUAWEI-BRAS-VT-MIB", "hwifVTMtu"), ("HUAWEI-BRAS-VT-MIB", "hwifVTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIfVtTableGroup = hwIfVtTableGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-VT-MIB", hwIfVtTableGroup=hwIfVtTableGroup, hwifVTRowStatus=hwifVTRowStatus, hwIfVtObjectGroups=hwIfVtObjectGroups, hwIfVtCompliance=hwIfVtCompliance, hwhwIFVTMibObjects=hwhwIFVTMibObjects, hwIfVtConformance=hwIfVtConformance, hwIFVTEntry=hwIFVTEntry, hwIFVTTable=hwIFVTTable, PYSNMP_MODULE_ID=hwIFVT, hwIfVtCompliances=hwIfVtCompliances, hwifVTMtu=hwifVTMtu, hwifVTDescr=hwifVTDescr, hwIFVT=hwIFVT, hwifVTNo=hwifVTNo)
