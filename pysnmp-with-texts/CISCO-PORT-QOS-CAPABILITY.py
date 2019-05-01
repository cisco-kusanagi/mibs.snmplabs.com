#
# PySNMP MIB module CISCO-PORT-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PORT-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Counter64, TimeTicks, Unsigned32, ObjectIdentity, IpAddress, Integer32, ModuleIdentity, Counter32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "Unsigned32", "ObjectIdentity", "IpAddress", "Integer32", "ModuleIdentity", "Counter32", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 209))
ciscoPortQosCapability.setRevisions(('2008-09-25 00:00', '2001-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortQosCapability.setRevisionsDescriptions(('Added ciscoPortQosCapabilityV12R0250SE capabilities.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortQosCapability.setLastUpdated('200809250000Z')
if mibBuilder.loadTexts: ciscoPortQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortQosCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-port-qos@cisco.com')
if mibBuilder.loadTexts: ciscoPortQosCapability.setDescription('Agent capabilities for the CISCO-PORT-QOS-MIB')
ciscoPortQosCapabilityCat2948gL3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setStatus('current')
if mibBuilder.loadTexts: ciscoPortQosCapabilityCat2948gL3.setDescription('IOS 12.0 Cisco PORT QOS MIB capabilities')
ciscoPortQosCapabilityV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setStatus('current')
if mibBuilder.loadTexts: ciscoPortQosCapabilityV12R0250SE.setDescription('MIB Capability from IOS release 12.2(50)SE.')
mibBuilder.exportSymbols("CISCO-PORT-QOS-CAPABILITY", ciscoPortQosCapabilityCat2948gL3=ciscoPortQosCapabilityCat2948gL3, ciscoPortQosCapability=ciscoPortQosCapability, ciscoPortQosCapabilityV12R0250SE=ciscoPortQosCapabilityV12R0250SE, PYSNMP_MODULE_ID=ciscoPortQosCapability)
