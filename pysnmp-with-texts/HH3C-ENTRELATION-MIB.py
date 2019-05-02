#
# PySNMP MIB module HH3C-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, TimeTicks, Integer32, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 15))
if mibBuilder.loadTexts: hh3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: hh3cEntityRelation.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cEntityRelation.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cEntityRelation.setDescription('The private MIB file includes the general relation information information of entities. Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. So this MIB is used to express these relations. ')
class Hh3cEntRelationType(TextualConvention, Integer32):
    description = 'entRelationType describe the relation type of the two entities (indicated by entityIndex and relatedEntityIndex) . stackport: this port is a stack port. entityIndex is the default uplinkport index, and relatedEntityIndex is the default downlinkport index. comboport: this port is a combo port. entityIndex is the default active port index, and relatedEntityIndex is the default inactive port index.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

hh3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1))
hh3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1))
hh3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cEntRelationTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEntRelationTable.setDescription('Entity MIB is used to express the physical location of the physical entities. Other relations, such as stack port pair and combo port pair, are not suitable to be implemented in Entity MIB. This MIB is used to express these relations. ')
hh3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-ENTRELATION-MIB", "hh3cEntRelationType"), (0, "HH3C-ENTRELATION-MIB", "hh3cEntityIndex"), (0, "HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex"))
if mibBuilder.loadTexts: hh3cEntRelationEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEntRelationEntry.setDescription('The information about a particular physical entity.')
hh3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 1), Hh3cEntRelationType())
if mibBuilder.loadTexts: hh3cEntRelationType.setStatus('current')
if mibBuilder.loadTexts: hh3cEntRelationType.setDescription('The index of hh3cEntRelationTable. entRelationType describe the relation type of the two entities(indicated by entityIndex and relatedEntityIndex) ')
hh3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: hh3cEntityIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cEntityIndex.setDescription('The index of hh3cEntRelationTable. entityIndex is the index of the entity. This index is identical to entPhysicalIndex in ENTITY-MIB')
hh3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRelatedEntityIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cRelatedEntityIndex.setDescription('The index of hh3cEntRelationTable. relatedEntityIndex is the entity index that entityIndex related to, This index is identical to entPhysicalIndex in ENTITY-MIB')
hh3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2))
hh3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1))
hh3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1, 1)).setObjects(("HH3C-ENTRELATION-MIB", "hh3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cEntRelationCompliance = hh3cEntRelationCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cEntRelationCompliance.setDescription('The compliance statement for systems supporting this MIB.')
hh3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2))
hh3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2, 1)).setObjects(("HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cEntRelationGroup = hh3cEntRelationGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cEntRelationGroup.setDescription('Standard H3C Entity Relation group.')
mibBuilder.exportSymbols("HH3C-ENTRELATION-MIB", hh3cEntRelationConformance=hh3cEntRelationConformance, hh3cEntRelation=hh3cEntRelation, hh3cEntRelationGroups=hh3cEntRelationGroups, hh3cEntRelationObjects=hh3cEntRelationObjects, hh3cEntRelationCompliances=hh3cEntRelationCompliances, hh3cEntRelationGroup=hh3cEntRelationGroup, hh3cEntRelationType=hh3cEntRelationType, PYSNMP_MODULE_ID=hh3cEntityRelation, hh3cEntityRelation=hh3cEntityRelation, hh3cEntRelationEntry=hh3cEntRelationEntry, Hh3cEntRelationType=Hh3cEntRelationType, hh3cEntityIndex=hh3cEntityIndex, hh3cEntRelationCompliance=hh3cEntRelationCompliance, hh3cEntRelationTable=hh3cEntRelationTable, hh3cRelatedEntityIndex=hh3cRelatedEntityIndex)
