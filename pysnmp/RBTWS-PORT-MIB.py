#
# PySNMP MIB module RBTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:45:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, TimeTicks, iso, ObjectIdentity, Counter32, MibIdentifier, Gauge32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6))
rbtwsPortMib.setRevisions(('2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: rbtwsPortMib.setLastUpdated('200805191722Z')
if mibBuilder.loadTexts: rbtwsPortMib.setOrganization('Enterasys Networks')
class RbtwsPhysPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class RbtwsPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class RbtwsPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

rbtwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1))
rbtwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1))
rbtwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsPortConfigTable.setStatus('current')
rbtwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-PORT-MIB", "rbtwsPortConfigPortNumber"))
if mibBuilder.loadTexts: rbtwsPortConfigEntry.setStatus('current')
rbtwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 1), RbtwsPhysPortNumber())
if mibBuilder.loadTexts: rbtwsPortConfigPortNumber.setStatus('current')
rbtwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 2), RbtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPortMode.setStatus('current')
rbtwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 3), RbtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPoeMode.setStatus('current')
rbtwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 4), RbtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigTrunkMaster.setStatus('current')
rbtwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2))
rbtwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1))
rbtwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2))
rbtwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortCompliance = rbtwsPortCompliance.setStatus('current')
rbtwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigPortMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigPoeMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortConfigGroup = rbtwsPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("RBTWS-PORT-MIB", RbtwsPortPoeMode=RbtwsPortPoeMode, rbtwsPortConfigTrunkMaster=rbtwsPortConfigTrunkMaster, rbtwsPortGroups=rbtwsPortGroups, PYSNMP_MODULE_ID=rbtwsPortMib, rbtwsPortMib=rbtwsPortMib, rbtwsPortConfigPortNumber=rbtwsPortConfigPortNumber, RbtwsPhysPortNumber=RbtwsPhysPortNumber, rbtwsPortObjects=rbtwsPortObjects, RbtwsPortMode=RbtwsPortMode, rbtwsPortConfigPoeMode=rbtwsPortConfigPoeMode, rbtwsPortConformance=rbtwsPortConformance, rbtwsPortConfigPortMode=rbtwsPortConfigPortMode, rbtwsPortConfigTable=rbtwsPortConfigTable, rbtwsPortDataObjects=rbtwsPortDataObjects, rbtwsPortConfigEntry=rbtwsPortConfigEntry, rbtwsPortCompliance=rbtwsPortCompliance, rbtwsPortCompliances=rbtwsPortCompliances, rbtwsPortConfigGroup=rbtwsPortConfigGroup)
