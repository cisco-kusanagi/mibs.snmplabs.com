#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHERLIKE-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, Integer32, Counter32, MibIdentifier, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Bits, Gauge32, ObjectIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter32", "MibIdentifier", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "ObjectIdentity", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherlikeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 587))
ciscoEtherlikeExtCapability.setRevisions(('2011-04-01 00:00', '2010-10-29 00:00', '2010-03-12 00:00',))
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setOrganization('Cisco Systems, Inc.')
ceeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setStatus('current')
ceeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setStatus('current')
ceeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-CAPABILITY", ceeCapV15R0002SGPCat4K=ceeCapV15R0002SGPCat4K, ciscoEtherlikeExtCapability=ciscoEtherlikeExtCapability, ceeCapV12R0250SYPCat6K=ceeCapV12R0250SYPCat6K, ceeCapV12R0233SXI4PCat6K=ceeCapV12R0233SXI4PCat6K, PYSNMP_MODULE_ID=ciscoEtherlikeExtCapability)
