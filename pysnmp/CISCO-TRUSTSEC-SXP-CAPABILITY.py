#
# PySNMP MIB module CISCO-TRUSTSEC-SXP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-SXP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoVrfName, = mibBuilder.importSymbols("CISCO-TC", "CiscoVrfName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Gauge32, IpAddress, MibIdentifier, NotificationType, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "Unsigned32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoTrustSecSxpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 591))
ciscoTrustSecSxpCapability.setRevisions(('2012-09-07 00:00', '2012-04-10 00:00', '2011-09-28 00:00', '2011-03-23 00:00', '2010-11-03 00:00', '2010-03-25 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecSxpCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SXP-CAPABILITY", ciscoTrustSecSxpCapV12R0233SXJPCat6k=ciscoTrustSecSxpCapV12R0233SXJPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV15R0101SGPCat4k=ciscoTrustSecSxpCapV15R0101SGPCat4k, ciscoTrustSecSxpCapV15R0101SYPCat6k=ciscoTrustSecSxpCapV15R0101SYPCat6k, ciscoTrustSecSxpCapV12R0250SYPCat6k=ciscoTrustSecSxpCapV12R0250SYPCat6k, ciscoTrustSecSxpCapV15R0001SYPCat6k=ciscoTrustSecSxpCapV15R0001SYPCat6k, ciscoTrustSecSxpCapV12R0233SXI4PCat6k=ciscoTrustSecSxpCapV12R0233SXI4PCat6k, ciscoTrustSecSxpCapability=ciscoTrustSecSxpCapability)
