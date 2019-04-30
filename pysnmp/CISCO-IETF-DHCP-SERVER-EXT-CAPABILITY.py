#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, Bits, ObjectIdentity, Unsigned32, Counter64, NotificationType, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfDhcpSrvExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 438))
ciscoIetfDhcpSrvExtCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfDhcpServerExtCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setStatus('current')
ciscoIetfDhcpServerExtCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY", ciscoIetfDhcpSrvExtCapability=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV12R02SRC=ciscoIetfDhcpServerExtCapabilityV12R02SRC, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV62R00=ciscoIetfDhcpServerExtCapabilityV62R00)
