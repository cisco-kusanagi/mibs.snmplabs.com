#
# PySNMP MIB module PDN-IF-EXT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IF-EXT-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdnIfExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnIfExt")
pdnIfExtConfig, = mibBuilder.importSymbols("PDN-IFEXT-MIB", "pdnIfExtConfig")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Gauge32, iso, ObjectIdentity, Unsigned32, TimeTicks, Counter32, Counter64, NotificationType, Bits, ModuleIdentity, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "iso", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "Counter64", "NotificationType", "Bits", "ModuleIdentity", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnIfExtEncapConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3))
pdnIfExtEncapConfig.setRevisions(('2003-12-16 09:00', '2001-11-13 00:00', '2001-11-12 00:00', '2000-05-11 00:00', '2000-05-03 00:00', '2000-05-02 00:00',))
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setLastUpdated('200312160900Z')
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setOrganization('Paradyne Networks MIB Working Group')
class PdnLinkRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("uplink", 1), ("other", 2))

pdnIfMultiprotocolEncapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1), )
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigTable.setStatus('current')
pdnIfMultiprotocolEncapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigEntry.setStatus('current')
pdnIfMultiprotocolEncapConfigIPRoutedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setStatus('current')
pdnIfMultiprotocolEncapConfigBridgedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigBridgedPDUs.setStatus('current')
pdnIfXLinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3), )
if mibBuilder.loadTexts: pdnIfXLinkConfigTable.setStatus('current')
pdnIfXLinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfXLinkConfigEntry.setStatus('current')
pdnIfXLinkConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1, 1), PdnLinkRole()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfXLinkConfigRole.setStatus('current')
pdnIfMultiprotocolEncapMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2))
pdnIfMultiprotocolEncapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1))
pdnIfMultiprotocolEncapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2))
pdnIfXConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4))
pdnIfXConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1))
pdnIfMultiprotocolEncapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapsulationOptionalGroup"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapCompliance = pdnIfMultiprotocolEncapCompliance.setStatus('current')
pdnIfMultiprotocolEncapsulationOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigIPRoutedPDUs"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigBridgedPDUs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapsulationOptionalGroup = pdnIfMultiprotocolEncapsulationOptionalGroup.setStatus('current')
pdnIfXLinkConfigOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfXLinkConfigOptionalGroup = pdnIfXLinkConfigOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IF-EXT-CONFIG-MIB", pdnIfMultiprotocolEncapConfigBridgedPDUs=pdnIfMultiprotocolEncapConfigBridgedPDUs, pdnIfXLinkConfigRole=pdnIfXLinkConfigRole, pdnIfMultiprotocolEncapMIBConformance=pdnIfMultiprotocolEncapMIBConformance, pdnIfMultiprotocolEncapCompliance=pdnIfMultiprotocolEncapCompliance, pdnIfExtEncapConfig=pdnIfExtEncapConfig, pdnIfXConfigMIBConformance=pdnIfXConfigMIBConformance, pdnIfMultiprotocolEncapConfigEntry=pdnIfMultiprotocolEncapConfigEntry, pdnIfXConfigMIBGroups=pdnIfXConfigMIBGroups, pdnIfMultiprotocolEncapConfigIPRoutedPDUs=pdnIfMultiprotocolEncapConfigIPRoutedPDUs, pdnIfXLinkConfigEntry=pdnIfXLinkConfigEntry, pdnIfMultiprotocolEncapConfigTable=pdnIfMultiprotocolEncapConfigTable, PYSNMP_MODULE_ID=pdnIfExtEncapConfig, pdnIfMultiprotocolEncapMIBGroups=pdnIfMultiprotocolEncapMIBGroups, PdnLinkRole=PdnLinkRole, pdnIfXLinkConfigTable=pdnIfXLinkConfigTable, pdnIfMultiprotocolEncapCompliances=pdnIfMultiprotocolEncapCompliances, pdnIfMultiprotocolEncapsulationOptionalGroup=pdnIfMultiprotocolEncapsulationOptionalGroup, pdnIfXLinkConfigOptionalGroup=pdnIfXLinkConfigOptionalGroup)
