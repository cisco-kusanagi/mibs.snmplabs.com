#
# PySNMP MIB module CISCO-INTERFACETOPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-INTERFACETOPN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, ObjectIdentity, Unsigned32, Bits, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier, NotificationType, Gauge32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier", "NotificationType", "Gauge32", "Integer32", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoTopNCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 544))
ciscoTopNCapability.setRevisions(('2007-07-06 00:00',))
if mibBuilder.loadTexts: ciscoTopNCapability.setLastUpdated('200707060000Z')
if mibBuilder.loadTexts: ciscoTopNCapability.setOrganization('Cisco Systems, Inc.')
ciscoTopNCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 544, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNCapV12R0233SXHPCat6k = ciscoTopNCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNCapV12R0233SXHPCat6k = ciscoTopNCapV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-CAPABILITY", ciscoTopNCapability=ciscoTopNCapability, PYSNMP_MODULE_ID=ciscoTopNCapability, ciscoTopNCapV12R0233SXHPCat6k=ciscoTopNCapV12R0233SXHPCat6k)
