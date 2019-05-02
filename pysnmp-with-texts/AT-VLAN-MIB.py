#
# PySNMP MIB module AT-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, NotificationType, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Counter32, MibIdentifier, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "Bits")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
atVlanInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16))
atVlanInfo.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2009-06-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atVlanInfo.setRevisionsDescriptions(('Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: atVlanInfo.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: atVlanInfo.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: atVlanInfo.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atVlanInfo.setDescription('The VLAN MIB, for retrieving VLAN specific system data.')
atVlanStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1))
atVlanStatNumCollections = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatNumCollections.setStatus('current')
if mibBuilder.loadTexts: atVlanStatNumCollections.setDescription('The number of unique VLAN statistic gathering instances defined on the device.')
atVlanStatCollectionTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2), )
if mibBuilder.loadTexts: atVlanStatCollectionTable.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionTable.setDescription('A table of VLAN statistic instances.')
atVlanStatCollectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1), ).setIndexNames((0, "AT-VLAN-MIB", "atVlanStatCollectionName"))
if mibBuilder.loadTexts: atVlanStatCollectionEntry.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionEntry.setDescription('Each entry represents a unique VLAN statistic gathering instance defined on the device.')
atVlanStatCollectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatCollectionName.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionName.setDescription('The name of a VLAN statistics collection instance.')
atVlanStatCollectionVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatCollectionVlanId.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionVlanId.setDescription('The VLAN ID of ingress packets being monitored by this VLAN statistics collection instance.')
atVlanStatCollectionPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatCollectionPortMap.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionPortMap.setDescription("A bitwise port map indicating the switch ports being monitored by this VLAN statistics collection instance. The bit position within the string, maps to the port with the same index in dot1dBasePortTable in BRIDGE-MIB. A binary '1' indicates that the port is being monitored by this VLAN statistics collection instance, with a '0' indicating that it is not.")
atVlanStatCollectionIngressPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatCollectionIngressPkts.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionIngressPkts.setDescription('The number of ingress packets received and counted by this VLAN statistics collection instance.')
atVlanStatCollectionIngressOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atVlanStatCollectionIngressOctets.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionIngressOctets.setDescription('The number of octets of data received from ingress packets counted by this VLAN statistics collection instance.')
atVlanStatCollectionResetStats = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atVlanStatCollectionResetStats.setStatus('current')
if mibBuilder.loadTexts: atVlanStatCollectionResetStats.setDescription("When read, this object will always return 2 (false). Setting its value to 1 (true) will cause the matching VLAN statistics collection instance's ingress packets and ingress octet values to be reset to zero.")
mibBuilder.exportSymbols("AT-VLAN-MIB", atVlanStatCollectionIngressOctets=atVlanStatCollectionIngressOctets, atVlanStatCollectionIngressPkts=atVlanStatCollectionIngressPkts, PYSNMP_MODULE_ID=atVlanInfo, atVlanStatCollectionPortMap=atVlanStatCollectionPortMap, atVlanStatCollectionName=atVlanStatCollectionName, atVlanInfo=atVlanInfo, atVlanStatNumCollections=atVlanStatNumCollections, atVlanStatCollectionResetStats=atVlanStatCollectionResetStats, atVlanStatCollectionTable=atVlanStatCollectionTable, atVlanStatCollectionEntry=atVlanStatCollectionEntry, atVlanStatCollectionVlanId=atVlanStatCollectionVlanId, atVlanStatistics=atVlanStatistics)
