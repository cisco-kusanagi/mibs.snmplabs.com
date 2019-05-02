#
# PySNMP MIB module CISCO-HSRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HSRP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, Counter32, Bits, Counter64, ModuleIdentity, MibIdentifier, ObjectIdentity, IpAddress, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter32", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHsrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
ciscoHsrpCapability.setRevisions(('2007-11-27 00:00', '1998-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHsrpCapability.setRevisionsDescriptions(('Added agent capability for IOS-XR 3.6', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHsrpCapability.setLastUpdated('200711270000Z')
if mibBuilder.loadTexts: ciscoHsrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHsrpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-hsrp@cisco.com')
if mibBuilder.loadTexts: ciscoHsrpCapability.setDescription('Agent capabilities for CISCO-HSRP-MIB')
ciscoHsrpCapabilityV12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setProductRelease('Cisco IOS 12.0(3)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV12R0 = ciscoHsrpCapabilityV12R0.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpCapabilityV12R0.setDescription('Cisco Hsrp MIB capabilities')
ciscoHsrpCapabilityV3R6CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHsrpCapabilityV3R6CRS1 = ciscoHsrpCapabilityV3R6CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoHsrpCapabilityV3R6CRS1.setDescription('Cisco Hsrp MIB capabilities')
mibBuilder.exportSymbols("CISCO-HSRP-CAPABILITY", ciscoHsrpCapabilityV3R6CRS1=ciscoHsrpCapabilityV3R6CRS1, ciscoHsrpCapability=ciscoHsrpCapability, ciscoHsrpCapabilityV12R0=ciscoHsrpCapabilityV12R0, PYSNMP_MODULE_ID=ciscoHsrpCapability)
