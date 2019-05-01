#
# PySNMP MIB module CISCO-FLEX-LINKS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLEX-LINKS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:58:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, ObjectIdentity, Unsigned32, ModuleIdentity, IpAddress, Counter32, Bits, Gauge32, NotificationType, TimeTicks, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter32", "Bits", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFlexLinksCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 444))
ciscoFlexLinksCapability.setRevisions(('2010-05-18 00:00', '2005-07-28 00:00', '2005-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlexLinksCapability.setRevisionsDescriptions(('Added cFlexLinksCapV12R0254SGPCat4K. Updated cFlexLinksCapV12R0218SXFPCat6k with VARIATION clause of cflIfConfigStatus.', 'Added cFlexLinksCapV12R0218SXFPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setDescription('The capabilities description of CISCO-FLEX-LINKS-MIB.')
ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoFlexLinksCapCatOSV08R0501.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0218SXFPCat6k.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0254SGPCat4K.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-CAPABILITY", ciscoFlexLinksCapability=ciscoFlexLinksCapability, ciscoFlexLinksCapCatOSV08R0501=ciscoFlexLinksCapCatOSV08R0501, cFlexLinksCapV12R0218SXFPCat6k=cFlexLinksCapV12R0218SXFPCat6k, cFlexLinksCapV12R0254SGPCat4K=cFlexLinksCapV12R0254SGPCat4K, PYSNMP_MODULE_ID=ciscoFlexLinksCapability)
