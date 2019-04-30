#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-POLICY-CONFIG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ObjectIdentity, Integer32, MibIdentifier, Counter32, TimeTicks, Gauge32, Counter64, NotificationType, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ObjectIdentity", "Integer32", "MibIdentifier", "Counter32", "TimeTicks", "Gauge32", "Counter64", "NotificationType", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosPolicyConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 363))
ciscoQosPolicyConfigCapability.setRevisions(('2007-06-28 00:00', '2003-10-20 00:00',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setLastUpdated('200706280000Z')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setOrganization('Cisco Systems, Inc.')
cqpcCapabilityCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setStatus('current')
cqpcCapabilityV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-CAPABILITY", cqpcCapabilityV12R0233SXHPCat6k=cqpcCapabilityV12R0233SXHPCat6k, ciscoQosPolicyConfigCapability=ciscoQosPolicyConfigCapability, PYSNMP_MODULE_ID=ciscoQosPolicyConfigCapability, cqpcCapabilityCatOSV08R0101Cat6k=cqpcCapabilityCatOSV08R0101Cat6k)
