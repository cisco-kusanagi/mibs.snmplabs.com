#
# PySNMP MIB module CISCO-DHCP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DHCP-SNOOPING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, TimeTicks, Bits, Gauge32, MibIdentifier, Unsigned32, NotificationType, Integer32, Counter32, IpAddress, ObjectIdentity, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Integer32", "Counter32", "IpAddress", "ObjectIdentity", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDhcpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 383))
ciscoDhcpSnoopingCapability.setRevisions(('2011-09-28 00:00', '2010-10-27 00:00', '2010-03-18 00:00', '2008-03-20 00:00', '2007-07-02 09:00', '2006-06-28 00:00', '2004-03-09 00:00',))
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setLastUpdated('201109280000Z')
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
cdsCapabilityV08R0301Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          of PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setStatus('current')
cdsCapabilityV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setStatus('current')
cdsCapabilityV08R0601Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setStatus('current')
cdsCapabilityV08R0601Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setStatus('current')
cdsCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setStatus('current')
cdsCapabilityV08R0701Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setStatus('current')
cdsCapabilityV08R0701Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setStatus('current')
cdsCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setStatus('current')
cdsCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setStatus('current')
cdsCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-DHCP-SNOOPING-CAPABILITY", cdsCapabilityV08R0601Cat6kPfc3=cdsCapabilityV08R0601Cat6kPfc3, cdsCapabilityV08R0601Cat6kPfc=cdsCapabilityV08R0601Cat6kPfc, cdsCapabilityV08R0701Cat6kPfc=cdsCapabilityV08R0701Cat6kPfc, PYSNMP_MODULE_ID=ciscoDhcpSnoopingCapability, cdsCapabilityV08R0301Cat6kPfc=cdsCapabilityV08R0301Cat6kPfc, cdsCapabilityV08R0701Cat6kPfc3=cdsCapabilityV08R0701Cat6kPfc3, ciscoDhcpSnoopingCapability=ciscoDhcpSnoopingCapability, cdsCapV12R0250SYPCat6k=cdsCapV12R0250SYPCat6k, cdsCapV15R0001SYPCat6k=cdsCapV15R0001SYPCat6k, cdsCapV12R0233SXHPCat6k=cdsCapV12R0233SXHPCat6k, cdsCapV12R0233SXI4PCat6k=cdsCapV12R0233SXI4PCat6k, cdsCapabilityV08R0301Cat6kPfc3=cdsCapabilityV08R0301Cat6kPfc3)
