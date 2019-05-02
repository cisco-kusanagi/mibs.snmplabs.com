#
# PySNMP MIB module CISCO-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SLB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, ModuleIdentity, Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, IpAddress, Bits, NotificationType, Counter64, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "IpAddress", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 181))
ciscoSlbCapability.setRevisions(('2008-07-24 00:00', '2008-02-07 00:00', '2006-12-09 00:00', '2006-03-21 00:00', '2001-03-09 00:00', '2000-10-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbCapability.setRevisionsDescriptions(('Added ciscoSlbCapc4710aceVA3R100 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added ciscoSlbCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance.', '- Added ciscoSlbCapabilityACSWV300RA12 agent capabilities for Application Control Engine (ACE). - Following change is done for ciscoSlbCapabilityV12R01: * STATUS changed to obsolete. * Commented out the VARIATION and other clauses for non-existent objects. - Added ciscoSlbCapabilityNewV12R01 which is same as ciscoSlbCapabilityV12R01 except it is not referencing the non-existent objects/groups.', 'Added ciscoIfCapabilityACSWV03R000 agent capabilities for Application Control Engine (ACE).', 'Extended MIB support for ciscoSlbEntriesGroup, and serveral new objects in the ciscoSlbVirtualServersGroup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbCapability.setLastUpdated('200807240000Z')
if mibBuilder.loadTexts: ciscoSlbCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbCapability.setDescription('Agent capabilities for the SLB-MIB')
ciscoSlbCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityV12R01 = ciscoSlbCapabilityV12R01.setProductRelease('Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityV12R01 = ciscoSlbCapabilityV12R01.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoSlbCapabilityV12R01.setDescription('IOS 12.1 Cisco SLB MIB capabilities')
ciscoIfCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityACSWV03R000.setDescription('ACSW (Application Control Software) 3.0 CISCO SLB MIB capabilities')
ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setProductRelease('ACSW (Application Control Software)\n                version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapabilityACSWV300RA12.setDescription('ACSW (Application Control Software) 3.0 CISCO SLB MIB capabilities')
ciscoSlbCapabilityNewV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityNewV12R01 = ciscoSlbCapabilityNewV12R01.setProductRelease('Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityNewV12R01 = ciscoSlbCapabilityNewV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapabilityNewV12R01.setDescription('IOS 12.1 Cisco SLB MIB capabilities')
ciscoSlbCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA1R700 = ciscoSlbCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA1R700 = ciscoSlbCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapc4710aceVA1R700.setDescription('ACSW (Application Control Software) A1(7) CISCO SLB MIB capabilities.')
ciscoSlbCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA3R100 = ciscoSlbCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA3R100 = ciscoSlbCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapc4710aceVA3R100.setDescription('ACSW (Application Control Software) A3(1) CISCO SLB MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SLB-CAPABILITY", PYSNMP_MODULE_ID=ciscoSlbCapability, ciscoSlbCapabilityV12R01=ciscoSlbCapabilityV12R01, ciscoSlbCapabilityNewV12R01=ciscoSlbCapabilityNewV12R01, ciscoSlbCapc4710aceVA1R700=ciscoSlbCapc4710aceVA1R700, ciscoSlbCapability=ciscoSlbCapability, ciscoSlbCapc4710aceVA3R100=ciscoSlbCapc4710aceVA3R100, ciscoSlbExtCapabilityACSWV300RA12=ciscoSlbExtCapabilityACSWV300RA12, ciscoIfCapabilityACSWV03R000=ciscoIfCapabilityACSWV03R000)
