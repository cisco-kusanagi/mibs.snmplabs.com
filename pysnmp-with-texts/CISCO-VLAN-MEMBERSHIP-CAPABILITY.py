#
# PySNMP MIB module CISCO-VLAN-MEMBERSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-MEMBERSHIP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, TimeTicks, NotificationType, Bits, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, MibIdentifier, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "NotificationType", "Bits", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "MibIdentifier", "iso", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanMembershipCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 316))
ciscoVlanMembershipCapability.setRevisions(('2010-10-29 00:00', '2010-03-21 00:00', '2007-07-12 00:00', '2004-01-15 00:00', '2003-09-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setRevisionsDescriptions(('Added capability statement cVlanMemberCapV12R0250SYPCat6K.', 'Added capability statement cVlanMemberCapV12R0233SXI4PCat6K.', 'Added cVlanMemberCapV12R0233SXHPCat6K.', 'Added cVlanMembershipCapCatOSV08R0301 agent capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setLastUpdated('201010290000Z')
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setDescription('Agent capabilities for CISCO-VLAN-MEMBERSHIP-MIB.')
cVlanMembershipCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanMembershipCapV12R0119ECat6K.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
cVlanMembershipCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanMembershipCapV12R0217SXCat6K.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
ciscoVlanMembershipCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanMembershipCapCatOSV08R0101.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
ciscoVlanMembershipCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanMembershipCapCatOSV08R0201.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
cVlanMembershipCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: cVlanMembershipCapCatOSV08R0301.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
cVlanMemberCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanMemberCapV12R0233SXHPCat6K.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
cVlanMemberCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanMemberCapV12R0233SXI4PCat6K.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
cVlanMemberCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanMemberCapV12R0250SYPCat6K.setDescription('CISCO-VLAN-MEMBERSHIP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-MEMBERSHIP-CAPABILITY", cVlanMembershipCapV12R0217SXCat6K=cVlanMembershipCapV12R0217SXCat6K, cVlanMembershipCapCatOSV08R0301=cVlanMembershipCapCatOSV08R0301, PYSNMP_MODULE_ID=ciscoVlanMembershipCapability, ciscoVlanMembershipCapCatOSV08R0201=ciscoVlanMembershipCapCatOSV08R0201, cVlanMemberCapV12R0250SYPCat6K=cVlanMemberCapV12R0250SYPCat6K, cVlanMemberCapV12R0233SXHPCat6K=cVlanMemberCapV12R0233SXHPCat6K, cVlanMembershipCapV12R0119ECat6K=cVlanMembershipCapV12R0119ECat6K, ciscoVlanMembershipCapability=ciscoVlanMembershipCapability, cVlanMemberCapV12R0233SXI4PCat6K=cVlanMemberCapV12R0233SXI4PCat6K, ciscoVlanMembershipCapCatOSV08R0101=ciscoVlanMembershipCapCatOSV08R0101)
