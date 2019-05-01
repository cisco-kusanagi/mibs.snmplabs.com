#
# PySNMP MIB module CISCO-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSTEM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, IpAddress, Counter64, Bits, NotificationType, TimeTicks, Gauge32, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "Bits", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 276))
ciscoSystemCapability.setRevisions(('2008-07-02 00:00', '2007-07-31 00:00', '2003-09-15 00:00', '2002-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSystemCapability.setRevisionsDescriptions(('Added ciscoSystemCapACSWV03R000 agent capabilities for Application Control Engine (ACE) Module. Added ciscoSystemCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added ciscoSystemCapabilityMGXV5R0500.', 'Added ciscoSystemCapCatOSV08R0101.', 'Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSystemCapability.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: ciscoSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSystemCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSystemCapability.setDescription('The Agent Capabilities for CISCO-SYSTEM-MIB.')
ciscoSystemCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                         BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapabilityV2R00.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapCatOSV08R0101.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapabilityMGXV5R0500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setProductRelease('MGX8850 5.5 Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapabilityMGXV5R0500.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setProductRelease('ACSW (Application Control Software)\n                    version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapACSWV03R000.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapc4710aceVA1R700.setDescription('CISCO-SYSTEM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYSTEM-CAPABILITY", ciscoSystemCapCatOSV08R0101=ciscoSystemCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoSystemCapability, ciscoSystemCapc4710aceVA1R700=ciscoSystemCapc4710aceVA1R700, ciscoSystemCapabilityV2R00=ciscoSystemCapabilityV2R00, ciscoSystemCapability=ciscoSystemCapability, ciscoSystemCapACSWV03R000=ciscoSystemCapACSWV03R000, ciscoSystemCapabilityMGXV5R0500=ciscoSystemCapabilityMGXV5R0500)
