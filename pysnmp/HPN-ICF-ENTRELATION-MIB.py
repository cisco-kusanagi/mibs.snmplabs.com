#
# PySNMP MIB module HPN-ICF-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, iso, Counter64, ObjectIdentity, TimeTicks, IpAddress, Bits, MibIdentifier, Counter32, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "Counter32", "NotificationType", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15))
if mibBuilder.loadTexts: hpnicfEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: hpnicfEntityRelation.setOrganization('')
class HpnicfEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

hpnicfEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1))
hpnicfEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1))
hpnicfEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfEntRelationTable.setStatus('current')
hpnicfEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationType"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfEntityIndex"), (0, "HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if mibBuilder.loadTexts: hpnicfEntRelationEntry.setStatus('current')
hpnicfEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 1), HpnicfEntRelationType())
if mibBuilder.loadTexts: hpnicfEntRelationType.setStatus('current')
hpnicfEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: hpnicfEntityIndex.setStatus('current')
hpnicfRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRelatedEntityIndex.setStatus('current')
hpnicfEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2))
hpnicfEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1))
hpnicfEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 1, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationCompliance = hpnicfEntRelationCompliance.setStatus('current')
hpnicfEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2))
hpnicfEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15, 2, 2, 1)).setObjects(("HPN-ICF-ENTRELATION-MIB", "hpnicfRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfEntRelationGroup = hpnicfEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-ENTRELATION-MIB", hpnicfEntRelationGroup=hpnicfEntRelationGroup, hpnicfEntRelationGroups=hpnicfEntRelationGroups, hpnicfRelatedEntityIndex=hpnicfRelatedEntityIndex, hpnicfEntRelationConformance=hpnicfEntRelationConformance, hpnicfEntRelationType=hpnicfEntRelationType, HpnicfEntRelationType=HpnicfEntRelationType, hpnicfEntRelationCompliances=hpnicfEntRelationCompliances, hpnicfEntRelationObjects=hpnicfEntRelationObjects, hpnicfEntRelationCompliance=hpnicfEntRelationCompliance, hpnicfEntityIndex=hpnicfEntityIndex, hpnicfEntRelationTable=hpnicfEntRelationTable, hpnicfEntRelationEntry=hpnicfEntRelationEntry, hpnicfEntityRelation=hpnicfEntityRelation, hpnicfEntRelation=hpnicfEntRelation, PYSNMP_MODULE_ID=hpnicfEntityRelation)
