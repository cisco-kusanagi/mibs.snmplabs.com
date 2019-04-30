#
# PySNMP MIB module CISCO-FLEX-LINKS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLEX-LINKS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, NotificationType, MibIdentifier, ObjectIdentity, Bits, Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "ObjectIdentity", "Bits", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "IpAddress", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoFlexLinksCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 444))
ciscoFlexLinksCapability.setRevisions(('2010-05-18 00:00', '2005-07-28 00:00', '2005-06-22 00:00',))
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setOrganization('Cisco Systems, Inc.')
ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setStatus('current')
cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setStatus('current')
cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-CAPABILITY", cFlexLinksCapV12R0218SXFPCat6k=cFlexLinksCapV12R0218SXFPCat6k, cFlexLinksCapV12R0254SGPCat4K=cFlexLinksCapV12R0254SGPCat4K, ciscoFlexLinksCapability=ciscoFlexLinksCapability, ciscoFlexLinksCapCatOSV08R0501=ciscoFlexLinksCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoFlexLinksCapability)
