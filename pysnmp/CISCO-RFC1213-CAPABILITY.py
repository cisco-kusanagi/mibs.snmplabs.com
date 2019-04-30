#
# PySNMP MIB module CISCO-RFC1213-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RFC1213-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibIdentifier, Integer32, Counter64, Counter32, iso, IpAddress, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, TimeTicks, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "Counter32", "iso", "IpAddress", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "TimeTicks", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFC1213Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 101))
ciscoRFC1213Capability.setRevisions(('2003-10-27 16:00', '2001-09-08 16:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRFC1213Capability.setLastUpdated('200310271600Z')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1213CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setStatus('current')
ciscoRFC1213CapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setStatus('current')
ciscoRFC1213CapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setStatus('current')
ciscoRFC1213CapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setStatus('current')
ciscoRFC1213CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1213-CAPABILITY", ciscoRFC1213CapabilityV12R00S=ciscoRFC1213CapabilityV12R00S, ciscoRFC1213Capability=ciscoRFC1213Capability, PYSNMP_MODULE_ID=ciscoRFC1213Capability, ciscoRFC1213CapabilityV12R02=ciscoRFC1213CapabilityV12R02, ciscoRFC1213CapCatOSV08R0101=ciscoRFC1213CapCatOSV08R0101, ciscoRFC1213CapabilityV12R01=ciscoRFC1213CapabilityV12R01, ciscoRFC1213CapabilityV10R02=ciscoRFC1213CapabilityV10R02)
