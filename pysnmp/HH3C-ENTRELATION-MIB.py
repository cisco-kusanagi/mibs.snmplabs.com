#
# PySNMP MIB module HH3C-ENTRELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ENTRELATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, IpAddress, Bits, TimeTicks, Counter32, Counter64, NotificationType, ObjectIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "IpAddress", "Bits", "TimeTicks", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cEntityRelation = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 15))
if mibBuilder.loadTexts: hh3cEntityRelation.setLastUpdated('200408190000Z')
if mibBuilder.loadTexts: hh3cEntityRelation.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cEntRelationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackport", 1), ("comboport", 2))

hh3cEntRelationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1))
hh3cEntRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1))
hh3cEntRelationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cEntRelationTable.setStatus('current')
hh3cEntRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-ENTRELATION-MIB", "hh3cEntRelationType"), (0, "HH3C-ENTRELATION-MIB", "hh3cEntityIndex"), (0, "HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex"))
if mibBuilder.loadTexts: hh3cEntRelationEntry.setStatus('current')
hh3cEntRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 1), Hh3cEntRelationType())
if mibBuilder.loadTexts: hh3cEntRelationType.setStatus('current')
hh3cEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: hh3cEntityIndex.setStatus('current')
hh3cRelatedEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 15, 1, 1, 1, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRelatedEntityIndex.setStatus('current')
hh3cEntRelationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2))
hh3cEntRelationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1))
hh3cEntRelationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 1, 1)).setObjects(("HH3C-ENTRELATION-MIB", "hh3cEntRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cEntRelationCompliance = hh3cEntRelationCompliance.setStatus('current')
hh3cEntRelationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2))
hh3cEntRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 15, 2, 2, 1)).setObjects(("HH3C-ENTRELATION-MIB", "hh3cRelatedEntityIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cEntRelationGroup = hh3cEntRelationGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-ENTRELATION-MIB", hh3cEntRelationGroup=hh3cEntRelationGroup, hh3cEntRelationTable=hh3cEntRelationTable, hh3cEntRelationGroups=hh3cEntRelationGroups, PYSNMP_MODULE_ID=hh3cEntityRelation, hh3cEntityIndex=hh3cEntityIndex, hh3cEntRelationObjects=hh3cEntRelationObjects, hh3cEntRelationConformance=hh3cEntRelationConformance, hh3cEntRelationCompliance=hh3cEntRelationCompliance, hh3cRelatedEntityIndex=hh3cRelatedEntityIndex, hh3cEntRelationEntry=hh3cEntRelationEntry, hh3cEntRelationType=hh3cEntRelationType, Hh3cEntRelationType=Hh3cEntRelationType, hh3cEntRelationCompliances=hh3cEntRelationCompliances, hh3cEntityRelation=hh3cEntityRelation, hh3cEntRelation=hh3cEntRelation)
