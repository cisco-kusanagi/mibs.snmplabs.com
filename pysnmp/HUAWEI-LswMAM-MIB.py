#
# PySNMP MIB module HUAWEI-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswMAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
hwdot1qVlanIndex, = mibBuilder.importSymbols("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Bits, TimeTicks, Gauge32, Counter64, ModuleIdentity, Unsigned32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "TimeTicks", "Gauge32", "Counter64", "ModuleIdentity", "Unsigned32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
hwLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3))
hwLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswMacPort.setOrganization(' ')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hwdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1), )
if mibBuilder.loadTexts: hwdot1qMacSearchTable.setStatus('current')
hwdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1), ).setIndexNames((0, "HUAWEI-LswMAM-MIB", "hwdot1qMacSearchAddress"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hwdot1qMacSearchEntry.setStatus('current')
hwdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAddress.setStatus('current')
hwdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchVlanID.setStatus('current')
hwdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchPort.setStatus('current')
hwdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qMacSearchAgeTime.setStatus('current')
hwdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2), )
if mibBuilder.loadTexts: hwdot1qTpFdbSetTable.setStatus('current')
hwdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbSetEntry.setStatus('current')
hwdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbSetAddress.setStatus('current')
hwdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetPort.setStatus('current')
hwdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetStatus.setStatus('current')
hwdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbSetOperate.setStatus('current')
hwdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3), )
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetTable.setStatus('current')
hwdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"), (0, "HUAWEI-LswMAM-MIB", "hwdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetEntry.setStatus('current')
hwdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetAddress.setStatus('current')
hwdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetPort.setStatus('current')
hwdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LswMAM-MIB", hwLswMacPort=hwLswMacPort, hwdot1qMacSearchVlanID=hwdot1qMacSearchVlanID, hwdot1qTpFdbGroupSetAddress=hwdot1qTpFdbGroupSetAddress, hwdot1qTpFdbSetEntry=hwdot1qTpFdbSetEntry, hwdot1qTpFdbSetAddress=hwdot1qTpFdbSetAddress, hwdot1qMacSearchAgeTime=hwdot1qMacSearchAgeTime, InterfaceIndex=InterfaceIndex, hwdot1qTpFdbSetTable=hwdot1qTpFdbSetTable, PYSNMP_MODULE_ID=hwLswMacPort, hwdot1qTpFdbSetStatus=hwdot1qTpFdbSetStatus, hwdot1qTpFdbGroupSetEntry=hwdot1qTpFdbGroupSetEntry, hwdot1qTpFdbSetOperate=hwdot1qTpFdbSetOperate, PortList=PortList, hwdot1qTpFdbGroupSetPort=hwdot1qTpFdbGroupSetPort, hwdot1qTpFdbGroupSetOperate=hwdot1qTpFdbGroupSetOperate, hwdot1qMacSearchPort=hwdot1qMacSearchPort, hwdot1qTpFdbSetPort=hwdot1qTpFdbSetPort, hwdot1qMacSearchTable=hwdot1qMacSearchTable, hwdot1qMacSearchEntry=hwdot1qMacSearchEntry, hwdot1qTpFdbGroupSetTable=hwdot1qTpFdbGroupSetTable, hwdot1qMacSearchAddress=hwdot1qMacSearchAddress)
