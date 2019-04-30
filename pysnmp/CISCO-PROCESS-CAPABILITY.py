#
# PySNMP MIB module CISCO-PROCESS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PROCESS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, Counter64, ObjectIdentity, NotificationType, Bits, Gauge32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "Gauge32", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoProcessCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 256))
ciscoProcessCapability.setRevisions(('2013-08-29 00:00', '2009-03-18 00:00', '2008-09-15 00:00', '2007-11-27 00:00', '2007-11-22 00:00', '2006-03-22 00:00', '2006-02-21 00:00', '2005-12-12 00:00', '2004-11-05 00:00', '2003-08-06 00:00', '2001-11-20 00:00',))
if mibBuilder.loadTexts: ciscoProcessCapability.setLastUpdated('201308290000Z')
if mibBuilder.loadTexts: ciscoProcessCapability.setOrganization('Cisco Systems, Inc.')
ciscoProcessCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setStatus('current')
ciscoProcessCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setStatus('current')
ciscoProcessCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setStatus('current')
ciscoProcessCapCatOSV07R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setProductRelease('Cisco CatOS 7.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setStatus('current')
ciscoProcessCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setStatus('current')
ciscoProcessCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setStatus('current')
ciscoProcessCapabilityV12R03T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setStatus('current')
ciscoProcessCapabilitySAN3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setProductRelease('SAN-OS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setStatus('current')
ciscoProcessCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setStatus('current')
ciscoProcessCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setStatus('current')
ciscoProcessCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setStatus('current')
ciscoProcessCapabilityIONV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setProductRelease('Modular IOS(ION) 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setStatus('current')
ciscoProcessCapabilityIOSV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setProductRelease('Cisco IOS 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setStatus('current')
ciscoProcessCapabilityGssV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setStatus('current')
ciscoProcessCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setStatus('current')
ciscoProcessCapabilityWAASV05R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setProductRelease('OS=WAAS\n                     OSVERSION=5.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-PROCESS-CAPABILITY", ciscoProcessCapIOSXRV2R0CRS1=ciscoProcessCapIOSXRV2R0CRS1, ciscoProcessCapabilityWAASV05R03=ciscoProcessCapabilityWAASV05R03, ciscoProcessCapabilityV12R02=ciscoProcessCapabilityV12R02, ciscoProcessCapabilitySAN3R0001=ciscoProcessCapabilitySAN3R0001, ciscoProcessCapc4710aceVA1R700=ciscoProcessCapc4710aceVA1R700, ciscoProcessCapabilityACSWV03R000=ciscoProcessCapabilityACSWV03R000, ciscoProcessCapabilityGssV03R00=ciscoProcessCapabilityGssV03R00, PYSNMP_MODULE_ID=ciscoProcessCapability, ciscoProcessCapabilityV12R03=ciscoProcessCapabilityV12R03, ciscoProcessCapabilityV12R00=ciscoProcessCapabilityV12R00, ciscoProcessCapabilityIOSV12R02SXH33=ciscoProcessCapabilityIOSV12R02SXH33, ciscoProcessCapCatOSV07R0201=ciscoProcessCapCatOSV07R0201, ciscoProcessCapabilityV12R01=ciscoProcessCapabilityV12R01, ciscoProcessCapabilityV12R03T=ciscoProcessCapabilityV12R03T, ciscoProcessCapability=ciscoProcessCapability, ciscoProcessCapabilityIONV12R02SXH33=ciscoProcessCapabilityIONV12R02SXH33, ciscoProcessCapabilityGssV03R01=ciscoProcessCapabilityGssV03R01, ciscoProcessCapabilityV12R02S=ciscoProcessCapabilityV12R02S)
