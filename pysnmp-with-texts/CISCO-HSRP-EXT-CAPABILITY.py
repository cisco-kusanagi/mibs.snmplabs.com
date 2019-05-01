#
# PySNMP MIB module CISCO-HSRP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HSRP-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, Counter64, ObjectIdentity, Integer32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Gauge32, MibIdentifier, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "Integer32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Gauge32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHsrpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10001))
ciscoHsrpExtCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHsrpExtCapability.setRevisionsDescriptions(('Added agent capabilities for IOS-XR 3.6', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-hsrp@cisco.com')
if mibBuilder.loadTexts: ciscoHsrpExtCapability.setDescription('Agent capabilities for CISCO-HSRP-EXT-MIB')
ciscoHsrpExtCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setProductRelease('Cisco IOS/ENA 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV1R0 = ciscoHsrpExtCapabilityV1R0.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpExtCapabilityV1R0.setDescription('Cisco Hsrp Ext MIB capabilities')
ciscoHsrpExtCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10001, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpExtCapabilityV3R6CRS1 = ciscoHsrpExtCapabilityV3R6CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpExtCapabilityV3R6CRS1.setDescription('Cisco Hsrp Ext MIB capabilities')
mibBuilder.exportSymbols("CISCO-HSRP-EXT-CAPABILITY", ciscoHsrpExtCapability=ciscoHsrpExtCapability, ciscoHsrpExtCapabilityV1R0=ciscoHsrpExtCapabilityV1R0, PYSNMP_MODULE_ID=ciscoHsrpExtCapability, ciscoHsrpExtCapabilityV3R6CRS1=ciscoHsrpExtCapabilityV3R6CRS1)
