#
# PySNMP MIB module ARISTA-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-QUEUE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, TimeTicks, Counter32, IpAddress, MibIdentifier, Gauge32, Bits, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "Bits", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 6))
aristaQueueMIB.setRevisions(('2014-08-15 00:00', '2012-08-23 13:00',))
if mibBuilder.loadTexts: aristaQueueMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaQueueMIB.setOrganization('Arista Networks, Inc.')
aristaQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1))
aristaQueueCounterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2))
class QueueIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PacketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unicast", 0), ("multicast", 1), ("mixedPacketType", 2))

class DropPrecedence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("dropPrecedence0", 0), ("dropPrecedence1", 1), ("dropPrecedence2", 2))

aristaIngressQueueTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1), )
if mibBuilder.loadTexts: aristaIngressQueueTable.setStatus('current')
aristaIngressQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1), ).setIndexNames((0, "ARISTA-QUEUE-MIB", "aristaIngressIfIndex"), (0, "ARISTA-QUEUE-MIB", "aristaIngressQueueIndex"))
if mibBuilder.loadTexts: aristaIngressQueueEntry.setStatus('current')
aristaIngressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaIngressIfIndex.setStatus('current')
aristaIngressQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 2), QueueIndex())
if mibBuilder.loadTexts: aristaIngressQueueIndex.setStatus('current')
aristaIngressQueuePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIngressQueuePktsDropped.setStatus('current')
aristaIngressQueueBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIngressQueueBytesDropped.setStatus('current')
aristaEgressQueueTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2), )
if mibBuilder.loadTexts: aristaEgressQueueTable.setStatus('current')
aristaEgressQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1), ).setIndexNames((0, "ARISTA-QUEUE-MIB", "aristaEgressIfIndex"), (0, "ARISTA-QUEUE-MIB", "aristaEgressQueueIndex"), (0, "ARISTA-QUEUE-MIB", "aristaEgressPacketType"))
if mibBuilder.loadTexts: aristaEgressQueueEntry.setStatus('current')
aristaEgressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aristaEgressIfIndex.setStatus('current')
aristaEgressQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 2), QueueIndex())
if mibBuilder.loadTexts: aristaEgressQueueIndex.setStatus('current')
aristaEgressPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 3), PacketType())
if mibBuilder.loadTexts: aristaEgressPacketType.setStatus('current')
aristaEgressQueuePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePkts.setStatus('current')
aristaEgressQueueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueBytes.setStatus('current')
aristaEgressQueuePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDropped.setStatus('current')
aristaEgressQueueBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueBytesDropped.setStatus('current')
aristaEgressQueuePktsDroppedQFull = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedQFull.setStatus('current')
aristaEgressQueuePktsDroppedNoBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueuePktsDroppedNoBuffer.setStatus('current')
aristaEgressQueueDropPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 6, 1, 2, 1, 10), DropPrecedence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEgressQueueDropPrec.setStatus('current')
aristaQueueCounterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1))
aristaQueueCounterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2))
aristaQueueCounterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 1, 1)).setObjects(("ARISTA-QUEUE-MIB", "aristaQueueCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaQueueCounterCompliance = aristaQueueCounterCompliance.setStatus('current')
aristaQueueCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 6, 2, 2, 1)).setObjects(("ARISTA-QUEUE-MIB", "aristaIngressQueuePktsDropped"), ("ARISTA-QUEUE-MIB", "aristaIngressQueueBytesDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePkts"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytes"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueBytesDropped"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedQFull"), ("ARISTA-QUEUE-MIB", "aristaEgressQueuePktsDroppedNoBuffer"), ("ARISTA-QUEUE-MIB", "aristaEgressQueueDropPrec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaQueueCounterGroup = aristaQueueCounterGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-QUEUE-MIB", aristaIngressQueueEntry=aristaIngressQueueEntry, aristaIngressQueueTable=aristaIngressQueueTable, aristaQueueCounterCompliance=aristaQueueCounterCompliance, aristaQueueCounterCompliances=aristaQueueCounterCompliances, aristaEgressQueueIndex=aristaEgressQueueIndex, aristaIngressQueuePktsDropped=aristaIngressQueuePktsDropped, aristaEgressQueueEntry=aristaEgressQueueEntry, aristaEgressPacketType=aristaEgressPacketType, aristaIngressQueueBytesDropped=aristaIngressQueueBytesDropped, aristaEgressQueueBytes=aristaEgressQueueBytes, PYSNMP_MODULE_ID=aristaQueueMIB, aristaEgressQueueBytesDropped=aristaEgressQueueBytesDropped, aristaQueueCounterGroup=aristaQueueCounterGroup, PacketType=PacketType, aristaEgressQueuePkts=aristaEgressQueuePkts, aristaEgressQueueTable=aristaEgressQueueTable, aristaIngressIfIndex=aristaIngressIfIndex, QueueIndex=QueueIndex, DropPrecedence=DropPrecedence, aristaQueueMIB=aristaQueueMIB, aristaQueue=aristaQueue, aristaQueueCounterGroups=aristaQueueCounterGroups, aristaEgressIfIndex=aristaEgressIfIndex, aristaEgressQueuePktsDroppedQFull=aristaEgressQueuePktsDroppedQFull, aristaQueueCounterConformance=aristaQueueCounterConformance, aristaEgressQueuePktsDropped=aristaEgressQueuePktsDropped, aristaEgressQueueDropPrec=aristaEgressQueueDropPrec, aristaEgressQueuePktsDroppedNoBuffer=aristaEgressQueuePktsDroppedNoBuffer, aristaIngressQueueIndex=aristaIngressQueueIndex)
