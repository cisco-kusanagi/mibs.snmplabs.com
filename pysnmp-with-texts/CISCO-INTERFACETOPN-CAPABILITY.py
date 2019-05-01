#
# PySNMP MIB module CISCO-INTERFACETOPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INTERFACETOPN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, MibIdentifier, iso, NotificationType, Integer32, TimeTicks, Bits, Gauge32, Counter64, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "iso", "NotificationType", "Integer32", "TimeTicks", "Bits", "Gauge32", "Counter64", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoTopNCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 544))
ciscoTopNCapability.setRevisions(('2007-07-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTopNCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTopNCapability.setLastUpdated('200707060000Z')
if mibBuilder.loadTexts: ciscoTopNCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTopNCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTopNCapability.setDescription('The capabilities description of INTERFACETOPN-MIB.')
ciscoTopNCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 544, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNCapV12R0233SXHPCat6k = ciscoTopNCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNCapV12R0233SXHPCat6k = ciscoTopNCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTopNCapV12R0233SXHPCat6k.setDescription('INTERFACETOPN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-CAPABILITY", ciscoTopNCapV12R0233SXHPCat6k=ciscoTopNCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoTopNCapability, ciscoTopNCapability=ciscoTopNCapability)
