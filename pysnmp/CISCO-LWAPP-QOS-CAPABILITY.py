#
# PySNMP MIB module CISCO-LWAPP-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, ObjectIdentity, Counter64, MibIdentifier, Integer32, Bits, iso, NotificationType, IpAddress, Gauge32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibIdentifier", "Integer32", "Bits", "iso", "NotificationType", "IpAddress", "Gauge32", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 505))
ciscoLwappQosCapability.setRevisions(('2010-03-25 00:00', '2006-05-15 00:00',))
if mibBuilder.loadTexts: ciscoLwappQosCapability.setLastUpdated('201003250000Z')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappQosCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 505, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setStatus('current')
ciscoLwappQosCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 505, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV7R0 = ciscoLwappQosCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV7R0 = ciscoLwappQosCapabilityCUWNSV7R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappQosCapability, ciscoLwappQosCapabilityCUWNSV7R0=ciscoLwappQosCapabilityCUWNSV7R0, ciscoLwappQosCapability=ciscoLwappQosCapability, ciscoLwappQosCapabilityCUWNSV4R0=ciscoLwappQosCapabilityCUWNSV4R0)
