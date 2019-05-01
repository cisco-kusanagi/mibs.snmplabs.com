#
# PySNMP MIB module CISCO-ENTITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Unsigned32, TimeTicks, iso, Counter32, Integer32, MibIdentifier, NotificationType, Gauge32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "iso", "Counter32", "Integer32", "MibIdentifier", "NotificationType", "Gauge32", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 277))
ciscoEntityCapability.setRevisions(('2014-04-03 00:00', '2013-07-19 00:00', '2009-03-24 00:00', '2008-07-03 00:00', '2006-11-16 00:00', '2006-05-26 00:00', '2006-03-24 00:00', '2006-02-08 00:00', '2003-08-12 00:00', '2003-08-08 00:00', '2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityCapability.setRevisionsDescriptions(('Added capability statement ciscoEntityCapNxOSV06R0201PMds.', 'Added capability statement ciscoEntityCapNxOSV06R0202PN7k.', 'Added ciscoEntityCapabilityGssV03R01 agent capabilities for Global Site Selector(GSS) release 3.1(0).', 'Added ciscoEntityCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance. Changed CISCO-ENTITY-MIB to ENTITY-MIB in the DESCRIPTION clause for ciscoEntityCapability. Changed the SUPPORT clause for ciscoEntityCapabilityV2R00, ciscoEntityCapV12R0111bEXCat6K, ciscoEntityCapV12R0214SXCat6K, ciscoEntityCapCatOSV08R0101, ciscoEntityCapabilityV20CRS1, ciscoEntityCapabilityACSWV03R000 agent capabilities to ENTITY-MIB from CISCO-ENTITY-MIB and modified the DESCRIPTION clause accordingly.', 'Added ciscoEntityCapabilityIOSXRV3R4 agent capabilities for IOS XR 3.4', 'Added ciscoEntityCapabilityACSWV03R000 agent capabilities for Cisco Application Control Engine (ACE).', 'Add VARIATION for the notification entConfigChange in ciscoEntityCapCatOSV08R0101.', 'Added ciscoEntityCapabilityV20CRS1 Agent capabilities for IOS XR release 2.0 CRS1', 'Updated the ciscoEntityCapability OID with the one assigned by CANA.', 'Added ciscoEntityCapV12R0111bEXCat6K ciscoEntityCapV12R0214SXCat6K and ciscoEntityCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityCapability.setLastUpdated('201404030000Z')
if mibBuilder.loadTexts: ciscoEntityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityCapability.setDescription('The Agent Capabilities for ENTITY-MIB.')
ciscoEntityCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityV2R00.setDescription('Agent capabilities for ENTITY-MIB.')
ciscoEntityCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapV12R0111bEXCat6K.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapV12R0214SXCat6K.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapCatOSV08R0101.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapabilityV20CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityV20CRS1.setDescription('ENTITY-MIB capabilities for IOS XR release 2.0')
ciscoEntityCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityACSWV03R000.setDescription('ENTITY-MIB capabilities for ACSW 3.0')
ciscoEntityCapabilityIOSXRV3R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityIOSXRV3R4.setDescription('ENTITY-MIB capabilities for IOS XR release 3.4')
ciscoEntityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for \n                    ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapc4710aceVA1R700.setDescription('ENTITY-MIB capabilities for ACSW A1(7)')
ciscoEntityCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityGssV03R01.setDescription('ENTITY-MIB capabilities for GSS 3.1(0)')
ciscoEntityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapNxOSV06R0202PN7k.setDescription('ENTITY-MIB capabilities capabilities.')
ciscoEntityCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapNxOSV06R0201PMds.setDescription('ENTITY-MIB capabilities capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-CAPABILITY", ciscoEntityCapCatOSV08R0101=ciscoEntityCapCatOSV08R0101, ciscoEntityCapNxOSV06R0201PMds=ciscoEntityCapNxOSV06R0201PMds, PYSNMP_MODULE_ID=ciscoEntityCapability, ciscoEntityCapc4710aceVA1R700=ciscoEntityCapc4710aceVA1R700, ciscoEntityCapV12R0214SXCat6K=ciscoEntityCapV12R0214SXCat6K, ciscoEntityCapabilityV2R00=ciscoEntityCapabilityV2R00, ciscoEntityCapV12R0111bEXCat6K=ciscoEntityCapV12R0111bEXCat6K, ciscoEntityCapNxOSV06R0202PN7k=ciscoEntityCapNxOSV06R0202PN7k, ciscoEntityCapabilityGssV03R01=ciscoEntityCapabilityGssV03R01, ciscoEntityCapabilityV20CRS1=ciscoEntityCapabilityV20CRS1, ciscoEntityCapability=ciscoEntityCapability, ciscoEntityCapabilityIOSXRV3R4=ciscoEntityCapabilityIOSXRV3R4, ciscoEntityCapabilityACSWV03R000=ciscoEntityCapabilityACSWV03R000)
