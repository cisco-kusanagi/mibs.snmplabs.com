#
# PySNMP MIB module PDN-IF-EXT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IF-EXT-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdnIfExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnIfExt")
pdnIfExtConfig, = mibBuilder.importSymbols("PDN-IFEXT-MIB", "pdnIfExtConfig")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, iso, TimeTicks, Bits, Gauge32, ModuleIdentity, MibIdentifier, NotificationType, Unsigned32, Integer32, Counter32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "TimeTicks", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "Counter32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnIfExtEncapConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3))
pdnIfExtEncapConfig.setRevisions(('2003-12-16 09:00', '2001-11-13 00:00', '2001-11-12 00:00', '2000-05-11 00:00', '2000-05-03 00:00', '2000-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnIfExtEncapConfig.setRevisionsDescriptions((' Jesus Pinto o Added LinkRole TEXTUAL-CONVENTION o Added pdnIfXLinkConfigTable.', ' Dragana Gough o updated object name for pdnIfMultiprotocolEncapConfigIPBridgedPDUs to pdnIfMultiprotocolEncapConfigBridgedPDUs.', ' Dragana Gough o updated comment for pdnIfMultiprotocolEncapConfigIPRoutedPDUs to fix description field o added new object pdnIfMultiprotocolEncapConfigIPBridgedPDUs to supported bridged pdus configuration', ' Dragana Gough o updated after mibwg meeting o changed table name o rearranged enum values in pdnIfExtConfigIPRoutedPDU o define groups for compliance ', ' Dragana Gough o changed enum names ', ' Dragana Gough o Initial Version ',))
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setLastUpdated('200312160900Z')
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setOrganization('Paradyne Networks MIB Working Group')
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setContactInfo('Paradyne Networks, Inc. 8545 126th Ave North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@eng.paradyne.com Editors Dragana Gough, Jesus Pinto')
if mibBuilder.loadTexts: pdnIfExtEncapConfig.setDescription('This Mib is created to facilitate configuration of interface related objects.')
class PdnLinkRole(TextualConvention, Integer32):
    description = 'Objects defined with this textual convention are used to indicate the usage of the link. uplink (1) : interface is used as uplink other (2) : interface is used for something other than uplink (e.g, subtending). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("uplink", 1), ("other", 2))

pdnIfMultiprotocolEncapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1), )
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigTable.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigTable.setDescription(' This table that contains additional interface configuration information. ')
pdnIfMultiprotocolEncapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigEntry.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigEntry.setDescription(' There will be one of these rows for each interface that supports RFC1483. ')
pdnIfMultiprotocolEncapConfigIPRoutedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setDescription("In the upstream direction user can configure the IP routed PDUs in the LLC SNAP encapsulation or VC Based Multiplexing encapsulation (RFC1483). If neither is configured 'none' is used. The direction is determined by the transmit direction. Initialy this object was developed for the endpoint use where the transmit direction is upstream. This object could be used for CO type equipment where the direction would be downstream.")
pdnIfMultiprotocolEncapConfigBridgedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("llcSnap", 2), ("vcBasedMultiplexing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigBridgedPDUs.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapConfigBridgedPDUs.setDescription("In the transmit direction user can configure the IP routed PDUs in the LLC SNAP encapsulation or VC Based Multiplexing encapsulation (RFC1483). If neither is configured 'none' is used.")
pdnIfXLinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3), )
if mibBuilder.loadTexts: pdnIfXLinkConfigTable.setStatus('current')
if mibBuilder.loadTexts: pdnIfXLinkConfigTable.setDescription('This table contains configuration information for interfaces that are capable of switch roles at run-time. ')
pdnIfXLinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfXLinkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: pdnIfXLinkConfigEntry.setDescription('An entry in this table represents an interface that is capable of being used as an uplink. Typically, this table will contain entries only for interfaces that are capable of switching roles. ')
pdnIfXLinkConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1, 1), PdnLinkRole()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIfXLinkConfigRole.setStatus('current')
if mibBuilder.loadTexts: pdnIfXLinkConfigRole.setDescription('This object allows users to configure the role (e.g., uplink) intended for this interface. ')
pdnIfMultiprotocolEncapMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2))
pdnIfMultiprotocolEncapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1))
pdnIfMultiprotocolEncapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2))
pdnIfXConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4))
pdnIfXConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1))
pdnIfMultiprotocolEncapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapsulationOptionalGroup"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapCompliance = pdnIfMultiprotocolEncapCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapCompliance.setDescription(' The compliance statement for SNMP entities which support RFC1483 Multiprotocol Encapsulation over ATM adaptation layer 5.')
pdnIfMultiprotocolEncapsulationOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigIPRoutedPDUs"), ("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigBridgedPDUs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfMultiprotocolEncapsulationOptionalGroup = pdnIfMultiprotocolEncapsulationOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIfMultiprotocolEncapsulationOptionalGroup.setDescription('A collection of objects providing optional configuration information about multiprotocol interface link.')
pdnIfXLinkConfigOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1, 1)).setObjects(("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfXLinkConfigOptionalGroup = pdnIfXLinkConfigOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIfXLinkConfigOptionalGroup.setDescription('configuration information for this optional group.')
mibBuilder.exportSymbols("PDN-IF-EXT-CONFIG-MIB", pdnIfXLinkConfigOptionalGroup=pdnIfXLinkConfigOptionalGroup, pdnIfXLinkConfigRole=pdnIfXLinkConfigRole, pdnIfXLinkConfigTable=pdnIfXLinkConfigTable, pdnIfXLinkConfigEntry=pdnIfXLinkConfigEntry, pdnIfMultiprotocolEncapConfigIPRoutedPDUs=pdnIfMultiprotocolEncapConfigIPRoutedPDUs, pdnIfXConfigMIBConformance=pdnIfXConfigMIBConformance, pdnIfMultiprotocolEncapCompliance=pdnIfMultiprotocolEncapCompliance, pdnIfMultiprotocolEncapConfigEntry=pdnIfMultiprotocolEncapConfigEntry, PdnLinkRole=PdnLinkRole, pdnIfMultiprotocolEncapMIBGroups=pdnIfMultiprotocolEncapMIBGroups, pdnIfXConfigMIBGroups=pdnIfXConfigMIBGroups, pdnIfMultiprotocolEncapConfigTable=pdnIfMultiprotocolEncapConfigTable, pdnIfExtEncapConfig=pdnIfExtEncapConfig, PYSNMP_MODULE_ID=pdnIfExtEncapConfig, pdnIfMultiprotocolEncapConfigBridgedPDUs=pdnIfMultiprotocolEncapConfigBridgedPDUs, pdnIfMultiprotocolEncapMIBConformance=pdnIfMultiprotocolEncapMIBConformance, pdnIfMultiprotocolEncapCompliances=pdnIfMultiprotocolEncapCompliances, pdnIfMultiprotocolEncapsulationOptionalGroup=pdnIfMultiprotocolEncapsulationOptionalGroup)
