#
# PySNMP MIB module CISCO-LWAPP-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-RF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, MibIdentifier, Counter64, Counter32, ObjectIdentity, TimeTicks, Bits, iso, ModuleIdentity, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "MibIdentifier", "Counter64", "Counter32", "ObjectIdentity", "TimeTicks", "Bits", "iso", "ModuleIdentity", "Unsigned32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 23999))
ciscoLwappRFCapability.setRevisions(('2012-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappRFCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappRFCapability.setLastUpdated('201202280000Z')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setDescription('Agent capabilities for CISCO-LWAPP-RF-MIB.')
ciscoLwappRFCapabilityCUWNSV7R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 23999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.3 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappRFCapabilityCUWNSV7R3.setDescription('CISCO-LWAPP-RF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-RF-CAPABILITY", ciscoLwappRFCapability=ciscoLwappRFCapability, ciscoLwappRFCapabilityCUWNSV7R3=ciscoLwappRFCapabilityCUWNSV7R3, PYSNMP_MODULE_ID=ciscoLwappRFCapability)
