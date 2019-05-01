#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-DHCP-SERVER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter64, ObjectIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, NotificationType, Unsigned32, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "NotificationType", "Unsigned32", "TimeTicks", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfDhcpSrvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 439))
ciscoIetfDhcpSrvCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setRevisionsDescriptions(('Added capability definition ciscoIetfDhcpServerCapabilityV12R02SRC for 12.2SRC.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dhcp-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setDescription('Agent capabilities for the CISCO-IETF-DHCP-SERVER-MIB.')
ciscoIetfDhcpServerCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerCapabilityV62R00.setDescription('CISCO-IETF-DHCP-SERVER-MIB capabilities for Cisco CNS Network Registrar 6.2')
ciscoIetfDhcpServerCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerCapabilityV12R02SRC.setDescription('CISCO-IETF-DHCP-SERVER-MIB capabilities for Cisco IOS 12.2SRC')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-CAPABILITY", ciscoIetfDhcpServerCapabilityV62R00=ciscoIetfDhcpServerCapabilityV62R00, ciscoIetfDhcpServerCapabilityV12R02SRC=ciscoIetfDhcpServerCapabilityV12R02SRC, ciscoIetfDhcpSrvCapability=ciscoIetfDhcpSrvCapability, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvCapability)
