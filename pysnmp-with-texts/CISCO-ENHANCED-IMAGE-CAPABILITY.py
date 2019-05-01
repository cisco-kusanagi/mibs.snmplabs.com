#
# PySNMP MIB module CISCO-ENHANCED-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENHANCED-IMAGE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity, MibIdentifier, Unsigned32, Counter32, NotificationType, iso, Bits, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Counter32", "NotificationType", "iso", "Bits", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ceImageCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 474))
ceImageCapability.setRevisions(('2005-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ceImageCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ceImageCapability.setLastUpdated('200512290000Z')
if mibBuilder.loadTexts: ceImageCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ceImageCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ceImageCapability.setDescription('Agent capabilities for CISCO-ENHANCED-IMAGE-MIB')
ceImageCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 474, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceImageCapabilityIOSXRV3R2R0CRS1 = ceImageCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceImageCapabilityIOSXRV3R2R0CRS1 = ceImageCapabilityIOSXRV3R2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ceImageCapabilityIOSXRV3R2R0CRS1.setDescription('CISCO-ENHANCED-IMAGE-MIB capabilities for IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-ENHANCED-IMAGE-CAPABILITY", ceImageCapability=ceImageCapability, PYSNMP_MODULE_ID=ceImageCapability, ceImageCapabilityIOSXRV3R2R0CRS1=ceImageCapabilityIOSXRV3R2R0CRS1)
