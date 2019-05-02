#
# PySNMP MIB module CISCO-VLAN-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-GROUP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Counter32, MibIdentifier, Counter64, Bits, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32, iso, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "Bits", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32", "iso", "ObjectIdentity", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVlanGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 590))
ciscoVlanGroupCapability.setRevisions(('2012-04-10 00:00', '2011-09-22 00:00', '2011-03-31 00:00', '2011-03-23 00:00', '2010-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanGroupCapability.setRevisionsDescriptions(('Added capability statement ciscoVlanGroupCapV15R0101SGPCat4k.', 'Added capability statement ciscoVlanGroupCapV15R0001SYPCat6k.', 'Added capability statement ciscoVlanGroupCapV15R0002SGPCat4k.', 'Added capability statement ciscoVlanGroupCapV12R0233SXJPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setLastUpdated('201204100000Z')
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanGroupCapability.setDescription('The capabilities description of CISCO-VLAN-GROUP-MIB.')
ciscoVlanGroupCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXI4PCat6K = ciscoVlanGroupCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupCapV12R0233SXI4PCat6K.setDescription('CISCO-VLAN-GROUP-MIB capabilities.')
ciscoVlanGroupCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV12R0233SXJPCat6k = ciscoVlanGroupCapV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupCapV12R0233SXJPCat6k.setDescription('CISCO-VLAN-GROUP-MIB capabilities.')
ciscoVlanGroupCapV15R0002SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setProductRelease('Cisco IOS 15.0(2)SG on Cat4k family switches\n                    (excluding switches with SUP7).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0002SGPCat4k = ciscoVlanGroupCapV15R0002SGPCat4k.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupCapV15R0002SGPCat4k.setDescription('CISCO-VLAN-GROUP-MIB capabilities.')
ciscoVlanGroupCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0001SYPCat6k = ciscoVlanGroupCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupCapV15R0001SYPCat6k.setDescription('CISCO-VLAN-GROUP-MIB capabilities.')
ciscoVlanGroupCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 590, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4k family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupCapV15R0101SGPCat4k = ciscoVlanGroupCapV15R0101SGPCat4k.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanGroupCapV15R0101SGPCat4k.setDescription('CISCO-VLAN-GROUP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-CAPABILITY", ciscoVlanGroupCapV15R0001SYPCat6k=ciscoVlanGroupCapV15R0001SYPCat6k, ciscoVlanGroupCapV15R0101SGPCat4k=ciscoVlanGroupCapV15R0101SGPCat4k, ciscoVlanGroupCapV15R0002SGPCat4k=ciscoVlanGroupCapV15R0002SGPCat4k, ciscoVlanGroupCapability=ciscoVlanGroupCapability, ciscoVlanGroupCapV12R0233SXJPCat6k=ciscoVlanGroupCapV12R0233SXJPCat6k, ciscoVlanGroupCapV12R0233SXI4PCat6K=ciscoVlanGroupCapV12R0233SXI4PCat6K, PYSNMP_MODULE_ID=ciscoVlanGroupCapability)
