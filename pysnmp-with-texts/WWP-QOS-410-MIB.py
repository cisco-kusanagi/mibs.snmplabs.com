#
# PySNMP MIB module WWP-QOS-410-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-QOS-410-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, ObjectIdentity, TimeTicks, Gauge32, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, iso, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "iso", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpQos410MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 29))
wwpQos410MIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpQos410MIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpQos410MIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpQos410MIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpQos410MIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpQos410MIB.setDescription('The MIB module for the WWP QOS specific information.')
class VlanId(TextualConvention, Integer32):
    description = 'A 12-bit VLAN ID used in the VLAN Tag header.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpQos410MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1))
wwpQos410 = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1))
wwpQos410NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2))
wwpQos410Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0))
wwpQos410MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3))
wwpQos410MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 1))
wwpQos410MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 2))
wwpQos410Table = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1), )
if mibBuilder.loadTexts: wwpQos410Table.setStatus('current')
if mibBuilder.loadTexts: wwpQos410Table.setDescription('A Table of QOS per vlan per port Entries.')
wwpQos410Entry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410VlanId"), (0, "WWP-QOS-410-MIB", "wwpQos410IngressPortId"), (0, "WWP-QOS-410-MIB", "wwpQos410EgressPortId"))
if mibBuilder.loadTexts: wwpQos410Entry.setStatus('current')
if mibBuilder.loadTexts: wwpQos410Entry.setDescription('The QOS per vlan per port Entry in the Table.')
wwpQos410VlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410VlanId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410VlanId.setDescription('Vlan ID for this instance of QOS. This Vlan Id should refer to the wwpVlanId in the WwpVlanEntry.')
wwpQos410IngressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410IngressPortId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410IngressPortId.setDescription("Ingress Port ID for this instance of. Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpQos410EgressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410EgressPortId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410EgressPortId.setDescription("Egress Port ID for this instance of. Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpQos410MinRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128000))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410MinRateLimit.setStatus('current')
if mibBuilder.loadTexts: wwpQos410MinRateLimit.setDescription('Bandwidth guaranteed for this QOS entry, specified in 64Kb/s increments. The maximum value for this object is 8Gb/s, if this egress port is the lead port of a link aggregation group. The total of all QOS entries for this port cannot exceed the total bandwidth of the port or the set will fail.')
wwpQos410MaxRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128000))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410MaxRateLimit.setStatus('current')
if mibBuilder.loadTexts: wwpQos410MaxRateLimit.setDescription('Bandwidth limit that cannot be exceeded by this QOS entry. The bandwidth is specified in 64Kb/s increments, with a maximum of 8Gb/s. The value specified cannot exceed the current bandwidth of the port. Values greater than 1 Gb/s can only be setup once a link agg group has been established.')
wwpQos410QueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("qSize16kb", 1), ("qSize32kb", 2), ("qSize64kb", 3), ("qSize128kb", 4), ("qSize256kb", 5), ("qSize512kb", 6), ("qSize1mb", 7), ("qSize2mb", 8), ("qSize4mb", 9), ("qSize8mb", 10), ("qSize16mb", 11), ("qSize32mb", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410QueueSize.setStatus('current')
if mibBuilder.loadTexts: wwpQos410QueueSize.setDescription('The size of the queue for this QOS entry.')
wwpQos410Weight = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("qw1", 1), ("qw2", 2), ("qw3", 3), ("qw4", 4), ("qw5", 5), ("qw6", 6), ("qw7", 7), ("qw8", 8), ("qw10", 9), ("qw12", 10), ("qw14", 11), ("qw16", 12), ("qw20", 13), ("qw24", 14), ("qw28", 15), ("qw32", 16), ("qw40", 17), ("qw48", 18), ("qw56", 19), ("qw64", 20), ("qw80", 21), ("qw96", 22), ("qw112", 23), ("qw128", 24), ("qw160", 25), ("qw192", 26), ("qw224", 27), ("qw256", 28), ("qw320", 29), ("qw384", 30), ("qw448", 31), ("qw512", 32), ("qw640", 33), ("qw768", 34), ("qw896", 35), ("qw1024", 36)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410Weight.setStatus('current')
if mibBuilder.loadTexts: wwpQos410Weight.setDescription('Value that is used to determine which QOS entries will receive the remaining bandwidth once Minimum Bandwidth requirements have been satisfied for all QOS entries. QOS entries with greater weight (smaller number) will receive a larger portion of this bandwidth.')
wwpQos410RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpQos410RowStatus.setStatus('current')
if mibBuilder.loadTexts: wwpQos410RowStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'.")
wwpQos410StatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2), )
if mibBuilder.loadTexts: wwpQos410StatsTable.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsTable.setDescription('A Table of QOS Stats per vlan per ingress/egress port Entries.')
wwpQos410StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410StatsVlanId"), (0, "WWP-QOS-410-MIB", "wwpQos410StatsIngressPortId"), (0, "WWP-QOS-410-MIB", "wwpQos410StatsEgressPortId"))
if mibBuilder.loadTexts: wwpQos410StatsEntry.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsEntry.setDescription('The QOS Stats per vlan per port Entry in the Table.')
wwpQos410StatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsVlanId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsVlanId.setDescription('Vlan ID for this instance of QOS. This Vlan Id should refer to the wwpVlanId in the WwpVlanEntry.')
wwpQos410StatsIngressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsIngressPortId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsIngressPortId.setDescription("Ingress Port ID for this instance of . Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpQos410StatsEgressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsEgressPortId.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsEgressPortId.setDescription("Egress Port ID for this instance of. Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpQos410StatsType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accepted", 1), ("discarded", 2))).clone('accepted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410StatsType.setStatus('current')
if mibBuilder.loadTexts: wwpQos410StatsType.setDescription('Determines which type of bytes to count, accepted bytes or discarded bytes for this QOS entry. The default will count accepted bytes.')
wwpQos410RxBytesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxBytesHi.setStatus('current')
if mibBuilder.loadTexts: wwpQos410RxBytesHi.setDescription('The number of bytes received for this QOS Entry.This counter represents the upper 32 bits of the counter value.')
wwpQos410RxBytesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxBytesLo.setStatus('current')
if mibBuilder.loadTexts: wwpQos410RxBytesLo.setDescription('The number of bytes received for this QOS Entry.This counter represents the lower 32 bits of the counter value.')
wwpQos410PriToQMapTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3), )
if mibBuilder.loadTexts: wwpQos410PriToQMapTable.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PriToQMapTable.setDescription('A Table of mapping of an RX-priority to a TX-queue.')
wwpQos410PriToQMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410RxPriority"))
if mibBuilder.loadTexts: wwpQos410PriToQMapEntry.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PriToQMapEntry.setDescription('The mapping Entry of an RX-priority to a TX-queue in the Table.')
wwpQos410RxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxPriority.setStatus('current')
if mibBuilder.loadTexts: wwpQos410RxPriority.setDescription('The RX-prioroty value for this entry.')
wwpQos410TxPriQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410TxPriQueue.setStatus('current')
if mibBuilder.loadTexts: wwpQos410TxPriQueue.setDescription('The TX-priority-queue value for this entry.')
wwpQos410PortTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4), )
if mibBuilder.loadTexts: wwpQos410PortTable.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortTable.setDescription('A Table of QOS per port Entries.')
wwpQos410PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortEntry.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortEntry.setDescription('The QOS per port Entry in the Table.')
wwpQos410PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortIndex.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortIndex.setDescription("Port ID for this instance of. Port ID's start at 1, and are consecutive for each additional port. This port Id should refer to the dot1dBasePort in the Dot1dBasePortEntry.")
wwpQos410PortProvisionedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortProvisionedBW.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortProvisionedBW.setDescription('Number of 64Kbps of bandwidth that is currently Provisioned for this port. This value is read-only and is updated each time a QOS entry is created for this port. If the port is a member of a Link Agg group and is not the lead port the value will be zero.')
wwpQos410PortTotalBW = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortTotalBW.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortTotalBW.setDescription("Number of 64Kbps of bandwidth that make up this port's total bandwidth. This value is read-only and is updated each time a QOS entry is created for this port. If the port is a member of a Link Agg group and this is not the lead port the value will be zero.")
wwpQos410PortProvisionedNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410PortProvisionedNotifEnabled.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortProvisionedNotifEnabled.setDescription('This variable indicates whether the system generates the wwpQos410PortOverProvisionedTrap and wwpQos410PortUnderProvisionedTrap. A false value prevents this notifications from being generated by this system.')
wwpQos410PortOverProvisionedTrap = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 1)).setObjects(("WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortOverProvisionedTrap.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortOverProvisionedTrap.setDescription('A wwpQos410PortOverProvisionedTrap notification is sent when the provisioned bandwidth exceeds the total bandwidth available for a port. This situation may also occur when changes in a link aggregation group (such as deleting a port from the group) decrease the total bandwidth or at the bootTime when the link aggregation groups are formed.')
wwpQos410PortUnderProvisionedTrap = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 2)).setObjects(("WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortUnderProvisionedTrap.setStatus('current')
if mibBuilder.loadTexts: wwpQos410PortUnderProvisionedTrap.setDescription('A wwpQos410PortUnderProvisionedTrap notification is sent when the previously over-provisioned situation is resolved for a port.')
mibBuilder.exportSymbols("WWP-QOS-410-MIB", wwpQos410StatsEgressPortId=wwpQos410StatsEgressPortId, wwpQos410MinRateLimit=wwpQos410MinRateLimit, wwpQos410PortOverProvisionedTrap=wwpQos410PortOverProvisionedTrap, wwpQos410StatsType=wwpQos410StatsType, wwpQos410PriToQMapTable=wwpQos410PriToQMapTable, wwpQos410StatsTable=wwpQos410StatsTable, wwpQos410MIBConformance=wwpQos410MIBConformance, wwpQos410Table=wwpQos410Table, wwpQos410PortTable=wwpQos410PortTable, wwpQos410EgressPortId=wwpQos410EgressPortId, wwpQos410MIBObjects=wwpQos410MIBObjects, wwpQos410RxPriority=wwpQos410RxPriority, wwpQos410PortTotalBW=wwpQos410PortTotalBW, wwpQos410PortProvisionedNotifEnabled=wwpQos410PortProvisionedNotifEnabled, wwpQos410TxPriQueue=wwpQos410TxPriQueue, PYSNMP_MODULE_ID=wwpQos410MIB, wwpQos410=wwpQos410, wwpQos410MIBGroups=wwpQos410MIBGroups, wwpQos410IngressPortId=wwpQos410IngressPortId, wwpQos410StatsIngressPortId=wwpQos410StatsIngressPortId, wwpQos410MaxRateLimit=wwpQos410MaxRateLimit, wwpQos410Weight=wwpQos410Weight, wwpQos410QueueSize=wwpQos410QueueSize, wwpQos410MIBCompliances=wwpQos410MIBCompliances, wwpQos410PortIndex=wwpQos410PortIndex, wwpQos410RowStatus=wwpQos410RowStatus, wwpQos410MIB=wwpQos410MIB, wwpQos410RxBytesLo=wwpQos410RxBytesLo, wwpQos410Entry=wwpQos410Entry, wwpQos410PortEntry=wwpQos410PortEntry, wwpQos410Notifications=wwpQos410Notifications, wwpQos410VlanId=wwpQos410VlanId, wwpQos410NotificationPrefix=wwpQos410NotificationPrefix, wwpQos410PortProvisionedBW=wwpQos410PortProvisionedBW, wwpQos410RxBytesHi=wwpQos410RxBytesHi, wwpQos410StatsVlanId=wwpQos410StatsVlanId, wwpQos410PortUnderProvisionedTrap=wwpQos410PortUnderProvisionedTrap, VlanId=VlanId, wwpQos410StatsEntry=wwpQos410StatsEntry, wwpQos410PriToQMapEntry=wwpQos410PriToQMapEntry)
