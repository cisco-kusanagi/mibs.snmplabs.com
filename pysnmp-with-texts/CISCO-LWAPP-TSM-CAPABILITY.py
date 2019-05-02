#
# PySNMP MIB module CISCO-LWAPP-TSM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-TSM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, NotificationType, Gauge32, IpAddress, iso, Bits, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "IpAddress", "iso", "Bits", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappTsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 506))
ciscoLwappTsmCapability.setRevisions(('2006-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappTsmCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setDescription('Agent capabilities for CISCO-LWAPP-TSM-MIB. ')
ciscoLwappTsmCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 506, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappTsmCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-TSM-MIB capabilities. ')
mibBuilder.exportSymbols("CISCO-LWAPP-TSM-CAPABILITY", ciscoLwappTsmCapability=ciscoLwappTsmCapability, ciscoLwappTsmCapabilityCUWNSV4R0=ciscoLwappTsmCapabilityCUWNSV4R0, PYSNMP_MODULE_ID=ciscoLwappTsmCapability)
