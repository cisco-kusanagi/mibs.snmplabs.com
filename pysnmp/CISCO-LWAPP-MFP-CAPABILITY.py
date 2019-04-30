#
# PySNMP MIB module CISCO-LWAPP-MFP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MFP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, iso, ModuleIdentity, IpAddress, Bits, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, NotificationType, Integer32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "ModuleIdentity", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappMfpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 504))
ciscoLwappMfpCapability.setRevisions(('2006-05-16 00:00',))
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappMfpCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 504, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MFP-CAPABILITY", ciscoLwappMfpCapabilityCUWNSV4R0=ciscoLwappMfpCapabilityCUWNSV4R0, ciscoLwappMfpCapability=ciscoLwappMfpCapability, PYSNMP_MODULE_ID=ciscoLwappMfpCapability)
