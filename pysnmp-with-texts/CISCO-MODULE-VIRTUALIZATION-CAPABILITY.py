#
# PySNMP MIB module CISCO-MODULE-VIRTUALIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODULE-VIRTUALIZATION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, ObjectIdentity, ModuleIdentity, Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, iso, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "iso", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoModuleVirtualizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 497))
ciscoModuleVirtualizationCapability.setRevisions(('2008-06-14 00:00', '2006-05-31 00:00', '2006-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setRevisionsDescriptions(('Added capability statement ciscoModVirtCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Corrected the contact E-mail id: cs-l4l7security@cisco.com', 'Added capability statement ciscoModuleVirtualizationCapabilityACSWV03R000 for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setLastUpdated('200806140000Z')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-l4l7security@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setDescription('The capabilities description of CISCO-MODULE-VIRTUALIZATION-MIB.')
ciscoModuleVirtualizationCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapabilityACSWV03R000.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
ciscoModVirtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoModVirtCapc4710aceVA1R700.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-VIRTUALIZATION-CAPABILITY", ciscoModuleVirtualizationCapability=ciscoModuleVirtualizationCapability, PYSNMP_MODULE_ID=ciscoModuleVirtualizationCapability, ciscoModVirtCapc4710aceVA1R700=ciscoModVirtCapc4710aceVA1R700, ciscoModuleVirtualizationCapabilityACSWV03R000=ciscoModuleVirtualizationCapabilityACSWV03R000)
