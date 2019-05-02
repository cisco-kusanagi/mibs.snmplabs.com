#
# PySNMP MIB module ARISTA-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-QUEUE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, ModuleIdentity, ObjectIdentity, TimeTicks, Counter32, Gauge32, MibIdentifier, NotificationType, iso, Integer32, IpAddress, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "iso", "Integer32", "IpAddress", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 6))
aristaQueueMIB.setRevisions(('2014-08-15 00:00', '2012-08-23 13:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaQueueMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses. Updated descriptions for PacketType, DropPrecedence, and aristaEgressQueueTable.', 'Initial version.',))
if mibBuilder.loadTexts: aristaQueueMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaQueueMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaQueueMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaQueueMIB.setDescription('The MIB module is for managing interface queuing on Arista devices. Arista Networks has a number of products. This MIB generalizes ingress and egress queue counters supported on all Arista products. Therefore, a platform may not support all table indices and counters listed in this MIB. For example, ingressQueueIndex in aristaIngressQueueTable, aristaEgressQueuePktsDroppedQFull, aristaEgressQueuePktsDroppedNoBuffer, and aristaEgressQueueDropPrec in aristaEgressQueueTable are not supported in 7050 series switches.')
aristaQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1))
aristaQueueCounterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2))
class QueueIndex(TextualConvention, Integer32):
    description = 'A unique value for each queue in an interface in the managed system.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PacketType(TextualConvention, Integer32):
    description = 'The packet type of the packets in a queue in an interface in the managed system. It is recommended that there are three packet types of packets in a queue: unicast, multicast, mixed packet type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unicast", 0), ("multicast", 1), ("mixedPacketType", 2))

class DropPrecedence(TextualConvention, Integer32):
    description = 'The drop precedences of the packets in a queue in an interface in the managed system. It is recommended that there are three levels of drop precedences of packets in a queue: DropPrecedence0, DropPrecedence1, and DropPrecedence2. When congestion occurs, packets marked with DropPrecedence2 are dropped first; packets marked with DropPrecedence0 are dropped last.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("dropPrecedence0", 0), ("dropPrecedence1", 1), ("dropPrecedence2", 2))

aristaIngressQueueTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1), )
if mibBuilder.loadTexts: aristaIngressQueueTable.setStatus('current')
if mibBuilder.loadTexts: aristaIngressQueueTable.setDescription('This table contains statistical information of the ingress queue in an interface.')
aristaIngressQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1), ).setIndexNames((0, "ARISTA-QUEUE-MIB", "aristaIngressIfIndex"), (0, "ARISTA-QUEUE-MIB", "aristaIngressQueueIndex"))
if mibBuilder.loadTexts: aristaIngressQueueEntry.setStatus('current')
if mibBuilder.loadTexts: aristaIngressQueueEntry.setDescription('A list of attributes of ingress queues in an interface. The attributes include dropped packets and dropped bytes of ingress queues.')
aristaIngressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaIngressIfIndex.setStatus('current')
if mibBuilder.loadTexts: aristaIngressIfIndex.setDescription('The index of an interface.')
aristaIngressQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 2), QueueIndex())
if mibBuilder.loadTexts: aristaIngressQueueIndex.setStatus('current')
if mibBuilder.loadTexts: aristaIngressQueueIndex.setDescription('The index of ingress queues in the interface. In the case that the ingress queue information is the sum of the statistics of all ingress queues, the queueIndex is set as zero.')
aristaIngressQueuePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIngressQueuePktsDropped.setStatus('current')
if mibBuilder.loadTexts: aristaIngressQueuePktsDropped.setDescription('The number of dropped packets due to congestion at the ingress port in an interface.')
aristaIngressQueueBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIngressQueueBytesDropped.setStatus('current')
if mibBuilder.loadTexts: aristaIngressQueueBytesDropped.setDescription('The number of dropped bytes due to congestion at the ingress port in an interface.')
aristaEgressQueueTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2), )
if mibBuilder.loadTexts: aristaEgressQueueTable.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueTable.setDescription('This table contains statistical objects for the egress queues of an interface.')
aristaEgressQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1), ).setIndexNames((0, "ARISTA-QUEUE-MIB", "aristaEgressIfIndex"), (0, "ARISTA-QUEUE-MIB", "aristaEgressQueueIndex"), (0, "ARISTA-QUEUE-MIB", "aristaEgressPacketType"))
if mibBuilder.loadTexts: aristaEgressQueueEntry.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueEntry.setDescription('A list of statistical information of egress queues in an interface. The statistical information includes transmitted packets, transmitted bytes, dropped packets, and dropped bytes of egress queues.')
aristaEgressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaEgressIfIndex.setStatus('current')
if mibBuilder.loadTexts: aristaEgressIfIndex.setDescription('The index of an interface.')
aristaEgressQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 2), QueueIndex())
if mibBuilder.loadTexts: aristaEgressQueueIndex.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueIndex.setDescription('The index of egress queues in the interface.')
aristaEgressPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 3), PacketType())
if mibBuilder.loadTexts: aristaEgressPacketType.setStatus('current')
if mibBuilder.loadTexts: aristaEgressPacketType.setDescription('The type of destination of packets in an egress queue in an interface.')
aristaEgressQueuePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePkts.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueuePkts.setDescription('The number of transmitted packets in the egress queue.')
aristaEgressQueueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueBytes.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueBytes.setDescription('The number of transmitted bytes in the egress queue.')
aristaEgressQueuePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDropped.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueuePktsDropped.setDescription('The number of packets discarded from this egress queue.')
aristaEgressQueueBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueBytesDropped.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueBytesDropped.setDescription('The number of bytes discarded from this egress queue.')
aristaEgressQueuePktsDroppedQFull = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedQFull.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedQFull.setDescription('The number of packets discarded from this egress queue when the queue is full.')
aristaEgressQueuePktsDroppedNoBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedNoBuffer.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedNoBuffer.setDescription('The number of packets discarded from this egress queue when there is no buffer.')
aristaEgressQueueDropPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 10), DropPrecedence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueDropPrec.setStatus('current')
if mibBuilder.loadTexts: aristaEgressQueueDropPrec.setDescription('The drop precedence of packets in this egress queue.')
aristaQueueCounterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1))
aristaQueueCounterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2))
aristaQueueCounterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1, 1)).setObjects(("ARISTA-QUEUE-MIB", "aristaQueueCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaQueueCounterCompliance = aristaQueueCounterCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaQueueCounterCompliance.setDescription('The compliance statement for Arista switches that support queue counters.')
aristaQueueCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2, 1)).setObjects(("ARISTA-QUEUE-MIB", "aristaIngressQueuePktsDropped"), ("ARISTA-QUEUE-MIB", "aristaIngressQueueBytesDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePkts"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytes"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytesDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedQFull"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedNoBuffer"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueDropPrec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaQueueCounterGroup = aristaQueueCounterGroup.setStatus('current')
if mibBuilder.loadTexts: aristaQueueCounterGroup.setDescription('The group of required objects in aristaIngressQueueTable and aristaEgressQueueTable.')
mibBuilder.exportSymbols("ARISTA-QUEUE-MIB", aristaEgressQueuePktsDropped=aristaEgressQueuePktsDropped, PYSNMP_MODULE_ID=aristaQueueMIB, aristaQueueCounterGroup=aristaQueueCounterGroup, aristaEgressPacketType=aristaEgressPacketType, aristaEgressQueueEntry=aristaEgressQueueEntry, PacketType=PacketType, aristaQueueCounterCompliances=aristaQueueCounterCompliances, aristaEgressQueueTable=aristaEgressQueueTable, DropPrecedence=DropPrecedence, aristaQueueCounterConformance=aristaQueueCounterConformance, aristaIngressIfIndex=aristaIngressIfIndex, aristaQueue=aristaQueue, aristaEgressQueueIndex=aristaEgressQueueIndex, aristaEgressQueuePktsDroppedNoBuffer=aristaEgressQueuePktsDroppedNoBuffer, aristaIngressQueueIndex=aristaIngressQueueIndex, aristaQueueCounterGroups=aristaQueueCounterGroups, aristaIngressQueueTable=aristaIngressQueueTable, aristaEgressQueueBytesDropped=aristaEgressQueueBytesDropped, aristaEgressQueueBytes=aristaEgressQueueBytes, aristaEgressQueuePktsDroppedQFull=aristaEgressQueuePktsDroppedQFull, QueueIndex=QueueIndex, aristaEgressQueuePkts=aristaEgressQueuePkts, aristaEgressIfIndex=aristaEgressIfIndex, aristaIngressQueueEntry=aristaIngressQueueEntry, aristaQueueCounterCompliance=aristaQueueCounterCompliance, aristaEgressQueueDropPrec=aristaEgressQueueDropPrec, aristaQueueMIB=aristaQueueMIB, aristaIngressQueueBytesDropped=aristaIngressQueueBytesDropped, aristaIngressQueuePktsDropped=aristaIngressQueuePktsDropped)
