#
# PySNMP MIB module CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, NotificationType, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Counter64, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoDynamicArpInspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 382))
ciscoDynamicArpInspCapability.setRevisions(('2011-03-24 00:00', '2010-05-07 00:00', '2007-07-02 00:00', '2004-01-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setRevisionsDescriptions(('Added cdaiCapV15R0002SGPCat4K agent capability statement.', 'Added cdaiCapV12R0254SGPCat4K agent capability statement.', 'Added cdaiCapV12R0233SXHPCat6k agent capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setLastUpdated('201103240000Z')
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setDescription('The capabilities description of CISCO-DYNAMIC-ARP-INSPECTION-MIB.')
cdaiCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: cdaiCapabilityCatOSV08R0301Cat6k.setDescription('CISCO-DYNAMIC-ARP-INSPECTION-MIB capabilities.')
cdaiCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cdaiCapV12R0233SXHPCat6k.setDescription('CISCO-DYNAMIC-ARP-INSPECTION-MIB capabilities.')
cdaiCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cdaiCapV12R0254SGPCat4K.setDescription('CISCO-DYNAMIC-ARP-INSPECTION-MIB capabilities.')
cdaiCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cdaiCapV15R0002SGPCat4K.setDescription('CISCO-DYNAMIC-ARP-INSPECTION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY", ciscoDynamicArpInspCapability=ciscoDynamicArpInspCapability, cdaiCapV12R0254SGPCat4K=cdaiCapV12R0254SGPCat4K, cdaiCapabilityCatOSV08R0301Cat6k=cdaiCapabilityCatOSV08R0301Cat6k, cdaiCapV15R0002SGPCat4K=cdaiCapV15R0002SGPCat4K, PYSNMP_MODULE_ID=ciscoDynamicArpInspCapability, cdaiCapV12R0233SXHPCat6k=cdaiCapV12R0233SXHPCat6k)
