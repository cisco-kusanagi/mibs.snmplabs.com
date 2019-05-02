#
# PySNMP MIB module CISCO-IEEE8021-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IEEE8021-CFM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Bits, MibIdentifier, Gauge32, TimeTicks, iso, NotificationType, ObjectIdentity, Integer32, IpAddress, Counter32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibIdentifier", "Gauge32", "TimeTicks", "iso", "NotificationType", "ObjectIdentity", "Integer32", "IpAddress", "Counter32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 578))
ciscoIeee8021CfmCapability.setRevisions(('2010-02-23 00:00', '2009-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setRevisionsDescriptions(('Added capability statement ciscoIeee8021CfmCapV12R0254SE.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setLastUpdated('201002230000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setDescription('The capabilities description of IEEE8021-CFM-MIB.')
ciscoIeee8021CfmCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapCatOSV08R0702.setDescription('IEEE8021-CFM-MIB capabilities.')
ciscoIeee8021CfmCapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapV12R0254SE.setDescription('IEEE8021-CFM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-CAPABILITY", ciscoIeee8021CfmCapCatOSV08R0702=ciscoIeee8021CfmCapCatOSV08R0702, PYSNMP_MODULE_ID=ciscoIeee8021CfmCapability, ciscoIeee8021CfmCapV12R0254SE=ciscoIeee8021CfmCapV12R0254SE, ciscoIeee8021CfmCapability=ciscoIeee8021CfmCapability)
