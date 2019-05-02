#
# PySNMP MIB module HPN-ICF-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, IpAddress, NotificationType, Gauge32, ObjectIdentity, Unsigned32, iso, MibIdentifier, TimeTicks, Counter64, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "iso", "MibIdentifier", "TimeTicks", "Counter64", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15))
if mibBuilder.loadTexts: hpnicfEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: hpnicfEntityRelation.setOrganization('')
if mibBuilder.loadTexts: hpnicfEntityRelation.setContactInfo('')
if mibBuilder.loadTexts: hpnicfEntityRelation.setDescription('The private MIB file includes the general relation information information of entities. Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. So this MIB is used to express these relations. ')
class HpnicfEntRelationType(TextualConvention, Integer32):
    description = 'entRelationType describe the relation type of the two entities (indicated by entityIndex and relatedEntityIndex) . stackport: this port is a stack port. entityIndex is the default uplinkport index, and relatedEntityIndex is the default downlinkport index. comboport: this port is a combo port. entityIndex is the default active port index, and relatedEntityIndex is the default inactive port index.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

hpnicfEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1))
hpnicfEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1))
hpnicfEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfEntRelationTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntRelationTable.setDescription('Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. This MIB is used to express these relations. ')
hpnicfEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationType"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntityIndex"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if mibBuilder.loadTexts: hpnicfEntRelationEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntRelationEntry.setDescription('The information about a particular physical entity.')
hpnicfEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 1), HpnicfEntRelationType())
if mibBuilder.loadTexts: hpnicfEntRelationType.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntRelationType.setDescription('The index of hpnicfEntRelationTable. entRelationType describe the relation type of the two entities(indicated by entityIndex and relatedEntityIndex) ')
hpnicfEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: hpnicfEntityIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntityIndex.setDescription('The index of hpnicfEntRelationTable. entityIndex is the index of the entity. This index is identical to entPhysicalIndex in ENTITY-MIB')
hpnicfRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRelatedEntityIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfRelatedEntityIndex.setDescription('The index of hpnicfEntRelationTable. relatedEntityIndex is the entity index that entityIndex related to, This index is identical to entPhysicalIndex in ENTITY-MIB')
hpnicfEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2))
hpnicfEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1))
hpnicfEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationCompliance = hpnicfEntRelationCompliance.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntRelationCompliance.setDescription('The compliance statement for systems supporting this MIB.')
hpnicfEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2))
hpnicfEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationGroup = hpnicfEntRelationGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfEntRelationGroup.setDescription('Standard Entity Relation group.')
mibBuilder.exportSymbols("HPN-ICF-ENTRELATION-MIB", hpnicfEntRelationTable=hpnicfEntRelationTable, HpnicfEntRelationType=HpnicfEntRelationType, PYSNMP_MODULE_ID=hpnicfEntityRelation, hpnicfEntRelationEntry=hpnicfEntRelationEntry, hpnicfEntRelationType=hpnicfEntRelationType, hpnicfEntityIndex=hpnicfEntityIndex, hpnicfEntRelationCompliance=hpnicfEntRelationCompliance, hpnicfEntRelationConformance=hpnicfEntRelationConformance, hpnicfEntRelationGroups=hpnicfEntRelationGroups, hpnicfEntRelation=hpnicfEntRelation, hpnicfRelatedEntityIndex=hpnicfRelatedEntityIndex, hpnicfEntRelationObjects=hpnicfEntRelationObjects, hpnicfEntityRelation=hpnicfEntityRelation, hpnicfEntRelationGroup=hpnicfEntRelationGroup, hpnicfEntRelationCompliances=hpnicfEntRelationCompliances)
