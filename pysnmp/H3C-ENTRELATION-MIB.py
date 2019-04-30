#
# PySNMP MIB module H3C-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter32, ObjectIdentity, Integer32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, MibIdentifier, IpAddress, NotificationType, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ObjectIdentity", "Integer32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "NotificationType", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15))
if mibBuilder.loadTexts: h3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: h3cEntityRelation.setOrganization('Huawei-3com Technologies co.,Ltd.')
class H3cEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

h3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1))
h3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1))
h3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: h3cEntRelationTable.setStatus('current')
h3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "H3C-ENTRELATION-MIB", "h3cEntRelationType"), (0, "H3C-ENTRELATION-MIB", "h3cEntityIndex"), (0, "H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if mibBuilder.loadTexts: h3cEntRelationEntry.setStatus('current')
h3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 1), H3cEntRelationType())
if mibBuilder.loadTexts: h3cEntRelationType.setStatus('current')
h3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: h3cEntityIndex.setStatus('current')
h3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRelatedEntityIndex.setStatus('current')
h3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2))
h3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1))
h3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 1, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationCompliance = h3cEntRelationCompliance.setStatus('current')
h3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2))
h3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 15, 2, 2, 1)).setObjects(("H3C-ENTRELATION-MIB", "h3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cEntRelationGroup = h3cEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-ENTRELATION-MIB", h3cEntRelationType=h3cEntRelationType, h3cEntRelationEntry=h3cEntRelationEntry, h3cEntRelationTable=h3cEntRelationTable, h3cRelatedEntityIndex=h3cRelatedEntityIndex, h3cEntRelationCompliances=h3cEntRelationCompliances, H3cEntRelationType=H3cEntRelationType, h3cEntityIndex=h3cEntityIndex, h3cEntRelationGroups=h3cEntRelationGroups, h3cEntRelationObjects=h3cEntRelationObjects, h3cEntRelationConformance=h3cEntRelationConformance, PYSNMP_MODULE_ID=h3cEntityRelation, h3cEntRelationCompliance=h3cEntRelationCompliance, h3cEntRelation=h3cEntRelation, h3cEntityRelation=h3cEntityRelation, h3cEntRelationGroup=h3cEntRelationGroup)
