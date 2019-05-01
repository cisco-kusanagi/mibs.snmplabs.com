#
# PySNMP MIB module CISCO-VSI-CONTROLLER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VSI-CONTROLLER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, iso, Gauge32, Unsigned32, ModuleIdentity, Integer32, TimeTicks, MibIdentifier, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVsiControllerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoVsiControllerCapability.setRevisions(('2002-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVsiControllerCapability.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setLastUpdated('200205020000Z')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setDescription('Agent capabilities for CISCO-VSI-CONTROLLER-MIB.')
ciscoVsiControllerCapabilityVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoVsiControllerCapabilityVR200.setDescription('The agent capabilities for CISCO-VSI-CONTROLLER-MIB.')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-CAPABILITY", ciscoVsiControllerCapabilityVR200=ciscoVsiControllerCapabilityVR200, ciscoVsiControllerCapability=ciscoVsiControllerCapability, PYSNMP_MODULE_ID=ciscoVsiControllerCapability)
