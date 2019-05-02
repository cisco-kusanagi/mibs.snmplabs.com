#
# PySNMP MIB module CISCO-ENHANCED-MEMPOOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENHANCED-MEMPOOL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Counter64, ObjectIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Counter64", "ObjectIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cempCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 462))
cempCapability.setRevisions(('2011-09-21 00:00', '2011-01-31 00:00', '2010-10-28 00:00', '2009-08-21 00:00', '2009-04-23 00:00', '2007-05-09 00:00', '2005-12-29 00:00', '2005-10-26 00:00', '2005-01-27 00:00', '2004-10-01 00:00', '2004-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cempCapability.setRevisionsDescriptions(('Added cempCapabilityNXOSV06R0001 agent capabilities for Cisco Nexus NX-OS 6.0(1).', 'Added cempCapabilityASA for 8.4.x version.', 'Added cempCapabilityNXOSV05R0201 agent capabilities for NX-OS release 5.2(1).', 'fixed/removed extra-unwanted comma in cempCapabilityNXOS501 agent capabilities', 'Added cempCapabilityNXOS501 agent capabilities for NX-OS release 5.0.', 'The following capability statements have been added: 1. cempCapabilityV12R05TP184x 2. cempCapabilityV12R05TP2801.', 'Added capability statement ciscoEmpCapCatOSV08R0601Cat6K.', 'Added cempCapabilityIOSXRV2R0CRS1 agent capabilities for IOS XR release 2.0 CRS1', 'Added agent capabilities for 38xx, 37xx, 26xx, 28xx, VG224 and IAD243x platforms.', 'Added cempCapabilityV12R03TP5000 for Cisco IOS 12.3T', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cempCapability.setLastUpdated('201109210000Z')
if mibBuilder.loadTexts: cempCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cempCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-memory@cisco.com')
if mibBuilder.loadTexts: cempCapability.setDescription('Agent capabilities for CISCO-ENHANCED-MEMPOOL-MIB.')
cempCapabilityV12R03T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03T = cempCapabilityV12R03T.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03T = cempCapabilityV12R03T.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R03T.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R03TP5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03TP5000 = cempCapabilityV12R03TP5000.setProductRelease('Cisco IOS 12.3T for AS5350, AS5400 and AS5850\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R03TP5000 = cempCapabilityV12R03TP5000.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R03TP5000.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TP37xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP37xx = cempCapabilityV12R04TP37xx.setProductRelease('Cisco IOS 12.4T for c3725 and c3745\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP37xx = cempCapabilityV12R04TP37xx.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TP37xx.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TP26xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP26xx = cempCapabilityV12R04TP26xx.setProductRelease('Cisco IOS 12.4T for c26xx and c2691\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP26xx = cempCapabilityV12R04TP26xx.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TP26xx.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TP38xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP38xx = cempCapabilityV12R04TP38xx.setProductRelease('Cisco IOS 12.4T for c3825 and c3845\n                        platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP38xx = cempCapabilityV12R04TP38xx.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TP38xx.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TP28xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP28xx = cempCapabilityV12R04TP28xx.setProductRelease('Cisco IOS 12.4T for c28xx platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TP28xx = cempCapabilityV12R04TP28xx.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TP28xx.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TPVG224 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPVG224 = cempCapabilityV12R04TPVG224.setProductRelease('Cisco IOS 12.4T for VG224 platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPVG224 = cempCapabilityV12R04TPVG224.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TPVG224.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R04TPIAD243x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPIAD243x = cempCapabilityV12R04TPIAD243x.setProductRelease('Cisco IOS 12.4T for IAD243x platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R04TPIAD243x = cempCapabilityV12R04TPIAD243x.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R04TPIAD243x.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityIOSXRV2R0CRS1 = cempCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityIOSXRV2R0CRS1 = cempCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityIOSXRV2R0CRS1.setDescription('CISCO-ENHANCED-MEMPOOL-MIB capabilities for IOS XR release 2.0')
cempCapabilityCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityCatOSV08R0601 = cempCapabilityCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityCatOSV08R0601 = cempCapabilityCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityCatOSV08R0601.setDescription('CISCO-ENHANCED-MEMPOOL-MIB capabilities.')
cempCapabilityV12R05TP184x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP184x = cempCapabilityV12R05TP184x.setProductRelease('Cisco IOS 12.5T for 184x platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP184x = cempCapabilityV12R05TP184x.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R05TP184x.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityV12R05TP2801 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP2801 = cempCapabilityV12R05TP2801.setProductRelease('Cisco IOS 12.5T for the 2801 platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityV12R05TP2801 = cempCapabilityV12R05TP2801.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityV12R05TP2801.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityNXOS501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOS501 = cempCapabilityNXOS501.setProductRelease('Cisco MDS & Nexus NX-OS 5.0 and above')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOS501 = cempCapabilityNXOS501.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityNXOS501.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities')
cempCapabilityNXOSV05R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV05R0201 = cempCapabilityNXOSV05R0201.setProductRelease('Cisco Nexus NX-OS 5.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV05R0201 = cempCapabilityNXOSV05R0201.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityNXOSV05R0201.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities to support 64bit values.')
cempCapabilityASA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityASA = cempCapabilityASA.setProductRelease('8.4.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityASA = cempCapabilityASA.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityASA.setDescription('CISCO-ENHANCED-MEMPOOL MIB capabilities to support 64 bit values in ASA for 8.4.x release.')
cempCapabilityNXOSV06R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 462, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV06R0001 = cempCapabilityNXOSV06R0001.setProductRelease('Cisco Nexus NX-OS 6.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cempCapabilityNXOSV06R0001 = cempCapabilityNXOSV06R0001.setStatus('current')
if mibBuilder.loadTexts: cempCapabilityNXOSV06R0001.setDescription('CISCO-ENHANCED-MEMPOOL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENHANCED-MEMPOOL-CAPABILITY", cempCapabilityV12R05TP184x=cempCapabilityV12R05TP184x, cempCapabilityV12R04TP38xx=cempCapabilityV12R04TP38xx, cempCapabilityV12R04TPIAD243x=cempCapabilityV12R04TPIAD243x, PYSNMP_MODULE_ID=cempCapability, cempCapabilityNXOSV05R0201=cempCapabilityNXOSV05R0201, cempCapabilityV12R03TP5000=cempCapabilityV12R03TP5000, cempCapabilityIOSXRV2R0CRS1=cempCapabilityIOSXRV2R0CRS1, cempCapabilityASA=cempCapabilityASA, cempCapabilityV12R03T=cempCapabilityV12R03T, cempCapabilityCatOSV08R0601=cempCapabilityCatOSV08R0601, cempCapabilityV12R05TP2801=cempCapabilityV12R05TP2801, cempCapabilityNXOSV06R0001=cempCapabilityNXOSV06R0001, cempCapabilityNXOS501=cempCapabilityNXOS501, cempCapabilityV12R04TPVG224=cempCapabilityV12R04TPVG224, cempCapabilityV12R04TP37xx=cempCapabilityV12R04TP37xx, cempCapabilityV12R04TP26xx=cempCapabilityV12R04TP26xx, cempCapability=cempCapability, cempCapabilityV12R04TP28xx=cempCapabilityV12R04TP28xx)
