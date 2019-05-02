#
# PySNMP MIB module CISCO-LWAPP-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, Bits, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, ObjectIdentity, Counter64, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 505))
ciscoLwappQosCapability.setRevisions(('2010-03-25 00:00', '2006-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappQosCapability.setRevisionsDescriptions(('Added ciscoLwappQosCapabilityCUWNSV7RO', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappQosCapability.setLastUpdated('201003250000Z')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setDescription('Agent capabilities for CISCO-LWAPP-QOS-MIB.')
ciscoLwappQosCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 505, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappQosCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-QOS-MIB capabilities.')
ciscoLwappQosCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 505, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV7R0 = ciscoLwappQosCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV7R0 = ciscoLwappQosCapabilityCUWNSV7R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappQosCapabilityCUWNSV7R0.setDescription('CISCO-LWAPP-QOS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappQosCapability, ciscoLwappQosCapabilityCUWNSV4R0=ciscoLwappQosCapabilityCUWNSV4R0, ciscoLwappQosCapabilityCUWNSV7R0=ciscoLwappQosCapabilityCUWNSV7R0, ciscoLwappQosCapability=ciscoLwappQosCapability)
