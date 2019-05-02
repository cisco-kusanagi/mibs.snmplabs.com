#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, IpAddress, Unsigned32, Bits, ModuleIdentity, Integer32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "IpAddress", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfDhcpSrvExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 438))
ciscoIetfDhcpSrvExtCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setRevisionsDescriptions(('Added capability definition ciscoIetfDhcpServerExtCapabilityV12R02SRC for 12.2SRC.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dhcp-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setDescription('Agent capabilities for the CISCO-IETF-DHCP-SERVER-EXT-MIB.')
ciscoIetfDhcpServerExtCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV62R00.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for Cisco CNS Network Registrar 6.2')
ciscoIetfDhcpServerExtCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV12R02SRC.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for Cisco IOS 12.2SRC')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV12R02SRC=ciscoIetfDhcpServerExtCapabilityV12R02SRC, ciscoIetfDhcpSrvExtCapability=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV62R00=ciscoIetfDhcpServerExtCapabilityV62R00)
