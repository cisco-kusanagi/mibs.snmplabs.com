#
# PySNMP MIB module TRAPEZE-NETWORKS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Gauge32, Counter64, TimeTicks, Integer32, NotificationType, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Gauge32", "Counter64", "TimeTicks", "Integer32", "NotificationType", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TrpzPhysPortNumberOrZero, TrpzPhysPortNumber = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumberOrZero", "TrpzPhysPortNumber")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 6))
trpzPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))
if mibBuilder.loadTexts: trpzPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: trpzPortMib.setOrganization('Trapeze Networks')
class TrpzPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class TrpzPortPoeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

trpzPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1))
trpzPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1))
trpzPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: trpzPortConfigTable.setStatus('current')
trpzPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortNumber"))
if mibBuilder.loadTexts: trpzPortConfigEntry.setStatus('current')
trpzPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 1), TrpzPhysPortNumber())
if mibBuilder.loadTexts: trpzPortConfigPortNumber.setStatus('current')
trpzPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 2), TrpzPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPortMode.setStatus('current')
trpzPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 3), TrpzPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPoeMode.setStatus('current')
trpzPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 4), TrpzPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigTrunkMaster.setStatus('current')
trpzPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2))
trpzPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1))
trpzPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2))
trpzPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortCompliance = trpzPortCompliance.setStatus('current')
trpzPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPoeMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortConfigGroup = trpzPortConfigGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-PORT-MIB", trpzPortGroups=trpzPortGroups, trpzPortObjects=trpzPortObjects, trpzPortConfigEntry=trpzPortConfigEntry, trpzPortConfigPortMode=trpzPortConfigPortMode, trpzPortConfigPortNumber=trpzPortConfigPortNumber, trpzPortConformance=trpzPortConformance, trpzPortCompliances=trpzPortCompliances, trpzPortConfigGroup=trpzPortConfigGroup, trpzPortConfigTable=trpzPortConfigTable, trpzPortDataObjects=trpzPortDataObjects, TrpzPortMode=TrpzPortMode, trpzPortMib=trpzPortMib, trpzPortConfigTrunkMaster=trpzPortConfigTrunkMaster, TrpzPortPoeMode=TrpzPortPoeMode, trpzPortCompliance=trpzPortCompliance, trpzPortConfigPoeMode=trpzPortConfigPoeMode, PYSNMP_MODULE_ID=trpzPortMib)
