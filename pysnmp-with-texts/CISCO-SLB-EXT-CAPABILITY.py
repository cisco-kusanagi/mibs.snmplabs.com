#
# PySNMP MIB module CISCO-SLB-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SLB-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, TimeTicks, Counter32, Bits, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "TimeTicks", "Counter32", "Bits", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 496))
ciscoSlbExtCapability.setRevisions(('2008-07-02 00:00', '2008-02-07 00:00', '2006-12-08 00:00', '2006-02-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbExtCapability.setRevisionsDescriptions(('Added capability statement ciscoSlbExtCapc4710aceVA3R100 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added capability statement ciscoSlbExtCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added capability statement ciscoSlbExtCapabilityACSWV300RA12 for Application Control Engine (ACE).', 'Added capability statement ciscoSlbExtCapabilityACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoSlbExtCapability.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: ciscoSlbExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbExtCapability.setDescription('The capabilities description of CISCO-SLB-EXT-MIB.')
ciscoSlbExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapabilityACSWV03R000.setDescription('ACSW (Application Control Software) 3.0 CISCO SLB MIB capabilities')
ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setProductRelease('ACSW (Application Control Software)\n                version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapabilityACSWV300RA12.setDescription('Agent capability for CISCO-SLB-EXT-MIB for ACE(Application Control Engine) module.')
ciscoSlbExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapc4710aceVA1R700.setDescription('Agent capability for CISCO-SLB-EXT-MIB for ACE(Application Control Engine) appliance.')
ciscoSlbExtCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapc4710aceVA3R100.setDescription('Agent capability for CISCO-SLB-EXT-MIB for ACE(Application Control Engine) appliance.')
mibBuilder.exportSymbols("CISCO-SLB-EXT-CAPABILITY", ciscoSlbExtCapabilityACSWV300RA12=ciscoSlbExtCapabilityACSWV300RA12, PYSNMP_MODULE_ID=ciscoSlbExtCapability, ciscoSlbExtCapabilityACSWV03R000=ciscoSlbExtCapabilityACSWV03R000, ciscoSlbExtCapability=ciscoSlbExtCapability, ciscoSlbExtCapc4710aceVA1R700=ciscoSlbExtCapc4710aceVA1R700, ciscoSlbExtCapc4710aceVA3R100=ciscoSlbExtCapc4710aceVA3R100)
