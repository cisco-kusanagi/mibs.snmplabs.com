#
# PySNMP MIB module CISCO-WAN-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, TimeTicks, Counter32, Counter64, Gauge32, Bits, iso, IpAddress, MibIdentifier, Integer32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "Counter64", "Gauge32", "Bits", "iso", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 99999))
ciscoWanModuleCapability.setRevisions(('2002-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanModuleCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanModuleCapability.setLastUpdated('200203060000Z')
if mibBuilder.loadTexts: ciscoWanModuleCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanModuleCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanModuleCapability.setDescription('The Agent Capabilities for CISCO-WAN-MODULE-MIB. - The ciscoWanModuleCapabilityV2R00 is for ATM Switch Service Module(AXSM). - The ciscoWanModuleCapabilityV21R60 is for Enhanced ATM Switch Service Module(AXSM-E).')
ciscoWanModuleCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV2R00 = ciscoWanModuleCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV2R00 = ciscoWanModuleCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanModuleCapabilityV2R00.setDescription('CISCO-WAN-MODULE-MIB Capabilities for ATM Switch Service Module(AXSM).')
ciscoWanModuleCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV21R60 = ciscoWanModuleCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV21R60 = ciscoWanModuleCapabilityV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoWanModuleCapabilityV21R60.setDescription('CISCO-WAN-MODULE-MIB Capabilities for Enhanced AXSM(AXSM-E) module.')
mibBuilder.exportSymbols("CISCO-WAN-MODULE-CAPABILITY", ciscoWanModuleCapabilityV21R60=ciscoWanModuleCapabilityV21R60, ciscoWanModuleCapability=ciscoWanModuleCapability, PYSNMP_MODULE_ID=ciscoWanModuleCapability, ciscoWanModuleCapabilityV2R00=ciscoWanModuleCapabilityV2R00)
