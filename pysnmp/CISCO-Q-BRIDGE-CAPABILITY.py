#
# PySNMP MIB module CISCO-Q-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-Q-BRIDGE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, Counter64, iso, Bits, NotificationType, Integer32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "Bits", "NotificationType", "Integer32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 389))
ciscoQBridgeCapability.setRevisions(('2011-09-27 00:00', '2011-07-27 00:00', '2008-10-28 00:00', '2004-01-15 00:00',))
if mibBuilder.loadTexts: ciscoQBridgeCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setOrganization('Cisco Systems, Inc.')
ciscoQBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setStatus('current')
ciscoQBridgeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setStatus('current')
ciscoQBridgeCapNxOSV05R0201PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setStatus('current')
ciscoQBridgeCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-Q-BRIDGE-CAPABILITY", PYSNMP_MODULE_ID=ciscoQBridgeCapability, ciscoQBridgeCapNxOSV05R0201PN7K=ciscoQBridgeCapNxOSV05R0201PN7K, ciscoQBridgeCapability=ciscoQBridgeCapability, ciscoQBridgeCapCatOSV08R0301=ciscoQBridgeCapCatOSV08R0301, ciscoQBridgeCapV15R0001SYPCat6K=ciscoQBridgeCapV15R0001SYPCat6K, ciscoQBridgeCapV12R0233SXIPCat6K=ciscoQBridgeCapV12R0233SXIPCat6K)
