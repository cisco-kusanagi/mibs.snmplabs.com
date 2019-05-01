#
# PySNMP MIB module CISCO-LWAPP-MFP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MFP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:05:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter32, ModuleIdentity, TimeTicks, iso, Integer32, MibIdentifier, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "iso", "Integer32", "MibIdentifier", "Bits", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappMfpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 504))
ciscoLwappMfpCapability.setRevisions(('2006-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappMfpCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setLastUpdated('200605160000Z')
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setDescription('Agent capabilities for CISCO-LWAPP-MFP-MIB. ')
ciscoLwappMfpCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 504, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappMfpCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-MFP-MIB capabilities')
mibBuilder.exportSymbols("CISCO-LWAPP-MFP-CAPABILITY", ciscoLwappMfpCapabilityCUWNSV4R0=ciscoLwappMfpCapabilityCUWNSV4R0, ciscoLwappMfpCapability=ciscoLwappMfpCapability, PYSNMP_MODULE_ID=ciscoLwappMfpCapability)
