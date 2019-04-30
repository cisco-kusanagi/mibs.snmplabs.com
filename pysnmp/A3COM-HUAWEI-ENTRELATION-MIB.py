#
# PySNMP MIB module A3COM-HUAWEI-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter64, Bits, Gauge32, TimeTicks, IpAddress, ObjectIdentity, Counter32, MibIdentifier, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter64", "Bits", "Gauge32", "TimeTicks", "IpAddress", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15))
if mibBuilder.loadTexts: h3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: h3cEntityRelation.setOrganization('Huawei-3com Technologies co.,Ltd.')
class H3cEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

h3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1))
h3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1))
h3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: h3cEntRelationTable.setStatus('current')
h3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntRelationType"), (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntityIndex"), (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if mibBuilder.loadTexts: h3cEntRelationEntry.setStatus('current')
h3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 1), H3cEntRelationType())
if mibBuilder.loadTexts: h3cEntRelationType.setStatus('current')
h3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: h3cEntityIndex.setStatus('current')
h3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRelatedEntityIndex.setStatus('current')
h3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2))
h3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1))
h3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1, 1)).setObjects(("A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationCompliance = h3cEntRelationCompliance.setStatus('current')
h3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2))
h3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2, 1)).setObjects(("A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationGroup = h3cEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-ENTRELATION-MIB", H3cEntRelationType=H3cEntRelationType, h3cEntRelationTable=h3cEntRelationTable, h3cEntRelationObjects=h3cEntRelationObjects, h3cEntRelationType=h3cEntRelationType, h3cEntRelationConformance=h3cEntRelationConformance, h3cEntRelationCompliance=h3cEntRelationCompliance, h3cEntityIndex=h3cEntityIndex, h3cRelatedEntityIndex=h3cRelatedEntityIndex, h3cEntityRelation=h3cEntityRelation, h3cEntRelationGroups=h3cEntRelationGroups, h3cEntRelation=h3cEntRelation, h3cEntRelationGroup=h3cEntRelationGroup, h3cEntRelationCompliances=h3cEntRelationCompliances, h3cEntRelationEntry=h3cEntRelationEntry, PYSNMP_MODULE_ID=h3cEntityRelation)
