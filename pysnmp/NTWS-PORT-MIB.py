#
# PySNMP MIB module NTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NtwsPhysPortNumber, NtwsPhysPortNumberOrZero = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumber", "NtwsPhysPortNumberOrZero")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, Counter32, Counter64, TimeTicks, MibIdentifier, ModuleIdentity, NotificationType, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "Counter64", "TimeTicks", "MibIdentifier", "ModuleIdentity", "NotificationType", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6))
ntwsPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2007-08-16 00:02', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: ntwsPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: ntwsPortMib.setOrganization('Nortel Networks')
class NtwsPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class NtwsPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

ntwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1))
ntwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1))
ntwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsPortConfigTable.setStatus('current')
ntwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-PORT-MIB", "ntwsPortConfigPortNumber"))
if mibBuilder.loadTexts: ntwsPortConfigEntry.setStatus('current')
ntwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 1), NtwsPhysPortNumber())
if mibBuilder.loadTexts: ntwsPortConfigPortNumber.setStatus('current')
ntwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 2), NtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPortMode.setStatus('current')
ntwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 3), NtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPoeMode.setStatus('current')
ntwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 4), NtwsPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigTrunkMaster.setStatus('current')
ntwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2))
ntwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1))
ntwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2))
ntwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortCompliance = ntwsPortCompliance.setStatus('current')
ntwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigPortMode"), ("NTWS-PORT-MIB", "ntwsPortConfigPoeMode"), ("NTWS-PORT-MIB", "ntwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortConfigGroup = ntwsPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-PORT-MIB", ntwsPortConfigEntry=ntwsPortConfigEntry, ntwsPortConfigGroup=ntwsPortConfigGroup, NtwsPortPoeMode=NtwsPortPoeMode, ntwsPortCompliances=ntwsPortCompliances, ntwsPortConfigPoeMode=ntwsPortConfigPoeMode, NtwsPortMode=NtwsPortMode, ntwsPortConfigTable=ntwsPortConfigTable, ntwsPortConfigTrunkMaster=ntwsPortConfigTrunkMaster, ntwsPortCompliance=ntwsPortCompliance, ntwsPortObjects=ntwsPortObjects, ntwsPortConformance=ntwsPortConformance, ntwsPortGroups=ntwsPortGroups, PYSNMP_MODULE_ID=ntwsPortMib, ntwsPortConfigPortMode=ntwsPortConfigPortMode, ntwsPortMib=ntwsPortMib, ntwsPortConfigPortNumber=ntwsPortConfigPortNumber, ntwsPortDataObjects=ntwsPortDataObjects)
