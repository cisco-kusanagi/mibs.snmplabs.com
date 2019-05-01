#
# PySNMP MIB module H3C-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, IpAddress, Gauge32, Bits, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, TimeTicks, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Gauge32", "Bits", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "TimeTicks", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15))
if mibBuilder.loadTexts: h3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: h3cEntityRelation.setOrganization('Huawei-3com Technologies co.,Ltd.')
if mibBuilder.loadTexts: h3cEntityRelation.setContactInfo('Platform Team Beijing Institute Huawei-3com Tech, Inc. Http://www.huawei-3com.com E-mail:support@huawei-3com.com ')
if mibBuilder.loadTexts: h3cEntityRelation.setDescription('The private mib file includes the general relation information information of entities. Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. So this mib is used to express these relations. ')
class H3cEntRelationType(TextualConvention, Integer32):
    description = 'entRelationType describe the relation type of the two entities (indicated by entityIndex and relatedEntityIndex) . stackport: this port is a stack port. entityIndex is the default uplinkport index, and relatedEntityIndex is the default downlinkport index. comboport: this port is a combo port. entityIndex is the default active port index, and relatedEntityIndex is the default inactive port index.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

h3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1))
h3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1))
h3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: h3cEntRelationTable.setStatus('current')
if mibBuilder.loadTexts: h3cEntRelationTable.setDescription('Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. This MIB is used to express these relations. ')
h3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "H3C-ENTRELATION-MIB", "h3cEntRelationType"), (0, "H3C-ENTRELATION-MIB", "h3cEntityIndex"), (0, "H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if mibBuilder.loadTexts: h3cEntRelationEntry.setStatus('current')
if mibBuilder.loadTexts: h3cEntRelationEntry.setDescription('The information about a particular physical entity.')
h3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 1), H3cEntRelationType())
if mibBuilder.loadTexts: h3cEntRelationType.setStatus('current')
if mibBuilder.loadTexts: h3cEntRelationType.setDescription('The index of h3cEntRelationTable. entRelationType describe the relation type of the two entities(indicated by entityIndex and relatedEntityIndex) ')
h3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: h3cEntityIndex.setStatus('current')
if mibBuilder.loadTexts: h3cEntityIndex.setDescription('The index of h3cEntRelationTable. entityIndex is the index of the entity. This index is identical to entPhysicalIndex in ENTITY-MIB')
h3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRelatedEntityIndex.setStatus('current')
if mibBuilder.loadTexts: h3cRelatedEntityIndex.setDescription('The index of h3cEntRelationTable. relatedEntityIndex is the entity index that entityIndex related to, This index is identical to entPhysicalIndex in ENTITY-MIB')
h3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2))
h3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1))
h3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationCompliance = h3cEntRelationCompliance.setStatus('current')
if mibBuilder.loadTexts: h3cEntRelationCompliance.setDescription('The compliance statement for systems supporting this MIB.')
h3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2))
h3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationGroup = h3cEntRelationGroup.setStatus('current')
if mibBuilder.loadTexts: h3cEntRelationGroup.setDescription('Standard HUAWEI Entity Relation group.')
mibBuilder.exportSymbols("H3C-ENTRELATION-MIB", h3cEntRelationGroups=h3cEntRelationGroups, h3cEntRelationCompliances=h3cEntRelationCompliances, h3cEntityRelation=h3cEntityRelation, h3cEntRelationGroup=h3cEntRelationGroup, h3cEntityIndex=h3cEntityIndex, PYSNMP_MODULE_ID=h3cEntityRelation, h3cEntRelationObjects=h3cEntRelationObjects, h3cEntRelationConformance=h3cEntRelationConformance, h3cEntRelationTable=h3cEntRelationTable, h3cEntRelation=h3cEntRelation, h3cEntRelationEntry=h3cEntRelationEntry, h3cEntRelationCompliance=h3cEntRelationCompliance, h3cRelatedEntityIndex=h3cRelatedEntityIndex, H3cEntRelationType=H3cEntRelationType, h3cEntRelationType=h3cEntRelationType)
