#
# PySNMP MIB module GERP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GERP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, IpAddress, Bits, ObjectIdentity, Counter32, Counter64, NotificationType, MibIdentifier, TimeTicks, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "IpAddress", "Bits", "ObjectIdentity", "Counter32", "Counter64", "NotificationType", "MibIdentifier", "TimeTicks", "iso", "ModuleIdentity")
TruthValue, RowStatus, DisplayString, TimeInterval, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TimeInterval", "MacAddress", "TextualConvention")
gerpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7))
gerpMib.setRevisions(('1908-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gerpMib.setRevisionsDescriptions(('Draft 1',))
if mibBuilder.loadTexts: gerpMib.setLastUpdated('200804010000Z')
if mibBuilder.loadTexts: gerpMib.setOrganization('Greentech MIB Working Group')
if mibBuilder.loadTexts: gerpMib.setContactInfo('Email: adama@observium.org')
if mibBuilder.loadTexts: gerpMib.setDescription(' The gerp MIB is targeted at easing gerp configuration via snmp tools.')
gerpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1))
gerp = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1))
gerpOnoff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpOnoff.setStatus('current')
if mibBuilder.loadTexts: gerpOnoff.setDescription('Enable/disable gerp function for this bridge.')
gerpHealthTime = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpHealthTime.setStatus('current')
if mibBuilder.loadTexts: gerpHealthTime.setDescription('The hello timer is used by master or edge node for ring health detection. The correct operational formula: FailedTimer >= 3 * HelloTimer ')
gerpHealthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpHealthTimeout.setStatus('current')
if mibBuilder.loadTexts: gerpHealthTimeout.setDescription('The timeout value used by master during ring health detection. The correct operational formula: FailedTimer >= 3 * HelloTimer')
gerpMajorFaultTime = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gerpMajorFaultTime.setStatus('current')
if mibBuilder.loadTexts: gerpMajorFaultTime.setDescription('The timeout value used by assitant edge during ring health detection.')
gerpPrefwdTimeout = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gerpPrefwdTimeout.setStatus('current')
if mibBuilder.loadTexts: gerpPrefwdTimeout.setDescription('The block timeout value used by node when portup event occurs.')
gerpDomainTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6), )
if mibBuilder.loadTexts: gerpDomainTable.setStatus('current')
if mibBuilder.loadTexts: gerpDomainTable.setDescription('A table that contains domain-specific information.')
gerpDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1), ).setIndexNames((0, "GERP-MIB", "gerpDomainId"))
if mibBuilder.loadTexts: gerpDomainEntry.setStatus('current')
if mibBuilder.loadTexts: gerpDomainEntry.setDescription('A list of information maintained by every domain.')
gerpDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: gerpDomainId.setStatus('current')
if mibBuilder.loadTexts: gerpDomainId.setDescription('The domain ID is used when network is managed in unit of domain, one domain should be a set of contiguous bridges.')
gerpMVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4093))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpMVlanId.setStatus('current')
if mibBuilder.loadTexts: gerpMVlanId.setDescription('The manage VLAN ID of the domain.')
gerpRingTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7), )
if mibBuilder.loadTexts: gerpRingTable.setStatus('current')
if mibBuilder.loadTexts: gerpRingTable.setDescription('A table that contains domain-and-ring-specific information.')
gerpRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1), ).setIndexNames((0, "GERP-MIB", "gerpDomainId"), (0, "GERP-MIB", "gerpRingId"))
if mibBuilder.loadTexts: gerpRingEntry.setStatus('current')
if mibBuilder.loadTexts: gerpRingEntry.setDescription('A list of information maintained by every ring.')
gerpRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: gerpRingId.setStatus('current')
if mibBuilder.loadTexts: gerpRingId.setDescription('The identifier of ethernet ring which reside in a domain.')
gerpRingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpRingLevel.setStatus('current')
if mibBuilder.loadTexts: gerpRingLevel.setDescription('The ring level,0 means master ring, while 1 means sub ring.')
gerpBrdgRole = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("master", 1), ("trans", 2), ("edge", 3), ("assEdge", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpBrdgRole.setStatus('current')
if mibBuilder.loadTexts: gerpBrdgRole.setDescription('The bridge role in ethernet ring.')
gerpPriComPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpPriComPortId.setStatus('current')
if mibBuilder.loadTexts: gerpPriComPortId.setDescription('The primary port id when bridge is master or transmit,the common port id otherwise.')
gerpSecEdgePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpSecEdgePortId.setStatus('current')
if mibBuilder.loadTexts: gerpSecEdgePortId.setDescription('The secondary port id when bridge is master or transmit,the edge port id otherwise.')
gerpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 7, 1, 1, 7, 1, 6), RowStatus().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gerpRowStatus.setStatus('current')
if mibBuilder.loadTexts: gerpRowStatus.setDescription('This object indicates the status of this ring.')
mibBuilder.exportSymbols("GERP-MIB", PYSNMP_MODULE_ID=gerpMib, gerpDomainTable=gerpDomainTable, gerpMib=gerpMib, gerpRingEntry=gerpRingEntry, gerpPrefwdTimeout=gerpPrefwdTimeout, gerpHealthTime=gerpHealthTime, gerpRingLevel=gerpRingLevel, gerpDomainId=gerpDomainId, gerpHealthTimeout=gerpHealthTimeout, gerpBrdgRole=gerpBrdgRole, gerpMVlanId=gerpMVlanId, gerpPriComPortId=gerpPriComPortId, gerpMIBObjects=gerpMIBObjects, gerpMajorFaultTime=gerpMajorFaultTime, gerpRingTable=gerpRingTable, gerpDomainEntry=gerpDomainEntry, gerpSecEdgePortId=gerpSecEdgePortId, gerp=gerp, gerpRingId=gerpRingId, gerpOnoff=gerpOnoff, gerpRowStatus=gerpRowStatus)
