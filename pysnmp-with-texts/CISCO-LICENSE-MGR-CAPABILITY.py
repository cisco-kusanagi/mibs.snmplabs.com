#
# PySNMP MIB module CISCO-LICENSE-MGR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LICENSE-MGR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, ObjectIdentity, Unsigned32, NotificationType, IpAddress, Gauge32, MibIdentifier, Counter64, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Unsigned32", "NotificationType", "IpAddress", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLicenseMgrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 495))
ciscoLicenseMgrCapability.setRevisions(('2008-07-21 00:00', '2006-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setRevisionsDescriptions(('Added VARIATIONS for MIB objects clmLicenseGracePeriod and clmNotificationsEnable to ciscoLicenseMgrCapabilityACSWV03R000 agent capability. Added capability statement ciscoLicMgrCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement ciscoLicenseMgrCapabilityACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setDescription('The capabilities description of CISCO-LICENSE-MGR-MIB.')
ciscoLicenseMgrCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoLicenseMgrCapabilityACSWV03R000.setDescription('ACSW (Application Control Software) 3.0 CISCO LICENSE MGR MIB capabilities')
ciscoLicMgrCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoLicMgrCapc4710aceVA1R700.setDescription('ACSW (Application Control Software) A1(7) CISCO LICENSE MGR MIB capabilities')
mibBuilder.exportSymbols("CISCO-LICENSE-MGR-CAPABILITY", ciscoLicenseMgrCapability=ciscoLicenseMgrCapability, ciscoLicenseMgrCapabilityACSWV03R000=ciscoLicenseMgrCapabilityACSWV03R000, PYSNMP_MODULE_ID=ciscoLicenseMgrCapability, ciscoLicMgrCapc4710aceVA1R700=ciscoLicMgrCapc4710aceVA1R700)
