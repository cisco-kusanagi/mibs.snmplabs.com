#
# PySNMP MIB module CISCO-IEEE8021-CFM-V2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IEEE8021-CFM-V2-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, iso, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "iso", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIeee8021CfmV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 579))
ciscoIeee8021CfmV2Capability.setRevisions(('2010-02-15 00:00', '2009-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setRevisionsDescriptions(('Added capability statement ciscoIeee8021CfmV2CapV12R0254SE.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setLastUpdated('201002150000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setDescription('The capabilities description of IEEE8021-CFM-V2-MIB.')
ciscoIeee8021CfmV2CapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2CapCatOSV08R0702.setDescription('IEEE8021-CFM-V2-MIB capabilities.')
ciscoIeee8021CfmV2CapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2CapV12R0254SE.setDescription('IEEE8021-CFM-V2-MIB capabilities')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-V2-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021CfmV2Capability, ciscoIeee8021CfmV2CapCatOSV08R0702=ciscoIeee8021CfmV2CapCatOSV08R0702, ciscoIeee8021CfmV2CapV12R0254SE=ciscoIeee8021CfmV2CapV12R0254SE, ciscoIeee8021CfmV2Capability=ciscoIeee8021CfmV2Capability)
