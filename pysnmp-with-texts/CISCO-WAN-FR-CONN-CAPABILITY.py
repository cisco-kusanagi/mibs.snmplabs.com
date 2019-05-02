#
# PySNMP MIB module CISCO-WAN-FR-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-FR-CONN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, NotificationType, ModuleIdentity, TimeTicks, MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Bits, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Bits", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanFrConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 358))
ciscoWanFrConnCapability.setRevisions(('2002-03-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanFrConnCapability.setRevisionsDescriptions(('Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setLastUpdated('200203270000Z')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setDescription('The Agent Capabilities for Frame Relay connection mib objects. - The capability cwFrConnCapabilityFrsm12V3R00 is for FRSM-12 module.')
cwFrConnCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setStatus('current')
if mibBuilder.loadTexts: cwFrConnCapabilityFrsm12V3R00.setDescription('Frame Relay Connection Agent Capabilities for Frame Relay Service Module(FRSM-12).')
mibBuilder.exportSymbols("CISCO-WAN-FR-CONN-CAPABILITY", ciscoWanFrConnCapability=ciscoWanFrConnCapability, PYSNMP_MODULE_ID=ciscoWanFrConnCapability, cwFrConnCapabilityFrsm12V3R00=cwFrConnCapabilityFrsm12V3R00)
