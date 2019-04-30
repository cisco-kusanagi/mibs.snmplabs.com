#
# PySNMP MIB module CISCO-SWITCH-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Bits, Counter64, NotificationType, ObjectIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 541))
ciscoSwitchQosCapability.setRevisions(('2014-10-03 00:00', '2014-04-03 00:00', '2013-10-16 00:00', '2011-09-26 00:00', '2010-11-17 00:00', '2010-03-19 00:00', '2008-06-04 00:00', '2007-06-29 00:00',))
if mibBuilder.loadTexts: ciscoSwitchQosCapability.setLastUpdated('201410030000Z')
if mibBuilder.loadTexts: ciscoSwitchQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoSwitchQosCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXHPCat6k = ciscoSwitchQosCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXHPCat6k = ciscoSwitchQosCapV12R0233SXHPCat6k.setStatus('current')
ciscoSwitchQosCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXIPCat6k = ciscoSwitchQosCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXIPCat6k = ciscoSwitchQosCapV12R0233SXIPCat6k.setStatus('current')
ciscoSwitchQosCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXI4PCat6k = ciscoSwitchQosCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0233SXI4PCat6k = ciscoSwitchQosCapV12R0233SXI4PCat6k.setStatus('current')
ciscoSwitchQosCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0250SYPCat6k = ciscoSwitchQosCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV12R0250SYPCat6k = ciscoSwitchQosCapV12R0250SYPCat6k.setStatus('current')
ciscoSwitchQosCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV15R0001SYPCat6k = ciscoSwitchQosCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV15R0001SYPCat6k = ciscoSwitchQosCapV15R0001SYPCat6k.setStatus('current')
ciscoSwitchQosCapV5R0003U0501gPN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV5R0003U0501gPN3K = ciscoSwitchQosCapV5R0003U0501gPN3K.setProductRelease('Cisco NX-OS 5.0(3)U5(1g) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV5R0003U0501gPN3K = ciscoSwitchQosCapV5R0003U0501gPN3K.setStatus('current')
ciscoSwitchQosCapV6R0002U0101PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV6R0002U0101PN3K = ciscoSwitchQosCapV6R0002U0101PN3K.setProductRelease('Cisco NX-OS 6.0(2)U1(1) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV6R0002U0101PN3K = ciscoSwitchQosCapV6R0002U0101PN3K.setStatus('current')
ciscoSwitchQosCapV06R0002U0201PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV06R0002U0201PN3K = ciscoSwitchQosCapV06R0002U0201PN3K.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus 3000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapV06R0002U0201PN3K = ciscoSwitchQosCapV06R0002U0201PN3K.setStatus('current')
ciscoSwitchQosCapNxOSV06R0210PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 541, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapNxOSV06R0210PN7K = ciscoSwitchQosCapNxOSV06R0210PN7K.setProductRelease('Cisco NX-OS 6.2(10) on Nexus 7000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchQosCapNxOSV06R0210PN7K = ciscoSwitchQosCapNxOSV06R0210PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-QOS-CAPABILITY", ciscoSwitchQosCapV06R0002U0201PN3K=ciscoSwitchQosCapV06R0002U0201PN3K, ciscoSwitchQosCapV12R0233SXI4PCat6k=ciscoSwitchQosCapV12R0233SXI4PCat6k, ciscoSwitchQosCapV12R0233SXHPCat6k=ciscoSwitchQosCapV12R0233SXHPCat6k, ciscoSwitchQosCapV12R0233SXIPCat6k=ciscoSwitchQosCapV12R0233SXIPCat6k, ciscoSwitchQosCapNxOSV06R0210PN7K=ciscoSwitchQosCapNxOSV06R0210PN7K, ciscoSwitchQosCapV12R0250SYPCat6k=ciscoSwitchQosCapV12R0250SYPCat6k, ciscoSwitchQosCapV6R0002U0101PN3K=ciscoSwitchQosCapV6R0002U0101PN3K, PYSNMP_MODULE_ID=ciscoSwitchQosCapability, ciscoSwitchQosCapV5R0003U0501gPN3K=ciscoSwitchQosCapV5R0003U0501gPN3K, ciscoSwitchQosCapability=ciscoSwitchQosCapability, ciscoSwitchQosCapV15R0001SYPCat6k=ciscoSwitchQosCapV15R0001SYPCat6k)
