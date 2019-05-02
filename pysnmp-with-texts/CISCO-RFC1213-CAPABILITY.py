#
# PySNMP MIB module CISCO-RFC1213-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RFC1213-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, ModuleIdentity, NotificationType, IpAddress, MibIdentifier, Counter32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "MibIdentifier", "Counter32", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRFC1213Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 101))
ciscoRFC1213Capability.setRevisions(('2003-10-27 16:00', '2001-09-08 16:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1213Capability.setRevisionsDescriptions(('Added ciscoRFC1213CapCatOSV08R0101.', 'Zero length for sysName disallowed.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1213Capability.setLastUpdated('200310271600Z')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setDescription('Agent capabilities for the RFC1213-MIB (MIB-II)')
ciscoRFC1213CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1213CapabilityV10R02.setDescription('RFC 1213 (MIB II) capabilities')
ciscoRFC1213CapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1213CapabilityV12R02.setDescription('RFC 1213 (MIB II) capabilities')
ciscoRFC1213CapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1213CapabilityV12R00S.setDescription('RFC 1213 (MIB II) capabilities')
ciscoRFC1213CapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1213CapabilityV12R01.setDescription('RFC 1213 (MIB II) capabilities')
ciscoRFC1213CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1213CapCatOSV08R0101.setDescription('RFC1213-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-RFC1213-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1213Capability, ciscoRFC1213CapabilityV12R00S=ciscoRFC1213CapabilityV12R00S, ciscoRFC1213CapCatOSV08R0101=ciscoRFC1213CapCatOSV08R0101, ciscoRFC1213Capability=ciscoRFC1213Capability, ciscoRFC1213CapabilityV12R01=ciscoRFC1213CapabilityV12R01, ciscoRFC1213CapabilityV12R02=ciscoRFC1213CapabilityV12R02, ciscoRFC1213CapabilityV10R02=ciscoRFC1213CapabilityV10R02)
