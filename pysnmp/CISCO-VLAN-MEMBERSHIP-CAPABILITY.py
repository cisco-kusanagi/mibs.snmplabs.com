#
# PySNMP MIB module CISCO-VLAN-MEMBERSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-MEMBERSHIP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso, Counter32, Gauge32, Counter64, Unsigned32, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso", "Counter32", "Gauge32", "Counter64", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVlanMembershipCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 316))
ciscoVlanMembershipCapability.setRevisions(('2010-10-29 00:00', '2010-03-21 00:00', '2007-07-12 00:00', '2004-01-15 00:00', '2003-09-15 00:00',))
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setLastUpdated('201010290000Z')
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setOrganization('Cisco Systems, Inc.')
cVlanMembershipCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setStatus('current')
cVlanMembershipCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setStatus('current')
ciscoVlanMembershipCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setStatus('current')
ciscoVlanMembershipCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setStatus('current')
cVlanMembershipCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setStatus('current')
cVlanMemberCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setStatus('current')
cVlanMemberCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setStatus('current')
cVlanMemberCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-MEMBERSHIP-CAPABILITY", cVlanMemberCapV12R0233SXHPCat6K=cVlanMemberCapV12R0233SXHPCat6K, ciscoVlanMembershipCapCatOSV08R0201=ciscoVlanMembershipCapCatOSV08R0201, ciscoVlanMembershipCapCatOSV08R0101=ciscoVlanMembershipCapCatOSV08R0101, cVlanMembershipCapV12R0119ECat6K=cVlanMembershipCapV12R0119ECat6K, cVlanMembershipCapV12R0217SXCat6K=cVlanMembershipCapV12R0217SXCat6K, cVlanMemberCapV12R0250SYPCat6K=cVlanMemberCapV12R0250SYPCat6K, cVlanMemberCapV12R0233SXI4PCat6K=cVlanMemberCapV12R0233SXI4PCat6K, cVlanMembershipCapCatOSV08R0301=cVlanMembershipCapCatOSV08R0301, PYSNMP_MODULE_ID=ciscoVlanMembershipCapability, ciscoVlanMembershipCapability=ciscoVlanMembershipCapability)
