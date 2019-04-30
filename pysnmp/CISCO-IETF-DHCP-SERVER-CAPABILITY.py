#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-DHCP-SERVER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, Bits, NotificationType, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, Gauge32, IpAddress, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "Gauge32", "IpAddress", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfDhcpSrvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 439))
ciscoIetfDhcpSrvCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setLastUpdated('200702141200Z')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfDhcpServerCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setStatus('current')
ciscoIetfDhcpServerCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-CAPABILITY", ciscoIetfDhcpServerCapabilityV62R00=ciscoIetfDhcpServerCapabilityV62R00, ciscoIetfDhcpSrvCapability=ciscoIetfDhcpSrvCapability, ciscoIetfDhcpServerCapabilityV12R02SRC=ciscoIetfDhcpServerCapabilityV12R02SRC, PYSNMP_MODULE_ID=ciscoIetfDhcpSrvCapability)
