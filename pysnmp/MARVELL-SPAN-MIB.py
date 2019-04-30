#
# PySNMP MIB module MARVELL-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-SPAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rndNotifications, rnd = mibBuilder.importSymbols("RADLAN-MIB", "rndNotifications", "rnd")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, IpAddress, Gauge32, ModuleIdentity, Integer32, iso, Bits, TimeTicks, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "Integer32", "iso", "Bits", "TimeTicks", "MibIdentifier", "Counter64")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
class SpanDestinationPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

class SpanSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("flow", 3), ("remote-vlan", 4))

class SpanSourceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('201503250000Z')
if mibBuilder.loadTexts: rlSpan.setOrganization('Marvell Computer Communications Ltd.')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 2), )
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 2, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 3), )
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 3, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanSourceSessionId"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceType"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 2), SpanSourceType())
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
mibBuilder.exportSymbols("MARVELL-SPAN-MIB", SpanSourceType=SpanSourceType, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpan=rlSpan, rlSpanSourceSessionId=rlSpanSourceSessionId, rlSpanMibVersion=rlSpanMibVersion, rlSpanSourceRowStatus=rlSpanSourceRowStatus, PYSNMP_MODULE_ID=rlSpan, rlSpanSourceType=rlSpanSourceType, rlSpanDestinationEntry=rlSpanDestinationEntry, rlSpanSourceDirection=rlSpanSourceDirection, rlSpanSourceEntry=rlSpanSourceEntry, rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, rlSpanSourceTable=rlSpanSourceTable, rlSpanDestinationTable=rlSpanDestinationTable, SpanSourceDirection=SpanSourceDirection, SpanDestinationPortType=SpanDestinationPortType, rlSpanDestinationPortType=rlSpanDestinationPortType, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex)
