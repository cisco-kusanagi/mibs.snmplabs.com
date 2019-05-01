#
# PySNMP MIB module CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, Unsigned32, Counter32, TimeTicks, Bits, IpAddress, Integer32, iso, ModuleIdentity, NotificationType, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "TimeTicks", "Bits", "IpAddress", "Integer32", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeInterval")
ciscoLwappClientRoamingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 501))
ciscoLwappClientRoamingCapability.setRevisions(('2010-02-06 00:00', '2006-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setRevisionsDescriptions(('Added ciscoLwappClientRoamingCapabilityCUWNSV7R0', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setLastUpdated('201002060000Z')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setDescription('Agent capabilities for CISCO-LWAPP-CLIENT-ROAMING-MIB.')
ciscoLwappClientRoamingCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-CLIENT-ROAMING-MIB capabilities.')
ciscoLwappClientRoamingCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapabilityCUWNSV7R0.setDescription('CISCO-LWAPP-CLIENT-ROAMING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY", ciscoLwappClientRoamingCapability=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapabilityCUWNSV7R0=ciscoLwappClientRoamingCapabilityCUWNSV7R0, PYSNMP_MODULE_ID=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapabilityCUWNSV4R0=ciscoLwappClientRoamingCapabilityCUWNSV4R0)
