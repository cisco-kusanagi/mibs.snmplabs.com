#
# PySNMP MIB module CISCO-ENHANCED-MEMPOOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENHANCED-MEMPOOL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Counter64, Gauge32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Bits, IpAddress, ObjectIdentity, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter64", "Gauge32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Bits", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cempCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 462))
cempCapability.setRevisions(('2011-09-21 00:00', '2011-01-31 00:00', '2010-10-28 00:00', '2009-08-21 00:00', '2009-04-23 00:00', '2007-05-09 00:00', '2005-12-29 00:00', '2005-10-26 00:00', '2005-01-27 00:00', '2004-10-01 00:00', '2004-06-15 00:00',))
if mibBuilder.loadTexts: cempCapability.setLastUpdated('201109210000Z')
if mibBuilder.loadTexts: cempCapability.setOrganization('Cisco Systems, Inc.')
cempCapabilityV12R03T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03T = cempCapabilityV12R03T.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03T = cempCapabilityV12R03T.setStatus('current')
cempCapabilityV12R03TP5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03TP5000 = cempCapabilityV12R03TP5000.setProductRelease('Cisco IOS 12.3T for AS5350, AS5400 and AS5850\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03TP5000 = cempCapabilityV12R03TP5000.setStatus('current')
cempCapabilityV12R04TP37xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP37xx = cempCapabilityV12R04TP37xx.setProductRelease('Cisco IOS 12.4T for c3725 and c3745\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP37xx = cempCapabilityV12R04TP37xx.setStatus('current')
cempCapabilityV12R04TP26xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP26xx = cempCapabilityV12R04TP26xx.setProductRelease('Cisco IOS 12.4T for c26xx and c2691\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP26xx = cempCapabilityV12R04TP26xx.setStatus('current')
cempCapabilityV12R04TP38xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP38xx = cempCapabilityV12R04TP38xx.setProductRelease('Cisco IOS 12.4T for c3825 and c3845\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP38xx = cempCapabilityV12R04TP38xx.setStatus('current')
cempCapabilityV12R04TP28xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP28xx = cempCapabilityV12R04TP28xx.setProductRelease('Cisco IOS 12.4T for c28xx platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP28xx = cempCapabilityV12R04TP28xx.setStatus('current')
cempCapabilityV12R04TPVG224 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPVG224 = cempCapabilityV12R04TPVG224.setProductRelease('Cisco IOS 12.4T for VG224 platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPVG224 = cempCapabilityV12R04TPVG224.setStatus('current')
cempCapabilityV12R04TPIAD243x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPIAD243x = cempCapabilityV12R04TPIAD243x.setProductRelease('Cisco IOS 12.4T for IAD243x platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPIAD243x = cempCapabilityV12R04TPIAD243x.setStatus('current')
cempCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityIOSXRV2R0CRS1 = cempCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityIOSXRV2R0CRS1 = cempCapabilityIOSXRV2R0CRS1.setStatus('current')
cempCapabilityCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityCatOSV08R0601 = cempCapabilityCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityCatOSV08R0601 = cempCapabilityCatOSV08R0601.setStatus('current')
cempCapabilityV12R05TP184x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP184x = cempCapabilityV12R05TP184x.setProductRelease('Cisco IOS 12.5T for 184x platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP184x = cempCapabilityV12R05TP184x.setStatus('current')
cempCapabilityV12R05TP2801 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP2801 = cempCapabilityV12R05TP2801.setProductRelease('Cisco IOS 12.5T for the 2801 platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP2801 = cempCapabilityV12R05TP2801.setStatus('current')
cempCapabilityNXOS501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOS501 = cempCapabilityNXOS501.setProductRelease('Cisco MDS & Nexus NX-OS 5.0 and above')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOS501 = cempCapabilityNXOS501.setStatus('current')
cempCapabilityNXOSV05R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV05R0201 = cempCapabilityNXOSV05R0201.setProductRelease('Cisco Nexus NX-OS 5.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV05R0201 = cempCapabilityNXOSV05R0201.setStatus('current')
cempCapabilityASA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityASA = cempCapabilityASA.setProductRelease('8.4.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityASA = cempCapabilityASA.setStatus('current')
cempCapabilityNXOSV06R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV06R0001 = cempCapabilityNXOSV06R0001.setProductRelease('Cisco Nexus NX-OS 6.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV06R0001 = cempCapabilityNXOSV06R0001.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENHANCED-MEMPOOL-CAPABILITY", cempCapabilityV12R04TP38xx=cempCapabilityV12R04TP38xx, PYSNMP_MODULE_ID=cempCapability, cempCapabilityASA=cempCapabilityASA, cempCapabilityNXOSV05R0201=cempCapabilityNXOSV05R0201, cempCapabilityV12R05TP2801=cempCapabilityV12R05TP2801, cempCapabilityV12R04TP28xx=cempCapabilityV12R04TP28xx, cempCapabilityIOSXRV2R0CRS1=cempCapabilityIOSXRV2R0CRS1, cempCapabilityV12R04TP26xx=cempCapabilityV12R04TP26xx, cempCapabilityNXOSV06R0001=cempCapabilityNXOSV06R0001, cempCapabilityV12R04TPVG224=cempCapabilityV12R04TPVG224, cempCapabilityV12R03TP5000=cempCapabilityV12R03TP5000, cempCapabilityV12R05TP184x=cempCapabilityV12R05TP184x, cempCapability=cempCapability, cempCapabilityV12R04TP37xx=cempCapabilityV12R04TP37xx, cempCapabilityNXOS501=cempCapabilityNXOS501, cempCapabilityCatOSV08R0601=cempCapabilityCatOSV08R0601, cempCapabilityV12R04TPIAD243x=cempCapabilityV12R04TPIAD243x, cempCapabilityV12R03T=cempCapabilityV12R03T)
