#
# PySNMP MIB module CISCO-TRUSTSEC-SXP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-SXP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoVrfName, = mibBuilder.importSymbols("CISCO-TC", "CiscoVrfName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, iso, ObjectIdentity, Bits, Counter64, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Gauge32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "ObjectIdentity", "Bits", "Counter64", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "Unsigned32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoTrustSecSxpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 591))
ciscoTrustSecSxpCapability.setRevisions(('2012-09-07 00:00', '2012-04-10 00:00', '2011-09-28 00:00', '2011-03-23 00:00', '2010-11-03 00:00', '2010-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setRevisionsDescriptions(('Added capapbility statement ciscoTrustSecSxpCapV15R0101SYPCat6k.', 'Added capability statement ciscoTrustSecSxpCapV15R0101SGPCat4k.', 'Added capability statement ciscoTrustSecSxpCapV15R0001SYPCat6k.', 'Added capability statement ciscoTrustSecSxpCapV12R0233SXJPCat6k.', 'Added agent capabilities statement ciscoTrustSecSxpCapV12R0250SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-SXP-MIB.')
ciscoTrustSecSxpCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
ciscoTrustSecSxpCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
ciscoTrustSecSxpCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV12R0233SXJPCat6k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
ciscoTrustSecSxpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV15R0001SYPCat6k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
ciscoTrustSecSxpCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV15R0101SGPCat4k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
ciscoTrustSecSxpCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapV15R0101SYPCat6k.setDescription('CISCO-TRUSTSEC-SXP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SXP-CAPABILITY", ciscoTrustSecSxpCapability=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV15R0101SGPCat4k=ciscoTrustSecSxpCapV15R0101SGPCat4k, ciscoTrustSecSxpCapV15R0001SYPCat6k=ciscoTrustSecSxpCapV15R0001SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV12R0233SXI4PCat6k=ciscoTrustSecSxpCapV12R0233SXI4PCat6k, ciscoTrustSecSxpCapV12R0250SYPCat6k=ciscoTrustSecSxpCapV12R0250SYPCat6k, ciscoTrustSecSxpCapV12R0233SXJPCat6k=ciscoTrustSecSxpCapV12R0233SXJPCat6k, ciscoTrustSecSxpCapV15R0101SYPCat6k=ciscoTrustSecSxpCapV15R0101SYPCat6k)
