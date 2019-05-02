#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-POLICY-CONFIG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, iso, IpAddress, TimeTicks, MibIdentifier, Counter32, Gauge32, ModuleIdentity, Counter64, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoQosPolicyConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 363))
ciscoQosPolicyConfigCapability.setRevisions(('2007-06-28 00:00', '2003-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setRevisionsDescriptions(('Add cqpcCapabilityV12R0233SXHPCat6k statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setLastUpdated('200706280000Z')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setDescription('The Agent capabilities for CISCO-QOS-POLICY-CONFIG-MIB')
cqpcCapabilityCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: cqpcCapabilityCatOSV08R0101Cat6k.setDescription('CISCO-QOS-POLICY-CONFIG-MIB capabilities.')
cqpcCapabilityV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cqpcCapabilityV12R0233SXHPCat6k.setDescription('CISCO-QOS-POLICY-CONFIG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-CAPABILITY", cqpcCapabilityCatOSV08R0101Cat6k=cqpcCapabilityCatOSV08R0101Cat6k, PYSNMP_MODULE_ID=ciscoQosPolicyConfigCapability, cqpcCapabilityV12R0233SXHPCat6k=cqpcCapabilityV12R0233SXHPCat6k, ciscoQosPolicyConfigCapability=ciscoQosPolicyConfigCapability)
