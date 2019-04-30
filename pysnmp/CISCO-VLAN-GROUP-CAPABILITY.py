#
# PySNMP MIB module CISCO-VLAN-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-GROUP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, TimeTicks, Gauge32, Integer32, Bits, NotificationType, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "TimeTicks", "Gauge32", "Integer32", "Bits", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoVlanGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 590))
ciscoVlanGroupCapability.setRevisions(('2012-04-10 00:00', '2011-09-22 00:00', '2011-03-31 00:00', '2011-03-23 00:00', '2010-03-22 00:00',))
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setLastUpdated('201204100000Z')
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setOrganization('Cisco Systems, Inc.')
ciscoVlanGroupCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setStatus('current')
ciscoVlanGroupCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setStatus('current')
ciscoVlanGroupCapV15R0002SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setProductRelease('Cisco IOS 15.0(2)SG on Cat4k family switches\n                    (excluding switches with SUP7).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setStatus('current')
ciscoVlanGroupCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setStatus('current')
ciscoVlanGroupCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4k family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanGroupCapability, ciscoVlanGroupCapV15R0002SGPCat4k=ciscoVlanGroupCapV15R0002SGPCat4k, ciscoVlanGroupCapV12R0233SXJPCat6k=ciscoVlanGroupCapV12R0233SXJPCat6k, ciscoVlanGroupCapability=ciscoVlanGroupCapability, ciscoVlanGroupCapV15R0101SGPCat4k=ciscoVlanGroupCapV15R0101SGPCat4k, ciscoVlanGroupCapV15R0001SYPCat6k=ciscoVlanGroupCapV15R0001SYPCat6k, ciscoVlanGroupCapV12R0233SXI4PCat6K=ciscoVlanGroupCapV12R0233SXI4PCat6K)
