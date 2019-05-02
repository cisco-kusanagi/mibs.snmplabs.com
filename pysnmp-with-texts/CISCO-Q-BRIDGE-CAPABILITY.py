#
# PySNMP MIB module CISCO-Q-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-Q-BRIDGE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, iso, Counter64, ObjectIdentity, Bits, NotificationType, MibIdentifier, Unsigned32, ModuleIdentity, TimeTicks, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "iso", "Counter64", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 389))
ciscoQBridgeCapability.setRevisions(('2011-09-27 00:00', '2011-07-27 00:00', '2008-10-28 00:00', '2004-01-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQBridgeCapability.setRevisionsDescriptions(('Added capability statement ciscoQBridgeCapV15R0001SYPCat6K.', 'Added capability statement ciscoQBridgeCapNxOSV05R0201PN7K.', 'Added ciscoQBridgeCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQBridgeCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setDescription('The capabilities description of Q-BRIDGE-MIB.')
ciscoQBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapCatOSV08R0301.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapV12R0233SXIPCat6K.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapNxOSV05R0201PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapNxOSV05R0201PN7K.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapV15R0001SYPCat6K.setDescription('Q-BRIDGE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-Q-BRIDGE-CAPABILITY", ciscoQBridgeCapCatOSV08R0301=ciscoQBridgeCapCatOSV08R0301, ciscoQBridgeCapV12R0233SXIPCat6K=ciscoQBridgeCapV12R0233SXIPCat6K, ciscoQBridgeCapV15R0001SYPCat6K=ciscoQBridgeCapV15R0001SYPCat6K, PYSNMP_MODULE_ID=ciscoQBridgeCapability, ciscoQBridgeCapNxOSV05R0201PN7K=ciscoQBridgeCapNxOSV05R0201PN7K, ciscoQBridgeCapability=ciscoQBridgeCapability)
