#
# PySNMP MIB module HH3C-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswMAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hh3cdot1qVlanIndex, = mibBuilder.importSymbols("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, Counter64, TimeTicks, MibIdentifier, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "TimeTicks", "MibIdentifier", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
hh3cLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3))
hh3cLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hh3cLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswMacPort.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hh3cdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1), )
if mibBuilder.loadTexts: hh3cdot1qMacSearchTable.setStatus('current')
hh3cdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1), ).setIndexNames((0, "HH3C-LswMAM-MIB", "hh3cdot1qMacSearchAddress"), (0, "HH3C-LswMAM-MIB", "hh3cdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hh3cdot1qMacSearchEntry.setStatus('current')
hh3cdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qMacSearchAddress.setStatus('current')
hh3cdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qMacSearchVlanID.setStatus('current')
hh3cdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qMacSearchPort.setStatus('current')
hh3cdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qMacSearchAgeTime.setStatus('current')
hh3cdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2), )
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetTable.setStatus('current')
hh3cdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"), (0, "HH3C-LswMAM-MIB", "hh3cdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetEntry.setStatus('current')
hh3cdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetAddress.setStatus('current')
hh3cdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetPort.setStatus('current')
hh3cdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetStatus.setStatus('current')
hh3cdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbSetOperate.setStatus('current')
hh3cdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3), )
if mibBuilder.loadTexts: hh3cdot1qTpFdbGroupSetTable.setStatus('current')
hh3cdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1), ).setIndexNames((0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"), (0, "HH3C-LswMAM-MIB", "hh3cdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hh3cdot1qTpFdbGroupSetEntry.setStatus('current')
hh3cdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cdot1qTpFdbGroupSetAddress.setStatus('current')
hh3cdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbGroupSetPort.setStatus('current')
hh3cdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("HH3C-LswMAM-MIB", hh3cdot1qTpFdbSetStatus=hh3cdot1qTpFdbSetStatus, hh3cdot1qTpFdbSetTable=hh3cdot1qTpFdbSetTable, hh3cdot1qTpFdbGroupSetOperate=hh3cdot1qTpFdbGroupSetOperate, hh3cdot1qTpFdbGroupSetPort=hh3cdot1qTpFdbGroupSetPort, InterfaceIndex=InterfaceIndex, hh3cdot1qTpFdbSetAddress=hh3cdot1qTpFdbSetAddress, hh3cdot1qTpFdbSetOperate=hh3cdot1qTpFdbSetOperate, PortList=PortList, hh3cdot1qTpFdbSetPort=hh3cdot1qTpFdbSetPort, hh3cdot1qMacSearchPort=hh3cdot1qMacSearchPort, hh3cdot1qTpFdbGroupSetAddress=hh3cdot1qTpFdbGroupSetAddress, hh3cdot1qMacSearchAgeTime=hh3cdot1qMacSearchAgeTime, PYSNMP_MODULE_ID=hh3cLswMacPort, hh3cdot1qMacSearchAddress=hh3cdot1qMacSearchAddress, hh3cdot1qMacSearchEntry=hh3cdot1qMacSearchEntry, hh3cdot1qTpFdbSetEntry=hh3cdot1qTpFdbSetEntry, hh3cdot1qMacSearchVlanID=hh3cdot1qMacSearchVlanID, hh3cdot1qMacSearchTable=hh3cdot1qMacSearchTable, hh3cLswMacPort=hh3cLswMacPort, hh3cdot1qTpFdbGroupSetEntry=hh3cdot1qTpFdbGroupSetEntry, hh3cdot1qTpFdbGroupSetTable=hh3cdot1qTpFdbGroupSetTable)
