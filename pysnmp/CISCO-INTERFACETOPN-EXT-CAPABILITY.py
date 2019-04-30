#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INTERFACETOPN-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Integer32, ModuleIdentity, Bits, Counter32, NotificationType, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Integer32", "ModuleIdentity", "Bits", "Counter32", "NotificationType", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTopNExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 543))
ciscoTopNExtCapability.setRevisions(('2012-09-07 01:00', '2007-07-06 00:00',))
if mibBuilder.loadTexts: ciscoTopNExtCapability.setLastUpdated('201209070100Z')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoTopNExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setStatus('current')
ciscoTopNExtCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-CAPABILITY", ciscoTopNExtCapV15R0001SY1PCat6K=ciscoTopNExtCapV15R0001SY1PCat6K, ciscoTopNExtCapV12R0233SXHPCat6k=ciscoTopNExtCapV12R0233SXHPCat6k, ciscoTopNExtCapability=ciscoTopNExtCapability, PYSNMP_MODULE_ID=ciscoTopNExtCapability)
