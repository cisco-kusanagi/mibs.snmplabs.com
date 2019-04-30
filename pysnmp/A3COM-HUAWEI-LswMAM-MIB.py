#
# PySNMP MIB module A3COM-HUAWEI-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LswMAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
hwdot1qVlanIndex, = mibBuilder.importSymbols("A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
lswCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "lswCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter32, Gauge32, ModuleIdentity, Integer32, iso, ObjectIdentity, NotificationType, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "iso", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
hwLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3))
hwLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswMacPort.setOrganization(' ')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hwdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1), )
if mibBuilder.loadTexts: hwdot1qMacSearchTable.setStatus('current')
hwdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchAddress"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hwdot1qMacSearchEntry.setStatus('current')
hwdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAddress.setStatus('current')
hwdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchVlanID.setStatus('current')
hwdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchPort.setStatus('current')
hwdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAgeTime.setStatus('current')
hwdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2), )
if mibBuilder.loadTexts: hwdot1qTpFdbSetTable.setStatus('current')
hwdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbSetEntry.setStatus('current')
hwdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbSetAddress.setStatus('current')
hwdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetPort.setStatus('current')
hwdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetStatus.setStatus('current')
hwdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetOperate.setStatus('current')
hwdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3), )
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetTable.setStatus('current')
hwdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetEntry.setStatus('current')
hwdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetAddress.setStatus('current')
hwdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetPort.setStatus('current')
hwdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswMAM-MIB", hwdot1qTpFdbSetPort=hwdot1qTpFdbSetPort, hwdot1qMacSearchAgeTime=hwdot1qMacSearchAgeTime, InterfaceIndex=InterfaceIndex, hwdot1qTpFdbGroupSetOperate=hwdot1qTpFdbGroupSetOperate, hwdot1qTpFdbSetOperate=hwdot1qTpFdbSetOperate, hwdot1qMacSearchAddress=hwdot1qMacSearchAddress, hwdot1qTpFdbGroupSetAddress=hwdot1qTpFdbGroupSetAddress, PortList=PortList, hwdot1qMacSearchVlanID=hwdot1qMacSearchVlanID, hwdot1qTpFdbSetTable=hwdot1qTpFdbSetTable, hwdot1qMacSearchPort=hwdot1qMacSearchPort, hwdot1qTpFdbSetStatus=hwdot1qTpFdbSetStatus, hwLswMacPort=hwLswMacPort, PYSNMP_MODULE_ID=hwLswMacPort, hwdot1qTpFdbSetEntry=hwdot1qTpFdbSetEntry, hwdot1qTpFdbSetAddress=hwdot1qTpFdbSetAddress, hwdot1qMacSearchTable=hwdot1qMacSearchTable, hwdot1qTpFdbGroupSetPort=hwdot1qTpFdbGroupSetPort, hwdot1qMacSearchEntry=hwdot1qMacSearchEntry, hwdot1qTpFdbGroupSetTable=hwdot1qTpFdbGroupSetTable, hwdot1qTpFdbGroupSetEntry=hwdot1qTpFdbGroupSetEntry)
