#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INTERFACETOPN-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, iso, Gauge32, Unsigned32, IpAddress, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter32, Counter64, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter32", "Counter64", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTopNExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 543))
ciscoTopNExtCapability.setRevisions(('2012-09-07 01:00', '2007-07-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTopNExtCapability.setRevisionsDescriptions(('Added capability statement ciscoTopNExtCapV15R0001SY1PCat6K. Added VARIATION citneInterfaceTopNInterfaceType in ciscoTopNExtCapV12R0233SXHPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTopNExtCapability.setLastUpdated('201209070100Z')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setDescription('The capabilities description of CISCO-INTERFACETOPN-EXT-MIB.')
ciscoTopNExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTopNExtCapV12R0233SXHPCat6k.setDescription('CISCO-INTERFACETOPN-EXT-MIB capabilities.')
ciscoTopNExtCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoTopNExtCapV15R0001SY1PCat6K.setDescription('CISCO-INTERFACETOPN-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-CAPABILITY", ciscoTopNExtCapability=ciscoTopNExtCapability, PYSNMP_MODULE_ID=ciscoTopNExtCapability, ciscoTopNExtCapV12R0233SXHPCat6k=ciscoTopNExtCapV12R0233SXHPCat6k, ciscoTopNExtCapV15R0001SY1PCat6K=ciscoTopNExtCapV15R0001SY1PCat6K)
