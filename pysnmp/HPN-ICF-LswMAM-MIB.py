#
# PySNMP MIB module HPN-ICF-LswMAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswMAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfdot1qVlanIndex, = mibBuilder.importSymbols("HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, NotificationType, iso, Counter32, Gauge32, Bits, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Counter32", "Gauge32", "Bits", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Counter64", "Integer32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
hpnicfLswMacPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3))
hpnicfLswMacPort.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hpnicfLswMacPort.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswMacPort.setOrganization('')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PortList(TextualConvention, OctetString):
    status = 'current'

hpnicfdot1qMacSearchTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1), )
if mibBuilder.loadTexts: hpnicfdot1qMacSearchTable.setStatus('current')
hpnicfdot1qMacSearchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchAddress"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchVlanID"))
if mibBuilder.loadTexts: hpnicfdot1qMacSearchEntry.setStatus('current')
hpnicfdot1qMacSearchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchAddress.setStatus('current')
hpnicfdot1qMacSearchVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4096), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchVlanID.setStatus('current')
hpnicfdot1qMacSearchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchPort.setStatus('current')
hpnicfdot1qMacSearchAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1qMacSearchAgeTime.setStatus('current')
hpnicfdot1qTpFdbSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2), )
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetTable.setStatus('current')
hpnicfdot1qTpFdbSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbSetAddress"))
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetEntry.setStatus('current')
hpnicfdot1qTpFdbSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetAddress.setStatus('current')
hpnicfdot1qTpFdbSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetPort.setStatus('current')
hpnicfdot1qTpFdbSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 6, 7, 9, 11))).clone(namedValues=NamedValues(("other", 1), ("learned", 3), ("static", 6), ("dynamic", 7), ("blackhole", 9), ("security", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetStatus.setStatus('current')
hpnicfdot1qTpFdbSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbSetOperate.setStatus('current')
hpnicfdot1qTpFdbGroupSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3), )
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetTable.setStatus('current')
hpnicfdot1qTpFdbGroupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1), ).setIndexNames((0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"), (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbGroupSetAddress"))
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetEntry.setStatus('current')
hpnicfdot1qTpFdbGroupSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetAddress.setStatus('current')
hpnicfdot1qTpFdbGroupSetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetPort.setStatus('current')
hpnicfdot1qTpFdbGroupSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1qTpFdbGroupSetOperate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LswMAM-MIB", hpnicfdot1qTpFdbSetStatus=hpnicfdot1qTpFdbSetStatus, hpnicfdot1qTpFdbSetEntry=hpnicfdot1qTpFdbSetEntry, hpnicfdot1qMacSearchAddress=hpnicfdot1qMacSearchAddress, hpnicfdot1qTpFdbSetPort=hpnicfdot1qTpFdbSetPort, hpnicfdot1qTpFdbGroupSetEntry=hpnicfdot1qTpFdbGroupSetEntry, hpnicfdot1qTpFdbSetAddress=hpnicfdot1qTpFdbSetAddress, hpnicfdot1qMacSearchTable=hpnicfdot1qMacSearchTable, hpnicfdot1qMacSearchVlanID=hpnicfdot1qMacSearchVlanID, hpnicfdot1qTpFdbGroupSetOperate=hpnicfdot1qTpFdbGroupSetOperate, hpnicfdot1qTpFdbSetOperate=hpnicfdot1qTpFdbSetOperate, hpnicfdot1qTpFdbGroupSetAddress=hpnicfdot1qTpFdbGroupSetAddress, hpnicfdot1qTpFdbGroupSetPort=hpnicfdot1qTpFdbGroupSetPort, PortList=PortList, hpnicfdot1qMacSearchPort=hpnicfdot1qMacSearchPort, PYSNMP_MODULE_ID=hpnicfLswMacPort, hpnicfLswMacPort=hpnicfLswMacPort, hpnicfdot1qMacSearchAgeTime=hpnicfdot1qMacSearchAgeTime, hpnicfdot1qMacSearchEntry=hpnicfdot1qMacSearchEntry, hpnicfdot1qTpFdbGroupSetTable=hpnicfdot1qTpFdbGroupSetTable, InterfaceIndex=InterfaceIndex, hpnicfdot1qTpFdbSetTable=hpnicfdot1qTpFdbSetTable)
