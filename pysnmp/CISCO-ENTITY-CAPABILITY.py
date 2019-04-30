#
# PySNMP MIB module CISCO-ENTITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, Counter32, ModuleIdentity, Gauge32, Unsigned32, Integer32, iso, ObjectIdentity, NotificationType, Bits, Counter64, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "Integer32", "iso", "ObjectIdentity", "NotificationType", "Bits", "Counter64", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 277))
ciscoEntityCapability.setRevisions(('2014-04-03 00:00', '2013-07-19 00:00', '2009-03-24 00:00', '2008-07-03 00:00', '2006-11-16 00:00', '2006-05-26 00:00', '2006-03-24 00:00', '2006-02-08 00:00', '2003-08-12 00:00', '2003-08-08 00:00', '2002-06-12 00:00',))
if mibBuilder.loadTexts: ciscoEntityCapability.setLastUpdated('201404030000Z')
if mibBuilder.loadTexts: ciscoEntityCapability.setOrganization('Cisco Systems, Inc.')
ciscoEntityCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setStatus('current')
ciscoEntityCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setStatus('current')
ciscoEntityCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setStatus('current')
ciscoEntityCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setStatus('current')
ciscoEntityCapabilityV20CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setStatus('current')
ciscoEntityCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setStatus('current')
ciscoEntityCapabilityIOSXRV3R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setStatus('current')
ciscoEntityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for \n                    ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setStatus('current')
ciscoEntityCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setStatus('current')
ciscoEntityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setStatus('current')
ciscoEntityCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-CAPABILITY", ciscoEntityCapV12R0111bEXCat6K=ciscoEntityCapV12R0111bEXCat6K, ciscoEntityCapNxOSV06R0202PN7k=ciscoEntityCapNxOSV06R0202PN7k, ciscoEntityCapCatOSV08R0101=ciscoEntityCapCatOSV08R0101, ciscoEntityCapability=ciscoEntityCapability, ciscoEntityCapabilityV20CRS1=ciscoEntityCapabilityV20CRS1, ciscoEntityCapabilityACSWV03R000=ciscoEntityCapabilityACSWV03R000, ciscoEntityCapabilityV2R00=ciscoEntityCapabilityV2R00, ciscoEntityCapNxOSV06R0201PMds=ciscoEntityCapNxOSV06R0201PMds, ciscoEntityCapc4710aceVA1R700=ciscoEntityCapc4710aceVA1R700, ciscoEntityCapabilityGssV03R01=ciscoEntityCapabilityGssV03R01, ciscoEntityCapV12R0214SXCat6K=ciscoEntityCapV12R0214SXCat6K, ciscoEntityCapabilityIOSXRV3R4=ciscoEntityCapabilityIOSXRV3R4, PYSNMP_MODULE_ID=ciscoEntityCapability)
