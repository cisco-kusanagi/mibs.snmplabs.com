#
# PySNMP MIB module MARVELL-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-SPAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rnd, rndNotifications = mibBuilder.importSymbols("RADLAN-MIB", "rnd", "rndNotifications")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, Bits, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Integer32, Counter64, iso, Gauge32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Bits", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Integer32", "Counter64", "iso", "Gauge32", "MibIdentifier", "NotificationType")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
class SpanDestinationPortType(TextualConvention, Integer32):
    description = 'SPAN destination mode type: 1 - monitor-only 2 - network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

class SpanSourceType(TextualConvention, Integer32):
    description = 'SPAN source type: 1 - port 2 - VLAN 3 - flow 4 - remote VLAN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("flow", 3), ("remote-vlan", 4))

class SpanSourceDirection(TextualConvention, Integer32):
    description = 'SPAN source direction: 1 - rx 2 - tx 3 - both.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpan.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('201503250000Z')
if mibBuilder.loadTexts: rlSpan.setOrganization('Marvell Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSpan.setContactInfo('marvell.com')
if mibBuilder.loadTexts: rlSpan.setDescription('This private MIB module for SPAN (Switched Port Analyzer).')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSpanMibVersion.setDescription("MIB's version, the current version is 1.")
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 2), )
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationTable.setDescription('The table holds information for SPAN destination per session id.')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 2, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationEntry.setDescription('Entry in the rlSpanDestinationTable.')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setDescription('SPAN session ID. This variable is the key for SPAN destination table. Uniquely identifies the SPAN destination.')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setDescription('Interface Index. This variable identifies the destination ifIndex')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setDescription('This variable indicates whether the current session is RSPAN (true) or SPAN (flase).')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationPortType.setDescription('This variable indicates whether the destination port acts as network port or analyzer only port.')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 2, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 219, 3), )
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceTable.setDescription('The table holds information for SPAN Source ports per session id.')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 219, 3, 1), ).setIndexNames((0, "MARVELL-SPAN-MIB", "rlSpanSourceSessionId"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceType"), (0, "MARVELL-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceEntry.setDescription('Entry in the rlSpanSourceTable.')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceSessionId.setDescription('SPAN session ID. This variable is the key for SPAN source table. Identifies the SPAN source.')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 2), SpanSourceType())
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceType.setDescription('This variable indicates the SPAN source type.')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceIndex.setDescription('This variable indicates the ifIndex of the SPAN source port or the flow Id of the class map (for flow span source type).')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceDirection.setDescription('This variable indicates the source direction for monitoring.')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
mibBuilder.exportSymbols("MARVELL-SPAN-MIB", PYSNMP_MODULE_ID=rlSpan, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex, SpanDestinationPortType=SpanDestinationPortType, rlSpanDestinationTable=rlSpanDestinationTable, rlSpanDestinationPortType=rlSpanDestinationPortType, rlSpanSourceType=rlSpanSourceType, rlSpanSourceDirection=rlSpanSourceDirection, rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, rlSpanSourceEntry=rlSpanSourceEntry, rlSpanSourceRowStatus=rlSpanSourceRowStatus, rlSpan=rlSpan, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, rlSpanSourceSessionId=rlSpanSourceSessionId, SpanSourceDirection=SpanSourceDirection, rlSpanDestinationEntry=rlSpanDestinationEntry, rlSpanMibVersion=rlSpanMibVersion, rlSpanSourceTable=rlSpanSourceTable, SpanSourceType=SpanSourceType)
