#
# PySNMP MIB module CISCO-ENTITY-ASSET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-ASSET-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntityAssetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 300))
ciscoEntityAssetCapability.setRevisions(('2003-09-04 00:00', '2003-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityAssetCapability.setRevisionsDescriptions(('Added ceAssetCapV12R0214SXCat6K and ceAssetCapCatOSV08R0101Cat6K.', 'Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setLastUpdated('200309040000Z')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setDescription('The capabilities description of CISCO-ENTITY-ASSET-MIB.')
ceAssetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapabilityV4R00.setDescription('Entity Asset Agent capabilities for monitoring the asset information of items in the ENTITY-MIB (RFC 2737) entPhysical Table.')
ceAssetCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapV12R0214SXCat6K.setDescription('CISCO-ENTITY-ASSET-MIB capabilities.')
ceAssetCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapCatOSV08R0101Cat6K.setDescription('CISCO-ENTITY-ASSET-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-CAPABILITY", ceAssetCapCatOSV08R0101Cat6K=ceAssetCapCatOSV08R0101Cat6K, ceAssetCapabilityV4R00=ceAssetCapabilityV4R00, PYSNMP_MODULE_ID=ciscoEntityAssetCapability, ceAssetCapV12R0214SXCat6K=ceAssetCapV12R0214SXCat6K, ciscoEntityAssetCapability=ciscoEntityAssetCapability)
