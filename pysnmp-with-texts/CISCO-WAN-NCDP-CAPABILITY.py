#
# PySNMP MIB module CISCO-WAN-NCDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-NCDP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, iso, Counter32, Counter64, MibIdentifier, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Gauge32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "iso", "Counter32", "Counter64", "MibIdentifier", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Gauge32", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanNcdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setLastUpdated('200109140000Z')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setDescription('The Agent Capabilities for CISCO-WAN-NCDP-MIB.')
ciscoWanNcdpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanNcdpCapabilityV3R00.setDescription('NCDP MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-NCDP-CAPABILITY", ciscoWanNcdpCapability=ciscoWanNcdpCapability, PYSNMP_MODULE_ID=ciscoWanNcdpCapability, ciscoWanNcdpCapabilityV3R00=ciscoWanNcdpCapabilityV3R00)
