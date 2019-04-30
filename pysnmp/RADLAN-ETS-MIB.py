#
# PySNMP MIB module RADLAN-ETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-ETS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
Percents, rnd = mibBuilder.importSymbols("RADLAN-MIB", "Percents", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ObjectIdentity, Counter64, TimeTicks, IpAddress, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ObjectIdentity", "Counter64", "TimeTicks", "IpAddress", "NotificationType", "Unsigned32")
RowPointer, TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
rlEtsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 201))
if mibBuilder.loadTexts: rlEtsMib.setLastUpdated('201003210000A')
if mibBuilder.loadTexts: rlEtsMib.setOrganization('Marvell Computer Communications Ltd.')
class EtsPriorityGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 15))
    namedValues = NamedValues(("priorityGroup0", 0), ("priorityGroup1", 1), ("priorityGroup2", 2), ("priorityGroup3", 3), ("priorityGroup4", 4), ("priorityGroup5", 5), ("priorityGroup6", 6), ("priorityGroup7", 7), ("priorityGroup15", 15))

class EtsAdminStatusReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("too-many-groups", 2), ("too-many-queues", 3), ("not-highest-queue", 4))

rlEtsFeatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsFeatureStatus.setStatus('current')
rlEtsPriorityGroupMappingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 201, 2), )
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingTable.setStatus('current')
rlEtsPriorityGroupMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 201, 2, 1), ).setIndexNames((0, "RADLAN-ETS-MIB", "rlEtsPriorityGroupMapping8021QPrio"))
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingEntry.setStatus('current')
rlEtsPriorityGroupMapping8021QPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: rlEtsPriorityGroupMapping8021QPrio.setStatus('current')
rlEtsPriorityGroupMappingAdminPG = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 2), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingAdminPG.setStatus('current')
rlEtsPriorityGroupMappingOperPG = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 3), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingOperPG.setStatus('current')
rlEtsPriorityGroupMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 201, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingStatus.setStatus('current')
rlEtsPriorityGroupMappingProblemReason = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 3), EtsAdminStatusReasonType().clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemReason.setStatus('current')
rlEtsPriorityGroupMappingProblemIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemIndex.setStatus('current')
rlEtsPriorityGroupBwAlloc = MibScalar((1, 3, 6, 1, 4, 1, 89, 201, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupBwAlloc.setStatus('current')
mibBuilder.exportSymbols("RADLAN-ETS-MIB", rlEtsPriorityGroupMapping8021QPrio=rlEtsPriorityGroupMapping8021QPrio, rlEtsMib=rlEtsMib, rlEtsPriorityGroupMappingAdminPG=rlEtsPriorityGroupMappingAdminPG, rlEtsPriorityGroupMappingStatus=rlEtsPriorityGroupMappingStatus, PYSNMP_MODULE_ID=rlEtsMib, rlEtsPriorityGroupMappingProblemReason=rlEtsPriorityGroupMappingProblemReason, rlEtsPriorityGroupMappingProblemIndex=rlEtsPriorityGroupMappingProblemIndex, EtsPriorityGroupType=EtsPriorityGroupType, rlEtsPriorityGroupMappingOperPG=rlEtsPriorityGroupMappingOperPG, rlEtsPriorityGroupBwAlloc=rlEtsPriorityGroupBwAlloc, rlEtsFeatureStatus=rlEtsFeatureStatus, EtsAdminStatusReasonType=EtsAdminStatusReasonType, rlEtsPriorityGroupMappingEntry=rlEtsPriorityGroupMappingEntry, rlEtsPriorityGroupMappingTable=rlEtsPriorityGroupMappingTable)
