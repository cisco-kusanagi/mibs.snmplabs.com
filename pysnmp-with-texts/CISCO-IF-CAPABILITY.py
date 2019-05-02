#
# PySNMP MIB module CISCO-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, Counter32, TimeTicks, Bits, ModuleIdentity, NotificationType, Integer32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "TimeTicks", "Bits", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "MibIdentifier", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 125))
ciscoIfCapability.setRevisions(('2008-03-17 00:00', '2006-11-03 00:00', '2006-10-30 00:00', '2006-07-17 00:00', '2006-02-02 00:00', '2004-08-09 00:00', '2004-02-21 00:00', '2004-02-20 00:00', '2003-03-14 00:00', '2002-06-12 00:00', '2000-02-09 00:00', '1998-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfCapability.setRevisionsDescriptions(('Added ciscoIfCapabilityc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine(ACE) Appliance.', 'Added ciscoIfCapabilityIOSXRV3R4CRS1 agent capability for IOS XR 3.4', 'Added capability for Cisco TelePresence System (CTS) and Cisco TelePresence Manager (CTM) platforms.', 'Added ciscoIfCapabilityACSWV03R000 agent capabilities for Cisco Application Control Software (ACSW) 3.0.', 'Added ciscoIfCapabilityIOSXRV2R0CRS1 agent capabilities for IOS XR release 2.0.', 'Added ciscoIfCapabilityV5R015 agent capabilities for MGX product series: MPSM Service Module and VXSM (Voice Switch Service Module).', 'Added following Agent capabilities for Catalyst 6000/6500 and Cisco 7600 series devices: ciscoIfCapabilityCatOSV08R0101 and ciscoIfCapabilityCatOSV08R0301.', 'Added ciscoIfCapabilityV5R00 agent capabilities for MGX product series: MPSM Service Module and VXSM (Voice Switch Service Module.', 'Added following Agent capabilities for MGX product series: - ciscoIfCapabilityV4R00 for AXSM 10 Gig. Module (AXSM-XG) and AXSM Enhanced Module (AXSM-E).', 'Added following Agent capabilities for MGX product series: - ciscoIfCapabilityPxmVR200 for PXM(Processor Switch Module) Module - ciscoIfCapabilityAxsmVR200 for AXSM(ATM Switch Service Module) - ciscoIfCapabilityAxsmeV21R60 for AXSM Enhanced Module. - ciscoIfCapabilityFrsm12V3R00 for Frame Relay Service Module(FRSM-12).', 'Modification of ifCounterDiscontinuityTime, ifTableLastChange object and LinkUp/Down trap objects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIfCapability.setLastUpdated('200803170000Z')
if mibBuilder.loadTexts: ciscoIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIfCapability.setDescription('Agent capabilities for IF-MIB')
ciscoIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV11R03.setDescription('IF MIB capabilities')
ciscoIfCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV12R00.setDescription('IF MIB capabilities')
ciscoIfCapabilityV12R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setProductRelease('Cisco IOS 12.1T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV12R01T.setDescription('IF MIB capabilities')
ciscoIfCapabilityPxmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setProductRelease('MGX8850 Release 2.00,BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityPxmVR200.setDescription('IF MIB capabilities for PXM45, PXM1 Modules.')
ciscoIfCapabilityAxsmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityAxsmVR200.setDescription('IF MIB capabilities for ATM Switch Service Module(AXSM).')
ciscoIfCapabilityAxsmeV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityAxsmeV21R60.setDescription('IF MIB capabilities for Enhanced ATM Switch Service Module (AXSM-E).')
ciscoIfCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityFrsm12V3R00.setDescription('IF MIB capabilities for Frame Relay Service Module(FRSM-12).')
ciscoIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV4R00.setDescription('IF MIB capabilities for 10 Gig. ATM Switch Service Module (AXSM-XG) and Enhanced ATM Switch Service Module (AXSM-E).')
ciscoIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV5R00.setDescription('IF MIB capabilities for Voice Switch Service Module (VXSM) and MPSM in release 5.0.0')
ciscoIfCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCatOSV08R0101.setDescription('IF MIB agent capabilities.')
ciscoIfCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCatOSV08R0301.setDescription('IF MIB agent capabilities.')
ciscoIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityV5R015.setDescription('IF MIB capabilities for Voice Switch Service Module (VXSM) 5.0.15')
ciscoIfCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityIOSXRV2R0CRS1.setDescription('IF-MIB capabilities for Cisco IOS XR in releases 2.0')
ciscoIfCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine (ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityACSWV03R000.setDescription('IF-MIB capabilities for Cisco ACSW 3.0.')
ciscoIfCapabilityCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCTSV100.setDescription('IF-MIB capabilities for CTS 1.0.0')
ciscoIfCapabilityCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityCTMV1000.setDescription('IF-MIB capabilities for CTM 1.0.0.0')
ciscoIfCapabilityIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityIOSXRV3R4CRS1.setDescription('IF-MIB capabilities for Cisco IOS XR in releases 3.4')
ciscoIfCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityc4710aceVA1R700.setDescription('IF-MIB capabilities for Cisco ACSW A1(7)')
mibBuilder.exportSymbols("CISCO-IF-CAPABILITY", ciscoIfCapability=ciscoIfCapability, PYSNMP_MODULE_ID=ciscoIfCapability, ciscoIfCapabilityFrsm12V3R00=ciscoIfCapabilityFrsm12V3R00, ciscoIfCapabilityAxsmeV21R60=ciscoIfCapabilityAxsmeV21R60, ciscoIfCapabilityPxmVR200=ciscoIfCapabilityPxmVR200, ciscoIfCapabilityIOSXRV2R0CRS1=ciscoIfCapabilityIOSXRV2R0CRS1, ciscoIfCapabilityV12R01T=ciscoIfCapabilityV12R01T, ciscoIfCapabilityAxsmVR200=ciscoIfCapabilityAxsmVR200, ciscoIfCapabilityc4710aceVA1R700=ciscoIfCapabilityc4710aceVA1R700, ciscoIfCapabilityCatOSV08R0301=ciscoIfCapabilityCatOSV08R0301, ciscoIfCapabilityV4R00=ciscoIfCapabilityV4R00, ciscoIfCapabilityV11R03=ciscoIfCapabilityV11R03, ciscoIfCapabilityIOSXRV3R4CRS1=ciscoIfCapabilityIOSXRV3R4CRS1, ciscoIfCapabilityCTMV1000=ciscoIfCapabilityCTMV1000, ciscoIfCapabilityCatOSV08R0101=ciscoIfCapabilityCatOSV08R0101, ciscoIfCapabilityV5R00=ciscoIfCapabilityV5R00, ciscoIfCapabilityV5R015=ciscoIfCapabilityV5R015, ciscoIfCapabilityACSWV03R000=ciscoIfCapabilityACSWV03R000, ciscoIfCapabilityV12R00=ciscoIfCapabilityV12R00, ciscoIfCapabilityCTSV100=ciscoIfCapabilityCTSV100)
