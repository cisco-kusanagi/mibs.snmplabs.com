#
# PySNMP MIB module CISCO-SWITCH-MULTICAST-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-MULTICAST-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, iso, Bits, Counter32, Gauge32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "iso", "Bits", "Counter32", "Gauge32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchMulticastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 546))
ciscoSwitchMulticastCapability.setRevisions(('2010-11-11 00:00', '2008-10-30 00:00', '2007-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setRevisionsDescriptions(('Added capability statement cswmCapabilityV12R0250SYPCat6kPfc4.', 'Added capability statement cswmCapabilityV12R0233SXIPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setLastUpdated('201011110000Z')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setDescription('The capabilities description of CISCO-SWITCH-MULTICAST-MIB.')
cswmCapabilityV12R0219SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0219SXHPCat6k.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
cswmCapabilityV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0233SXIPCat6k.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
cswmCapabilityV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: cswmCapabilityV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-MULTICAST-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-MULTICAST-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchMulticastCapability, cswmCapabilityV12R0233SXIPCat6k=cswmCapabilityV12R0233SXIPCat6k, cswmCapabilityV12R0250SYPCat6kPfc4=cswmCapabilityV12R0250SYPCat6kPfc4, ciscoSwitchMulticastCapability=ciscoSwitchMulticastCapability, cswmCapabilityV12R0219SXHPCat6k=cswmCapabilityV12R0219SXHPCat6k)
