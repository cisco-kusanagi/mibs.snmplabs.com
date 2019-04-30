#
# PySNMP MIB module CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibIdentifier, TimeTicks, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, IpAddress, Counter32, Integer32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter32", "Integer32", "Bits", "Unsigned32")
TextualConvention, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "DisplayString")
ciscoLwappClientRoamingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 501))
ciscoLwappClientRoamingCapability.setRevisions(('2010-02-06 00:00', '2006-05-09 00:00',))
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setLastUpdated('201002060000Z')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappClientRoamingCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setStatus('current')
ciscoLwappClientRoamingCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY", ciscoLwappClientRoamingCapabilityCUWNSV4R0=ciscoLwappClientRoamingCapabilityCUWNSV4R0, ciscoLwappClientRoamingCapability=ciscoLwappClientRoamingCapability, PYSNMP_MODULE_ID=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapabilityCUWNSV7R0=ciscoLwappClientRoamingCapabilityCUWNSV7R0)
