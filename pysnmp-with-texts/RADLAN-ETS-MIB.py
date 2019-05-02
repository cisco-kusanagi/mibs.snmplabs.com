#
# PySNMP MIB module RADLAN-ETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-ETS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:46:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
Percents, rnd = mibBuilder.importSymbols("RADLAN-MIB", "Percents", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, iso, Bits, NotificationType, Unsigned32, Integer32, ObjectIdentity, ModuleIdentity, Gauge32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "iso", "Bits", "NotificationType", "Unsigned32", "Integer32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Counter32", "MibIdentifier")
TextualConvention, RowStatus, TruthValue, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "RowPointer", "DisplayString")
rlEtsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 201))
if mibBuilder.loadTexts: rlEtsMib.setLastUpdated('201003210000A')
if mibBuilder.loadTexts: rlEtsMib.setOrganization('Marvell Computer Communications Ltd.')
if mibBuilder.loadTexts: rlEtsMib.setContactInfo('marvell.com')
if mibBuilder.loadTexts: rlEtsMib.setDescription('Added: EtsPriorityGroupType rlEtsFeatureStatus rlEtsPriorityGroupMappingTable rlEtsPriorityGroupBwAllocTable.')
class EtsPriorityGroupType(TextualConvention, Integer32):
    description = 'Priority group enumerator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 15))
    namedValues = NamedValues(("priorityGroup0", 0), ("priorityGroup1", 1), ("priorityGroup2", 2), ("priorityGroup3", 3), ("priorityGroup4", 4), ("priorityGroup5", 5), ("priorityGroup6", 6), ("priorityGroup7", 7), ("priorityGroup15", 15))

class EtsAdminStatusReasonType(TextualConvention, Integer32):
    description = 'Administarative reason enumerator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("too-many-groups", 2), ("too-many-queues", 3), ("not-highest-queue", 4))

rlEtsFeatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsFeatureStatus.setStatus('current')
if mibBuilder.loadTexts: rlEtsFeatureStatus.setDescription('This scalar indicates ETS enable status.')
rlEtsPriorityGroupMappingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 201, 2), )
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingTable.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingTable.setDescription('This table describes Enhanced Transmission Selection Priority to Priority Group Mapping.')
rlEtsPriorityGroupMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 201, 2, 1), ).setIndexNames((0, "RADLAN-ETS-MIB", "rlEtsPriorityGroupMapping8021QPrio"))
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingEntry.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingEntry.setDescription('Each entry in this table describes The priority to priority group mapping. The index is represented by rlEtsPriorityGroupMapping8021QPrio.')
rlEtsPriorityGroupMapping8021QPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: rlEtsPriorityGroupMapping8021QPrio.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMapping8021QPrio.setDescription('802.1Q Priority.')
rlEtsPriorityGroupMappingAdminPG = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 2), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingAdminPG.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingAdminPG.setDescription('Administrative (desired) Priority group of this priority.')
rlEtsPriorityGroupMappingOperPG = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 3), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingOperPG.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingOperPG.setDescription('Operational (current) priority group of this priority.')
rlEtsPriorityGroupMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingStatus.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingStatus.setDescription('The status of a table entry. It is used to add/delete an entry from this table.')
rlEtsPriorityGroupMappingProblemReason = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 3), EtsAdminStatusReasonType().clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemReason.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemReason.setDescription('Reason if priority to priority group, admin status is not equal to operational status.')
rlEtsPriorityGroupMappingProblemIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemIndex.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemIndex.setDescription('Index of problematic PG if rlEtsPriorityGroupMappingProblemReason = too-many-queues(2) or index of problematic queue if rlEtsPriorityGroupMappingProblemReason = too-many-groups(1).')
rlEtsPriorityGroupBwAlloc = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupBwAlloc.setStatus('current')
if mibBuilder.loadTexts: rlEtsPriorityGroupBwAlloc.setDescription('Enhanced Transmission Selection Priority Group Bandwidth Allocation identifier. Each pair of octets represent priority group with corresponding bandwidth')
mibBuilder.exportSymbols("RADLAN-ETS-MIB", rlEtsPriorityGroupMappingOperPG=rlEtsPriorityGroupMappingOperPG, rlEtsPriorityGroupMappingAdminPG=rlEtsPriorityGroupMappingAdminPG, PYSNMP_MODULE_ID=rlEtsMib, rlEtsPriorityGroupMapping8021QPrio=rlEtsPriorityGroupMapping8021QPrio, rlEtsPriorityGroupMappingStatus=rlEtsPriorityGroupMappingStatus, EtsAdminStatusReasonType=EtsAdminStatusReasonType, rlEtsFeatureStatus=rlEtsFeatureStatus, rlEtsPriorityGroupMappingProblemIndex=rlEtsPriorityGroupMappingProblemIndex, rlEtsPriorityGroupMappingEntry=rlEtsPriorityGroupMappingEntry, rlEtsPriorityGroupBwAlloc=rlEtsPriorityGroupBwAlloc, EtsPriorityGroupType=EtsPriorityGroupType, rlEtsPriorityGroupMappingProblemReason=rlEtsPriorityGroupMappingProblemReason, rlEtsPriorityGroupMappingTable=rlEtsPriorityGroupMappingTable, rlEtsMib=rlEtsMib)
