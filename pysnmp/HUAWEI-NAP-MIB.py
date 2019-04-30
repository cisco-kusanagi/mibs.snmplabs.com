#
# PySNMP MIB module HUAWEI-NAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Bits, Counter32, MibIdentifier, TimeTicks, iso, Counter64, Integer32, ModuleIdentity, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TextualConvention, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "iso", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TextualConvention", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwNap = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206))
hwNap.setRevisions(('2009-03-17 10:27',))
if mibBuilder.loadTexts: hwNap.setLastUpdated('200903171027Z')
if mibBuilder.loadTexts: hwNap.setOrganization('Huawei Technologies Co.,Ltd.')
class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
hwNapScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1))
hwNapTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2))
hwNapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3))
hwNapNeighborNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborNum.setStatus('current')
hwNapNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1), )
if mibBuilder.loadTexts: hwNapNeighborTable.setStatus('current')
hwNapNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1), ).setIndexNames((0, "HUAWEI-NAP-MIB", "hwNapNeighborIndex"))
if mibBuilder.loadTexts: hwNapNeighborEntry.setStatus('current')
hwNapNeighborIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborIndex.setStatus('current')
hwNapLocalPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapLocalPortName.setStatus('current')
hwNapNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("detecting", 1), ("established", 2), ("ipAssigned", 3), ("abnormal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborStatus.setStatus('current')
hwNapNeighborAbnormalReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 0), ("portNotSupport", 1), ("slaveDisable", 2), ("masterIpAssignError", 3), ("slaveIpAssignError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborAbnormalReason.setStatus('current')
hwNapStatusNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3, 1)).setObjects(("HUAWEI-NAP-MIB", "hwNapLocalPortName"), ("HUAWEI-NAP-MIB", "hwNapNeighborStatus"), ("HUAWEI-NAP-MIB", "hwNapNeighborAbnormalReason"))
if mibBuilder.loadTexts: hwNapStatusNotify.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-NAP-MIB", hwNapNotifications=hwNapNotifications, hwNapLocalPortName=hwNapLocalPortName, hwNapNeighborTable=hwNapNeighborTable, hwNapNeighborIndex=hwNapNeighborIndex, PYSNMP_MODULE_ID=hwNap, hwNapScalarObjects=hwNapScalarObjects, hwNap=hwNap, hwNapNeighborEntry=hwNapNeighborEntry, hwNapNeighborStatus=hwNapNeighborStatus, hwNapNeighborNum=hwNapNeighborNum, hwNapNeighborAbnormalReason=hwNapNeighborAbnormalReason, hwNapTableObjects=hwNapTableObjects, DateAndTime=DateAndTime, hwNapStatusNotify=hwNapStatusNotify)
